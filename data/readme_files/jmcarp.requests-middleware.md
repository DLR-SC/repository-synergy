requests-middleware
===================

.. image:: https://badge.fury.io/py/requests-middleware.png
    :target: http://badge.fury.io/py/requests-middleware

.. image:: https://travis-ci.org/jmcarp/requests-middleware.png?branch=master
    :target: https://travis-ci.org/jmcarp/requests-middleware

*TL;DR*: **requests-middleware** is a custom transport adapter that allows simple
composition of HTTP interactions.

The `python-requests`_ library makes excellent use of transport adapters to
allow for easy extension and modification of HTTP interactions. There are
adapters for SSL configuration, rate-limiting, and testing, and writing your
own adapters is easy.

But what if you want to use more than one of those behaviors for the same
session? What if you want HTTP caching *and* rate-limiting? Requests only
uses one adapter per URL. You could write a new
`CachingRateLimitingHTTPAdapter`, but that's probably not the best solution.

**requests-middleware** is an effort to preserve the modularity of adapters,
while allowing simple composition of multiple types of interaction. Want to
use HTTP caching, respect robots.txt files, and limit your application to
10 requests per hour? No problem!

.. code-block:: python

    import requests
    from requests_middleware import MiddlewareHTTPAdapter
    from requests_middleware.contrib.cacheware import CacheMiddleware
    from requests_middleware.contrib.robotware import RobotsMiddleware
    from requests_middleware.contrib.throttleware import \
        ThrottleMiddleware, RequestsPerHourThrottler

    session = requests.Session()
    middlewares = [
        CacheMiddleware(),
        RobotsMiddleware(),
        ThrottleMiddleware(RequestsPerHourMiddleware(10)),
    ]
    adapter = MiddlewareHTTPAdapter(middlewares)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

.. _python-requests: https://github.com/kennethreitz/requests
.. _httpcache: https://github.com/Lukasa/httpcache
