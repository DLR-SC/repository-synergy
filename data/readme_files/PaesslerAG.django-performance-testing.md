==========================
Django Performance Testing
==========================

.. image:: https://travis-ci.org/PaesslerAG/django-performance-testing.svg?branch=master
        :target: https://travis-ci.org/PaesslerAG/django-performance-testing

.. contents:: Performance testing for Django through your automated tests!

Don't wait with performance testing until the end of the project! We have learned
already that more frequent feedback on smaller chunks of changes is much better,
e.g.: TDD, CI, DevOps, Agile, etc.

This library helps by providing performance testing from the start -
integrating it seamlessly into your existing development cycle, without
requiring changes to your development workflow.

Unlike regular performance testing tools (``ab``, ``tsung``, etc.), this
libary relies on indirect (proxy) indicators to performance - e.g.: the number
of queries executed. It's a good rule of thumb that the more SQL there is, the
slower it will be. And this way "performance" testing won't be slower than your
normal tests! (Disclaimer: while this tool is useful, classic performance
testing is still recommended!)


Setup
=====

* install it via ``pip install django-performance-testing``
* add it to your settings and it auto-registers itself
  ::

      settings.INSTALLED_APPS = [
         ...
         'django_performance_testing',
         ...
      ]

Usage
=====

* set your limits (see below for detail)
* and run your test ``manage.py test <your app>``

For any limit violations, there will be a test failure.

After the test run, you could generate the `Worst Items Report`
by running ``manage.py djpt_worst_report``.

The data is collected into ``settings.DJPT_DATAFILE_PATH`` file,
or into ``djpt.results_collected``.


Supported Limits
================

Querycount
----------

Sets the limit in the number of queries executed inside the given scope.
Limits can be set for the ``total`` number of queries, or more specifically,
based on types of queries - ``read`` (``SELECT``), ``write`` (
``INSERT``, ``UPDATE``, ``DELETE``), and ``other`` (e.g.:
transaction (savepoints)).

When no (or ``None``) value is provided for a given limit type, that is 
ignored during the check, as if there were no limit rules for. Thus it's 
possible to only focus on no write queries, while ignoring all the other queries
that might be executed.

Time
----

Sets the limit on the ``total`` elapsed seconds.

Setting Limits
==============

Predefined limit points
-----------------------

Following are the keys that are currently supported for
``settings.PERFORMANCE_LIMITS`` dictionary

* ``django.test.client.Client`` - every call to its ``request`` method
  is limited, i.e.: ``GET``, ``POST``, etc.
* ``Template.render`` - every ``render`` call is checked for limits.
  Note: it's   recursive, i.e.: `include` and similar tags result in a check
* for testcase classes, there is

  * ``test method`` - the actual various ``unittest`` test methods that
    you write for your app
  * ``test setUp`` - the ``TestCase.setUp`` methods you write for your test
    classes
  * ``test tearDown`` - the ``TestCase.tearDown`` methods you write for your
    test classes
  * ``test setUpClass`` - the ``TestCase.setUpClass`` methods you write for
    your test classes
  * ``test tearDownClass`` - the ``TestCase.tearDownClass`` methods you write for
    your test classes

For each of the above keys, there is a ``dict`` that holds the actual limits.
The keys are the limit types (``queries`` and/or ``time``), and the value is
yet another ``dict``, holding the actual limit values. For valid values, see
the description of the limits above, or look at the sample settings

Sample Settings
~~~~~~~~~~~~~~~

::

    PERFORMANCE_LIMITS = {
        'test method': {
            'queries': {'total': 50},  # want to keep the tests focused
            'time': {'total': 0.2},  # want fast integrated tests, so aiming for 1/5 seconds
        },
        'django.test.client.Client': {
            'queries': {
                'read': 30,
                'write': 8,  # do not create complex object structures in the web
                             # process
            },
        },
        'Template.render': {
            'queries': {
                'write': 0,  # rendering a template should never write to the database!
                'read': 0
            }
        }
    }

Ad-Hoc Limits
-------------

While the built-in measurement points are great, sometimes, when profiling
and trying to improve sections of the code, more granular limits are needed.

Context managers for python/django code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
All limits can be used as context managers, e.g.:


::

    from django_performance_testing.queries import QueryBatchLimit
    from django_performance_testing.timing import TimeLimit
    ...
    
    def my_method_with_too_many_queries(request):
        with QueryBatchLimit(write=0, read=10):  # initialize form
            form = MyForm(request.POST)
        with QueryBatchLimit(write=0, read=3):  # validate it
            is_valid = form.is_valid()
        if is_valid:
            with QueryBatchLimit(read=0, write=8):  # save it
                form.save()
            with QueryBatchLimit(read=0, write=0):  # redirect
                return HttpResponseRedirect(...)
        else:
            with QueryBatchLimit(write=0):  # render form
                with TimeLimit(total=0.01):   # we need superfast templates
                    return form_invalid(form)

Template tag for templates
~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a single template tag that can be used after ``{% load djpt_limits %}``,
namely ``djptlimit``. It takes

* a single string positional argument, the name of the limit - as per
  ``settings.DJPT_KNOWN_LIMITS_DOTTED_PATHS``, see below
* keyword arguments that will be passed to the actual limit.

It can be used directly in your tempaltes like

::

    {% load djpt_limits %}
    {% djptlimit 'TimeLimit' total=3 %}
    {{ slow_rendering }}
    {% enddjptlimit %}

When debugging more complext template hierarchies, where e.g.: the slow part
might not even be our own template, then
`{{ block.super }} <https://docs.djangoproject.com/en/1.10/ref/templates/language/>`_
could be helpful

::

    {% extends "base.html" %}
    {% block title %}
    {% djptlimit 'QueryBatchLimit' read=3 %}
    {{ block.super }}
    {% enddjptlimit %}
    {% endblock %}

``settings.DJPT_KNOWN_LIMITS_DOTTED_PATHS``
...........................................

This is an array of full class paths, similar to how
`settings.MIDDLEWARE <https://docs.djangoproject.com/en/1.10/topics/http/middleware/#activating-middleware>`_
are defined, e.g.: ``['django_performance_testing.timing.TimeLimit']``.

The name of the limit is the classname part of the class.

Unless you have written a custom limit, this setting doesn't need to be set explicitly,
as the app has defaults that include all limits.

Release Notes
=============

* 0.7.3 - conform to latest flake8
* 0.7.1 - bugfix a test
* 0.7.0 - separate data collection and reporting

  * introduce ``djpt_worst_report`` management command

  * backwards incompatibe changes:

    * Collectors are expected to have ``get_sample_results`` method to allow easier and 
      more realistic testing
    * Worst Items Report is not printed anymore after the test run.
    * ``settings.DJPT_PRINT_WORST_REPORT`` doesn't have much effect anymore, will be
      dropped in a subsequent release


* 0.6.1

  * add support for Django 1.11 (and thus for Python 3.6 too)

* 0.6.0

  * django test runner integration now uses ``settings.DJPT_KNOWN_LIMITS_DOTTED_PATHS``
    for the collectors/limits it initializes, thus allowing 3rd party collectors/limits
  * new predefined limit points: ``test setUp``, ``test tearDown``, ``test setUpClass``,
    ``test tearDownClass``

* 0.5.0

  * backwards incompatible - remove ``--djpt-no-report`` and use
    ``settings.DJPT_PRINT_WORST_REPORT`` instead to suppress the printing of the report
    (to address incompatibilities with third party testrunner extensions)

* 0.4.0

  * add ``--djpt-no-report`` argument to disable output of performance report on shell

* 0.3.0

  * introduced ``django_performance_testing.core.limits_registry``. This keeps
    track of all limits, and enforces that across the django project all limits
    have unique names. This also warranted the introduction of
    ``settings.DJPT_KNOWN_LIMITS_DOTTED_PATHS``.
  * introduced ``djptlimit`` template tag to be used for ad-hoc template
    debugging

* 0.2.0

  * add timing measurement that can be limited
  * remove uniqueness check for ``collector.id_``, as the problems it caused
    for testing outweighed its benefit for developer debugging aid
  * backwards incompatible:

    * change how settings based limits are specified
    * change the worst report data output/data structure

* 0.1.1 - bugfix release

  * bugfix: attributes set by on test methods (e.g.: ``@unittest.skip``)
    are now recognizable again and not lost due to the library's patching

* 0.1.0 - initial release

  * supports Django 1.8, 1.9, 1.10 on python 2.7, 3.3, 3.4, and 3.5
  * query counts are reported and can be limited, by categories -
    ``read``, ``write``, ``other``, and ``total`` 
  * support ad-hoc limits by using it as a context manager
  * predefined limits support:

    * ``django.test.client.Client`` - all calls to its request method
    * actual ``unittest`` ``test_<foo>`` methods
    * ``Template.render``

.. contributing start

Contributing
============

As an open source project, we welcome contributions.

The code lives on `github <https://github.com/PaesslerAG/django-performance-testing>`_.

Reporting issues/improvements
-----------------------------

Please open an `issue on github <https://github.com/PaesslerAG/django-performance-testing/issues/>`_
or provide a `pull request <https://github.com/PaesslerAG/django-performance-testing/pulls/>`_
whether for code or for the documentation.

For non-trivial changes, we kindly ask you to open an issue, as it might be rejected.
However, if the diff of a pull request better illustrates the point, feel free to make
it a pull request anyway.

Pull Requests
-------------

* for code changes

  * it must have tests covering the change. You might be asked to cover missing scenarios
  * the latest ``flake8`` will be run and shouldn't produce any warning
  * if the change is significant enough, documentation has to be provided

Setting up all Python versions
------------------------------

::

    sudo apt-get -y install software-properties-common
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    for version in 3.3 3.5 3.6; do
      py=python$version
      sudo apt-get -y install ${py} ${py}-dev
    done

Code of Conduct
---------------

As it is a Django extension, it follows
`Django's own Code of Conduct <https://www.djangoproject.com/conduct/>`_.
As there is no mailing list yet, please just email one of the main authors
(see ``setup.py`` file or `github contributors`_)


.. contributing end


.. _github contributors: https://github.com/PaesslerAG/django-performance-testing/graphs/contributors
