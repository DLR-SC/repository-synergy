Flask-MongoKit
==============

.. image:: https://secure.travis-ci.org/jarus/flask-mongokit.png
   :target: http://travis-ci.org/jarus/flask-mongokit

Flask-MongoKit simplifies to use `MongoKit`_, a powerful `MongoDB`_ ORM 
in Flask applications.

.. _MongoKit: http://namlook.github.com/mongokit/
.. _MongoDB: http://www.mongodb.org/
.. _here: http://bitbucket.org/Jarus/flask-mongokit/

Installation
------------
The installation is thanks to the Python Package Index and `pip`_ really simple.

::

   $ pip install Flask-MongoKit

If you only can use `easy_install` than use

::

   $ easy_install Flask-MongoKit

.. _pip: http://pip.openplans.org/

Flask-MongoKit requires to run some packages (they will be installed automatically if they not already installed):

* Flask
* MongoKit
* pymongo

Changelog
=========

* **0.6 (08.07.2012)**

  * Use the new app context and again the old request context.
  * The MongoKit object is now subscriptable and support the typical syntax to 
    get a collection.::

        db['my_collection'].insert({'x': 5})

  * Restructured and improved test suite.
  * Sounds crazy but improved python2.5 support.

* **0.5 (02.07.2012)**

  * You don't need a request context anymore for the mongodb connection.
    (A bad decision ... look in 0.6)

* **0.4 (23.02.2012)**

  * Support new import system of flask. Use now::

      from flask.ext.mongokit import Mongokit
