==============================
Request Tracker REST Interface
==============================

.. image:: https://secure.travis-ci.org/z4r/python-rtkit.png?branch=master
    :target: http://travis-ci.org/z4r/python-rtkit

.. image:: https://coveralls.io/repos/z4r/python-rtkit/badge.png?branch=master
    :target: https://coveralls.io/r/z4r/python-rtkit
    
.. image:: https://pypip.in/v/python-rtkit/badge.png
   :target: https://crate.io/packages/python-rtkit/

.. image:: https://pypip.in/d/python-rtkit/badge.png
   :target: https://crate.io/packages/python-rtkit/

`Best Practical RT`_ (Request Tracker) data access python module for REST interface.

.. contents::
    :local:

.. _installation:

Installation
============
Using pip::

    $ pip install python-rtkit

Using pip dev::

    $ pip install git+https://github.com/z4r/python-rtkit

.. _summary:

RT REST API Summary
===================
More detailed version: `Request Tracker Wiki`_

+----+----+--------------------------------+--------------------------------------------------------+
| 01 |  W | Create ticket                  | ticket/new                                             |
+----+----+--------------------------------+--------------------------------------------------------+
| 02 | RW | Read/Update ticket             | ticket/<ticket-id>                                     |
+----+----+--------------------------------+--------------------------------------------------------+
| 03 |  W | Create ticket comment          | ticket/<ticket-id>/comment                             |
+----+----+--------------------------------+--------------------------------------------------------+
| 04 | RW | Read/Update ticket links       | ticket/<ticket-id>/links                               |
+----+----+--------------------------------+--------------------------------------------------------+
| 05 | R  | Read ticket attachments        | ticket/<ticket-id>/attachments                         |
+----+----+--------------------------------+--------------------------------------------------------+
| 06 | R  | Read ticket attachment         | ticket/<ticket-id>/attachments/<attachment-id>         |
+----+----+--------------------------------+--------------------------------------------------------+
| 07 | R  | Read ticket attachment content | ticket/<ticket-id>/attachments/<attachment-id>/content |
+----+----+--------------------------------+--------------------------------------------------------+
| 08 | R  | Read ticket history            | ticket/<ticket-id>/history                             |
+----+----+--------------------------------+--------------------------------------------------------+
| 09 | R  | Read detailed ticket history   | ticket/<ticket-id>/history?format=l                    |
+----+----+--------------------------------+--------------------------------------------------------+
| 10 | R  | Read ticket history item       | ticket/<ticket-id>/history/id/<history-id>             |
+----+----+--------------------------------+--------------------------------------------------------+
| 11 | R  | Read user by id                | user/<user-id>                                         |
+----+----+--------------------------------+--------------------------------------------------------+
| 12 | R  | Read user by name              | user/<user-Name>                                       |
+----+----+--------------------------------+--------------------------------------------------------+
| 13 | R  | Read queue by id               | queue/<queue-id>                                       |
+----+----+--------------------------------+--------------------------------------------------------+
| 14 | R  | Read queue by name             | queue/<queue-Name>                                     |
+----+----+--------------------------------+--------------------------------------------------------+
| 15 | R  | Search tickets                 | search/ticket?query=<q>&orderby=<o>&format=<f>         |
+----+----+--------------------------------+--------------------------------------------------------+

.. _authentication_handlers:

Authentication Handlers
=======================

Basic Authentication
--------------------

::

    from rtkit.resource import RTResource
    from rtkit.authenticators import BasicAuthenticator
    from rtkit.errors import RTResourceError

    from rtkit import set_logging
    import logging
    set_logging('debug')
    logger = logging.getLogger('rtkit')

    resource = RTResource('http://<HOST>/REST/1.0/', '<USER>', '<PWD>', BasicAuthenticator)

Cookie-based Authentication
---------------------------

::

    from rtkit.resource import RTResource
    from rtkit.authenticators import CookieAuthenticator
    from rtkit.errors import RTResourceError

    from rtkit import set_logging
    import logging
    set_logging('debug')
    logger = logging.getLogger('rtkit')

    resource = RTResource('http://<HOST>/REST/1.0/', '<USER>', '<PWD>', CookieAuthenticator)

QueryString Authentication
---------------------------

::

    from rtkit.resource import RTResource
    from rtkit.authenticators import QueryStringAuthenticator
    from rtkit.errors import RTResourceError

    from rtkit import set_logging
    import logging
    set_logging('debug')
    logger = logging.getLogger('rtkit')

    resource = RTResource('http://<HOST>/REST/1.0/', '<USER>', '<PWD>', QueryStringAuthenticator)

Kerberos Authentication
---------------------------

::

    from rtkit.resource import RTResource
    from rtkit.authenticators import KerberosAuthenticator
    from rtkit.errors import RTResourceError

    from rtkit import set_logging
    import logging
    set_logging('debug')
    logger = logging.getLogger('rtkit')

    resource = RTResource(url, None, None, KerberosAuthenticator)

.. warning:: Remeber to install `urllib2_kerberos`.

.. _overview:

Overview on Low Level API
=========================

Create ticket
-------------

::

    content = {
        'content': {
            'Queue': 1,#'', 2
            'Subject': 'New Ticket',
            'Text': 'My useless\ntext on\nthree lines.',
        }
    }
    try:
        response = resource.post(path='ticket/new', payload=content,)
        logger.info(response.parsed)
    except RTResourceError as e:
        logger.error(e.response.status_int)
        logger.error(e.response.status)
        logger.error(e.response.parsed)

::

 #OK
 [DEBUG] POST ticket/new
 [DEBUG] {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] u'content=Queue: 1\nText: My useless\n text on\n three lines.\nSubject: New Ticket\n'
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] 'RT/3.8.10 200 Ok\n\n# Ticket 17 created.\n\n'
 [INFO] RESOURCE_STATUS: 200 Ok
 [INFO] [[('id', 'ticket/17')]]

::

 #MISSING OR MISSPELLED QUEUE
 [DEBUG] POST ticket/new
 [DEBUG] {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] u'content=Queue: \nText: My useless\n text on\n three lines.\nSubject: New Ticket\n'
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] 'RT/3.8.10 200 Ok\n\n# Could not create ticket.\n# Could not create ticket. Queue not set\n\n'
 [INFO] RESOURCE_STATUS: 400 Could not create ticket. Queue not set
 [ERROR] 400
 [ERROR] 400 Could not create ticket. Queue not set
 [ERROR] []

::

 #NO PERMISSION ON QUEUE
 [DEBUG] POST ticket/new
 [DEBUG] {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] u'content=Queue: 2\nText: My useless\n text on\n three lines.\nSubject: New Ticket\n'
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] "RT/3.8.10 200 Ok\n\n# Could not create ticket.\n# No permission to create tickets in the queue '___Approvals'\n\n"
 [INFO] RESOURCE_STATUS: 400 No permission to create tickets in the queue '___Approvals'
 [ERROR] 400
 [ERROR] 400 No permission to create tickets in the queue '___Approvals'
 [ERROR] []

Read a ticket
-------------

::

    try:
        response = resource.get(path='ticket/1')
        for r in response.parsed:
            for t in r:
                logger.info(t)
    except RTResourceError as e:
        logger.error(e.response.status_int)
        logger.error(e.response.status)
        logger.error(e.response.parsed)

::

 #TICKET FOUND
 [DEBUG] GET ticket/1
 [DEBUG] {'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] None
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] 'RT/3.8.10 200 Ok\n\nid: ticket/1\nQueue: General\nOwner: Nobody\nCreator: pyrtkit\nSubject: pyrt-create4\nStatus: open\nPriority: 5\nInitialPriority: 0\nFinalPriority: 0\nRequestors:\nCc:\nAdminCc:\nCreated: Sun Jul 03 10:48:57 2011\nStarts: Not set\nStarted: Not set\nDue: Not set\nResolved: Not set\nTold: Wed Jul 06 12:58:00 2011\nLastUpdated: Thu Jul 07 14:42:32 2011\nTimeEstimated: 0\nTimeWorked: 25 minutes\nTimeLeft: 0\n\n'
 [INFO] RESOURCE_STATUS: 200 Ok
 [INFO] ('id', 'ticket/1')
 [INFO] ('Queue', 'General')
 [INFO] ('Owner', 'Nobody')
 [INFO] ('Creator', 'pyrtkit')
 [INFO] ('Subject', 'pyrt-create4')
 [INFO] ('Status', 'open')
 [INFO] ('Priority', '5')
 [INFO] ('InitialPriority', '0')
 [INFO] ('FinalPriority', '0')
 [INFO] ('Requestors', '')
 [INFO] ('Cc', '')
 [INFO] ('AdminCc', '')
 [INFO] ('Created', 'Sun Jul 03 10:48:57 2011')
 [INFO] ('Starts', 'Not set')
 [INFO] ('Started', 'Not set')
 [INFO] ('Due', 'Not set')
 [INFO] ('Resolved', 'Not set')
 [INFO] ('Told', 'Wed Jul 06 12:58:00 2011')
 [INFO] ('LastUpdated', 'Thu Jul 07 14:42:32 2011')
 [INFO] ('TimeEstimated', '0')
 [INFO] ('TimeWorked', '25 minutes')
 [INFO] ('TimeLeft', '0')

::

 #TICKET NOT FOUND
 [DEBUG] GET ticket/100
 [DEBUG] {'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] None
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] 'RT/3.8.10 200 Ok\n\n# Ticket 100 does not exist.\n\n\n'
 [INFO] RESOURCE_STATUS: 404 Ticket 100 does not exist
 [ERROR] 404
 [ERROR] 404 Ticket 100 does not exist
 [ERROR] []

Edit a ticket or ticket's links
-------------------------------
Ticket (or ticket's links) editing hasn't all-or-nothing behaviour; so it's very difficult to capture errors.
For example trying to change Queue to a not admitted one (or to edit an unknown field) RT will return:

::

 RT/3.8.10 409 Syntax Error

 # queue: You may not create requests in that queue.
 # spam: Unknown field.

 id:
 Subject: Try Edit Ticket
 TimeWorked: 1
 Queue: 2
 Spam: 10

For now rtkit will raise SyntaxError with the errors list in e.response.parsed

::

 [DEBUG] POST ticket/1
 [DEBUG] {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain', 'User-Agent': 'pyRTkit/0.0.1'}
 [DEBUG] u'content=Queue: 2\nSpam: 10\nTimeWorked: 1\nSubject: Try Edit Ticket\n'
 [INFO] HTTP_STATUS: 200 OK
 [DEBUG] 'RT/3.8.10 409 Syntax Error\n\n# queue: You may not create requests in that queue.\n# spam: Unknown field.\n\nid: \nSubject: Try Edit Ticket\nTimeWorked: 1\nQueue: 2\nSpam: 10\n\n'
 [INFO] RESOURCE_STATUS: 409 Syntax Error
 [ERROR] 409
 [ERROR] 409 Syntax Error
 [ERROR] [[('queue', 'You may not create requests in that queue.'), ('spam', 'Unknown field.')]]

Comment on a Ticket with Attachments
------------------------------------

Usually your requests will be something like this.

::

    try:
        params = {
            'content': {
                'Action': 'comment',
                'Text': 'Comment with attach',
                'Attachment': 'x.txt, 140x105.jpg',
            },
            'attachment_1': file('x.txt'),
            'attachment_2': file('140x105.jpg'),
        }
        response = resource.post(path='ticket/16/comment', payload=params,)
        for r in response.parsed:
            for t in r:
                logger.info(t)
    except RTResourceError as e:
        logger.error(e.response.status_int)
        logger.error(e.response.status)
        logger.error(e.response.parsed)
        
Custom Fields
-------------

To create or update a tkt with Custom Fields you must use this notation::

    content = {
        'content': {
            'Queue': 1,
            'Subject' : 'New Ticket',
            'Text' : 'My useless\ntext on\nthree lines.',
            'CF.{Need For Approval}': 'Yes' 
        }
    }

.. warning:: With RT/3.8 you can't use ``?`` inside the names of your custom fields, with RT/3.6 ``/()`` too.

.. _license:

License
=======

This software is licensed under the ``Apache License 2.0``. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. _references:

References
==========
* `Best Practical RT`_
* `Request Tracker Wiki`_

.. _Best Practical RT: http://bestpractical.com/rt/
.. _Request Tracker Wiki: http://requesttracker.wikia.com/wiki/REST


.. image:: https://d2weczhvl823v0.cloudfront.net/z4r/python-rtkit/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

