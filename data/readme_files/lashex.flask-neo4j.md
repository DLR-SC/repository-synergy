Flask-Neo4j
===========
.. image:: https://img.shields.io/pypi/v/Flask-Neo4j.svg
   :target: https://pypi.python.org/pypi/Flask-Neo4j

.. image:: https://img.shields.io/pypi/pyversions/Flask-Neo4j.png
   :target: https://pypi.python.org/pypi/Flask-Neo4j

.. image:: https://img.shields.io/pypi/dm/Flask-Neo4j.svg
   :target: https://pypi.python.org/pypi/Flask-Neo4j

.. image:: https://secure.travis-ci.org/lashex/flask-neo4j.png
   :target: http://travis-ci.org/lashex/flask-neo4j

.. image:: https://img.shields.io/pypi/wheel/Flask-Neo4j.png
   :target: https://pypi.python.org/pypi/Flask-Neo4j

A Flask extension that provides simple interaction with the Neo4j graph
database.

The underlying Neo4j capabilities are made possible by the fine `py2neo <http://py2neo.org>`_ library.


Installation
------------
Using pip::

    pip install flask-neo4j

Usage
-----
Typical usage looks like this::

    from flask import Flask
    from flask.ext.neo4j import Neo4j
    from py2neo import Node,Relationship

    # Configuration
    GRAPH_DATABASE='http://localhost:7474/db/data/'
    GRAPH_USER = 'neo4j'
    GRAPH_PASSWORD = 'admin'

    app = Flask(__name__)
    app.config.from_object(__name__)
    graph_indexes = {'Species': Node}
    flask4j = Neo4j(app, graph_indexes).gdb
    print flask4j.neo4j_version
    nosferatu = Node('species',full_name='Dracula nosferatu',species_name='nosferatu')
    genus = Node('genus',name='Dracula')
    nosferatu_memberof_genus = Relationship(nosferatu,'Member-of',genus)
    flask4j.create(nosferatu_memberof_genus)



    # which all results in a graph that looks like:
    #  (species)-[:MEMBER_OF]->(genus)



Links
-----

* `py2neo documentation <http://http://py2neo.org>`_
