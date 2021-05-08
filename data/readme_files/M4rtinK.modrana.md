=======
modRana
=======

.. image:: https://travis-ci.org/M4rtinK/modrana.svg?branch=master
    :target: https://travis-ci.org/M4rtinK/modrana

ModRana is a flexible GPS navigation system for mobile Linux devices.

Development
===========

Pull requests welcome ! :D

Devices
=======

Confirmed to run on:

- desktop PCs
- the Jolla smartphone and other Sailfish OS devices
- Nokia N900
- Android 4.0+ devices
- Nokia N9 & N950
- Neo FreeRunner
- Smart Q7

Dependencies
============

- Python 2.5+ (including Python 3.2+)

GTK GUI
-------

- PyGTK
- PyCairo
- Python-Location (N900)

Qt 5/QML GUI
------------

- Qt 5.1+
- Python 3.2+
- PyOtherSide 1.3+
- a supported Qt Quick components set
  - Qt Quick Controls 2
  - Sailfish Silica

Ancestry
========

ModRana started as a fork of the `Rana project <http://wiki.openstreetmap.org/wiki/Rana>`_,
but currently uses code from many open source projects:

- Upoints - GPX handling
- Odict - ordered dictionaries
- GPSD Python bindings
- AGTL - Fix object, PinchMap element
- Popup QML element from Mitakuluu
- ThreadManager class from Anaconda
- geopy - Geonames access
- googlemaps - Google API
- configobj - configuration file handling
- PyCha - route profile graphs
- urllib3 - tile download connection reuse
- argparse - startup argument handling
- gprof2dot - profiling

Licence
=======

ModRana is licensed under GPLv3.

Resources
=========

- `modRana project website <http://www.modrana.org>`_
- `discussion thread on talk.maemo.org <http://talk.maemo.org/showthread.php?t=58861>`_
- `main source code repository <https://github.com/M4rtinK/modrana>`_
- `translation project on Transifex <https://www.transifex.com/martink/modrana>`_
- `Sailfish OS package on OpenRepos <https://openrepos.net/content/martink/modrana-0>`_
- `nightly packages for Fedora <https://copr.fedorainfracloud.org/coprs/m4rtink/modrana-nightly>`_
