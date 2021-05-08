Splicer [![Build Status](https://travis-ci.org/trivio/splicer.png)](https://travis-ci.org/trivio/splicer)
======================

``splicer`` makes the entire world look like a SQL database. 
It is a python module for working with data from disparate sources 
using commands to those familiar with SQL. It aims to make quick 
one off queries and ETL scripts more declarative rather than procedural.


Inspired by projects like BigQuery, Postgres Foreign Data Wrappers
and Multicorn, except no database is required.

``splicer`` enables:

* Analysts to create Datasets linking various
  foreign tables together along with User Defined Functions written in python. 
  Once defined, the datasets can be queried via SQL Select statements to create 
  new Views of the Data.

* Extension Developers to create extensions that make various data sources
  REST endpoints, log files, NoSQL Servers, traditional Databases,
  CSV Files to behave like tables.

  ``splicer`` will take advantage of these various sources' capabilities where 
  appropriate and will compensate for sources that lack basic
  features. 

  For example if a database supports joins and you want to query
  two tables within that database, ``splicer`` will have that system
  perform the join for you. If however you're working with a less
  sophisticated source, like plain files, ``splicer`` will perform the
  operations for you locally.


Enough reading! [Try it out][1] 

[1]: https://splicer.readthedocs.org/en/latest/install.html#installation "Installing Splicer"
