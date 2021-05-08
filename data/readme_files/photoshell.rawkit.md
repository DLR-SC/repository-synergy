rawkit
======

.. image:: https://badge.fury.io/py/rawkit.svg?
  :alt: Package Status
  :target: https://pypi.python.org/pypi/rawkit

.. image:: https://readthedocs.org/projects/rawkit/badge/?version=latest
   :alt: Docs Status
   :target: https://rawkit.readthedocs.org/en/latest/

.. image:: https://secure.travis-ci.org/photoshell/rawkit.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/photoshell/rawkit

.. image:: https://img.shields.io/coveralls/photoshell/rawkit.svg?style=flat
   :alt: Test Coverage Status
   :target: https://coveralls.io/r/photoshell/rawkit

.. image:: http://unmaintained.tech/badge.svg
   :target: http://unmaintained.tech/
   :alt: No Maintenance Intended

``rawkit`` (pronounced `rocket`) is a ctypes-based LibRaw_ binding for
Python inspired by the Wand_ API.

.. sourcecode:: python

    from rawkit.raw import Raw
    from rawkit.options import WhiteBalance

    with Raw(filename='some/raw/image.CR2') as raw:
      raw.options.white_balance = WhiteBalance(camera=False, auto=True)
      raw.save(filename='some/destination/image.ppm')

for more info, see the docs_

.. _LibRaw: http://www.libraw.org/
.. _Wand: http://docs.wand-py.org
.. _docs: https://rawkit.readthedocs.org/en/latest/
