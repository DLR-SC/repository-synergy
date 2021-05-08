|PyPi| |Azure| |Codecov|

.. |PyPi| image:: https://badge.fury.io/py/joblib.svg
   :target: https://badge.fury.io/py/joblib
   :alt: Joblib version

.. |Azure| image:: https://dev.azure.com/joblib/joblib/_apis/build/status/joblib.joblib?branchName=master
   :target: https://dev.azure.com/joblib/joblib/_build?definitionId=3&_a=summary&branchFilter=40
   :alt: Codecov coverage

.. |Codecov| image:: https://codecov.io/gh/joblib/joblib/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/joblib/joblib
   :alt: Codecov coverage


The homepage of joblib with user documentation is located on:

https://joblib.readthedocs.io

Getting the latest code
=======================

To get the latest code using git, simply type::

    git clone git://github.com/joblib/joblib.git

If you don't have git installed, you can download a zip or tarball
of the latest code: http://github.com/joblib/joblib/archives/master

Installing
==========

You can use `pip` to install joblib::

    pip install joblib

from any directory or::

    python setup.py install

from the source directory.

Dependencies
============

- Joblib has no mandatory dependencies besides Python (supported versions are
  2.7+ and 3.4+).
- Joblib has an optional dependency on Numpy (at least version 1.6.1) for array
  manipulation.
- Joblib includes its own vendored copy of
  `loky <https://github.com/tomMoral/loky>`_ for process management.
- Joblib can efficiently dump and load numpy arrays but does not require numpy
  to be installed.
- Joblib has an optional dependency on
  `python-lz4 <https://pypi.python.org/pypi/lz4>`_ as a faster alternative to
  zlib and gzip for compressed serialization.
- Joblib has an optional dependency on psutil to mitigate memory leaks in
  parallel worker processes.
- Some examples require external dependencies such as pandas. See the
  instructions in the `Building the docs`_ section for details.

Workflow to contribute
======================

To contribute to joblib, first create an account on `github
<http://github.com/>`_. Once this is done, fork the `joblib repository
<http://github.com/joblib/joblib>`_ to have your own repository,
clone it using 'git clone' on the computers where you want to work. Make
your changes in your clone, push them to your github account, test them
on several computers, and when you are happy with them, send a pull
request to the main repository.

Running the test suite
======================

To run the test suite, you need the pytest (version >= 3) and coverage modules.
Run the test suite using::

    pytest joblib

from the root of the project.

Building the docs
=================

To build the docs you need to have sphinx (>=1.4) and some dependencies
installed::

    pip install -U -r .readthedocs-requirements.txt

The docs can then be built with the following command::

    make doc

The html docs are located in the ``doc/_build/html`` directory.


Making a source tarball
=======================

To create a source tarball, eg for packaging or distributing, run the
following command::

    python setup.py sdist

The tarball will be created in the `dist` directory. This command will
compile the docs, and the resulting tarball can be installed with
no extra dependencies than the Python standard library. You will need
setuptool and sphinx.

Making a release and uploading it to PyPI
=========================================

This command is only run by project manager, to make a release, and
upload in to PyPI::

    python setup.py sdist bdist_wheel upload_docs --upload-dir doc/_build/html
    twine upload dist/*

Updating the changelog
======================

Changes are listed in the CHANGES.rst file. They must be manually updated
but, the following git command may be used to generate the lines::

    git log --abbrev-commit --date=short --no-merges --sparse

Licensing
---------

joblib is **BSD-licenced** (3 clause):

    This software is OSI Certified Open Source Software.
    OSI Certified is a certification mark of the Open Source Initiative.

    Copyright (c) 2009-2011, joblib developpers
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of Gael Varoquaux. nor the names of other joblib
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

    **This software is provided by the copyright holders and contributors
    "as is" and any express or implied warranties, including, but not
    limited to, the implied warranties of merchantability and fitness for
    a particular purpose are disclaimed. In no event shall the copyright
    owner or contributors be liable for any direct, indirect, incidental,
    special, exemplary, or consequential damages (including, but not
    limited to, procurement of substitute goods or services; loss of use,
    data, or profits; or business interruption) however caused and on any
    theory of liability, whether in contract, strict liability, or tort
    (including negligence or otherwise) arising in any way out of the use
    of this software, even if advised of the possibility of such
    damage.**