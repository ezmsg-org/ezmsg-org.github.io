How to profile the performance of a signal processor / method /ezmsg Unit?
################################################################################

For transport-level characterization, `ezmsg` now provides two complementary performance layers:

- ``ezmsg-perf hotpath`` runs fast, focused benchmarks against the hottest message paths.
- ``ezmsg-perf run`` runs the broader end-to-end scenario suite across different topologies and transports.

In general, use ``hotpath`` during development to catch regressions quickly, and use ``run`` less often as the slower, more realistic integration benchmark.

Hot-path benchmarking
=====================

``ezmsg-perf hotpath`` is designed to be quick and stable enough for frequent use. It reports per-case latency and throughput for a narrow set of paths such as:

- same-process ``local``
- same-process ``shm``
- same-process ``tcp``

Example:

.. code-block:: bash

    uv run ezmsg-perf hotpath

You can disable local delivery process-wide to make same-process publishers characterize SHM or TCP behavior by default:

.. code-block:: bash

    EZMSG_ALLOW_LOCAL=0 uv run ezmsg-perf hotpath

You can also compare branches or refs using the interleaved A/B runner:

.. code-block:: bash

    uv run ezmsg-perf ab --ref-a dev --ref-b CURRENT

Full performance suite
======================

``ezmsg-perf run`` remains the broader end-to-end suite. It exercises realistic topologies such as fan-in, fan-out, and relay configurations over longer runs. It is better for validating user-facing performance, but slower and generally noisier than ``hotpath``.
