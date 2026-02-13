Transport and Messaging Internals
#################################

This page documents the runtime components and data-transport behavior used by `ezmsg`. These internals apply equally to the low-level and high-level APIs.

GraphServer, Publisher, Subscriber, Channel
===========================================

- **GraphServer**: a lightweight TCP service that tracks the topic DAG, keeps a registry of publishers/subscribers, and notifies subscribers when their upstream publishers change. It also brokers shared-memory segment creation and attachment.
- **Publisher**: a client that registers a topic with the GraphServer, opens a channel server (TCP listener), and broadcasts messages. It owns shared-memory buffers and enforces backpressure so buffers are not reused until all subscribers have released a message.
- **Subscriber**: a client that registers a topic with the GraphServer, receives updates that list the upstream publisher IDs it should listen to, and maintains local channels for those publishers.
- **Channel**: a process-local "middle-man" for a single publisher. It receives message telemetry from the publisher (or direct local messages), caches the most recent messages, and notifies all local subscribers in that process.

Connection Lifecycle (Publisher -> GraphServer -> Subscriber -> Channel)
========================================================================

1. A **Publisher** connects to the **GraphServer**, allocates shared-memory buffers, and registers its topic. It starts a small TCP server so Channels can connect back to it, then reports that server's address to the GraphServer.
2. A **Subscriber** connects to the **GraphServer** and registers its topic. The GraphServer computes upstream publishers from the topic DAG and sends the Subscriber an `UPDATE` list of publisher IDs.
3. For each publisher ID, the Subscriber asks the local **ChannelManager** to register a **Channel**. If a Channel does not yet exist in this process, it is created by:
4. The **Channel** requesting a channel allocation from the GraphServer for the given publisher ID. The GraphServer returns a new channel ID plus the publisher's server address.
5. The **Channel** connects to the Publisher's channel server, receives the topic and shared-memory name, and attempts to attach to shared memory. It reports whether SHM attach succeeded plus its process ID.
6. The **Publisher** completes the handshake by returning the configured number of buffers. The Channel is now ready to receive messages and notify local subscribers.
7. When graph topology changes (connect/disconnect or new publishers), the GraphServer sends new `UPDATE` messages and Subscribers add or remove Channels as needed.

Transport Selection: Local, SHM, TCP
====================================

`ezmsg` uses the fastest transport available per Publisher/Channel pair:

- **Local transport (same process)**: the Publisher pushes the object directly into the Channel (`put_local`), and the Channel stores it in the `MessageCache` without serialization. This is the lowest-overhead path.
- **Shared memory (different process, SHM OK)**: the Publisher serializes the object using `MessageMarshal` (pickle protocol 5 with buffer support), writes it into a ring of shared-memory buffers, and notifies the Channel with a `TX_SHM` message. The Channel reads from shared memory using the message ID and caches the deserialized object.
- **TCP (fallback or forced)**: if SHM is unavailable (attach failed, remote host) or `force_tcp=True`, the Publisher sends a `TX_TCP` payload (header + serialized buffers) directly over the channel socket. The Channel deserializes it and caches the result.

MessageCache and Deserialization Overhead
=========================================

Every Channel maintains a fixed-size `MessageCache` (one slot per shared-memory buffer). This cache is the key to reducing deserialization overhead:

- For SHM and TCP, the Channel **deserializes each message once per process** and stores the object in the cache.
- All Subscribers in that process read the same cached object -- they do not deep copy.
- When all local Subscribers have released a message, the Channel frees the cache entry and acknowledges the Publisher so the buffer can be reused.

This design keeps serialization/deserialization out of the hot path for local delivery and prevents repeated deserialization when multiple Subscribers in the same process read the same message.

Publisher-Channel Buffers and Backpressure
==========================================

Every Publisher (and thus every Channel) is configured with a fixed number of buffers (`num_buffers`, default 32). These buffers define a ring:

- Each message gets a monotonically increasing `msg_id`.
- The buffer index is `msg_id % num_buffers`.
- The Channel maintains a `MessageCache` with the same size, so each buffer index maps to one cache slot.

Backpressure is the mechanism that prevents a buffer slot from being overwritten while any subscriber still needs its message:

- The **Publisher** checks whether the next buffer index is free. If not, it waits until all leases for that buffer are released.
- When the **Channel** notifies local subscribers of a new message, it **leases** that buffer index for each subscriber. This records "who still needs this message."
- When a subscriber finishes reading the message (or drops it in leaky mode), the Channel **releases** that subscriber’s lease.
- Once all leases for that buffer index are released, the Channel clears the cache entry and acknowledges the Publisher so it can reuse the slot.

Backpressure works the same way for local, SHM, and TCP delivery. The transport only affects how the Channel receives the message bytes; buffer ownership and release are always enforced by the same lease/ack mechanism.

Zero-copy Semantics and Message Ownership
=========================================

Publishers in `ezmsg` serialize messages to shared memory, and eventually to a module-scoped **MessageCache** which is shared by several Subscribers. Subscribers receive a "zero-copy" view of this message that is:

- The originally published object itself in the case local transport was used.
- Backed by Publisher-controlled shared memory if SHM transport was used.
- A shared/cached version of the deserialized object if TCP transport was used.

This results in very low messaging overhead and high messaging performance with **some important safety considerations.**

.. important:: Treat incoming messages as **immutable**. If you need to modify data or republish it, do **not** modify data in place without a very strong understanding of the implications. Generally, you should **create a new message or copy the payload first**. Do **not** republish the same object instance you received.

Why this matters (two concrete failure modes):

1. **Mutating a locally cached message affects other subscribers.** Example: Publisher A and Subscribers B/C/D are in the same process. If Subscriber B mutates the message it received, Subscribers C and D will see those changes because they are reading the same cached object.
2. **Republishing a shared-memory-backed message can corrupt downstream readers.** Example: Publisher A (Process X) publishes an `AxisArray` into shared memory, Subscriber B (Process Y) receives it, then republishes *the same object* via Publisher C to Subscriber D (also in Process Y). Because Publisher C and Subscriber D are local, the object is passed via the local cache. Meanwhile Publisher A sees the shared-memory buffer as free (because Subscriber B has acknowledged receipt and backpressure has been released) and overwrites it, so Subscriber D now observes mutated data.

In the low-level API, subscriber messages are received via `Subscriber.recv()` or `Subscriber.recv_zero_copy()`. `recv()` wraps `recv_zero_copy()` and returns a deep copy of the message; `recv_zero_copy()` yields the shared cached object.

**The high-level `ezmsg` API uses zero-copy semantics for subscriber delivery in all cases. This has been the effective behavior since 2023 (V3.2.0+) and is now the documented behavior.** This specifically applies to coroutines wrapped with the high-level `@ez.subscriber` decorator (the `message` you receive **is that shared object**).

.. note:: The `zero_copy` argument (default `False`) on `@ez.subscriber` previously controlled whether a deepcopy was performed before delivering the message. As detailed in `issue #209 <https://github.com/ezmsg-org/ezmsg/issues/209>`_, a backend change in early 2023 (V3.2.0+) resulted in this argument being ignored, so all coroutines decorated with `@ez.subscriber` receive zero-copy input messages. The maintainers have decided this is preferable behavior because it optimizes message throughput at the expense of code safety. In an upcoming version of `ezmsg`, the `zero_copy` keyword argument will be formally deprecated/retired since it no longer has any effect. If you would like to restore the safety previously guaranteed by `zero_copy=False`, add `message = deepcopy(message)` as the first line in your coroutine.
