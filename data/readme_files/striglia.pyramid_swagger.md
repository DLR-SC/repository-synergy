:PyPI: https://pypi.python.org/pypi/pyramid_swagger
:Documentation: http://pyramid-swagger.readthedocs.org/en/latest/
:Source: https://github.com/striglia/pyramid_swagger
:License: Copyright © 2014 Scott Triglia under the `BSD 3-clause <http://opensource.org/licenses/BSD-3-Clause>`_
:Build status:
    .. image:: https://travis-ci.org/striglia/pyramid_swagger.png?branch=master
        :target: https://travis-ci.org/striglia/pyramid_swagger?branch=master
        :alt: Travis CI
    .. image:: https://ci.appveyor.com/api/projects/status/ufmlmpwy1vj3yjgk/branch/master?svg=true
        :target: https://ci.appveyor.com/project/striglia/pyramid-swagger
        :alt: Appveyor (Windows CI)
:Current coverage on master:
    .. image:: https://coveralls.io/repos/striglia/pyramid_swagger/badge.png
        :target: https://coveralls.io/r/striglia/pyramid_swagger
:Persistent chat for questions:
    .. image:: https://badges.gitter.im/Join%20Chat.svg
        :alt: Join the chat at https://gitter.im/striglia/pyramid_swagger
        :target: https://gitter.im/striglia/pyramid_swagger?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


pyramid_swagger
===============

This project offers convenient tools for using Swagger to define and validate
your interfaces in a Pyramid webapp.

Full documentation is available at http://pyramid-swagger.readthedocs.org/.


How to contribute
-----------------

#. Fork this repository on Github: https://help.github.com/articles/fork-a-repo/
#. Clone your forked repository: https://help.github.com/articles/cloning-a-repository/
#. Make a feature branch for your changes:

    ::

        git remote add upstream https://github.com/striglia/pyramid_swagger.git
        git fetch upstream
        git checkout upstream/master -b my-feature-branch

#. Create and activate the virtual environment, this will provide you with all the
   libraries and tools necessary for pyramid_swagger development:

    ::

        make
        source .activate.sh

#. Make sure the test suite works before you start:

    ::

        tox -e py27    # Note: use py35 for Python 3.5, see tox.ini for possible values

#. Commit patches: http://gitref.org/basic/
#. Push to github: ``git pull && git push origin``
#. Send a pull request: https://help.github.com/articles/creating-a-pull-request/


Running a single test
*********************

Make sure you have activated the virtual environment (see above).

::

    py.test -vvv tests/tween_test.py::test_response_properties
