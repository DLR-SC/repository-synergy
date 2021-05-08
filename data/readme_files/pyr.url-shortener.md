Gurl-shortener: demo URL shortening service in python
=====================================================

A demo application for a very simple URL shortening service

The app relies on:

- flask_: A python micro web framework
- bootstrap_: A CSS & JS framework


Installing
----------

Pip::

    pip install url_shortener

Pypi:

    https://pypi.python.org/pypi/url_shortener

Manual::

    python setup.py install

Configuration
-------------

You can either modify the ``config.py`` file or provide environment
variables to configure ``url_shortener``. The following environment
variables can be tweaked:

- ``REDIS_HOST``: Address at which the redis server lives, defaults to ``127.0.0.1``.
- ``REDIS_PORT``: Port on which to contact redis, defaults to ``6379``.
- ``URL_PREFIX``: URL scheme for your short url host
- ``LISTEN_HOST``: Address to bind to for the short url service
- ``LISTEN_PORT``: Port to bind to
- ``RIEMANN_HOST``: Address to use to contact riemann, defaults to ``127.0.0.1``
- ``RIEMANN_PORT``: Port to use to contact riemann, defaults to ``5555``
- ``RIEMANN_PROTOCOL``: Riemann protocol to use, defaults to ``UDP``
- ``LOG_FILE_PATH``: Where to log, no defaults
- ``LOG_LEVEL``: level at which to log, defaults to ``DEBUG``

Logging
-------

When not run in debug mode, the application will output logs for consumption by
logstash, using logstash_formatter_

Usage
-----

The service can simply be started by invoking: ``url-shortener``, alternately deployments
can be done with gunicorn_. To start the service with gunicorn with 8 worker processes for
instance, the following can be used:

::

  gunicorn  -w 8 --log-file=/var/log/url-shortener/gunicorn.log --log-level=info url_shortener:app

.. _flask: http://flask.pocoo.org
.. _bootstrap: http://twitter.github.io/bootstrap
.. _logstash_formatter: https://github.com/exoscale/python-logstash-formatter
.. _gunicorn: http://gunicorn.org
