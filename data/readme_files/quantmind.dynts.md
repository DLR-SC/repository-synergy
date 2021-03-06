A statistic package for python with enphasis on timeseries analysis.
Built around numpy_, it provides several back-end timeseries classes including R-based objects via rpy2_.
It is shipped with a domain specific language for timeseries analysis
and manipulation built on to of ply_.

|

:Badges: |license|  |pyversions| |status| |pypiversion|
:Master CI: |master-build| |coverage-master|
:Documentation: http://quantmind.github.io/dynts/
:Dowloads: http://pypi.python.org/pypi/dynts/
:Source: http://github.com/quantmind/dynts
:Platforms: Linux, OSX, Windows. Python 3.5 and above
:Keywords: timeseries, quantitative, finance, statistics, numpy, R, web

|

.. contents::
    :local:


Timeseries
========================

To create a timeseries object directly::

	>>> from dynts import timeseries
	>>> ts = timeseries('test')
	>>> ts.type
	'numpy'
	>>> ts.name
	'test'
	>>> ts
	TimeSeries:numpy:test
	>>> str(ts)
	'test'


DSL
=======
The package comes with a Domain-Specific-Language (DSL_) dedicated
to timeserie analysis and manipulation.
This is a simple multiplication::

	>>> from dynts import api
	>>> e = api.parse('2*GOOG')
	>>> e
	2.0 * goog
	>>> len(e)
	2
	>>> list(e)
	[2.0, goog]
	>>> ts = api.evaluate(e).unwind()
	>>> ts
	TimeSeries:numpy:2.0 * goog
	>>> len(ts)
	251


Requirements
=====================
There are few requirements that must be met:

* python_ 2.6 up to python 3.3.
* numpy_ version 1.5.1 or higher for arrays and matrices.
* ply_ version 3.3 or higher, the building block of the DSL_.
* ccy_ for date and currency manipulation.

R backend
===============================
Depending on the back-end used, additional dependencies need to be met.
For example, there are back-ends depending on the following R packages:

* rpy2_ if an R_ TimeSeries back-end is used (default).
* zoo_ and PerformanceAnlytics_ for the ``zoo`` back-end (currently the default one)
* timeSeries_ for the ``rmetrics`` back-end

Installing rpy2_ on Linux is straightforward, on windows it requires the
`python for windows`__ extension library.

Optional Requirements
===============================

* cython_ for performance. The library is not strictly dependent on cython, however its usage
  is highly recommended. If available several python modules will be replaced by more efficient compiled C code.
* xlwt_ to create spreadsheet from timeseries.
* matplotlib_ for plotting.
* djpcms_ for the ``web.views`` module.

__ http://sourceforge.net/projects/pywin32/files/


.. _running-tests:

Running Tests
=================
There are three types of tests available:

* ``regression`` for unit and regression tests.
* ``profile`` for analysing performance of different backends and impact of cython_.
* ``bench`` same as ``profile`` but geared towards speed rather than profiling.

From the distribution directory type::

	python setup.py test

This will run by default the regression tests. To run a profile test
type::

	python runtests.py -t profile <test-name>

where ``<test-name>`` is the name of a profile test.
To obtain a list of available tests for each test type, run::

	python setup.py test -l

for unit tests, or::

	python runtests.py -t profile --list

for profile, or::

	python runtests.py -t bench --list

from benchmarks.

It is needed since during tests some data is fetched from google finance.

To access coverage of tests you need to install the coverage_ package and run the tests using::

	coverage run runtests.py

and to check out the coverage report::

	coverage report -m



.. |pypiversion| image:: https://badge.fury.io/py/dynts.svg
    :target: https://pypi.python.org/pypi/dynts
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/dynts.svg
  :target: https://pypi.python.org/pypi/dynts
.. |license| image:: https://img.shields.io/pypi/l/dynts.svg
  :target: https://pypi.python.org/pypi/dynts
.. |status| image:: https://img.shields.io/pypi/status/dynts.svg
  :target: https://pypi.python.org/pypi/dynts
.. |master-build| image:: https://travis-ci.org/quantmind/dynts.svg?branch=master
  :target: https://travis-ci.org/quantmind/dynts
.. |coverage-master| image:: https://coveralls.io/repos/github/quantmind/dynts/badge.svg?branch=master
  :target: https://coveralls.io/github/quantmind/dynts?branch=master
.. _numpy: http://numpy.scipy.org/
.. _ply: http://www.dabeaz.com/ply/
.. _rpy2: http://rpy.sourceforge.net/rpy2.html
.. _DSL: http://en.wikipedia.org/wiki/Domain-specific_language
.. _R: http://www.r-project.org/
.. _ccy: http://code.google.com/p/ccy/
.. _zoo: http://cran.r-project.org/web/packages/zoo/index.html
.. _PerformanceAnlytics: http://cran.r-project.org/web/packages/PerformanceAnalytics/index.html
.. _timeSeries: http://cran.r-project.org/web/packages/timeSeries/index.html
.. _Python: http://www.python.org/
.. _xlwt: http://pypi.python.org/pypi/xlwt
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _djpcms: http://djpcms.com
.. _coverage: http://nedbatchelder.com/code/coverage/
.. _cython: http://www.cython.org/
.. _flot: http://code.google.com/p/flot/
.. _Sparklines: http://www.omnipotent.net/jquery.sparkline/
