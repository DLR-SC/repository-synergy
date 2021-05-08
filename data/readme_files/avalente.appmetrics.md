AppMetrics
++++++++++

.. image:: https://travis-ci.org/avalente/appmetrics.png?branch=master
    :target: https://travis-ci.org/avalente/appmetrics
    :alt: Build status


.. image:: https://coveralls.io/repos/avalente/appmetrics/badge.png
    :target: https://coveralls.io/r/avalente/appmetrics
    :alt: Code coverage


``AppMetrics`` is a python library used to collect useful run-time application's metrics, based on
`Folsom from Boundary <https://github.com/boundary/folsom>`_, which is in turn inspired by
`Metrics from Coda Hale <https://github.com/codahale/metrics>`_.

The library's purpose is to help you collect real-time metrics from your Python applications,
being them web apps, long-running batches or whatever. ``AppMetrics`` is not a persistent store,
you must provide your own persistence layer, maybe by using well established monitoring tools.

``AppMetrics`` works on python 2.7 and 3.3.

Getting started
---------------

Install ``AppMetrics`` into your python environment::

    pip install appmetrics

or, if you don't use ``pip``, download and unpack the package an then::

    python setup.py install

Once you have installed ``AppMetrics`` you can access it by the ``metrics`` module::

    >>> from appmetrics import metrics
    >>> histogram = metrics.new_histogram("test")
    >>> histogram.notify(1.0)
    True
    >>> histogram.notify(2.0)
    True
    >>> histogram.notify(3.0)
    True
    >>> histogram.get()
    {'arithmetic_mean': 2.0, 'kind': 'histogram', 'skewness': 0.0, 'harmonic_mean': 1.6363636363636365, 'min': 1.0, 'standard_deviation': 1.0, 'median': 2.0, 'histogram': [(3.0, 3), (5.0, 0)], 'percentile': [(50, 2.0), (75, 2.0), (90, 3.0), (95, 3.0), (99, 3.0), (99.9, 3.0)], 'n': 3, 'max': 3.0, 'variance': 1.0, 'geometric_mean': 1.8171205928321397, 'kurtosis': -2.3333333333333335}

Basically you create a new metric by using one of the ``metrics.new_*`` functions. The metric will be stored into
an internal registry, so you can access it in different places in your application::

    >>> test_histogram = metrics.metric("test")
    >>> test_histogram.notify(4.0)
    True

The ``metrics`` registry is thread-safe, you can safely use it in multi-threaded web servers.

Using the ``with_histogram`` decorator we can time a function::

    >>> import time, random
    >>> @metrics.with_histogram("test")
    ... def my_worker():
    ...     time.sleep(random.random())
    ...
    >>> my_worker()
    >>> my_worker()
    >>> my_worker()

and let's see the results::

    >>> metrics.get("test")
    {'arithmetic_mean': 0.41326093673706055, 'kind': 'histogram', 'skewness': 0.2739718270714368, 'harmonic_mean': 0.14326954591313346, 'min': 0.0613858699798584, 'standard_deviation': 0.4319169569113129, 'median': 0.2831099033355713, 'histogram': [(1.0613858699798584, 3), (2.0613858699798584, 0)], 'percentile': [(50, 0.2831099033355713), (75, 0.2831099033355713), (90, 0.895287036895752), (95, 0.895287036895752), (99, 0.895287036895752), (99.9, 0.895287036895752)], 'n': 3, 'max': 0.895287036895752, 'variance': 0.18655225766752892, 'geometric_mean': 0.24964828731906127, 'kurtosis': -2.3333333333333335}

It is also possible to time specific sections of the code by using the ``timer`` context manager::

    >>> import time, random
    ... def my_worker():
    ...     with metrics.timer("test"):
    ...         time.sleep(random.random())
    ...

Let's print the metrics data on the screen every 5 seconds::

    >>> from appmetrics import reporter
    >>> def stdout_report(metrics):
    ...     print metrics
    ...
    >>> reporter.register(stdout_report, reporter.fixed_interval_scheduler(5))
    '5680173c-0279-46ec-bd88-b318f8058ef4'
    >>> {'test': {'arithmetic_mean': 0.0, 'kind': 'histogram', 'skewness': 0.0, 'harmonic_mean': 0.0, 'min': 0, 'standard_deviation': 0.0, 'median': 0.0, 'histogram': [(0, 0)], 'percentile': [(50, 0.0), (75, 0.0), (90, 0.0), (95, 0.0), (99, 0.0), (99.9, 0.0)], 'n': 0, 'max': 0, 'variance': 0.0, 'geometric_mean': 0.0, 'kurtosis': 0.0}}
    >>> my_worker()
    >>> my_worker()
    >>> {'test': {'arithmetic_mean': 0.5028266906738281, 'kind': 'histogram', 'skewness': 0.0, 'harmonic_mean': 0.2534044030939462, 'min': 0.14868521690368652, 'standard_deviation': 0.50083167520453, 'median': 0.5028266906738281, 'histogram': [(1.1486852169036865, 2), (2.1486852169036865, 0)], 'percentile': [(50, 0.14868521690368652), (75, 0.8569681644439697), (90, 0.8569681644439697), (95, 0.8569681644439697), (99, 0.8569681644439697), (99.9, 0.8569681644439697)], 'n': 2, 'max': 0.8569681644439697, 'variance': 0.2508323668881758, 'geometric_mean': 0.35695727672917066, 'kurtosis': -2.75}}
    >>> reporter.remove('5680173c-0279-46ec-bd88-b318f8058ef4')
    <Timer(Thread-1, started daemon 4555313152)>



Decorators
**********

The ``metrics`` module also provides a couple of decorators: ``with_histogram`` and ``with_meter`` which are
an easy and fast way to use ``AppMetrics``: just decorate your functions/methods and you will have metrics
collected for them. You can decorate multiple functions with the same metric's name, as long as the decorator's
type and parameters are the same, or a ``DuplicateMetricError`` will be raised.
See the documentation for `Histograms`_ and `Meters`_ for more details.


API
---

``AppMetrics`` exposes a simple and consistent API; all the metric objects have three methods:

 * ``notify(value)``   - add a new value to the metric
 * ``get()``           - get the computed metric's value (if any)
 * ``raw_data()``      - get the raw data stored in the metrics

However, the ``notify`` input type and the ``get()`` and ``raw_data()`` data format depend on the kind
of metric chosen. Please notice that ``get()`` returns a dictionary with the mandatory
field ``kind`` which depends on the metric's type.

Metrics
-------

Several metric types are available:

Counters
********

Counter metrics provide increment and decrement capabilities for a single integer value.
The ``notify`` method accepts an integer: the counter will be incremented or decremented according
to the value's sign. Notice that the function tries to cast the input value to integer, so
a ``TypeError`` or a ``ValueError`` may be raised::

    >>> counter = metrics.new_counter("test")
    >>> counter.notify(10)
    >>> counter.notify(-5)
    >>> counter.get()
    {'kind': 'counter', 'value': 5}
    >>> counter.notify("wrong")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "appmetrics/simple_metrics.py", line 40, in notify
        value = int(value)
    ValueError: invalid literal for int() with base 10: 'wrong'

Gauges
******

Gauges are point-in-time single value metrics. The ``notify`` method accepts any data type::

    >>> gauge = metrics.new_gauge("gauge_test")
    >>> gauge.notify("version 1.0")
    >>> gauge.get()
    {'kind': 'gauge', 'value': 'version 1.0'}

The ``gauge`` metric is useful to expose almost-static values such as configuration parameters, constants and so on.
Although you can use any python data type as the value, you won't be able to use the ``wsgi`` middleware unless
you use a valid ``json`` type.

Histograms
**********

Histograms are collections of values on which statistical analysis are performed automatically. They are useful
to know how the application is performing. The ``notify`` method accepts a single floating-point value, while
the ``get`` method computes and returns the following values:

 * arithmetic mean
 * geometric mean
 * harmonic mean
 * data distribution histogram with automatic bins
 * kurtosis
 * maximum value
 * median
 * minimum value
 * number of values
 * 50, 75, 90, 95, 99 and 99.9th percentiles of the data distribution
 * skewness
 * standard deviation
 * variance

Notice that the ``notify`` method tries to cast the input value to a float, so a ``TypeError`` or a ``ValueError`` may
be raised.

You can use the histogram metric also by the ``with_histogram`` decorator: the time spent in the decorated
function will be collected by an ``histogram`` with the given name::

    >>> @metrics.with_histogram("histogram_test")
    ... def fun(v):
    ...     return v*2
    ...
    >>> fun(10)
    20
    >>> metrics.metric("histogram_test").raw_data()
    [5.9604644775390625e-06]

The full signature is::

    with_histogram(name, reservoir_type, *reservoir_args, **reservoir_kwargs)

where:

 * name is the metric's name
 * reservoir_type is a string which identifies a ``reservoir`` class, see reservoirs documentation
 * reservoir_args and reservoir_kwargs are passed to the chosen reservoir's \_\_init\_\_


Sample types
^^^^^^^^^^^^

To avoid unbound memory usage, the histogram metrics are generated from a *reservoir* of values.

Uniform reservoir
.................

The default *reservoir* type is the *uniform* one, in which a fixed number of values (default 1028)
is kept, and when the reservoir is full new values replace older ones randomly with an uniform
probability distribution, ensuring that the sample is always statistically representative.
This kind of reservoir must be used when you are interested in statistics over the whole stream of
observations. Use ``"uniform"`` as ``reservoir_type`` in ``with_histogram``.


Sliding window reservoir
........................

This *reservoir* keeps a fixed number of observations (default 1028) and when a new value comes in the first
one is discarded. The statistics are representative of the last N observations. Its ``reservoir_type``
is ``sliding_window``.

Sliding time window reservoir
.............................

This *reservoir* keeps observation for a fixed amount of time (default 60 seconds), older values get discarded.
The statistics are representative of the last N seconds, but if you have a lot of readings in N seconds this could
eat a lot amount of memory. Its ``reservoir_type`` is ``sliding_time_window``.

Exponentially-decaying reservoir
................................

This *reservoir* keeps a fixed number of values (default 1028), with
`exponential decaying <http://dimacs.rutgers.edu/~graham/pubs/papers/fwddecay.pdf>`_ of older values
in order to give greater significance to recent data. The bias towards newer values can be adjusted by
specifying a proper `alpha` value to the reservoir's init (defaults to 0.015).
Its ``reservoir_type`` is ``exp_decaying``.


Meters
******

Meters are increment-only counters that measure the rate of events (such as ``"http requests"``) over time. This kind of
metric is useful to collect throughput values (such as ``"requests per second"``), both on average and on different time
intervals::

    >>> meter = metrics.new_meter("meter_test")
    >>> meter.notify(1)
    >>> meter.notify(1)
    >>> meter.notify(3)
    >>> meter.get()
    {'count': 5, 'kind': 'meter', 'five': 0.0066114184713530035, 'mean': 0.27743058841197027, 'fifteen': 0.0022160607980413085, 'day': 2.3147478365093123e-05, 'one': 0.031982234148270686}

The return values of the ``get`` method are the following:

 * ``count``: number of operations collected so far
 * ``mean``: the average throughput since the metric creation
 * ``one``: one-minute
   `exponentially-weighted moving average <http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>`_
   (*EWMA*)
 * ``five``: five-minutes *EWMA*
 * ``fifteen``: fifteen-minutes *EWMA*
 * ``day``: last day *EWMA*
 * ``kind``: "meter"

Notice that the ``notify`` method tries to cast the input value to an integer, so a ``TypeError`` or a ``ValueError``
may be raised.

You can use the meter metric also by the ``with_meter`` decorator: the number of calls to the decorated
function will be collected by a ``meter`` with the given name.

Tagging
-------

You can group several metrics together by "tagging" them::

    >>> metrics.new_histogram("test1")
    <appmetrics.histogram.Histogram object at 0x10ac2a950>
    >>> metrics.new_gauge("test2")
    <appmetrics.simple_metrics.Gauge object at 0x10ac2a990>
    >>> metrics.new_meter("test3")
    <appmetrics.meter.Meter object at 0x10ac2a9d0>
    >>> metrics.tag("test1", "group1")
    >>> metrics.tag("test3", "group1")
    >>> metrics.tags()
    {'group1': set(['test1', 'test3'])}
    >>> metrics.metrics_by_tag("group1")
    {'test1': {'arithmetic_mean': 0.0, 'skewness': 0.0, 'harmonic_mean': 0.0, 'min': 0, 'standard_deviation': 0.0, 'median': 0.0, 'histogram': [(0, 0)], 'percentile': [(50, 0.0), (75, 0.0), (90, 0.0), (95, 0.0), (99, 0.0), (99.9, 0.0)], 'n': 0, 'max': 0, 'variance': 0.0, 'geometric_mean': 0.0, 'kurtosis': 0.0}, 'test3': {'count': 0, 'five': 0.0, 'mean': 0.0, 'fifteen': 0.0, 'day': 0.0, 'one': 0.0}}
    >>> metrics.untag('test1', 'group1')
    True
    >>> metrics.untag('test1', 'group1')
    False


As you can see above, four functions are available:

 * ``metrics.tag(metric_name, tag_name)``: tag the metric named ``<metric_name>`` with ``<tag_name>``.
   Raise ``InvalidMetricError`` if ``<metric_name>`` does not exist.
 * ``metrics.tags()``: return the currently defined tags.
 * ``metrics.metrics_by_tag(tag_name)``: return a dictionary with metric names as keys
   and metric values as returned by ``<metric_object>.get()``. Return an empty dictionary if ``tag_name`` does
   not exist.
 * ``metrics.untag(metric_name, tag_name)``: remove the tag named ``<metric_name>`` from the metric named
   ``<metric_name>``. Return True if the tag was removed, False if either the metric or the tag did not exist. When a
   tag is no longer used, it gets implicitly removed.


External access
---------------

You can access the metrics provided by ``AppMetrics`` externally by the ``WSGI``
middleware found in ``appmetrics.wsgi.AppMetricsMiddleware``. It is a standard ``WSGI``
middleware with only ``werkzeug`` as external dependency and it can be plugged in any framework supporting
the ``WSGI`` standard, for example in a ``Flask`` application::

    from flask import Flask
    from appmetrics import metrics

    metrics.new_histogram("test-histogram")
    metrics.new_gauge("test-counter")
    metrics.metric("test-counter").notify(10)

    app = Flask(__name__)

    @app.route('/hello')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        from appmetrics.wsgi import AppMetricsMiddleware
        app.wsgi_app = AppMetricsMiddleware(app.wsgi_app)
        app.run()

If you launch the above application you can ask for metrics::

    $ curl http://localhost:5000/hello
    Hello World!

    $ curl http://localhost:5000/_app-metrics
    ["test-counter", "test-histogram"]

    $ curl http://localhost:5000/_app-metrics/test-counter
    10

In this way you can easily expose your application's metrics to an external monitoring service.
Moreover, since the ``AppMetricsMiddleware`` exposes a full *RESTful API*, you can create metrics
from anywhere and also populate them with foreign application's data.

Usage
*****

As usual, instantiate the middleware with the wrapped ``WSGI`` application; it looks for
request paths starting with ``"/_app-metrics"``: if not found, the wrapped application
is called. The following resources are defined:

``/_app-metrics/metrics``
  - **GET**: return the list of the registered metrics
``/_app-metrics/metrics/<name>``
  - **GET**: return the value of the given metric or ``404``.
  - **PUT**: create a new metric with the given name. The body must be a ``JSON`` object with a
    mandatory attribute named ``"type"`` which must be one of the metrics types allowed,
    by the ``"metrics.METRIC_TYPES"`` dictionary, while the other attributes are
    passed to the ``new_<type>`` function as keyword arguments.
    Request's ``content-type`` must be ``"application/json"``.
  - **POST**: add a new value to the metric. The body must be a ``JSON`` object with a mandatory
    attribute named ``"value"``: the notify method will be called with the given value.
    Other attributes are ignored.
    Request's ``content-type`` must be ``"application/json"``.
  - **DELETE**: remove the metric with the given name. Return "deleted" or "not deleted".
``/_app-metrics/tags``
  - **GET**: return the list of registered tags
``/_app-metrics/tags/<name>``
  - **GET**: return the metrics tagged with the given tag. If the value of the ``GET`` parameter ``"expand"``
    is ``"true"``, a JSON object is returned, with the name of each tagged metric as keys and corresponding values.
    If it is ``"false"`` or not provided, the list of metric names is returned.
    Return a ``404`` if the tag does not exist
``/_app-metrics/tags/<tag_name>/<metric_name>``
  - **PUT**: tag the metric named ``<metric_name>`` with ``<tag_name>``. Return a ``400`` if the given metric
    does not exist.
  - **DELETE**: remove the tag ``<tag_name>`` from ``<metric_name>``. Return "deleted" or "not deleted". If
    ``<tag_name>`` is no longer used, it gets implicitly removed.


The response body is always encoded in JSON, and the ``Content-Type`` is ``application/json``.
The root doesn't have to be ``"/_app-metrics"``, you can customize it by providing your own to
the middleware constructor.

A standalone ``AppMetrics`` webapp can be started by using ``werkzeug``'s development server::

    $ python -m werkzeug.serving appmetrics.wsgi.standalone_app
    * Running on http://127.0.0.1:5000/

The standalone app mounts on the root (no ``_app-metrics`` prefix). DON'T use it for production purposes!!!

Reporting
---------

``AppMetrics`` provides another easy way to get your application's metrics: the ``reporter`` module. It allows
to register any number of callbacks that will be called at scheduled times with the metrics, allowing you
to "export" your application's metrics into your favourite storage system.
The main entry point for the ``reporter`` feature is ``reporter.register``::

    reporter.register(callback, schedule, tag=None)

where:

* *callback* must be a callback function that will be called with a dictionary of ``{metric name: metric values}``
* *schedule* must be an iterable object yielding a future timestamp (in ``time.time()`` format) at each iteration
* *tag* must be a tag to narrow the involved metrics to the ones with that tag, if ``None`` all the
  available metrics will be used.

When a callback is registered, a new thread will be started, waiting for the next scheduled call. Please notice
that the callback will be executed in a thread. ``register`` returns an opaque id identifying the registration.

A callback registration can be removed by calling ``reporter.remove`` with the id returned by ``register``.

``reporter`` provides a simple scheduler object, ``fixed_interval_scheduler``::

    >>> sched = reporter.fixed_interval_scheduler(10)
    >>> next(sched)
    1397297405.672592
    >>> next(sched)
    1397297415.672592
    >>> next(sched)
    1397297425.672592

CSV reporter
************

A simple reporter callback is exposed by ``reporter.CSVReporter``. As the name suggests, it will create
csv reports with metric values, a file for each metric, a row for each call. See ``examples/csv_reporter.py``


Testing
-------

``AppMetrics`` has an exhaustive, fully covering test suite, made up by both doctests and unit tests. To run the
whole test suite (including the coverage test), just issue::

    $ nosetests --with-coverage --cover-package=appmetrics --cover-erase

You will need to install a couple of packages in your python environment, the list is in the
``"requirements.txt"`` file.
