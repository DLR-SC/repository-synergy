libpebble2
==========

.. image:: https://travis-ci.org/pebble/libpebble2.svg?branch=master
    :target: https://travis-ci.org/pebble/libpebble2

libpebble2 is a python library for interacting with Pebble devices. It:

* Supports connections to Pebble QEMU instances and to watches via the Pebble mobile app or Bluetooth serial.
* Supports connection to watches running both 2.x and 3.x firmware on aplite or basalt hardware
* Provides automatic serialisation and deserialisation of pebble protocol messages
* Asynchronous information is provided by a usable event system
* Features a simple DSL for defining new message types
* Provides ready-made implementations several Pebble Protocol services, including BlobDB and app installation
* Works on Python 2.7 and 3.4

Installation
------------

::

   pip install libpebble2

Or, grab the source from https://github.com/pebble/libpebble2 and: ::

   python setup.py install

Documentation
-------------

`Over here! <https://libpebble2.readthedocs.org/en/latest/>`_
