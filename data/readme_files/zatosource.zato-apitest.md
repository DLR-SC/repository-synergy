zato-apitest - API Testing for Humans
=====================================

Introduction
------------

zato-apitest is a friendly command line tool for creating beautiful tests of HTTP-based REST, XML and SOAP APIs with as little
hassle as possible.

Tests are written in plain English, with no programming needed, and can be trivially easy extended in Python if need be.

Note that zato-apitest is meant to test APIs only. It's doesn't simulate a browser nor any sort of user interactions. It's meant
purely for machine-machine API testing.

Originally part of [Zato] (https://zato.io) - open-source ESB, SOA, REST, APIs and cloud integrations in Python.

In addition to HTTP Zato itself supports AMQP, ZeroMQ, WebSphere MQ, including JMS, Redis, FTP, OpenERP, SMTP, IMAP, SQL, Amazon S3,
OpenStack Swift and more so it's guaranteed zato-apitest will grow support for more protocols and transport layers with time.

Here's how a built-in demo test case looks like:

![zato-apitest demo run](https://raw.githubusercontent.com/zatosource/zato-apitest/master/docs/gfx/demo.png)

What it can do
--------------

- Invoke HTTP APIs

- Use [JSON Pointers] (https://zato.io/blog/posts/json-pointer-rfc-6901.html) or [XPath] (https://en.wikipedia.org/wiki/XPath)
  to set request's elements to strings, integers, floats, lists, random ones from a set of values, random strings, dates now/random/before/after/between.

- Check that JSON and XML elements, exist, don't exist,
  that an element is an integer, float, list, empty, non-empty, that it belongs to a list or doesn't.

- Set custom HTTP headers, user agent strings, method and SOAP action.

- Check that HTTP headers are or are not of expected value, that a header exists or not, contains a value or not, is empty or not,
  starts with a value or not and ends with a value or not.

- Read configuration from environment and config files.

- Store values extracted out of previous steps for use in subsequent steps, i.e. get a list of objects, pick ID of the first one
  and use this ID in later steps.

- Can be integrated with JUnit

- Can be very easily extended in Python

More information
--------------------

Check out the project's website for [more information](https://zato.io/docs/test/apitest/index.html),
including a getting started tutorial and dozens of usage examples.
