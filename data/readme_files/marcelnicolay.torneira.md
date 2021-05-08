Torneira - Lightweight Web Framework
====================================

Torneira is a lightweight web framework build on top of Tornado_. It's name
came from the idea of getting rapid and fluid development ('torneira' is the
portuguese word for water tap).

.. image:: https://secure.travis-ci.org/marcelnicolay/torneira.png?branch=master
   :alt: Build Status
   :target: https://secure.travis-ci.org/marcelnicolay/torneira

Installation
------------

Torrneira is available under PyPI_. You can install using pip:

    $ pip install torneira

Quick start
-----------

To build an app using torneira, you just need 3 files: one for your urls
definitions (normally urls.py), one for settings (settings.py) and another for
your handlers (handlers.py). The Application and HTTPServer stuff is already
setup to you.

To start the server on por 8888, just run the following command in the base
directory of your app:

    $ torneira

In the directory `demos/simple_app/` there is a minimal app already configured.
If you want to see a more complex app that uses more available features, take a
look at `demos/more_complex_app`.

To see all options that `torneira` command support, run:

    $ torneira --help

Contributing
------------

Send a pull request (preferred) or patches using ``git format-patch``. Also,
torneira comes with some tests in `tests/` directory. Make sure you don't break
anything accidentally and also write some tests for your fix/feature.

Issues
------

Please report any issues on `GitHub issues`_.

Dependencies
------------

 * Tornado_ (tested with 2.3 and 2.4)

Optional dependencies:

 * Mako_ (if you want to use Mako templates instead of built-in tornado.template)
 * `SQL Alchemy`_ (only if using torneira.models)

On Python 2.5 we also need simplejson_ module.

.. _GitHub issues: https://github.com/marcelnicolay/torneira/issues
.. _Mako: http://www.makotemplates.org/
.. _PyPI: http://pypi.python.org/package/torneira/
.. _SQL Alchemy: http://www.sqlalchemy.org/
.. _simplejson: http://code.google.com/p/simplejson/
.. _Tornado: http://www.tornadoweb.org/
