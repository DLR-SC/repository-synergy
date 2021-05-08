Experimental image mining using OpenCV
======================================

Attempting to build tools to mine interesting data from large collections of scanned images

Current
-------

* bin/locate-thumbnail:
    - `Reconstructing thumbnails using OpenCV: <http://chris.improbable.org/2013/06/30/reconstructing-thumbnails-using-opencv/>`_
    - `Upgrading Image Thumbnails… Or How to Fill a Large Display Without Your Content Team Quitting <http://blogs.loc.gov/digitalpreservation/2014/08/upgrading-image-thumbnails-or-how-to-fill-a-large-display-without-your-content-team-quitting/>`_
* bin/extract-figures:
    - `locate interesting non-text elements (images, figures, tables, etc.) on scanned book pages <http://chris.improbable.org/2013/08/31/extracting-images-from-scanned-pages/>`_

Prerequisites
-------------

* Python 2.6+
* OpenCV 2.4+
* numpy

Using Mac Homebrew this should install cleanly::

    brew install python numpy opencv

On Ubuntu 12.04 Precise the following is known to work - note the need for a PPA to get OpenCV 2.4+::

    sudo add-apt-repository ppa:alexei.colin/opencv
    sudo apt-get update
    sudo apt-get install python-numpy python-opencv
    
Discussion
----------

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/acdha/image-mining?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join Chat on Gitter.im
