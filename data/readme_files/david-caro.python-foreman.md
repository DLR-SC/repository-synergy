python-foreman
==============
|pypi-ver| |travis-status| |downloads-count| |python-ver| |license|


Simple library to acces the Foreman API, the full documentation can be found
here:

 http://python-foreman.readthedocs.org


Installation
==============

Execute as root::

  $ python setup.py sdist
  $ pip install ./dist/python-foreman-\*.tar.gz


Plugins
=============

The plugins should be a simple module file with the a dictionary named *DEFS*
with the definitions of the new methods as in the `definitions.py` file


.. |travis-status| image:: https://travis-ci.org/david-caro/python-foreman.svg?branch=master
    :alt: Travis build status
    :scale: 100%
    :target: https://travis-ci.org/david-caro/python-foreman

.. |pypi-ver| image::  https://img.shields.io/pypi/v/python-foreman.svg
    :target: https://pypi.python.org/pypi/python-foreman/
    :alt: Latest Version in PyPI

.. |python-ver| image:: https://img.shields.io/pypi/pyversions/python-foreman.svg
    :target: https://pypi.python.org/pypi/python-foreman/
    :alt: Supported Python versions

.. |downloads-count| image:: https://img.shields.io/pypi/dm/python-foreman.svg?period=month
    :target: https://pypi.python.org/pypi/python-foreman/
    :alt: Downloads

.. |license| image:: https://img.shields.io/badge/license-GPLv2-blue.svg
    :target: https://github.com/david-caro/python-foreman/blob/master/LICENSE
    :alt: Project Licens
