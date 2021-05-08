.. image:: https://img.shields.io/pypi/v/backports.lzma.svg
   :alt: Package on Python Package Index (PyPI)
   :target: https://pypi.python.org/pypi/backports.lzma
.. image:: https://img.shields.io/conda/vn/conda-forge/backports.lzma.svg
   :alt: Conda package from conda-forge channel
   :target: https://anaconda.org/conda-forge/backports.lzma
.. image:: https://img.shields.io/conda/vn/anaconda/backports.lzma.svg
   :alt: Conda package from Anaconda (default) channel
   :target: https://anaconda.org/anaconda/backports.lzma
.. image:: https://img.shields.io/travis/peterjc/backports.lzma/master.svg?label=master&logo=travis
   :alt: Linux testing with TravisCI
   :target: https://travis-ci.org/peterjc/backports.lzma/branches
.. image:: https://img.shields.io/appveyor/ci/peterjc/backports-lzma/master.svg?label=master&logo=CircleCI
   :alt: Windows testing with AppVeyor
   :target: https://ci.appveyor.com/project/peterjc/backports-lzma/history
.. image:: https://img.shields.io/pypi/dm/backports-lzma.svg
   :alt: PyPI downloads
   :target: https://pypistats.org/packages/backports-lzma

Introduction
============

Python 3.3 onwards includes module ``lzma`` in the standard library, providing
support for working with LZMA and XZ compressed files via the XZ Utils C
library (XZ Utils is in a sense LZMA v2). See:

* Python's lzma - http://docs.python.org/dev/library/lzma.html
* XZ Utils - http://tukaani.org/xz/

This code is a backport of the Python 3.3 standard library module ``lzma`` for
use on older versions of Python where it was not included. It is available
from PyPI (released downloads only) and GitHub (repository):

* PyPI - http://pypi.python.org/pypi/backports.lzma/
* GitHub - https://github.com/peterjc/backports.lzma

There are some older Python libraries like PylibLZMA and PyLZMA but these are
both using LZMA Utils (not XZ Utils, so they have no XZ support).

* PylibLZMA - http://pypi.python.org/pypi/pyliblzma
* PyLZMA - http://pypi.python.org/pypi/pylzma/
* LZMA Utils - http://tukaani.org/lzma/


Supported Platforms
===================

The ``lmza`` module provided with Python 3.3 should work on all the main
operating systems, so in theory so too should this backport:

* Mac OS X: Tested under Python 2.6, 2.7, 3.0 to 3.4 inclusive
* Linux: Tested under Python 2.6, 2.7, 3.0 to 3.6 inclusive
* Windows: Tested under Python 2.7, 3.6 covering 32-bit and 64-bit,
  and MSVC and mingw32 compilers

Other than some minor changes in the exceptions for some errors, based on the
unit tests everything seems to be working fine.

Support under Python 2.6 and 2.7 appears to be working in that all the
appropriate unit tests now pass. Supporting older verions of Python 2 is
probably going to be too much work.

We now also support the PyPy implementation of Python 2.7, currently tested
with PyPy 5.8.0. It does not currently work on the  PyPy implementation of
Python 3, but that comes with the ``lzma`` standard library module anyway.


Installation
============

I recommend the Conda packaging system which supports Linux, MacOS and
Windows. Thanks to the ``conda-forge`` package you should be able to install
this library with one line, and have the dependencies handled automatically::

    $ conda install -c conda-forge backports.lzma

If you are on Linux, there is a good chance that the system packages will
include this library and handle the dependencies, e.g. on RedHat/CentOS try::

    $ sudo yum install python-backports-lzma

Otherwise, first you must install the XZ Utils C library. On RedHat or
CentOS Linux sytems, try::

    $ sudo yum install xz-devel

On a Debian based Linux distribution use::

    $ sudo apt-get install liblzma-dev

Otherwise do this from source, this is what I do on Mac OS X::

    $ curl -L -O http://tukaani.org/xz/xz-5.0.4.tar.gz
    $ tar -zxvf xz-5.0.4.tar.gz
    $ cd xz-5.0.4
    $ ./configure --prefix=$HOME
    $ make
    $ make check
    $ make install

Now you can install this ``lzma`` backport. If using ``pip``, this should
work::

    $ pip install backports.lzma

Otherwise, you can compile this the old fashioned way. First download and
decompress the source code, or clone the github repository::

    $ git clone git://github.com/peterjc/backports.lzma.git
    $ cd backports.lzma
    $ python setup.py install
    $ cd test
    $ python test_lzma.py

To install for a specific version of Python, replace ``python`` (which will
use the system's default Python) in the above with a specific version like
``python2``, ``python2.6`` or ``python3``, ``python3.2``, etc.

This should find the XZ Util header file and library automatically (and will
check for a local install under your home directory). You should now be able
to import the backport from Python as shown below.

If you are trying to install this under the system Python, you will need
admin rights and replace ``python setup.py install`` with
``sudo python setup.py install`` instead.


Usage
=====

The expected usage is as follows if you want to prioritise the standard
library provided lzma if present::

    try:
        import lzma
    except ImportError:
        from backports import lzma
    #Then use lzma as normal, for example:
    assert b"Hello!" == lzma.decompress(lzma.compress(b"Hello!"))

Please refer to the ``lzma`` documentation online:
http://docs.python.org/dev/library/lzma.html

Note that while ``lzma`` should be available on Python 3.3 onwards, you can
still install the backport. This is useful for two reasons, first testing the
two act the same way, and second it is possible that your Python installation
lacks the standard library ``lzma``. This can happen if Python was installed
from source and XZ Utils was not available. If this was a systems level Python
install, as a user you could still install XZ Utils and this backport under
your own account.

This is using the shared ``backports`` namespace introduced by Brandon Rhodes
as documented here: http://pypi.python.org/pypi/backports/ and
http://bitbucket.org/brandon/backports


Revisions
=========

* v0.0.1 - January 2013
   * First public release
* v0.0.2 - April 2013
   * Fix the seekable attribute on Python 2 (Tomer Chachamu)
   * More search paths for lib/include headers (Wynn Wilkes)
* v0.0.3 - June 2014
   * Supports unicode filenames on Python 2 (Irving Reid)
* v0.0.4 - September 2014
   * Declare namespace package to avoid warnings (Ralph Bean)
     (Later retracted from PyPI due to installation problems with
     ``setuptools`` versus ``distutils``, see GitHub issue #8 and #9).
* v0.0.5 - June 2016
   * Backported fix for Python Issue 19839 to ignore non-LZMA trailing data
     (original Python 3.5.1 patch by Nadeem Vawda, backported by Deroko, see
     GitHub pull request #5).
* v0.0.6 - June 2016
   * Updated namespace packaging declaration now required by more recent
     versions of setuptools which prevented simple installation of v0.0.4
     and v0.0.5 from PyPI.
* v0.0.7 - February 2017
   * Check and prefer the ``sys.prefix`` at installation time to find the
     ``lib`` and ``include`` headers (John Kirkham).
* v0.0.8 - February 2017
   * Switch to using ``README.rst`` for this document in order to display
     nicely on PyPI.
* v0.0.9 - 3 January 2018
   * Now compiles under Windows with passing tests, checked under AppVeyor
     (see GitHub pull request #25 by Nehal J Wani).
* v0.0.10 - 8 January 2018
   * Now supports PyPy (specifically their Python 2 implementation, but not
     yet pypy3 which implements Python 3; see GitHub pull requests #27 and
     #29 by Michał Górny).
* v0.0.11 - 16 May 2018
   * Should address namespace issues in v0.0.4, v0.0.5 and v0.0.6 related to
     a problem in setuptools, and causing side effects with other backports
     (see pull request #32 from Toshio Kuratomi, and issues #8, #16 and #28).
* v0.0.12 - 30 June 2018
   * Fixes locale issue in ``setup.py`` under Python 3 (see #33 reported by
     Ben Hearsum).
* v0.0.13 - 11 July 2018
   * Use ``setuptools`` instead of ``distutils`` if available, useful for
     compiling your own wheel or egg files (see #34 from @wiggin15).
* v0.0.14 - 12 September 2019
   * Back ported fix decompressing files using ``FORMAT_ALONE`` without
     end markers (see #40 from Ma Kin and Python issue 21872).


Contributors
============

The initial Python lzma module implementation was by Per Øyvind Karlsen, which
was then rewritten by Nadeem Vawda and included with Python 3.3. Based on this
work, it was backported to also run on Python 2.6, 2.7 and 3.0, 3.1 and 3.2 by
Peter Cock.

Later contributors include: Tomer Chachamu, Wynn Wilkes, Irving Reid,
Ralph Bean, Deroko, John Kirkham, Nehal J Wani, Michał Górny, Toshio Kuratomi,
Ma Lin.


Bug Reports
===========

Please report any reproducible bugs via the GitHub issue tracker at
https://github.com/peterjc/backports.lzma/issues including details about
your operating system, version of Python, XY Utils, the lzma backport etc.
Reproducible test cases are particularly helpful.

If you can demonstrate a problem in this backport but not in the ``lzma``
module included with Python 3.3 or later, then it is clearly something we
will need to fix.

Any issues in the ``lzma`` module as bundled with Python 3.3 or later
should be reported to the Python project at http://bugs.python.org instead
(and we can hopefully apply any official fix to the backport as well).


Release Process
===============

The version is incremented in file ``backports/lzma/__init__.py`` (from where
``setup.py`` will extract it at runtime).

After testing locally and with TravisCI (see below), new releases are tagged
in git as follows::

    $ git tag backports.lzma.vX.X.X

Tags must explicitly be pushed to GitHub::

    $ git push origin master --tags

I then use the following to upload a new release to the Python Packaging Index
(PyPI)::

    $ python setup.py sdist
    $ twine upload dist/backports.lzma-X.X.X.tar.gz

If not already installed, try ``pip install twine``.

The update then appears on http://pypi.python.org/pypi/backports.lzma/


Automated Testing
=================

TravisCI is being used for continuous integration testing under Linux, see
https://travis-ci.org/peterjc/backports.lzma

.. image:: https://img.shields.io/travis/peterjc/backports.lzma/master.svg
   :alt: Linux testing with TravisCI
   :target: https://travis-ci.org/peterjc/backports.lzma/branches

Similarly, AppVeyor is being used for testing under Windows, see:
https://ci.appveyor.com/project/peterjc/backports-lzma/history

.. image:: https://img.shields.io/appveyor/ci/peterjc/backports-lzma/master.svg
   :alt: Windows testing with AppVeyor
   :target: https://ci.appveyor.com/project/peterjc/backports-lzma/history
