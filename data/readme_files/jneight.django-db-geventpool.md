django-db-geventpool
====================

.. image:: http://img.shields.io/travis/jneight/django-db-geventpool.svg
   :target: https://travis-ci.org/jneight/django-db-geventpool
   :alt: travis

.. image:: https://img.shields.io/pypi/v/django-db-geventpool.svg
   :target: https://pypi.python.org/pypi/django-db-geventpool
   :alt: pypi version

.. image:: http://img.shields.io/pypi/l/django-db-geventpool.svg
   :target: https://pypi.python.org/pypi/django-db-geventpool
   :alt: pypi license

Another DB pool using gevent for PostgreSQL DB.

Python 3 is supported, but if `gevent` is not installed successfully it will use fallback to `eventlet`.

psycopg2
--------

django-db-geventpool requires psycopg2:

* ``psycopg2>=2.5.1`` for CPython 2 and 3 (or `psycopg2-binary <https://pypi.org/project/psycopg2-binary/>`_—see `notes in the psycopg2 2.7.4 release <http://initd.org/psycopg/articles/2018/02/08/psycopg-274-released/>`_)
* ``psycopg2cffi>=2.7`` for PyPy


Patch psycopg2
--------------

Before using the pool, psycopg2 must be patched with psycogreen, if you are using `gunicorn webserver <http://www.gunicorn.org/>`_,
a good place is the `post_fork() <http://docs.gunicorn.org/en/latest/settings.html#post-fork>`_ function at the config file:

.. code:: python

   from psycogreen.gevent import patch_psycopg     # use this if you use gevent workers
   from psycogreen.eventlet import patch_psycopg   # use this if you use eventlet workers

   def post_fork(server, worker):
       patch_psycopg()
       worker.log.info("Made Psycopg2 Green")


Settings
---------

  + Set *ENGINE* in your database settings to: 
      + *'django_db_geventpool.backends.postgresql_psycopg2'*
      + For postgis: *'django_db_geventpool.backends.postgis'*
  + Add *MAX_CONNS* to *OPTIONS* to set the maximun number of connections allowed to database (default=4)
  + Add *'CONN_MAX_AGE': 0* to settings to disable default django persistent connection feature. And read below note if you are manually spawning greenlets 

.. code:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '',
            'PORT': '',
            'ATOMIC_REQUESTS': False,
            'CONN_MAX_AGE': 0,
            'OPTIONS': {
                'MAX_CONNS': 20
            }
        }
    }

Using ORM when not serving requests
-----------------------------------------------

If you are using django with celery (or other), or have code that manually spawn greenlets it will not be sufficient to set CONN_MAX_AGE to 0.
Django only checks for long-live connections when finishing a request - So if you manually spawn a greenlet (or task spawning one) its connections will
not get cleaned up and will live until timeout. In production this can cause quite some open connections and while developing it can hamper your tests cases.

To solve it make sure that each greenlet (or task) either sends the django.core.signals.request_finished signal or calls django.db.close_old_connections() right before it ends

The decorator method with your greenlet or task is preferred, but the other alternatives are also valid

.. code:: python

   from django_db_geventpool.utils import close_connection

   @close_connection
   def foo_worker()
        ...

or 

.. code:: python

   from django.core.signals import request_finished

   def foo_worker():
      ...
      request_finished.send(sender="greenlet")

or

.. code:: python

   from django.db import close_old_connections
   
   def foo_worker():
      ...
      close_old_connections()


Other pools
------------

* `django-db-pool <https://github.com/gmcguire/django-db-pool>`_
* `django-postgresql <https://github.com/kennethreitz/django-postgrespool>`_
