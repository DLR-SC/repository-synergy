slacker_log_handler
===================

.. image:: https://img.shields.io/pypi/v/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/wheel/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/format/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/pyversions/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/status/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

Python log handler that posts to a Slack channel. Posts to the Slack API
using https://github.com/os/slacker.

For a different implementation using webhooks instead of Slacker, see
https://github.com/claudetech/python-slack-log or read
http://www.pythian.com/blog/logging-for-slackers/

Created with the intention of using for a Django project, but some
effort has been made to make it generic enough that any Python project
could use it.

Installation
------------

.. code-block:: bash

    pip install slacker-log-handler

Options
-------

api_key (required)
~~~~~~~~~~~~~~~~~~

Generate a key at https://api.slack.com/

channel (required)
~~~~~~~~~~~~~~~~~~

Set which channel you want to post to, e.g. "#general".

username
~~~~~~~~

The username that will post to Slack. Defaults to "Python logger".

icon_url
~~~~~~~~

URL to an image to use as the icon for the logger user

icon_emoji
~~~~~~~~~~

emoji to use as the icon. Overrides icon_url. If neither icon_url nor
icon_emoji is set, :heavy_exclamation_mark: will be used.

fail_silent
~~~~~~~~~~~
Defaults to False.
If your API key is invalid or for some other reason the API call returns an error,
this option will silently ignore the API error.
If you enable this setting, **make sure you have another log handler** that will also handle the same log events,
or they may be lost entirely.


Django configuration
--------------------
Logging reference: https://docs.djangoproject.com/en/stable/topics/logging/

This example will send INFO and ERRORS to Slack, as well as errors to admin emails.

-  Set ``SLACK_API_KEY`` in your settings module.

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'slack-error': {
                'level': 'ERROR',
                'api_key': SLACK_API_KEY,
                'class': 'slacker_log_handler.SlackerLogHandler',
                'channel': '#general'
            },
            'slack-info': {
                'level': 'INFO',
                'api_key': SLACK_API_KEY,
                'class': 'slacker_log_handler.SlackerLogHandler',
                'channel': '#general'
            },
            'loggers': {
                'django.request': {
                    'handlers': ['mail_admins', 'slack-error', 'slack-info'],
                    'level': 'ERROR',
                    'propagate': True,
                },
            }
        }
    }

Example Python logging handler
------------------------------

This is how you use `slacker_log_handler` as a regular Python logging handler.
This example will send a error message to a slack channel.

.. code-block:: python

    import logging
    from slacker_log_handler import SlackerLogHandler, NoStacktraceFormatter

    # Create slack handler
    slack_handler = SlackerLogHandler('my-channel-token', 'my-channel-name', stack_trace=True)

    # Create logger
    logger = logging.getLogger('debug_application')
    logger.addHandler(slack_handler)

    # OPTIONAL: Define a log message formatter.
    # If you have set stack_trace=True, any exception stack traces will be included as Slack message attachments.
    # You therefore need to use NoStacktraceFormatter as a base to exclude the trace from the main message text.
    formatter = NoStacktraceFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    slack_handler.setFormatter(formatter)

    # Define the minimum level of log messages you want to send to Slack
    slack_handler.setLevel(logging.DEBUG)

    # Test logging
    logger.error("Debug message from slack!")

Slack message formatting
------------------------

This example use a subclass that will send a formatted message to a slack channel.
Reference: https://api.slack.com/docs/message-formatting

.. code-block:: python

  class CustomLogHandler(SlackerLogHandler):
      def build_msg(self, record):
          message = "> New message :\n" + record.getMessage()
          return message

License
-------

Apache 2.0

Slacker is also under Apache 2.0.

See also: https://api.slack.com/terms-of-service
