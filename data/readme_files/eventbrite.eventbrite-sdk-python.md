===============================
eventbrite-sdk-python
===============================

.. image:: https://badge.fury.io/py/eventbrite.png
    :target: http://badge.fury.io/py/eventbrite

.. image:: https://travis-ci.org/eventbrite/eventbrite-sdk-python.svg?branch=master
        :target: https://travis-ci.org/eventbrite/eventbrite-sdk-python


* Official Eventbrite_ SDK for Python
* Full Documentation: http://eventbrite-sdk-python.readthedocs.org/
* API Reference: https://developer.eventbrite.com/docs/

Installation from PyPI
----------------------

::

    $ pip install eventbrite

If you need to, you can also use `easy_install`::

    $ easy_install eventbrite

Usage
-----

The Eventbrite Python SDK makes it trivial to interact with the Eventbrite API:

.. code-block:: python

    >>> from eventbrite import Eventbrite
    >>> eventbrite = Eventbrite('my-oauth-token')
    >>> user = eventbrite.get_user()  # Not passing an argument returns yourself
    >>> user['id']
    1234567890
    >>> user['name']
    Daniel Roy Greenfeld

You can also specify API endpoints manually:

.. code-block:: python

    >>> user = eventbrite.get('/users/me')
    >>> user['id']
    1234567890
    >>> user['name']
    Daniel Roy Greenfeld

Expansions_ can be included in a returned GET resource by simply adding the ``expand`` keyword to the calling method:

.. code-block:: python

    >>> event = eventbrite.get_event('my-event-id')
    >>> 'ticket_classes' in evbobject
    False
    >>> event = eventbrite.get_event('my-event-id', expand='ticket_classes')
    >>> 'ticket_classes' in evbobject
    True

.. _Expansions: http://www.eventbrite.com/developer/v3/reference/expansions/

Usage with Frameworks
----------------------

When using Flask, you can convert incoming webhook requests into Eventbrite
API objects using the `webhook_to_object()` method:

.. code-block:: python

    @app.route('/webhook', methods=['POST'])
    def webhook():


        # Use the API client to convert from a webhook to an API object
        api_object = eventbrite.webhook_to_object(request)

        # Process the API object
        if api_object.type == 'User':
            do_user_process(api_object)

        if api_object.type == 'Event':
            do_event_process(api_object)

        return ""

Versioning
----------

Because this client interacts with Eventbrite's third API (a.k.a. APIv3), we are tying our release numbers against it in a modified-semantic system:

* 3.x.x where '3' matches the API version. This will not change until Eventbrite releases a new API version.
* x.0.x where '0' is increased any time there is a significant change to the API that possibly breaks backwards compatibility
* x.x.1 where '1' is increased on any release that does not break backwards compatibility (small, new features, enhancements, bugfixes)

.. _requests: https://pypi.python.org/pypi/requests
.. _Eventbrite: https://www.eventbrite.com

Contributing
------------

Bug reports and pull requests are welcome on GitHub at https://github.com/eventbrite/eventbrite-sdk-python.


License
-------

The library is available as Open Source under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

