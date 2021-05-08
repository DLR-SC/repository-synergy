=====================
Django Database Tools
=====================

Django Db Tools is a set of Database tools that are helpful when running 
applications with Django in production. The primary initial tool allows for
flipping a site in and out of a read-only mode. 

Currently the following functionality is being worked on:

- A header displaying the read only mode
- Ability to render a template explaining posts are not allowed

Installation
============

#. Add the ``db_tools`` directory to your Python path.

#. Add the following middleware to your project's ``settings.py`` file::

       MIDDLEWARE_CLASSES = (
           # ...
           'dbtools.middleware.ReadOnlyMiddleware',
           # ...
       )

Configuration
=============

The db tools has two modes which you can control:

#. READ_ONLY_MODE

This mode ensures all users even if already logged in act as anonymous users 
on your site. To enable this you need to set the following environment variable:

    READ_ONLY_MODE = True

#. GET_ONLY_MODE

This mode disallows all POST requests to your site. If your site only allows 
inserting data as POSTS then this should be sufficient to allow your users to
view their data, but also ensure no new data is written. To enable this set the 
following environment variable:

    GET_ONLY_MODE = True

