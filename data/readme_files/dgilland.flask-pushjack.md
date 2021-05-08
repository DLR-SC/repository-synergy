**************
Flask-Pushjack
**************

|version| |travis| |coveralls| |license|

Flask extension for push notifications on APNS (iOS) and GCM (Android).


Links
=====

- Project: https://github.com/dgilland/flask-pushjack
- Documentation: http://flask-pushjack.readthedocs.org
- PyPi: https://pypi.python.org/pypi/flask-pushjack/
- TravisCI: https://travis-ci.org/dgilland/flask-pushjack


Quickstart
==========

Whether using ``APNS`` or ``GCM``, Flask-Pushjack provides an API client for each.


APNS
----

.. code-block:: python

    from flask import Flask
    from flask_pushjack import FlaskAPNS

    config = {
        'APNS_CERTIFICATE': '<path/to/certificate.pem>'
    }

    app = Flask(__name__)
    app.config.update(config)

    client = FlaskAPNS()
    client.init_app(app)

    with app.app_context():
        token = '<device token>'

        # Send to single device.
        res = client.send(token, alert, **options)

        # List of all tokens sent.
        res.tokens

        # List of any subclassed APNSServerError objects.
        res.errors

        # Dict mapping token => APNSServerError.
        res.token_errors

        # Send to multiple devices.
        client.send([token], alert, **options)

        # Get expired tokens.
        expired_tokens = client.get_expired_tokens()


GCM
---

.. code-block:: python

    from flask import Flask
    from flask_pushjack import FlaskGCM

    config = {
        'GCM_API_KEY': '<api-key>'
    }

    app = Flask(__name__)
    app.config.update(config)

    client = FlaskGCM()
    client.init_app(app)

    with app.app_context():
        token = '<device token>'

        # Send to single device.
        res = client.send(token, alert, **options)

        # List of requests.Response objects from GCM Server.
        res.responses

        # List of messages sent.
        res.messages

        # List of registration ids sent.
        res.registration_ids

        # List of server response data from GCM.
        res.data

        # List of successful registration ids.
        res.successes

        # List of failed registration ids.
        res.failures

        # List of exceptions.
        res.errors

        # List of canonical ids (registration ids that have changed).
        res.canonical_ids


        # Send to multiple devices.
        client.send([token], alert, **options)


For more details, please see the documentation for pushjack at http://pushjack.readthedocs.org.


Configuration
-------------

APNS
++++

==================================  ===
``APNS_CERTIFICATE``                File path to certificate PEM file (**must be set**). Default: ``None``
``APNS_ENABLED``                    Whether to enable sending. Default ``True``
``APNS_SANDBOX``                    Whether to use sandbox server. Default: ``False``
``APNS_DEFAULT_ERROR_TIMEOUT``      Timeout when polling APNS for error after sending. Default: ``10``
``APNS_DEFAULT_EXPIRATION_OFFSET``  Message expiration (secs) from now. Default: ``2592000`` (1 month)
``APNS_DEFAULT_BATCH_SIZE``         Number of notifications to group together when sending.
==================================  ===


GCM
+++

======================  ===
``GCM_API_KEY``         API key (**must be set**). Default: ``None``
``GCM_ENABLED``         Whether to enable sending. Default ``True``
======================  ===


.. |version| image:: http://img.shields.io/pypi/v/flask-pushjack.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-pushjack/

.. |travis| image:: http://img.shields.io/travis/dgilland/flask-pushjack/master.svg?style=flat-square
    :target: https://travis-ci.org/dgilland/flask-pushjack

.. |coveralls| image:: http://img.shields.io/coveralls/dgilland/flask-pushjack/master.svg?style=flat-square
    :target: https://coveralls.io/r/dgilland/flask-pushjack

.. |license| image:: http://img.shields.io/pypi/l/flask-pushjack.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-pushjack/
