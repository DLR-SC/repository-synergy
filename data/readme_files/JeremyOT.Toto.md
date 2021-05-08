Toto
===============
Toto is a small framework intended to accelerate web service development. It is
built on top of [Tornado][tornado] and can currently use [MySQL][mysql], [MongoDB][mongodb], [PostgreSQL][postgres] or
[Redis][redis] as a backing database.

[![Build Status](https://travis-ci.org/JeremyOT/Toto.svg)](https://travis-ci.org/JeremyOT/Toto)

Features
--------
* Uses JSON (or BSON or msgpack) for easy consumption by clients on any platform
* Easy to add new methods
* Simple authentication built in with HMAC-SHA1 verification for authenticated requests
* Session state persistence for authenticated requests
* Sessions stored in database to simplify scaling across servers

Installation
------------
The simplest way to install Toto is with pip. Simply run `pip install -e git+git://github.com/JeremyOT/Toto.git#egg=Toto`
to install the latest version of the Toto module on your machine.

Documentation
-------------
Complete documentation is available here: [http://toto.li/docs/][docs].

Usage
-----

Getting started with Toto is easy, all you need to do is make a new instance of `toto.TotoServer`
and call `run()`. Toto needs a root module to use for method lookup. By default, a `TotoServer`
will look for a module called `methods`. The `method_module` parameter can be used to specify
another module by name.

Configuration
-------------
By default, Toto is configured to run on port 8888 and connect to a MongoDB server
running on localhost. Configuration can be performed in three ways with each overriding the last:

1. By passing options as named parameters to the `TotoServer` constructor.
2. Through a configuration file by passing the path to the config file as the first parameter to
   the `TotoServer` constructor.
3. With command line parameters (`--option='string value' --option=1234`)

Combining the configuration methods can be useful when debugging. Run your script with `--help`
to see a full list of available parameters.

Methods
-------

Methods are referenced by name in each request. `a.b.c` (or `a/b/c`) maps to `methods.a.b.c`. To add new
methods, add modules and packages to the `methods` (or specified) package (see the account package for
reference) and ensure that each callable module defines `invoke(handler, parameters)`
where `handler` is the `TotoHandler` (subclass of `tornado.web.RequestHandler`) handling
the current request.

`handler.connection.db` provides direct access to the database used by the sessions and
accounts framework.

`handler.session` provides access to the current session or `None` if not authenticated.
Available properties:

* `session.user_id` - the current user ID
* `session.expires` - the unix timestamp when the session will expire
* `session.session_id` - the current session ID
* `session.state` - a python dict containing the current state, you must call
`session.save_state()` to persist any changes. The session object acts like a proxy to state so
you can use dictionary accessors on it directly.

To enforce authentication for any method, decorate the `invoke()` function with
`@toto.invocation.authenticated`. Unauthorized attempts to call authenticated methods
will return a not authorized error.

Required parameters can be specified by decorating an `invoke()` function with
`@toto.invocation.requires(param1, param2,...)`.

Method modules can take advantage of [Tornado's][tornado] non-blocking features by decorating
an `invoke()` function with `@toto.invocation.asynchronous`. Data can be sent
to the client with `handler.respond()` and `handler.raw_respond()`. Optionally, modules can
implement `on_connection_close()` to clean up any resources if the client closes the
connection. See `RequestHandler.on_connection_close()` in the [Tornado][tornado] documentation
for more information.

It is important to remember that [Tornado][tornado] requires that all calls to `respond()`, `respond_raw()`, `write()`,
`flush()` and `finish()` are performed on the main thread. You can schedule a function to
run on the main thread with `IOLoop.instance().add_callback(callback)`.

_Note: Any data returned from a call to `method.invoke()` will be sent to the client as
JSON data and be used to generate the `x-toto-hmac` header for verification. This may cause
issues with asynchronous methods. If `method.invoke()` returns `None`, a response will not
automatically be sent to the client and no `x-toto-hmac` header will be generated._

Requests
-----------
Non-authenticated methods:

1. Call service with JSON object in the form: `{"method": "a.b.c", "parameters": <parameters>}`. Instead of passing
the "method" argument in the request body, it is also possible to call methods by URL. The URL equivalent to the
above call is `http://service.com/service/a/b/c`.
2. Parse response JSON.

Account Creation:

1. Call `account.create` method with `{"user_id": <user_id>, "password": <password>}`.
2. Verify that the base64 encoded HMAC-SHA1 of the response body with `<user_id>` as the key matches the `x-toto-hmac` 
header in the response.
3. Parse response JSON.
4. Read and store `session_id` from the response object.

Login:

1. Call `account.login` method with `{"user_id": <user_id>, "password": <password>}`.
2. Verify that the base64 encoded HMAC-SHA1 of the response body with `<user_id>` as the key matches the `x-toto-hmac` 
header in the response.
3. Parse response JSON.
4. Read and store `session_id` from the response object.

Authenticated methods:

1. Login (see-above).
2. Call service with JSON object in the form: `{"method": "a.b.c", "parameters": <parameters>}`
with the `x-toto-session-id` header set to the session ID returned from login and the `x-toto-hmac` header
set to the base64 encoded HMAC-SHA1 generated with `<user_id>` as the key and the JSON request string as
the message.
3. Verify that the base64 encoded HMAC-SHA1 of the response body with `<user_id>` as the key matches the `x-toto-hmac` 
header in the response.
4. Parse response JSON.

_Note: These instructions assume that `method.invoke()` returns an object to be serialized
and sent to the client. Methods that return None can be used the send any data and must be
handled accordingly._

Events
======
Sometimes you may need to send events from one request to another. Toto's `toto.events.EventManager` makes this easy.

To send an event use `EventManager.instance().send('eventname', args)`. EventManager uses python's `cPickle` module
for serialization so you can pass anything cPickle can handle as `args`.

To receive an event, you must register a handler with `TotoHandler.register_event_handler('eventname', handler)`.
`handler` is a function that takes one parameters and will be called with `args` when the `EventManager` sends an event
with 'eventname'. Toto's events were primarily designed to be combined with tornado's support for non-blocking requests.
See the "chat" template for an example.

_Toto's event system supports sending events across multiple instances both on the same machine and in a distributed
system. Run your server with --help for more configuration options_

Daemonization
=============
The Toto server can be run as a daemon by passing the argument `--start`. To stop any running processes pass
`--stop`. This will stop any processes that share the specified pid file format (default `toto.pid`). The
`--processes=<n>` option may be used to specify the number of server instances to run. Multiple instances will be run
on sequential ports starting at the port specified by `--port`. If `0` is used as the argument to `--processes`, Toto
will run one process per cpu as detected by Python's `multiprocessing` module. Additional daemonization options can
be viewed from `--help`.

Clients
=======
To help you get started, JavaScript and iOS client libraries are in development at [https://github.com/JeremyOT/TotoClient-JS](https://github.com/JeremyOT/TotoClient-JS)
and [https://github.com/JeremyOT/TotoClient-iOS](https://github.com/JeremyOT/TotoClient-iOS) respectively.

[tornado]:http://www.tornadoweb.org
[mysql]:http://www.mysql.com
[mongodb]:http://www.mongodb.org
[docs]:http://toto.li/docs/ "http://toto.li/docs/"
[postgres]:http://www.postgresql.org/
[redis]:http://redis.io/
