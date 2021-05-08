# django-user-streams

**Simple, fast user news feeds for Django**

**Author:** Jamie Matthews. [Follow me on Twitter](http://twitter.com/j4mie).

[![build-status-image]][travis]

## Requirements

* Django 1.3, 1.4, 1.5

## Overview

An app for creating *news feeds* (also known as *activity streams*) for users,
notifying them of activity happening around your site. Optimised for speed,
pluggability and simplicity.

News feed items are stored as a string and a timestamp. You can't store any
additional metadata about the stream items, such as generic foreign keys to and
`Actor` or a `Target`. You just store the item content as plain text (or HTML).
If you need links to other objects, just insert an `<a>` tag.

## DEPRECATED
**PLEASE NOTE:** _This repository is no longer actively maintained or regularly used by DabApps and therefore should be considered deprecated. Please find alternative packages for your needs or feel free to create and maintain your own fork._

## Installation

You can install django-user-streams from PyPI:

    pip install django-user-streams

Add `user_streams` to your `INSTALLED_APPS` setting. You also need a *backend*,
which defines how your streams are stored. These are described below.

    INSTALLED_APPS = [
        ...
        'user_streams',
        'user_streams.backends.user_streams_single_table_backend',
        ...
    ]

    USER_STREAMS_BACKEND = 'user_streams.backends.user_streams_single_table_backend.SingleTableDatabaseBackend'

Finally, if you're using a backend that stores stream items using Django's model
layer, run `manage.py syncdb` to create the necessary database tables.

## API

### Adding items to streams

To create a stream item:

    import user_streams

    user = User.objects.get(username='jamie')
    user_streams.add_stream_item(user, 'This is the contents of the stream item')

The first argument to `add_stream_item` can be a single `User` instance, or a queryset
representing multiple users. In the latter case, the message you supply is added
to the stream of each user in the queryset.

    import user_streams

    user_streams.add_stream_item(User.objects.all(), 'Broadcast message to all users')

You can also specify the creation time for the stream item by passing a
`datetime.datetime` instance as the value of the `created_at` argument.

    python
    import user_streams
    from datetime import datetime

    user = User.objects.get(username='jamie')
    user_streams.add_stream_item(user, 'You have a new message!', created_at=datetime.now())

#### A note on time zones

When a stream item is created, Django's [timezone support settings][use_tz] will be respected.

If timezone support is enabled by setting `USE_TZ` to `True`, then timezone-aware datestamps will be used, and stream items will be stored in the database using a UTC offset.  You will need to convert the timestamps to your users' local time at the last possible moment (when the `datetime` object is formatted for presentation to the user).

If timezone support is disabled by setting `USE_TZ` to `False`, then timezone-naive datestamps will be used, and stream items should be dealt with as using localtime.

#### Time zones and Django 1.3 compatibility

Django's timezone support was added in 1.4, so things work a little differently if you're using `django-user-streams` with Django 1.3.

By default, if you don't pass a `created_at` argument to `add_stream_item`, the
value of `datetime.datetime.now()` will be used to timestamp your stream items.
This is probably the least surprising behaviour, and if your app only ever deals
with users in one timezone (and those users are in the same timezone as your
web server), it's probably fine.

If your users are all over the world, however, this is a bad idea. The reasons
for this are discussed in
[this blog post by Armin Ronacher](http://lucumr.pocoo.org/2011/7/15/eppur-si-muove/).
The best way to store timestamps in the database is to use the UTC timezone.
You can then convert them to your users' local time at the last possible moment
(when the `datetime` object is formatted for presentation to the user).

To support this, you can either provide the `created_at` argument every time
you call the `add_stream_item` method:

    user_streams.add_stream_item(user, 'You have a new message!',
                                 created_at=datetime.utcnow())

Alternatively, you can set the `USER_STREAMS_USE_UTC` setting (in your
`settings.py`) to `True` (it's `False` by default). If you do this,
`datetime.utcnow()` will be used instead of `datetime.now()` to generate
the timestamps for each stream item.

If you do either of these things, the `created_at` property of each of your
stream items will be set to UTC time. It's your responsibility to convert
this to each user's local time for formatting. Take a look at
[times](https://github.com/nvie/times) for an easy way to deal with that.

Support for Django 1.3 and the `USER_STREAMS_USE_UTC` setting is intended to be deperecated at some point in the future.

### Getting the stream for a user

To retrieve the stream items for a user:

    import user_streams

    user = User.objects.get(username='jamie')
    items = user_streams.get_stream_items(user)

This will return an iterable of objects, each of which is guaranteed to have two
properties: `created_at`, which will be a `datetime.datetime` instance
representing the creation timestamp of the message, and `content`, which will
contain the contents of the message as a string. The objects will be ordered by
their `created_at` field, with the most recent first. The iterable that is
returned will be *lazy*, meaning that you can slice it (and pass it to a Django
`Paginator` object) without loading all of the items from the database.

### Backends

Stream storage is abstracted into `Backend` classes. Three backends are
included with `django-user-streams`. Each backend is kept in a separate
reusable app, which must be added to `INSTALLED_APPS` separately to the main
`user_streams` app. This is to ensure that only the database tables required
for each backend are created (assuming you are using a backend that stores
data through Django's model layer).

Which backend you choose depends on the scale of your application, as well as
your expected usage patterns. The pros and cons of each are described below.

#### SingleTableDatabaseBackend

`user_streams.backends.user_streams_single_table_backend.SingleTableDatabaseBackend`

The simplest backend. Your stream items are stored in a single database table,
consisting of a foreign key to a `User` object, a `DateTimeField` timestamp, and
a `TextField` to store your message. Fetching a stream for a user should be
extremely fast, as no database joins are involved. The tradeoff is storage
space: If you send a message to multiple users, the message is stored multiple
times, once for each user. If you regularly broadcast messages to thousands of
users, you may find that the table gets very large.

#### ManyToManyDatabaseBackend

`user_streams.backends.user_streams_many_to_many_backend.ManyToManyDatabaseBackend`

This backend stores your messages in a table with a `ManyToManyField`
relationship to your `User` objects. Each message is only stored *once*, with a
row in the intermediate table for each recipient. This means you need much less
space for broadcast messages, but your queries may be slightly slower.

#### RedisBackend

`user_streams.backends.user_streams_redis_backend.RedisBackend`

Stores your messages in Redis sorted sets, one set for each user,  with a Unix
timestamp (the `created_at` attribute) as the score for each item. This approach
is described in more detail
[here](http://blog.waxman.me/how-to-build-a-fast-news-feed-in-redis). The
iterable returned by `get_stream_items` uses `ZREVRANGE` to retrieve each slice of the
feed, and `ZCARD` to get the complete size of the set of items. This backend
should be screamingly fast.

*Note: the Redis backend requires the `redis-py` library. Install with `pip
install redis`.*

##### Redis backend settings

The following settings control the behaviour of the Redis backend:

`USER_STREAMS_REDIS_KEY_PREFIX`

Each key generated by the backend will be prefixed with the value of this
setting. The default prefix is "user_streams".

`USER_STREAMS_REDIS_CLIENT_ARGUMENTS`

A dictionary of keyword arguments which will be passed to the constructor
of the Redis client instance.

#### Writing your own backend

You can create your own backend to store messages in whatever data store suits
your application. Backends are simple classes which must implement two methods:

##### add_stream_item

`add_stream_item(self, users, content, created_at)`

`users` will be an *iterable* of `User` instances (you don't need to worry
about accepting a single instance - your backend method will always be called
with an iterable, which may be a list containing only one `User`.

`content` will be a string containing the stream message to store.

`created_at` will be a Python `datetime.datetime` object representing the
time at which the stream item was created.

##### get_stream_items

`get_stream_items(self, user)`

This method should return an iterable of messages for the given `User`, sorted
by timestamp with the newest first. Each item must be an object with two
attributes: `created_at` (which must be a Python `datetime.datetime` object)
and `content` (which must be a string containing the message contents).

While this method could simply return a `list` of messages, it's much more
efficient to assume that the list will be paginated in some way, and support
slicing and counting the objects on-demand, in whatever method your data store
supports. To do this, you should return an iterable object, overriding
`__getitem__` and `__len__`. See the implementation of `RedisBackend` for an
example.

## Alternatives

https://github.com/justquick/django-activity-stream

## Development

To contribute: fork the repository, make your changes, add some tests, commit,
push to a feature branch, and open a pull request.

### How to run the tests

Clone the repo, install the requirements into your virtualenv, then type
`python manage.py test user_streams`. You can also use
`python manage.py test user_streams user_streams_single_table_backend user_streams_many_to_many_backend user_streams_redis_backend` to
run the tests for all the backends. Any of the above should also work if
you've installed `django-user-streams` into an existing Django project (of
course, only run the tests for the backend you're using).

## Changelog

#### 0.6.0

* Add compatibility with Django 1.4's support for timezones

#### 0.5.0

* Backends renamed to make app_labels less generic (for example, `many_to_many`
  is now `user_streams_many_to_many_backend`).

#### 0.4.0

* Add tests for pagination of results
* Fix result loading in RedisBackend

#### 0.3.0

* Fix slicing behaviour in Redis backend

#### 0.2.0

* Fix packaging

#### 0.1.0

* Initial release.

## License

Copyright (c) DabApps
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of DabApps.

[build-status-image]: https://secure.travis-ci.org/dabapps/django-user-streams.png?branch=master
[travis]: http://travis-ci.org/dabapps/django-user-streams?branch=master
[use_tz]: https://docs.djangoproject.com/en/1.4/topics/i18n/timezones/
