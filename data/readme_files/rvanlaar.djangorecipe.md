Djangorecipe: easy install of Django with buildout
==================================================

With djangorecipe you can manage your django site in a way that is familiar to
buildout users. For example:

- ``bin/django`` to run django instead of ``bin/python manage.py``.

- ``bin/test`` to run tests instead of ``bin/python manage.py test yourproject``.
  (Including running coverage "around" your test).

- ``bin/django`` automatically uses the right django settings. So you can have
  a ``development.cfg`` buildout config and a ``production.cfg``, each telling
  djangorecipe to use a different django settings module. ``bin/django`` will
  use the right setting automatically, no need to set an environment variable.

Djangorecipe is developed on github at
https://github.com/rvanlaar/djangorecipe, you can submit bug reports there. It
is tested with travis-ci and the code quality is checked via landscape.io:


.. image:: https://secure.travis-ci.org/rvanlaar/djangorecipe.png?branch=master
   :target: http://travis-ci.org/rvanlaar/djangorecipe/

.. image:: https://landscape.io/github/rvanlaar/djangorecipe/master/landscape.svg?style=flat
   :target: https://landscape.io/github/rvanlaar/djangorecipe/master
   :alt: Code Health



Setup
-----------

You can see an example of how to use the recipe below with some of the most
common settings::

    [buildout]
    show-picked-versions = true
    parts =
        django
    eggs =
        yourproject
        gunicorn
    develop = .
    # ^^^ Assumption: the current directory is where you develop 'yourproject'.
    versions = versions

    [versions]
    Django = 1.8.2
    gunicorn = 19.3.0

    [django]
    recipe = djangorecipe
    settings = development
    eggs = ${buildout:eggs}
    project = yourproject
    test = yourproject
    scripts-with-settings = gunicorn
    # ^^^ This line generates a bin/gunicorn-with-settings script with
    # the correct django environment settings variable already set.


Earlier versions of djangorecipe used to create a project structure for you,
if you wanted it to. Django itself generates good project structures now. Just
run ``bin/django startproject <projectname>``. The main directory created is
the one where you should place your buildout and probably a ``setup.py``.

Startproject creates a ``manage.py`` script for you. You can remove it, as the
``bin/django`` script that djangorecipe creates is the (almost exact)
replacement for it.

See django's documentation for `startproject
<https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-startproject>`_.

You can also look at `cookiecutter <https://cookiecutter.readthedocs.org/>`_.



Supported options
-----------------

The recipe supports the following options.

project
  This option sets the name for your project.

settings
  You can set the name of the settings file which is to be used with
  this option. This is useful if you want to have a different
  production setup from your development setup. It defaults to
  `development`.

test
  If you want a script in the bin folder to run all the tests for a
  specific set of apps this is the option you would use. Set this to
  the list of app labels which you want to be tested. Normally, it is
  recommended that you use this option and set it to your project's name.

scripts-with-settings
  Script names you add to here (like 'gunicorn') get a duplicate script
  created with '-with-settings' after it (so:
  ``bin/gunicorn-with-settings``). They get the settings environment variable
  set. At the moment, it is mostly useful for gunicorn, which cannot be run
  from within the django process anymore. So the script must already be passed
  the correct settings environment variable.

  **Note**: the package the script is in must be in the "eggs" option of your
  part. So if you use gunicorn, add it there (or add it as a dependency of
  your project).

eggs
  Like most buildout recipes, you can/must pass the eggs (=python packages)
  you want to be available here. Often you'll have a list in the
  ``[buildout]`` part and re-use it here by saying ``${buildout:eggs}``.

coverage
  If you set ``coverage = true``, ``bin/test`` will start coverage recording
  before django starts. The ``coverage`` library must be importable. See the
  extra coverage notes further below.

The options below are for older projects or special cases mostly:

dotted-settings-path
  Use this option to specify a custom settings path to be used. By default,
  the ``project`` and ``settings`` option values are concatenated, so for
  instance ``myproject.development``. ``dotted-settings-path =
  somewhere.else.production`` allows you to customize it.

extra-paths
  All paths specified here will be used to extend the default Python
  path for the `bin/*` scripts. Use this if you have code somewhere without a
  proper ``setup.py``.

control-script
  The name of the script created in the bin folder. This script is the
  equivalent of the `manage.py` Django normally creates. By default it
  uses the name of the section (the part between the `[ ]`). Traditionally,
  the part is called ``[django]``.

initialization
  Specify some Python initialization code to be inserted into the
  `control-script`. This functionality is very limited. In particular, be
  aware that leading whitespace is stripped from the code given.

wsgi
  An extra script is generated in the bin folder when this is set to
  `true`. This is mostly only useful when deploying with apache's
  mod_wsgi. The name of the script is the same as the control script, but with
  ``.wsgi`` appended. So often it will be ``bin/django.wsgi``.

wsgi-script
  Use this option if you need to overwrite the name of the script above.

deploy_script_extra
  In the `wsgi` deployment script, you sometimes need to wrap the application
  in a custom wrapper for some cloud providers. This setting allows extra
  content to be appended to the end of the wsgi script. For instance
  ``application = some_extra_wrapper(application)``. The limits described
  above for `initialization` also apply here.

testrunner
  This is the name of the testrunner which will be created. It
  defaults to `test`.



Coverage notes
--------------

Starting in django 1.7, you cannot use a custom test runner (like django-nose)
anymore to automatically run your tests with coverage enabled. The new app
initialization mechanism already loads your ``models.py``, for instance,
before the test runner gets called. So your ``models.py`` shows up as largely
untested.

With ``coverage = true``, ``bin/test`` starts coverage recording before django
gets called. It also prints out a report and export xml results (for recording
test results in Jenkins, for instance) and html results.

Behind the scenes, ``true`` is translated to a default of ``report xml_report
html_report``. These space-separated function names are called in turn on the
coverage instance. See the `coverage API docs
<http://coverage.readthedocs.io/en/latest/api.html>`_ for the available
functions. If you only want a quick report and xml output, you can set
``coverage = report xml_report`` instead.

Note that you cannot pass options to these functions, like html output
location. For that, add a ``.coveragerc`` next to your ``buildout.cfg``. See
the `coverage configuration file docs
<http://coverage.readthedocs.io/en/latest/config.html>`_. Here is an example::

    [run]
    omit =
        */migrations/*
        *settings.py
    source = your_app

    [report]
    show_missing = true

    [html]
    directory = htmlcov

    [xml]
    output = coverage.xml



Example configuration for mod_wsgi
---------------------------------------------------

If you want to deploy a project using mod_wsgi you could use this
example as a starting point::

    <Directory /path/to/buildout>
         Order deny,allow
         Allow from all
    </Directory>
    <VirtualHost 1.2.3.4:80>
         ServerName      my.rocking.server
         CustomLog       /var/log/apache2/my.rocking.server/access.log combined
         ErrorLog        /var/log/apache2/my.rocking.server/error.log
         WSGIScriptAlias / /path/to/buildout/bin/django.wsgi
    </VirtualHost>

Corner case: there is a problem when several wsgi scripts are combined in a
single virtual host instance of Apache. This is due to the fact that Django
uses the environment variable DJANGO_SETTINGS_MODULE. This variable gets set
once when the first wsgi script loads. The rest of the wsgi scripts will fail,
because they need a different settings modules. However the environment
variable DJANGO_SETTINGS_MODULE is only set once. The new `initialization`
option that has been added to djangorecipe can be used to remedy this problem
as shown below::

    [django]
    settings = acceptance
    initialization =
        import os
        os.environ['DJANGO_SETTINGS_MODULE'] = '${django:project}.${django:settings}'


Generating a control script for PyDev
---------------------------------------------------

Running Django with auto-reload in PyDev requires adding a small snippet
of code::

  import pydevd
  pydevd.patch_django_autoreload(patch_remote_debugger=False, patch_show_console=True)

just before the `if __name__ == "__main__":` in the `manage.py` module (or in
this case the control script, normally ``bin/django``, that is generated). The
following example buildout generates two control scripts: one for command-line
usage and one for PyDev, with the required snippet, using the recipe's
`initialization` option::

    [buildout]
    parts = django pydev
    eggs =
        mock

    [django]
    recipe = djangorecipe
    eggs = ${buildout:eggs}
    project = dummyshop

    [pydev]
    <= django
    initialization =
        import pydevd
        pydevd.patch_django_autoreload(patch_remote_debugger=False, patch_show_console=True)


Example usage of django-configurations
--------------------------------------

django-configurations (http://django-configurations.readthedocs.org/en/latest/)
is an application that helps you organize your Django settings into classes.
Using it requires modifying the manage.py file.  This is done easily using the
recipe's `initialization` option::

    [buildout]
    parts = django
    eggs =
        hashlib

    [django]
    recipe = djangorecipe
    eggs = ${buildout:eggs}
    project = myproject
    initialization =
        # Patch the manage file for django-configurations
        import os
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
        os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
        from configurations.management import execute_from_command_line
        import django
        django.core.management.execute_from_command_line = execute_from_command_line
