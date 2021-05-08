Retrace
=======

Retrace your steps and try again.
---------------------------------

|PyPI Downloads| |PyPI Version| |Build Status|

Retrace provides a configurable decorator which allows you to wrap
Python callables and retry them on errors or other specific conditions.

Docs
----

It is simple and elegant.

See the documentation at:

::

   http://d0ugal.github.io/retrace/

Quickstart
----------

First, ``pip install retrace``.

.. code:: python

   import retrace

   @retrace.retry
   def unstable():
       # ...

Boom. Done.

This function will now be retied up to 5 times if it raises an
exception. You can customise how often it is retried, limit the
exceptions and add validators to further verify the return value. Check
out the docs for all this and more.

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/retrace.svg
   :target: https://pypi.python.org/pypi/retrace
.. |PyPI Version| image:: https://img.shields.io/pypi/v/retrace.svg
   :target: https://pypi.org/project/retrace/
.. |Build Status| image:: https://img.shields.io/travis/d0ugal/retrace/master.svg
   :target: https://travis-ci.org/d0ugal/retrace