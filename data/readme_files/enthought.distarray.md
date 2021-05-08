.. Travis badge
.. image:: https://travis-ci.org/enthought/distarray.svg?branch=master
   :target: https://travis-ci.org/enthought/distarray

.. codecov badge
.. image:: http://codecov.io/github/enthought/distarray/coverage.svg?branch=master
    :target: http://codecov.io/github/enthought/distarray?branch=master

.. readthedocs badge
.. image:: https://readthedocs.org/projects/distarray/badge/?version=master
   :target: http://distarray.readthedocs.org/en/master/

.. pypi badge
.. image:: https://badge.fury.io/py/distarray.svg
    :target: http://badge.fury.io/py/distarray

.. All content before the next comment will be stripped off for release.
.. *** begin README content ***

DistArray
=========

*Think globally, act locally.*

DistArray provides general multidimensional NumPy-like distributed arrays to
Python.  It intends to bring the strengths of NumPy to data-parallel
high-performance computing.  DistArray has a similar API to `NumPy`_.

DistArray is ready for real-world testing and deployment; however, the project
is still evolving rapidly, and we appreciate continued input from the
scientific-Python community.

DistArray is for users who

* know and love Python and NumPy,
* want to scale NumPy to larger distributed datasets,
* want to interactively play with distributed data but also
* want to run batch-oriented distributed programs;
* want an easier way to drive and coordinate existing MPI-based codes,
* have a lot of data that may already be distributed,
* want a global view ("think globally") with local control ("act locally"),
* need to tap into existing parallel libraries like Trilinos, PETSc, or
  Elemental,
* want the interactivity of IPython and the performance of MPI.

DistArray is designed to work with other packages that implement the
`Distributed Array Protocol`_.

.. _Distributed Array Protocol: http://distributed-array-protocol.readthedocs.org
.. _NumPy: http://www.numpy.org

Please see our documentation at `readthedocs`_ (or in the `docs` directory) for
more, or ask us questions on our `mailing list`_.  Pull requests gladly accepted.


.. _readthedocs: http://distarray.readthedocs.org
.. _mailing list: https://groups.google.com/forum/#!forum/distarray
