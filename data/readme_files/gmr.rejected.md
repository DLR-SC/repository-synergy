Rejected
========

Rejected is a AMQP consumer daemon and message processing framework. It allows
for rapid development of message processing consumers by handling all of the
core functionality of communicating with RabbitMQ and management of consumer
processes.

Rejected runs as a master process with multiple consumer configurations that are
each run it an isolated process. It has the ability to collect statistical
data from the consumer processes and report on it.

Rejected supports Python 2.7 and 3.4+.

|Version| |Status| |Coverage| |License|

Features
--------

- Automatic exception handling including connection management and consumer restarting
- Smart consumer classes that can automatically decode and deserialize message bodies based upon message headers
- Metrics logging and submission to statsd and InfluxDB
- Built-in profiling of consumer code
- Ability to write asynchronous code in consumers allowing for parallel communication with external resources

Documentation
-------------

https://rejected.readthedocs.io

Example Consumers
-----------------
.. code:: python

    from rejected import consumer
    import logging

    LOGGER = logging.getLogger(__name__)


    class Test(consumer.Consumer):

        def process(self, message):
            LOGGER.debug('In Test.process: %s' % message.body)

Async Consumer
^^^^^^^^^^^^^^
To make a consumer async, you can decorate the
`Consumer.prepare <http://rejected.readthedocs.org/en/latest/api_consumer.html#rejected.consumer.Consumer.prepare>`_
and `Consumer.process <http://rejected.readthedocs.org/en/latest/api_consumer.html#rejected.consumer.Consumer.process>`_
methods using Tornado's
`@gen.coroutine <http://www.tornadoweb.org/en/stable/gen.html#tornado.gen.coroutine>`_.
Asynchronous consumers do not allow for concurrent processing multiple messages in the same process, but
rather allow you to use asynchronous clients like
`Tornado's <http://tornadoweb.org>`_
`AsyncHTTPClient <http://www.tornadoweb.org/en/stable/httpclient.html>`_ and the
`Queries <http://queries.readthedocs.org/en/latest/tornado_session.html>`_
PostgreSQL library to perform parallel tasks using coroutines when processing a single message.

.. code:: python

    import logging

    from rejected import consumer

    from tornado import gen
    from tornado import httpclient


    class AsyncExampleConsumer(consumer.Consumer):

        @gen.coroutine
        def process(self):
            LOGGER.debug('Message: %r', self.body)
            http_client = httpclient.AsyncHTTPClient()
            results = yield [http_client.fetch('http://www.github.com'),
                             http_client.fetch('http://www.reddit.com')]
            LOGGER.info('Length: %r', [len(r.body) for r in results])


Example Configuration
---------------------
.. code:: yaml

    %YAML 1.2
    ---
    Application:
      poll_interval: 10.0
      stats:
        log: True
        influxdb:
          enabled: True
          scheme: http
          host: localhost
          port: 8086
          user: username
          password: password
          database: dbname
        statsd:
          enabled: True
          host: localhost
          port: 8125
          prefix: applications.rejected
      Connections:
        rabbitmq:
          host: localhost
          port: 5672
          user: guest
          pass: guest
          ssl: False
          vhost: /
          heartbeat_interval: 300
      Consumers:
        example:
          consumer: rejected.example.Consumer
          sentry_dsn: https://[YOUR-SENTRY-DSN]
          connections:
            - name: rabbitmq1
              consume: True
          drop_exchange: dlxname
          qty: 2
          queue: generated_messages
          qos_prefetch: 100
          ack: True
          max_errors: 100
          config:
            foo: True
            bar: baz

    Daemon:
      user: rejected
      group: daemon
      pidfile: /var/run/rejected/example.%(pid)s.pid

    Logging:
      version: 1
      formatters:
        verbose:
          format: "%(levelname) -10s %(asctime)s %(process)-6d %(processName) -25s %(name) -20s %(funcName) -25s: %(message)s"
          datefmt: "%Y-%m-%d %H:%M:%S"
        verbose_correlation:
          format: "%(levelname) -10s %(asctime)s %(process)-6d %(processName) -25s %(name) -20s %(funcName) -25s: %(message)s {CID %(correlation_id)s}"
          datefmt: "%Y-%m-%d %H:%M:%S"
        syslog:
          format: "%(levelname)s <PID %(process)d:%(processName)s> %(name)s.%(funcName)s: %(message)s"
        syslog_correlation:
          format: "%(levelname)s <PID %(process)d:%(processName)s> %(name)s.%(funcName)s: %(message)s {CID %(correlation_id)s)"
      filters:
        correlation:
          '()': rejected.log.CorrelationFilter
          'exists': True
        no_correlation:
          '()': rejected.log.CorrelationFilter
          'exists': False
      handlers:
        console:
          class: logging.StreamHandler
          formatter: verbose
          debug_only: false
          filters: [no_correlation]
        console_correlation:
          class: logging.StreamHandler
          formatter: verbose_correlation
          debug_only: false
          filters: [correlation]
        syslog:
          class: logging.handlers.SysLogHandler
          facility: daemon
          address: /var/run/syslog
          formatter: syslog
          filters: [no_correlation]
        syslog_correlation:
          class: logging.handlers.SysLogHandler
          facility: daemon
          address: /var/run/syslog
          formatter: syslog
          filters: [correlation]
      loggers:
        helper:
          level: INFO
          propagate: true
          handlers: [console, console_correlation, syslog, syslog_correlation]
        rejected:
          level: INFO
          propagate: true
          handlers: [console, console_correlation, syslog, syslog_correlation]
        tornado:
          level: INFO
          propagate: true
          handlers: [console, console_correlation, syslog, syslog_correlation]
      disable_existing_loggers: true
      incremental: false

Version History
---------------
Available at https://rejected.readthedocs.org/en/latest/history.html

.. |Version| image:: https://img.shields.io/pypi/v/rejected.svg?
   :target: https://pypi.python.org/pypi/rejected

.. |Status| image:: https://img.shields.io/travis/gmr/rejected.svg?
   :target: https://travis-ci.org/gmr/rejected

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/rejected.svg?
   :target: https://codecov.io/github/gmr/rejected?branch=master

.. |License| image:: https://img.shields.io/pypi/l/rejected.svg?
   :target: https://rejected.readthedocs.org

