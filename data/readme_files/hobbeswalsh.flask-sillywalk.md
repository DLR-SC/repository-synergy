flask-sillywalk
===============

A Flask extension that implements Swagger support (http://swagger.wordnik.com/)

What's Swagger?
---------------

Swagger is a spec to help you document your APIs. It's flexible and
produces beautiful API documentation that can then be used to build
API-explorer-type sites, much like the one at
http://developer.wordnik.com/docs -- To read more about the Swagger
spec, head over to https://github.com/wordnik/swagger-core/wiki or
http://swagger.wordnik.com

Git Repository and issue tracker: https://github.com/hobbeswalsh/flask-sillywalk
Documentation: http://flask-sillywalk.readthedocs.org/en/latest/

.. |travisci| image::  https://travis-ci.org/hobbeswalsh/flask-sillywalk.png
.. _travisci: https://travis-ci.org/hobbeswalsh/flask-sillywalk

|travisci|_

Why do I want it?
-----------------

* You want your API to be easy to read.
* You want other people to be able to use your API easily.
* You'd like to build a really cool API explorer.
* It's Friday night and your friend just ditched on milkshakes.


How do I get it?
----------------

From your favorit shell:: 

    $ pip install flask-sillywalk


How do I use it?
----------------

I'm glad you asked. In order to use this code, you need to first
instantiate a SwaggerApiRegistry, which will keep track of all your API
endpoints and documentation.

Usage::
    
    from flask import Flask
    from flask.ext.sillywalk import SwaggerApiRegistry, ApiParameter, ApiErrorResponse

    app = Flask("my_api")
    registry = SwaggerApiRegistry(
      app,
      baseurl="http://localhost:5000/api/v1",
      api_version="1.0",
      api_descriptions={"cheese": "Operations with cheese."})
    register = registry.register
    registerModel = registry.registerModel

Then, instead of using the "@app.route" decorator that you're used to
using with Flask, you use the "register" decorator you defined above (or
"registerModel" if you're registering a class that describes a possible
API return value).

Now that we've got an API registry, we can register some functions. The
@register decorator, when just given a path (like @app.route), will
register a GET method with no possible parameters. In order to document a
method with parameters, we can feed the @register function some
parameters.

Usage::

    @register("/api/v1/cheese/random")
    def get_random_cheese():
      """Fetch a random Cheese from the database.
      Throws OutOfCheeseException if this is not a cheese shop."""
      return htmlify(db.cheeses.random())

    @register("/api/v1/cheese/<cheeseName>",
      parameters=[
        ApiParameter(
            name="cheeseName",
            description="The name of the cheese to fetch",
            required=True,
            dataType="str",
            paramType="path",
            allowMultiple=False)
      ],
      responseMessages=[
        ApiErrorResponse(400, "Sorry, we're fresh out of that cheese.")
      ])
    def get_cheese(cheeseName):
      """Gets a single cheese from the database."""
      return htmlify(db.cheeses.fetch(name=cheeseName))

Now, if you navigate to http://localhost:5000/api/v1/resources.json you
should see the automatic API documentation. See documentation for all the
cheese endpoints at http://localhost:5000/api/v1/cheese.json


What's left to do?
------------------

Well, lots, actually. This release:

* Doesn't support XML (but do we really want to?)
* Doesn't support the full swagger spec (e.g. "type" in data models
* Lots more. Let me know!
