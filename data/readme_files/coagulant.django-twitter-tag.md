Django Twitter Tag
==================

.. image:: https://secure.travis-ci.org/coagulant/django-twitter-tag.png?branch=dev
    :target: https://travis-ci.org/coagulant/django-twitter-tag

.. image:: https://coveralls.io/repos/coagulant/django-twitter-tag/badge.png?branch=dev
    :target: https://coveralls.io/r/coagulant/django-twitter-tag/

A django template tag to display user's recent tweets / search results.
Version 1.0 uses Twitter API 1.1.

Basic features are limiting numbers of displayed tweets, filtering out replies and retweets.
Library exposes each tweet ``json`` in template, adding extra attributes: ``html`` and ``datetime``.
First one makes urls, hashtags or twitter usernames clickable, juts like you expect them to be.
Last one provides python datetime object to ease output in templates.
Urls are expanded by default. Library handles twitter exceptions gracefully,
returning last successful response.

Usage
-----

* Load tag in your template like this::

    {% load twitter_tag %}


* Get user's (``futurecolors`` in example) most recent tweets and store them in ``tweets`` variable::

    {% get_tweets for "futurecolors" as tweets %}


* Now you have a list of tweets in your template context, which you can iterate over like this::

    <ul>
    {% for tweet in tweets %}
        <li>{{ tweet.html|safe }}</li>
    {% endfor %}
    </ul>


Installation
------------

This app works with python 2.7 and 3.3, Django 1.4-1.6.

Recommended way to install is pip::

  pip install django-twitter-tag


Add ``twitter_tag`` to ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (...
                      'twitter_tag',
                      ...
                     )

Configuration
-------------

Twitter `API 1.1`_ requires authentication for every request you make,
so you have to provide some credentials for oauth dance to work.
First, `create an application`_, second, request access token on newly created
app page. The `process of obtaining a token`_ is explained in detail in docs.

Here is an example of how your config might look like::

    # settings.py
    # Make sure to replace with your own values, theses are just made up

    # Your access token: Access token
    TWITTER_OAUTH_TOKEN = '91570701-BQMM5Ix9AJUC5JtM5Ix9DtwNAiaaYIYGN2CyPgduPVZKSX'
    # Your access token: Access token secret
    TWITTER_OAUTH_SECRET = 'hi1UiXm8rF4essN3HlaqMz7GoUvy3e4DsVkBAVsg4M'
    # OAuth settings: Consumer key
    TWITTER_CONSUMER_KEY = '3edIOec4uu00IGFxvQcwJe'
    # OAuth settings: Consumer secret
    TWITTER_CONSUMER_SECRET = 'YBD6GyFpvumNbNA218RAphszFnkifxR8K9h8Rdtq1A'

For best performance you should set up `django cache framework`_. Cache is used both internally
to store last successful json response and externally (see Caching below).

.. _API 1.1: https://dev.twitter.com/docs/api/1.1
.. _create an application: https://dev.twitter.com/apps
.. _process of obtaining a token: https://dev.twitter.com/docs/auth/tokens-devtwittercom
.. _django cache framework: https://docs.djangoproject.com/en/dev/topics/cache/

Examples
--------

You can specify number of tweets to show::

    {% get_tweets for "futurecolors" as tweets limit 10 %}


To filter out tweet replies (that start with @ char)::

    {% get_tweets for "futurecolors" as tweets exclude "replies" %}


To ignore native retweets::

    {% get_tweets for "futurecolors" as tweets exclude "retweets" %}


Or everything from above together::

    {% get_tweets for "futurecolors" as tweets exclude "replies, retweets" limit 10 %}


Search tag (experimental)
-------------------------

You can search for tweets::

    {% search_tweets for "python 3" as tweets limit 5 %}

Search api arguments are supported via key=value pairs::

    {% search_tweets for "python 3" as tweets lang='eu' result_type='popular' %}

Relevant `API docs for search`_.

.. _API docs for search: https://dev.twitter.com/docs/api/1.1/get/search/tweets

Caching
-------

It's strongly advised to use template caching framework to reduce the amount of twitter API calls
and avoid reaching `rate limit`_ (currently, 180 reqs in 15 minutes)::

    {% load twitter_tag cache %}
    {% cache 60 my_tweets %}
    {% get_tweets for "futurecolors" as tweets exclude "retweets" %}
    ...
    {% endcache %}


.. _rate limit: https://dev.twitter.com/docs/rate-limiting/1.1

Extra
-----

Tweet's properties
~~~~~~~~~~~~~~~~~~

get_tweets returns a list of tweets into context. Each tweets is a json dict, that has
exactly the same attributes, as stated in API 1.1 docs, describing `tweet json`_.
Tweet's created timestamp is converted to python object and is available in templates::

    {{ tweet.datetime|date:"D d M Y" }}

.. _tweet json: https://dev.twitter.com/docs/platform-objects/tweets

Tweet's html
~~~~~~~~~~~~

Tweet also has extra ``html`` property, which contains tweet, formatted for html output
with all needed links. Note, Twitter has `guidelines for developers`_ on how embeded tweets
should look like.

.. _guidelines for developers: https://dev.twitter.com/terms/display-requirements

Exception handling
~~~~~~~~~~~~~~~~~~

Any Twitter API exceptions like 'Over capacity' are silenced and logged.
Django cache is used internally to store last successful response in case `twitter is down`_.

.. _twitter is down: https://dev.twitter.com/docs/error-codes-responses

Going beyond
~~~~~~~~~~~~
Since version 1.0 you can create your own template tags for specific twitter queries,
not supported by this library. Simply inherit from ``twitter_tag.templatetags.twitter_tag.BaseTwitterTag``
and implement your own ``get_json`` method (tag syntax is contolled by django-classy-tags).

Development
-----------

To install `development version`_, use ``pip install django-twitter-tag==dev``

.. _development version: https://github.com/coagulant/django-twitter-tag/archive/dev.tar.gz#egg=django_twitter_tag-dev

Tests
-----

Run::

    DJANGO_SETTINGS_MODULE = twitter_tag.test_settings python setup.py test
