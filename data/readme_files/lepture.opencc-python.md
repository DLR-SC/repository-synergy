OpenCC for Python
=================

An OpenCC_ converter for Python.

.. _OpenCC: https://github.com/BYVoid/OpenCC

Installation
------------

You should install OpenCC (1.0.x) library first.

Install the python library with pip::

    $ pip install OpenCC


Features
--------

1. Compatible with CPython and PyPy (c-types)
2. Cython implementation (TODO)


Usage
-----

This library has only one method::

    >>> import opencc
    >>> opencc.convert('乾坤一擲')
    >>> opencc.convert('乾坤一掷', config='s2t.json')

Config
------

Convert method accepts an additional config parameter. Available configs::

    hk2s.json
    s2hk.json
    s2t.json
    s2tw.json
    s2twp.json
    t2s.json
    tw2s.json
    tw2sp.json
