multidimensional_urlencode
==========================

Python library to urlencode a multidimensional dict.

.. image:: https://travis-ci.org/uber/multidimensional_urlencode.png?branch=master
    :target: https://travis-ci.org/uber/multidimensional_urlencode

Quick Start
===========

multidimensional_urlencode lets you url encode a multidimensional dict:

.. code-block:: python

    >>> try:
    ...     from urllib.parse import unquote
    ... except:
    ...     from urllib import unquote
    >>> from multidimensional_urlencode import urlencode
    >>> e = urlencode({"a": {"b": {"c": [1, 2, 3], "d": "e"}}})
    >>> unquote(e)
    'a[b][c][]=1&a[b][c][]=2&a[b][c][]=3&a[b][d]=e'

Documentation
=============

`Documentation can be found here <http://multidimensional-urlencode.readthedocs.org/en/latest/>`_

Authors
=======

* Sam Marcellus <marcellus@uber.com>
* Charles-Axel Dein <charles@uber.com>

License
=======

Available under the MIT License.

Copyright Uber 2017
