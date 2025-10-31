List of Extensions
#######################

`ezmsg` extensions can be installed individually or all at once. To install all the extension packages in one go, you can use the following command:

.. code-block:: bash

    pip install "ezmsg[all_ext]"


This will install all the available public extension packages for `ezmsg` that are listed in `pyproject.toml`.
If you prefer to install a subset of extension packages, you can use the following command:

.. code-block:: bash

    pip install "ezmsg[zmq,sigproc,...]"

Please note that the `ezmsg` package itself can still be installed without any additional extensions using `pip install ezmsg`.

Extensions can be managed manually as well. Here are some of the extensions we manage or are aware of:

- `ezmsg-sigproc <https://github.com/ezmsg-org/ezmsg-sigproc>`_ -- Timeseries signal processing modules
- `ezmsg-learn <https://github.com/ezmsg-org/ezmsg-learn>`_ -- Machine learning modules for streaming signal processing
- `ezmsg-lsl <https://github.com/ezmsg-org/ezmsg-lsl>`_ -- Source unit for LSL Inlet and sink unit for LSL Outlet
- `ezmsg-websocket <https://github.com/ezmsg-org/ezmsg-websocket>`_ -- Websocket server and client nodes for `ezmsg` graphs
- `ezmsg-zmq <https://github.com/ezmsg-org/ezmsg-zmq>`_ -- ZeroMQ pub and sub nodes for `ezmsg` graphs
- `ezmsg-panel <https://github.com/griffinmilsap/ezmsg-panel>`_ -- Plotting tools for `ezmsg` that use `panel <https://github.com/holoviz/panel>`_
- `ezmsg-blackrock <https://github.com/griffinmilsap/ezmsg-blackrock>`_ -- Interface for Blackrock Cerebus ecosystem (incl. Neuroport) using `pycbsdk`
- `ezmsg-unicorn <https://github.com/griffinmilsap/ezmsg-unicorn>`_ -- g.tec Unicorn Hybrid Black integration for `ezmsg`
- `ezmsg-gadget <https://github.com/griffinmilsap/ezmsg-gadget>`_ -- USB-gadget with HID control integration for Raspberry Pi (Zero/W/2W, 4, CM4)
- `ezmsg-openbci <https://github.com/griffinmilsap/ezmsg-openbci>`_ -- OpenBCI Cyton serial interface for `ezmsg`
- `ezmsg-ssvep <https://github.com/griffinmilsap/ezmsg-ssvep>`_ -- Tools for running SSVEP experiments with `ezmsg`
- `ezmsg-vispy <https://github.com/pperanich/ezmsg-vispy>`_ -- `ezmsg` visualization toolkit using PyQt6 and vispy.

|ezmsg_logo_small| Extension API References
***********************************************

For detailed API documentation, visit the individual package documentation sites:

Core Extensions
===============

* `ezmsg-sigproc <https://www.ezmsg.org/ezmsg-sigproc/>`_ - Timeseries signal processing modules
* `ezmsg-learn <https://www.ezmsg.org/ezmsg-learn/>`_ - Machine learning modules for streaming signal processing

Data Acquisition & Streaming
=============================

* `ezmsg-blackrock <https://www.ezmsg.org/ezmsg-blackrock/>`_ - Interface for Blackrock Cerebus ecosystem (incl. Neuroport)
* `ezmsg-lsl <https://www.ezmsg.org/ezmsg-lsl/>`_ - Lab Streaming Layer integration

Data Formats & Events
======================

* `ezmsg-event <https://www.ezmsg.org/ezmsg-event/>`_ - Signal events like neural spikes and heartbeats
* `ezmsg-xdf <https://www.ezmsg.org/ezmsg-xdf/>`_ - XDF (Extensible Data Format) file support

Communication & Visualization
==============================

* `ezmsg-zmq <https://www.ezmsg.org/ezmsg-zmq/>`_ - ZeroMQ pub/sub units for distributed messaging
* `ezmsg-tools <https://www.ezmsg.org/ezmsg-tools/>`_ - Tools to visualize running graphs and data

.. note::
   Additional extensions are being documented and their API references will be added here as they become available.

.. |ezmsg_logo_small| image:: ../_static/_images/ezmsg_logo.png
  :width: 40
  :alt: ezmsg logo
