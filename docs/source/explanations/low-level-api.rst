Low-level API
#####################

`ezmsg` exposes two layers of API that build on the same pub/sub core:

A **low-level API** that lets you create publishers and subscribers directly, and a **high-level API** that lets you describe a processing graph (a dataflow pipeline) and have ezmsg manage execution for you.

This page explains the low-level model and how it differs from the high-level API so you can choose the right tool for the job.


|ezmsg_logo_small| The Low-level Model
****************************************

At its core, `ezmsg` is a publish/subscribe messaging system.

- A **publisher** can send messages to **many subscribers**.
- A **subscriber** can listen to **many publishers**.
- **Channels** route messages between publishers and subscribers; they are **created and managed automatically** when you connect endpoints.
- Messages can be any Python object. `AxisArray` is optional, not required (but strongly encouraged when it is a good fit).

The low-level API gives you direct access to these primitives. You decide **when** to publish, **how** to receive, and **how** to schedule your own control flow. This makes the low-level API a good fit when you want to integrate messaging into an existing application structure instead of adopting the full `ezmsg` pipeline runtime.

For a detailed breakdown of runtime components, transport selection, backpressure, and zero-copy semantics, see :doc:`transport-messaging-internals`.

|ezmsg_logo_small| Relationship to the High-level API
******************************************************

The high-level API is a **stream-based dataflow runtime**. You define a graph of processing nodes (`Unit` and `Collection`) and connect their input/output streams. The graph is then executed by `ezmsg` (typically via `ez.run()`), which wraps your main entry point and manages scheduling, process layout, and message flow.

Under the hood, the high-level API is **built on the same publisher/subscriber primitives**. Input/output streams are convenience wrappers around those low-level endpoints.


|ezmsg_logo_small| Choosing the Right API
*******************************************

The **low-level API** is a good fit when:

- You already have an application loop or framework you want to keep.
- You want explicit control over concurrency and scheduling.
- You only need a small number of pub/sub links instead of a full graph.
- You are integrating `ezmsg` into a larger system that already manages process lifetime.

The **high-level API** is a good fit when:

- You want to express a graph of processing steps and let `ezmsg` execute it.
- You want consistent dataflow semantics and standardized stream connections.
- You benefit from the pipeline tooling (graph visualization, CLI integration, etc.).
- You want a structured way to scale across threads/processes without managing it yourself.

.. important:: The low-level API is not more performant than the high-level API. There is no meaningful performance hit when using the high-level API.


|ezmsg_logo_small| Examples
********************************

The ezmsg repository includes example scripts that demonstrate the low-level API in both synchronous and asynchronous styles:

- `ezmsg/examples/simple_publisher.py`
- `ezmsg/examples/simple_subscriber.py`
- `ezmsg/examples/simple_async_publisher.py`
- `ezmsg/examples/simple_async_subscriber.py`

.. important:: The synchronous low-level API is a **convenience wrapper** around the async implementation. Internally it uses a threaded `asyncio` loop and calls like ``run_coroutine_threadsafe`` to bridge into the async backend. This is ergonomic (and familiar to users coming from ROS2-style semantics), but it comes with **throughput overhead**. For high data-rate paths, the async low-level API is recommended.

.. note:: For a full introduction to the high-level API, see the :doc:`Tutorials <../tutorials/content-tutorials>` and the :doc:`Pipeline how-to <../how-tos/pipeline/content-pipeline>`.

.. |ezmsg_logo_small| image:: ../_static/_images/ezmsg_logo.png
  :width: 40
  :alt: ezmsg logo
