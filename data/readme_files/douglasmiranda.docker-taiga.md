=============================================
Deploy your Taiga services with Docker
=============================================

    *Taiga is a project management platform for agile developers & designers and project managers who want a beautiful tool that makes work truly enjoyable. http://taiga.io*

.. image:: https://raw.githubusercontent.com/douglasmiranda/docker-taiga/master/docker-taiga.jpg
    :alt: Docker Taiga

Goodies
-------

* Python 3.6
* Postgres 10
* Alpine Linux images
* Gevent worker for gunicorn
* django-anymail integration

I've tried to containerize every module, so we have:

* frontend_
* backend_
    * celery worker
        * redis
    * rabbitmq
* events_
    * rabbitmq

Bonus: I've added a config if you want to use mailgun.

.. _frontend: frontend/
.. _backend: https://github.com/taigaio/taiga-back
.. _events: events/

Quickstart
----------

I'm going to write some better instructions soon, but for now, if you want to
try it, just type:

::

    docker-compose up

PS: This will load the *docker-compose.override.yml* too (useful for local / dev envs)

PS: since the frontend port is mapped to 80, just go to your brower and http://localhost. The login credentials are **admin** with password **123123**.

On production, just rename the file **productionenv-template--rename-this-file.env** to **production.env**

::

    docker-compose -f docker-compose.yml -f docker-compose.production.yml up

Learn more about `docker compose override / extends`_.

.. _`docker compose override / extends`: https://docs.docker.com/compose/extends/

Tips, Tricks and Notes
----------------------

* Most of the configurations you will be able to do on docker-compose.yml and .env file.
* Because of lxml and cryptography you would have to spin up a server with more RAM than you would want, but if you build locally, push to a registry and just pull on your server, you won't be compiling on deploy. =]
* I plan to use Caddy instead of Nginx, but don't know when, you may want to look, it's nice.

Credits
-------

https://taigaio.github.io/taiga-doc/dist/setup-production.html

Inspired by:

* https://github.com/benhutchins/docker-taiga
* https://github.com/ipedrazas/taiga-docker