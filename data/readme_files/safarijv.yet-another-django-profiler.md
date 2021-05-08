yet-another-django-profiler README
==================================

.. image:: https://img.shields.io/pypi/v/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/

.. image:: https://travis-ci.org/safarijv/yet-another-django-profiler.svg?branch=master
    :target: https://travis-ci.org/safarijv/yet-another-django-profiler

.. image:: https://coveralls.io/repos/safarijv/yet-another-django-profiler/badge.svg
    :target: https://coveralls.io/r/safarijv/yet-another-django-profiler

.. image:: https://img.shields.io/pypi/pyversions/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/l/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: License

.. image:: https://img.shields.io/pypi/dm/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/status/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/wheel/yet-another-django-profiler.svg
    :target: https://pypi.python.org/pypi/yet-another-django-profiler/
    :alt: Wheel Status

Yet Another Django Profiler attempts to combine the best features of assorted
other Django profiling utilities that have been created over the years.
(For more background information, see my
`blog post <http://blog.safariflow.com/2013/11/21/profiling-django-via-middleware/>`_
on the topic.)

Installation
------------
First, get the code via pip install::

    pip install yet-another-django-profiler

Then add ``yet_another_django_profiler.middleware.ProfilerMiddleware`` to your
``MIDDLEWARE`` or ``MIDDLEWARE_CLASSES`` Django setting (typically at the end
of the list, if you want to include profiling data on the other middleware
that's in use).  If you want to generate call graphs with the middleware, you
also need to install `Graphviz <http://www.graphviz.org/Download.php>`_.  If
you want to use the "profile" management command, you'll also need to add
``yet_another_django_profiler`` to the ``INSTALLED_APPS`` setting.

Middleware Usage
----------------
The simplest usage is to just add a ``profile`` parameter to the URL of a
Django view.  This uses Graphviz to generate a PDF representation of the call
graph for the code executed to perform the view, and returns that as the
response to the request instead of the rendered view itself.  So calling a
URL like ``http://localhost:8000/admin/?profile`` shows a PDF like
`this <https://github.com/safarijv/yet-another-django-profiler/blob/master/docs/admin_call_graph.pdf?raw=true>`_
in the browser.

Alternatively, you can display a table of called functions ordered by the
desired statistic by using a URL such as ``http://localhost:8000/?profile=time``.
The available sorting options are:

* ``calls`` (call count)

* ``cumulative`` (cumulative time)

* ``file`` (file name, same as ``module``)

* ``module`` (file name, same as ``file``)

* ``pcalls`` (primitive call count)

* ``line`` (line number)

* ``name`` (function name)

* ``nfl`` ( function name/file/line)

* ``stdname`` (standard name)

* ``time`` (internal time)

By default, only the top 20% of function calls are included in the table.  To
change that, add a ``fraction`` parameter with the desired display ratio
(hence the default value is ``fraction=.2``).  Alternatively, you can
instead specify a maximum number of function calls to display using the
``max_calls`` parameter.  And if you specify a regular expression with the
``pattern`` parameter, only calls of functions whose names match the
specified pattern will be displayed.  (I'd recommend sticking to basic
sub-strings unless you really enjoy figuring out how to URL-escape special
characters.) By default when using yappi it will use `cpu` clock type if
what you want is `wall` time you can use ``clock=wall``.

Views which return a StreamingHttpResponse can be profiled, but the profiling
data stops at the return of the response from the view; the iteration over the
content isn't profiled.

If you forget the available sorting options and such, you can use
``profile=help`` as a request parameter to display the usage instructions in
the browser.

Management Command Usage
------------------------
yet-another-django-profiler includes a ``profile`` management command which can
be used to profile other Django management commands::


    usage: manage.py profile [-h] [--version] [-v {0,1,2,3}]
                             [--settings SETTINGS] [--pythonpath PYTHONPATH]
                             [--traceback] [--no-color] [-o PATH] [-s SORT]
                             [-f FRACTION] [-m MAX_CALLS] [-p PATTERN]
                             [-b BACKEND] [-c CLOCK]
                             other_command ...

    Profile another Django management command

    positional arguments:
      other_command         The management command to be profiled
      command_arguments     Arguments of the management command being profiled

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      -o PATH, --output PATH
                            Path to a file in which to store the profiling output
                            (required if generating a call graph PDF, other
                            results are output to the console by default)
      -s SORT, --sort SORT  Statistic by which to sort the profiling data (default
                            is to generate a call graph PDF instead)
      -f FRACTION, --fraction FRACTION
                            The fraction of total function calls to display (the
                            default of .2 is omitted if max-calls or pattern are
                            specified)
      -m MAX_CALLS, --max-calls MAX_CALLS
                            The maximum number of function calls to display
      -p PATTERN, --pattern PATTERN
                            Regular expression filter for function display names
      -b BACKEND, --backend BACKEND
                            Profiler backend to use (cProfile or yappi)
      -c CLOCK, --clock CLOCK
                            Yappi clock type to use (cpu or wall)

Sample usage:

* ``django-admin.py profile -s time test --failfast my_app/my_module.py:TestClass.test_function``
* ``django-admin.py profile -o ~/Downloads/call_graph.pdf collectstatic``

Settings
--------
The middleware is designed to be available whenever the ``DEBUG`` setting is
True, and removes itself from the middleware chain otherwise (so it can safely
be left in the dependencies for production deployments without performance or
security problems).  If for some reason you want to change this behavior, you
can set the ``YADP_ENABLED`` boolean setting directly to determine whether the
middleware is active or not.

If you have pages where the default profiling parameter names conflict with
existing parameters in the application, you can choose different ones via the
following settings:

* ``YADP_PROFILE_PARAMETER`` (default is "profile")

* ``YADP_FRACTION_PARAMETER`` (default is "fraction")

* ``YADP_MAX_CALLS_PARAMETER`` (default is "max_calls")

* ``YADP_PATTERN_PARAMETER`` (default is "pattern")

* ``YADP_CLOCK_PARAMETER`` (default is "cpu")

You can use Yappi (`Yet Another Python Profiler <https://code.google.com/p/yappi/>`_)
as a profiler backend instead of cProfile. To do that just specify
``YADP_PROFILER_BACKEND = 'yappi'`` in the settings.  Note that Yappi does not
currently work on PyPy or CPython 3.2.

An effort is made to convert the absolute Python file paths provided by the
profiler to full-qualified module names (which are typically shorter and
easier to understand at a glance).  The default rules should work in most cases
but can be customized via the following settings:

* ``YADP_MODULE_PARENT_DIR_PATTERNS`` is a list of regular expression patterns.
  Everything in a module path up to and including a match of one of these
  patterns is removed from statistic tables and call graphs.  The default list
  is ``[r'\.egg[/\\]', r'site-packages[/\\]', r'python\d+\.\d+[/\\]']``.  The
  absolute path of the current working directory is also pruned.

* If the previous setting doesn't allow sufficient customization for your
  needs, the ``YADP_PATH_TO_MODULE_FUNCTION`` setting can be used to completely
  replace the function used for this task.  It should be the fully qualified
  name of your custom function, which takes an absolute file path as input and
  returns what you want to appear in the profiling output to represent that
  path.

In order to get simple and meaningful profiling data, a
`few other changes <https://github.com/safarijv/yet-another-django-profiler/blob/master/docs/settings.rst>`_
to your settings may be in order.

Running Tests
-------------
To run tests in all currently supported combinations of Python and Django, run
``tox``.  If you're running tox from a Python 2 environment, you can instead
run ``detox`` to execute all the test environments in parallel.  See the
`tox documentation <https://tox.readthedocs.org/en/latest/>`_ for instructions
on running a single test case or environment.

Internationalization
--------------------
Translations of text that can appear in the profiling results pages are managed
on `Transifex <https://www.transifex.com/projects/p/yet-another-django-profiler/>`_.
Feel free to request to be added as translator for a not-yet-supported language.
Django recommends not translating management command text for
`assorted technical reasons <https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/#management-commands-and-locales>`_,
so those phrases currently aren't included.

For development tasks involving the translations (uploading message changes to
Transifex or fetching the latest translations from it), use
`transifex-client <http://docs.transifex.com/guides/client>`_.  By default, pip
installs a rather old stable version so you may want to specify a newer one::

    pip install transifex-client==0.11b3

When running the makemessages or compilemessages management commands, do so
from the ``yet_another_django_profiler`` directory.

License
-------
Due to gprof2dot being licensed under the LGPL v3, that's the license that
applies to this package as a whole.  However, the rest of the source files are
individually licensed under a more permissive 3-clause BSD license (so it is
possible to assemble a BSD-licensed package that omits only the call graph
generation feature).
