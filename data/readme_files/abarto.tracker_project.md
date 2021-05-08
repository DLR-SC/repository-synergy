===============
tracker_project
===============

A simple Django project to report and track geo-located incidents within certain areas of interest. Whenever a new incident occurs the user is reported in real-time and the event is marked in a map (using `Google Maps JavaScript API <https://developers.google.com/maps/documentation/javascript/>`_). It's is possible to report the locations manually, but there's also a view that uses the `geolocator <https://github.com/onury/geolocator>`_ library to automatically detect the user's location.

This project created to demonstrate how to use `GeoDjango <https://docs.djangoproject.com/en/1.7/ref/contrib/gis/>`_ and send real-time notifications using `gevent-socketio <https://github.com/abourget/gevent-socketio>`_ and `RabbitMQ <http://www.rabbitmq.com/>`_. For an in depth description of the project see the following `blogpost <http://www.machinalis.com/blog/rt-notifications-gevent-gis/>`_.

The default configuration uses `PostgreSQL <http://www.postgresql.org/>`_ with the `PostGIS <http://postgis.net/>`_ extensions as database back-end, but it can also work with other GeoDjango compatible databases like `SQLite <http://www.sqlite.org/>`_ + `SpatiaLite <https://www.gaia-gis.it/fossil/libspatialite/index>`_.

Update #2
=========

I've created yet another implementation of the project using `Django channels <https://github.com/andrewgodwin/channels>`_ for the real-time notifications. You can check it out in the `use-django-channels <https://github.com/abarto/tracker_project/tree/use-django-channels>`_ branch.

Update
======

Some people asked me about a Node.js+socket.io (instead of the gevent-socketio) implementation of the project, so I created a `node_js <https://github.com/abarto/tracker_project/tree/node_js>`_ branch for it.

Requirements
============

Before you can run this project, the following packages need to be installed:

Ubuntu
------

* python-dev
* postgresql
* postgresql-server-dev-all
* postgis
* python-virtualenv
* libevent-dev
* rabbitmq-server

Fedora
------

* python-devel
* postgresql-server
* libpqxx-devel
* postgis
* python-virtualenv
* libevent-devel
* rabbitmq-server

Installation
============

Clone the repository: ::

    $ git clone git@github.com:abarto/tracker-project.git

Create and activate the virtual environment: ::

    $ cd tracker-project/
    $ virtualenv venv/
    $ . venv/bin/activate

Install the requirements: ::

    (venv)$ pip install -r requirements.txt

Initialize nodeenv, and install bower: ::

    (venv)$ nodeenv -p
    (venv)$ npm install -g bower

Create the database and the database user, install the PostGIS extensions: ::

    $ sudo -u postgres psql
    postgres=# CREATE ROLE tracker_project LOGIN PASSWORD 'tracker_project' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    postgres=# CREATE DATABASE tracker_project WITH OWNER = tracker_project;
    postgres=# \connect tracker_project;
    postgres=# CREATE EXTENSION postgis;

Initialize the database and set-up the Django environment: ::

    (venv)$ cd tracker_project/
    (venv)$ python ./manage.py migrate
    (venv)$ python ./manage.py bower_install

At this point it is possible to run the development server by using the special socketio_runserver management command ::

    (venv)$ python ./manage.py socketio_runserver

If you want to run in it in a production environment. Follow the instructions of the next section.

Running the application
=======================

The application can be run using `Chaussette <https://chaussette.readthedocs.org/en/1.2/>`_, with the ``socketio`` backend: ::

    (venv)$ chaussette --backend socketio --port 8000 tracker_project.wsgi.application

Please notice that the application won't server the static files, so before you can start using it, you need to run the ``collectstatic`` management command: ::

    (venv)$ python ./manage.py collectstatic

and then use a regular HTTP server like `nginx <http://nginx.com>`_ (we've included a sample configuration file) to server the files.

You can also use socket and process managers like `Circus <https://chaussette.readthedocs.org/en/1.2/#using-chaussette-in-circus>`_ or `Supervisor <https://chaussette.readthedocs.org/en/1.2/#using-chaussette-in-supervisor>`_.

Vagrant
-------

A `Vagrant <https://www.vagrantup.com/>`_ configuration file is included if you want to test the project.

Acknowledgements
================

The basic architecture for the notifications system follows the guidelines presented by Jeremy West in the blogpost `Django, Gevent, and Socket.io <http://www.pixeldonor.com/2014/jan/10/django-gevent-and-socketio/>`_. We also used the code for his `socketio_runserver <https://github.com/iamjem/socketio_runserver>`_ management command.
