Extensions
##########

ezmsg uses `Python namespace packages <https://packaging.python.org/en/latest/guides/packaging-namespace-packages/>`_ to provide a modular ecosystem of extensions. Namespace packages allow multiple independently distributed packages to share a common namespace (``ezmsg.*``), so you can install only what you need while keeping imports consistent.

For example, installing ``ezmsg-sigproc`` makes the ``ezmsg.sigproc`` module available:

.. code-block:: bash

    pip install ezmsg-sigproc

.. code-block:: python

    from ezmsg.sigproc.butterworthfilter import ButterworthFilter

Each extension is a separate package with its own dependencies, versioning, and release cycle. This keeps the core ``ezmsg`` package lightweight while allowing the ecosystem to grow.

|ezmsg_logo_small| Official Extensions
**************************************

These namespace packages are maintained by the ezmsg organization:

.. list-table::
   :header-rows: 1
   :widths: 20 50 15 15

   * - Package
     - Description
     - Docs
     - Source
   * - `ezmsg-baseproc <https://pypi.org/project/ezmsg-baseproc/>`_
     - Base processor classes and protocols for building message-processing components
     - `docs <https://www.ezmsg.org/ezmsg-baseproc/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-baseproc>`_
   * - `ezmsg-blackrock <https://pypi.org/project/ezmsg-blackrock/>`_
     - Interface for Blackrock Cerebus ecosystem (incl. Neuroport) using pycbsdk
     - `docs <https://www.ezmsg.org/ezmsg-blackrock/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-blackrock>`_
   * - `ezmsg-event <https://pypi.org/project/ezmsg-event/>`_
     - Discrete signal events like neural spikes, heartbeats, and triggers
     - `docs <https://www.ezmsg.org/ezmsg-event/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-event>`_
   * - `ezmsg-learn <https://pypi.org/project/ezmsg-learn/>`_
     - Machine learning modules for streaming signal processing
     - `docs <https://www.ezmsg.org/ezmsg-learn/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-learn>`_
   * - `ezmsg-lsl <https://pypi.org/project/ezmsg-lsl/>`_
     - Lab Streaming Layer (LSL) inlet and outlet units
     - `docs <https://www.ezmsg.org/ezmsg-lsl/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-lsl>`_
   * - `ezmsg-neo <https://pypi.org/project/ezmsg-neo/>`_
     - Load and stream data from Neo-supported file formats (Blackrock, BrainVision, etc.)
     - `docs <https://www.ezmsg.org/ezmsg-neo/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-neo>`_
   * - `ezmsg-panel <https://pypi.org/project/ezmsg-panel/>`_
     - Real-time plotting and dashboards using Panel/HoloViz
     - `docs <https://www.ezmsg.org/ezmsg-panel/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-panel>`_
   * - `ezmsg-redis <https://pypi.org/project/ezmsg-redis/>`_
     - Redis pub/sub units for distributed messaging
     - `docs <https://www.ezmsg.org/ezmsg-redis/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-redis>`_
   * - `ezmsg-sigproc <https://pypi.org/project/ezmsg-sigproc/>`_
     - Timeseries signal processing: filtering, spectral analysis, resampling, and more
     - `docs <https://www.ezmsg.org/ezmsg-sigproc/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-sigproc>`_
   * - `ezmsg-simbiophys <https://pypi.org/project/ezmsg-simbiophys/>`_
     - Simulated biophysical signals: oscillators, noise generators, synthetic EEG
     - `docs <https://www.ezmsg.org/ezmsg-simbiophys/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-simbiophys>`_
   * - `ezmsg-tools <https://pypi.org/project/ezmsg-tools/>`_
     - Visualization and debugging tools for running ezmsg graphs
     - `docs <https://www.ezmsg.org/ezmsg-tools/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-tools>`_
   * - `ezmsg-websocket <https://pypi.org/project/ezmsg-websocket/>`_
     - WebSocket server and client units for web integration
     - `docs <https://www.ezmsg.org/ezmsg-websocket/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-websocket>`_
   * - `ezmsg-xdf <https://pypi.org/project/ezmsg-xdf/>`_
     - XDF (Extensible Data Format) file reading and writing
     - `docs <https://www.ezmsg.org/ezmsg-xdf/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-xdf>`_
   * - `ezmsg-zmq <https://pypi.org/project/ezmsg-zmq/>`_
     - ZeroMQ pub/sub units for distributed messaging
     - `docs <https://www.ezmsg.org/ezmsg-zmq/>`_
     - `github <https://github.com/ezmsg-org/ezmsg-zmq>`_

|ezmsg_logo_small| Community Extensions
***************************************

These extensions are maintained by community members:

- `ezmsg-unicorn <https://github.com/griffinmilsap/ezmsg-unicorn>`_ -- g.tec Unicorn Hybrid Black integration
- `ezmsg-gadget <https://github.com/griffinmilsap/ezmsg-gadget>`_ -- USB-gadget with HID control for Raspberry Pi (Zero/W/2W, 4, CM4)
- `ezmsg-openbci <https://github.com/griffinmilsap/ezmsg-openbci>`_ -- OpenBCI Cyton serial interface
- `ezmsg-ssvep <https://github.com/griffinmilsap/ezmsg-ssvep>`_ -- Tools for running SSVEP experiments
- `ezmsg-vispy <https://github.com/pperanich/ezmsg-vispy>`_ -- Visualization toolkit using PyQt6 and VisPy

.. note::
   Want to create your own extension? Use the `ezmsg-template <https://github.com/ezmsg-org/ezmsg-template>`_ repository as a starting point.

.. |ezmsg_logo_small| image:: ../_static/_images/ezmsg_logo.png
  :width: 40
  :alt: ezmsg logo
