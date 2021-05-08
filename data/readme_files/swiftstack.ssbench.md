.. contents::  :depth:  1

What Is This?
=============

`SwiftStack`_ Benchmark Suite (``ssbench``) is a flexible and scalable
benchmarking tool for the `OpenStack Swift`_ object storage system.

The ``ssbench-master run-scenario`` command will run benchmark "scenarios"
against an
OpenStack Swift cluster, utilizing one or more distributed ``ssbench-worker``
processes, saving statistics about the run to a file.  The ``ssbench-master
report-scenario`` command can then generate a
report from the saved statistics.  By default, ``ssbench-master run-scenario``
will generate a report to STDOUT immediately following a benchmark run in
addition to saving the raw results to a file.

Coordination between the ``ssbench-master`` and one or more ``ssbench-worker``
processes is managed through a pair of `PyZMQ`_ sockets.  This
allows ``ssbench-master`` to distribute the benchmark run across many, many
client servers while still coordinating the entire run (each worker can be
given a job referencing an object created by a different worker).

.. _`PyZMQ`: http://zeromq.github.com/pyzmq/
.. _`OpenStack Swift`: http://docs.openstack.org/developer/swift/
.. _`SwiftStack`: http://swiftstack.com/


Project Status
==============

Continuous Integration: |travisci|

Code Quality: |landscape|

.. |travisci| image:: https://travis-ci.org/swiftstack/ssbench.png?branch=master
    :target: https://travis-ci.org/swiftstack/ssbench

.. |landscape| image:: https://landscape.io/github/swiftstack/ssbench/master/landscape.png
    :target: https://landscape.io/github/swiftstack/ssbench/master


Installation
============

These instructions setup a _virtualenv_ environment for `ssbench`. This avoids
conflicts between ssbench and other libraries that may installed systemwide
(such as libzmq). It is strongly advised to avoid installing `ssbench`
systemwide to avoid such conflicts.

If a system install of `libzmq` is present, to ensure that `ssbench` will work
correctly, the `pyzmq` package must be installed with its bundled version of
`libzmq`.  The below steps demonstrate how to accomplish that on various
distributions.

Ubuntu (Precise & Trusty tested)
--------------------------------

Installation on Ubuntu Precise or Trusty::

  $ sudo apt-get update
  $ sudo apt-get install -y gcc g++ python-dev python-virtualenv
  $ virtualenv ./ssbench-env
  $ ./ssbench-env/bin/pip install pyzmq==14.0.1 --install-option="--zmq=bundled"
  $ ./ssbench-env/bin/pip install ssbench

Fedora 18
---------

Installation on Fedora 18 using its stock Python 2.7 (NOT ACTUALLY TESTED YET)::

  $ sudo yum install -y gcc gcc-c++ python-devel python-virtualenv
  $ virtualenv ./ssbench-env
  $ ./ssbench-env/bin/pip install pyzmq==14.0.1 --install-option="--zmq=bundled"
  $ ./ssbench-env/bin/pip install ssbench

RHEL 6.6
--------

Installation on RHEL 6.6 using its stock Python 2.6::

  $ sudo rpm -Uvh http://mirror.pnl.gov/epel/6/i386/epel-release-6-8.noarch.rpm
  $ sudo yum makecache
  $ sudo yum install -y gcc gcc-c++ python-devel python-virtualenv
  $ virtualenv ./ssbench-env
  $ ./ssbench-env/bin/pip install pyzmq==14.0.1 --install-option="--zmq=bundled"
  $ ./ssbench-env/bin/pip install ssbench

CentOS 6.6
----------

Installation on CentOS 6.6 using its stock Python 2.6::

  $ sudo rpm -Uvh http://mirror.pnl.gov/epel/6/i386/epel-release-6-8.noarch.rpm
  $ sudo yum makecache
  $ sudo yum install -y gcc gcc-c++ python-devel python-virtualenv
  $ virtualenv ./ssbench-env
  $ ./ssbench-env/bin/pip install pyzmq==14.0.1 --install-option="--zmq=bundled"
  $ ./ssbench-env/bin/pip install ssbench

OS X
----

On the Mac, I recommend installing `Homebrew`_ and using that to install Python
2.7 and zeromq.  I haven't tested a fresh install in a while, but I had far
less problems with Cython and gevent-zeromq on OS X, probably because the
`Homebrew`_ Python was newer than Ubuntu 12.04's?

.. _`Homebrew`: http://mxcl.github.com/homebrew/

Then you should be able to just ``pip install ssbench``.


How Does It Work?
=================

Scenarios
---------

A "scenario" (sometimes called a "CRUD scenario") is a utf8-encoded JSON file
defining a benchmark run.  Specifically, it defines:

- A ``name`` for the scenario (an arbitrary string)
- A ``sizes`` list of "object size" classes.  Each object size class has a
  ``name``, a ``size_min`` minimum object size, a ``size_max`` maximum object
  size (in bytes), and an
  optional ``crud_profile`` for just this size.  If ``crud_profile`` is not
  given for a size, the top-level ``crud_profile`` will be used.  The
  ``crud_profile`` here is just like the top-level one, an array of 4 numbers
  whose relative sizes determine the percent chance of a Create, Read, Update,
  or Delete operation.  Objects created or updated within an object size
  class will have a size (in bytes) chosen at random uniformly between the
  minimum and maximum sizes.
- An ``initial_files`` dictionary of initial file-counts per size class.  Each
  size class can have zero or
  more objects uploaded *prior* to the benchmark run itself.  The proportion of
  initial files also defines the probability distribution of object sizes
  during the benchmark run itself.  So if a particular object size class is not
  included in ``initial_files`` or has a value of 0 in ``initial_files``, then
  no objects in that size class will be used during the benchmark run.  Each
  initial object's name and container is deterministic and, as an optimization,
  if an object of the right name is in the right container, it will not be
  uploaded again; note that initial objects are not deleted after each
  benchmark run, so this can speed up subsequent runs quite a bit.
- An ``operation_count`` of operations to perform during the benchmark run.
  An operation is
  either a CREATE, READ, UPDATE, or DELETE of an object.  This value may be
  overridden for any given run with the ``-o COUNT`` flag to ``ssbench-master
  run-scenario``.
- A ``run_seconds`` number of seconds the benchmark scenario should run.  This
  is mutually exclusive with ``operation_count``, so only one of those two
  should be specified.  Both values may be overridden with command-line
  arguments to ``ssbench-master``.
- A ``crud_profile`` which determines the distribution of each kind of operation.
  For instance, ``[3, 4, 2, 2]`` would mean 27% CREATE, 36% READ, 18% UPDATE,
  and 18% DELETE.
- A ``user_count`` which determines the maximum client concurrency during the
  benchmark run.  The user is responsible for ensuring there are enough workers
  running to support the scenario's defined ``user_count``.  (Each
  ``ssbench-worker`` process uses `gevent`_ to achieve very efficient
  concurrency for the benchmark client requests.)  This value may be overridden
  for any given run with the ``-u COUNT`` flag to ``ssbench-master
  run-scenario``.
- A ``container_base`` which is a string used to construct the names of
  containers used by ssbench.  It defaults to ``ssbench``, resulting in
  container names like ``ssbench_000061``.
- A ``container_count`` which determines how many Swift containers are used for
  the benchmark run.  This key is optional in the scenario file and defaults to
  100.  This value may be overridden for any given run with the ``-c
  COUNT`` flag to ``ssbench-master run-scenario``.
- A ``container_concurrency`` value which determines the level of client
  concurrency used by ``ssbench-master`` to create the benchmark containers.
  This value is optional and defaults to 10.
- A ``delete_after`` value appends expiring time(in seconds) to all objects.
  It emulates continuous loads of PUT operation (CREATE and UPDATE) with
  X-Delete-After header. If setting 0 (or None by default), this feature is
  disable and all objects will not be expired. This value may be overridden
  for any given run with the ``--delete-after DELETE_AFTER`` flag to
  ``ssbench-master run-scenario``.
- A ``policy`` which is the name of a Storage Policy. This storage policy
  should already exist in your Swift cluster. All containers created for the
  run will be created with this Storage Policy.
  This can be overridden for any given run with the ``--policy storage-policy``
  flag to ``ssbench-master run-scenario``.

For each operation of the benchmark run, a size category is first chosen based
on the relative counts for each size category in the ``initial_files``
dictionary.  This probability for each size category appears under the "% Ops"
column in the report.  Then an operation type is chosen based on that size
category's CRUD profile (which can be individually specified or may be
inherited from the "top level" CRUD profile).

If each size category has its own CRUD profile, then the overall CRUD profile
of the benchmark run will be a weighted average between the values in the "%
Ops" column and the CRUD profile of each size category.  This weighted average
CRUD profile is included in the report on the "CRUD weighted average" line.

.. _`gevent`: http://www.gevent.org/

``ssbench`` comes with a few canned scenarios, but users are encouraged to
experiment and define their own.

Here is an example JSON scenario file::

  {
    "name": "Small test scenario",
    "sizes": [{
      "name": "tiny",
      "size_min": 4096,
      "size_max": 65536
    }, {
      "name": "small",
      "size_min": 100000,
      "size_max": 200000
    }],
    "initial_files": {
      "tiny": 100,
      "small": 10
    },
    "operation_count": 500,
    "crud_profile": [3, 4, 2, 2],
    "user_count": 7
  }

**Beware:** hand-editing JSON is error-prone.  Watch out for trailing
commas, in particular.

Usage
-----

The ``ssbench-worker`` script's usage message may be generated with::

  $ ssbench-worker -h
  usage: ssbench-worker [-h] [--zmq-host ZMQ_HOST]
                        [--zmq-work-port ZMQ_WORK_PORT]
                        [--zmq-results-port ZMQ_RESULTS_PORT] [-c CONCURRENCY]
                        [--retries RETRIES] [--batch-size COUNT] [-p COUNT] [-v]
                        worker_id

  ...

The ``ssbench-master`` command requires one sub-command, which is currently
either ``run-scenario`` to actually run a benchmark scenario,
``report-scenario`` to report on an existing scenario result data file, or
``kill-workers`` to tell connected ``ssbench-worker`` processes not started
with ``--workers`` to kill themselves::

  usage: ssbench-master [-h] [-v] [-q]

                        {report-scenario,kill-workers,run-scenario,cleanup-containers}
                        ...

  SwiftStack Benchmark (ssbench) version 0.2.20

  positional arguments:
    {report-scenario,kill-workers,run-scenario,cleanup-containers}
      kill-workers        Tell all workers to exit.
      run-scenario        Run CRUD scenario, saving statistics. You must supply
                          a valid set of v1.0 or v2.0 auth credentials. See
                          usage message for run-scenario for more details.
      report-scenario     Generate a report from saved scenario statistics.
                          Various types of reports may be generated, with the
                          default being a "textual summary".
      cleanup-containers  Recursively delete all ssbench containers and their
                          objects.

  optional arguments:
    -h, --help            show this help message and exit
    -v, --verbose         Enable more verbose output. (default: False)
    -q, --quiet           Suppress most output (including progress characters
                          during run). (default: False)

The ``run-scenario`` sub-command of ``ssbench-master`` actually
runs a benchmark scenario::

  $ ssbench-master run-scenario -h
  usage: ssbench-master run-scenario [-h] -f SCENARIO_FILE
                                     [--zmq-bind-ip BIND_IP]
                                     [--zmq-work-port PORT]
                                     [--zmq-results_port PORT] [-V AUTH_VERSION]
                                     [-A AUTH_URL] [-U USER] [-K KEY]
                                     [--os-username <auth-user-name>]
                                     [--os-password <auth-password>]
                                     [--os-tenant-id <auth-tenant-id>]
                                     [--os-tenant-name <auth-tenant-name>]
                                     [--os-auth-url <auth-url>]
                                     [--os-auth-token <auth-token>]
                                     [--os-storage-url <storage-url>]
                                     [--os-region-name <region-name>]
                                     [--os-service-type <service-type>]
                                     [--os-endpoint-type <endpoint-type>]
                                     [--os-cacert <ca-certificate>] [--insecure]
                                     [-S STORAGE_URL] [-T TOKEN] [-c COUNT]
                                     [-u COUNT] [-o COUNT] [-r SECONDS]
                                     [-b BYTES] [--workers COUNT]
                                     [--batch-size COUNT] [--profile] [--noop]
                                     [-k] [--connect-timeout CONNECT_TIMEOUT]
                                     [--network-timeout NETWORK_TIMEOUT]
                                     [-s STATS_FILE] [-R] [--csv]
                                     [--pctile PERCENTILE]
                                     [--delete-after DELETE_AFTER]
  ...


The ``report-scenario`` sub-command of ``ssbench-master`` reports on a
previously-run benchmark scenario::

  $ ssbench-master report-scenario -h
  usage: ssbench-master report-scenario [-h] -s STATS_FILE [-f REPORT_FILE]
                                        [--pctile PERCENTILE] [--csv]
                                        [-r RPS_HISTOGRAM] [--profile]
  ...

The ``kill-workers`` sub-command of ``ssbench-master`` kills all
``ssbench-worker`` processes which are pointed at the ``ssbench-master``
ZMQ sockets (this is useful for multi-server benchmark runs where the workers
were not started with ``ssbench-master``'s ``--workers`` option)::

  $ ssbench-master kill-workers -h
  usage: ssbench-master kill-workers [-h] [--zmq-bind-ip BIND_IP]
                                     [--zmq-work-port PORT]
                                     [--zmq-results_port PORT]
  ...

The ``cleanup-containers`` sub-command of ``ssbench-master`` recursively
deletes all ssbench-created containers and objects.  It takes all the same
authorization-related options as ``run-scenario``::

  $ ssbench-master cleanup-containers -h
  usage: ssbench-master cleanup-containers [-h] [-b CONTAINER_BASE]
                                           [-c CONCURRENCY] [-V AUTH_VERSION]
                                           [-A AUTH_URL] [-U USER] [-K KEY]
                                           [--os-username <auth-user-name>]
                                           [--os-password <auth-password>]
                                           [--os-tenant-id <auth-tenant-id>]
                                           [--os-tenant-name <auth-tenant-name>]
                                           [--os-auth-url <auth-url>]
                                           [--os-auth-token <auth-token>]
                                           [--os-storage-url <storage-url>]
                                           [--os-region-name <region-name>]
                                           [--os-service-type <service-type>]
                                           [--os-endpoint-type <endpoint-type>]
                                           [--os-cacert <ca-certificate>]
                                           [--insecure] [-S STORAGE_URL]
                                           [-T TOKEN]
  ...


Authentication
--------------

``ssbench-master`` supports all the same authentication arguments, with similar
semantics, as `python-swiftclient`_'s command-line tool, ``swift``.

For v1.0 authentication, you just need ``ST_AUTH``, ``ST_USER``, and ``ST_KEY``
defined in the environment or overridden/set on the command-line with ``-A``,
``-U``, and ``-K``, respectively.

For v2.0 authentication (Keystone), it's more complicated and you should refer
to Keystone and/or `python-swiftclient`_ documentation for more help.

Regardless of which version of authentication is used, you may specify ``-S
<storage_url>`` on the command-line to override the Storage URL returned from
the authentication system.

.. _`python-swiftclient`: https://github.com/openstack/python-swiftclient


Load Balancing
--------------

You can bypass your normal load-balancing scheme by telling ``ssbench-master``
to distribute load across a specified set of Storage URLs.  This is done by
specifying one or more ``-S STORAGE_URL`` options to ``ssbench-master``.  Any
storage URL returned from the auth server will be ignored and a randomly chosen
command-line-specified storage URL will be used instead.

Note that each ``ssbench-worker`` process will create a fully-populated
connection pool for each unique ``-S`` argument specified.  Each connection
pool will contain a number of sockets equal to the ``-c`` option (which defaults
to 64).  So a large number of unique ``-S`` arguments for ``ssbench-worker``
and a large ``-c`` value for ``ssbench-worker`` processes will not mix well.


Example Multi-Server Run
------------------------

Start one or more ``ssbench-worker`` processes on each server (each
``ssbench-worker`` process defaults to a maximum `gevent`_-based concurrency
of 64, but the ``-c`` option can override that default).  Use the
``--zmq-host`` command-line parameter to specify the host on which you will run
``ssbench-master``.::

  bench-host-01$ ssbench-worker -c 1000 --zmq-host bench-host-01 1 &
  bench-host-01$ ssbench-worker -c 1000 --zmq-host bench-host-01 2 &

  bench-host-02$ ssbench-worker -c 1000 --zmq-host bench-host-01 3 &
  bench-host-02$ ssbench-worker -c 1000 --zmq-host bench-host-01 4 &

Finally, run one ``ssbench-master`` process which will manage and coordinate
the multi-server benchmark run::

  bench-host-01$ ssbench-master run-scenario -f scenarios/very_small.scenario -u 2000 -o 40000

The above example would involve a total client concurrency of 2000, spread
evenly among the four workers on two hosts (``bench-host-01`` and
``bench-host-02``).  The four workers, as started in the above example,
could support a maximum total client concurrency (``-u`` option to
``ssbench-master``) up to 4000.


Example Simple Single-Server Run
--------------------------------

If you only need workers running on the local host, you can do so with a single
command.  Simply use the ``--workers COUNT`` option to ``ssbench-master``::

  $ ssbench-master run-scenario -f scenarios/very_small.scenario -u 4 -c 80 -o 613 --pctile 50 --workers 2
  INFO:SwiftStack Benchmark (ssbench version 0.2.14)
  INFO:Spawning local ssbench-worker (logging to /tmp/ssbench-worker-local-0.log) with ssbench-worker ... --concurrency 2 --batch-size 1 0
  INFO:Spawning local ssbench-worker (logging to /tmp/ssbench-worker-local-1.log) with ssbench-worker ... --concurrency 2 --batch-size 1 1
  INFO:Starting scenario run for "Small test scenario"
  INFO:Ensuring 80 containers (ssbench_*) exist; concurrency=10...
  INFO:Initializing cluster with stock data (up to 4 concurrent workers)
  INFO:Starting benchmark run (up to 4 concurrent workers)
  Benchmark Run:
    X    work job raised an exception
    .  <  1s first-byte-latency
    o  <  3s first-byte-latency
    O  < 10s first-byte-latency
    * >= 10s first-byte-latency
    _  <  1s last-byte-latency  (CREATE or UPDATE)
    |  <  3s last-byte-latency  (CREATE or UPDATE)
    ^  < 10s last-byte-latency  (CREATE or UPDATE)
    @ >= 10s last-byte-latency  (CREATE or UPDATE)
  ....._........_.._......_.._..__.._.._..._...__...__._..._._..................
  ....._.._....__........._.._._......__.._.._._......._..__.._....._..._...__._
  ...._......_....____....__._.........._...._...._......._....__._.._._..__._..
  ....__.._..._._._....._......_...._...__...._...___.........._.._._..___..._._
  ....._._....__.............._.__..._...._...._...._._.._....___........_.__.._
  _..__._.__.._.................__......._......._...._.____...._.._....._...._.
  ..._.............__.._..._.._.._._._._...._.._.._....__._._........_......_.__
  .........._._...._.._.........._........_._.._....._......._....._.
  INFO:Deleting population objects from cluster
  INFO:Calculating statistics...

  Small test scenario  (generated with ssbench version 0.2.14)
  Worker count:   2   Concurrency:   4  Ran 2013-06-07 17:23:16 UTC to 2013-06-07 17:23:22 UTC (5s)
  Object expiration (X-Delete-After): None (sec)

  % Ops    C   R   U   D       Size Range       Size Name
   91%   % 10  75  15   0        4 kB -   8 kB  tiny
    9%   % 10  75  15   0       20 kB -  40 kB  small
  ---------------------------------------------------------------------
           10  75  15   0      CRUD weighted average

  TOTAL
         Count:   613  (   0 error;    0 retries:  0.00%)  Average requests per second: 118.7
                              min       max      avg      std_dev  50%-ile                   Worst latency TX ID
         First-byte latency:  0.004 -   0.044    0.017  (  0.008)    0.016  (all obj sizes)  txe026893bbf09486c83fcdb629f6f25a3
         Last-byte  latency:  0.004 -   0.157    0.029  (  0.024)    0.019  (all obj sizes)  tx6f988120ec5044329f817-0051b21708
         First-byte latency:  0.004 -   0.044    0.016  (  0.007)    0.016  (    tiny objs)  tx1d35c8e273bf4bbeb6298-0051b21705
         Last-byte  latency:  0.004 -   0.157    0.028  (  0.024)    0.019  (    tiny objs)  tx6f988120ec5044329f817-0051b21708
         First-byte latency:  0.005 -   0.044    0.018  (  0.008)    0.016  (   small objs)  txe026893bbf09486c83fcdb629f6f25a3
         Last-byte  latency:  0.005 -   0.120    0.031  (  0.026)    0.021  (   small objs)  tx87bf30db5a70412b97a5c71ae60036c1

  CREATE
         Count:    64  (   0 error;    0 retries:  0.00%)  Average requests per second: 12.5
                              min       max      avg      std_dev  50%-ile                   Worst latency TX ID
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (all obj sizes)
         Last-byte  latency:  0.024 -   0.157    0.067  (  0.023)    0.060  (all obj sizes)  tx6f988120ec5044329f817-0051b21708
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (    tiny objs)
         Last-byte  latency:  0.024 -   0.157    0.064  (  0.022)    0.059  (    tiny objs)  tx6f988120ec5044329f817-0051b21708
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (   small objs)
         Last-byte  latency:  0.061 -   0.120    0.087  (  0.020)    0.089  (   small objs)  tx87bf30db5a70412b97a5c71ae60036c1

  READ
         Count:   459  (   0 error;    0 retries:  0.00%)  Average requests per second: 88.9
                              min       max      avg      std_dev  50%-ile                   Worst latency TX ID
         First-byte latency:  0.004 -   0.044    0.017  (  0.008)    0.016  (all obj sizes)  txe026893bbf09486c83fcdb629f6f25a3
         Last-byte  latency:  0.004 -   0.044    0.017  (  0.008)    0.016  (all obj sizes)  txe026893bbf09486c83fcdb629f6f25a3
         First-byte latency:  0.004 -   0.044    0.016  (  0.007)    0.016  (    tiny objs)  tx1d35c8e273bf4bbeb6298-0051b21705
         Last-byte  latency:  0.004 -   0.044    0.017  (  0.007)    0.016  (    tiny objs)  tx1d35c8e273bf4bbeb6298-0051b21705
         First-byte latency:  0.005 -   0.044    0.018  (  0.008)    0.016  (   small objs)  txe026893bbf09486c83fcdb629f6f25a3
         Last-byte  latency:  0.005 -   0.044    0.019  (  0.008)    0.017  (   small objs)  txe026893bbf09486c83fcdb629f6f25a3

  UPDATE
         Count:    90  (   0 error;    0 retries:  0.00%)  Average requests per second: 18.1
                              min       max      avg      std_dev  50%-ile                   Worst latency TX ID
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (all obj sizes)
         Last-byte  latency:  0.021 -   0.143    0.062  (  0.021)    0.061  (all obj sizes)  tx9a502107a0c246e69a987d120a2b9919
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (    tiny objs)
         Last-byte  latency:  0.021 -   0.143    0.062  (  0.022)    0.061  (    tiny objs)  tx9a502107a0c246e69a987d120a2b9919
         First-byte latency:  N/A   -   N/A      N/A    (  N/A  )    N/A    (   small objs)
         Last-byte  latency:  0.036 -   0.085    0.065  (  0.015)    0.065  (   small objs)  tx732aae54c9484689b8fea-0051b21709

  INFO:Scenario run results saved to /tmp/ssbench-results/Small_test_scenario.u4.o613.r-.2013-06-07.102314.stat.gz
  INFO:You may generate a report with:
    .../ssbench-master report-scenario -s /tmp/ssbench-results/Small_test_scenario.u4.o613.r-.2013-06-07.102314.stat.gz


Benchmark Reports
-----------------

The default, textual table report may be seen in the above example output.  You
can also specify ``--csv`` when running a scenario or generating a report later
to generate a CSV report instead.  This feature is still pretty new so expect
the CSV report output to change over time.

Right now, the default report's CSV version is two lines: a line of column
header names and one line of actual data.  Both lines are *very* long and the
set of columns present in any given CSV report will depend on the scenario
which was run.  Some column names have the ``--pctile`` value in them and many
columns have the object sizes in them, which are defined in the scenario file.
You can think of the two CVS lines as a linear denormalization of the contents
of the two-dimensional table output.

IPv6 support
------------
`ssbench` supports IPv6 for both the Swift communication, as well as between the
master and the workers. When using a hostname, `ssbench` will attempt to
guess whether to use IPv6 or not. If the host resolves to both IPv4 and IPv6,
`ssbench` picks IPv4. If this is not the desired behavior, please specify the IP
address explicitly. To bind to all interfaces, use the `::` address for IPv6;
for localhost, use `::1`.


How Does It Scale?
==================

Scalability and Throughput
--------------------------

Assuming the Swift cluster being benchmarked is not the bottleneck, the
scalability of ssbench may be increased by

- Running up to one ``ssbench-worker`` process per CPU core on any number of
  benchmarking servers.
- Increasing the default ``--batch-size`` parameter (defaults to 1) on both the
  ``ssbench-master`` and ``ssbench-worker`` command-lines.  Note that if you
  are running everything on one server and using the ``--workers`` argument to
  ``ssbench-master``, the ``--batch-size`` parameter passed to
  ``ssbench-master`` will be passed on to the automatically-started
  ``ssbench-worker`` processes.
- For optimal scalability, the user-count (concurrency) should be greater than
  and also an even multiple of both the batch-size and number of
  ``ssbench-worker`` processes.

As a simple example, on my quad-core MacBook Pro, I get around **9,800** requests
per second with ``--noop`` (see below) with this command-line (a
``--batch-size`` of 1)::

  $ ssbench-master run-scenario ... -u 24 -o 30000 --workers 3 --noop

But with a ``--batch-size`` of 8, I can get around **19,500** requests per second::

  $ ssbench-master run-scenario ... -u 24 -o 30000 --workers 3 --noop --batch-size 8

HTTPS on OS X
-------------

When running ``ssbench-worker`` on a Mac, using HTTPS, I got a significant
speed-up when setting ``OPENSSL_X509_TEA_DISABLE=1`` in the environment of my
``ssbench-worker`` processes.  I found this tip via a `curl blog post`_ after
noticing a process named ``trustevaluationagent`` chewing up a lot of CPU
during a benchmark run against a cluster using HTTPS.

.. _`curl blog post`: http://daniel.haxx.se/blog/2011/11/05/apples-modified-ca-cert-handling-and-curl/

The No-op Mode
--------------

To test the maximum throughput of the ``ssbench-master`` <==>
``ssbench-worker`` infrastructure, you can add ``--noop`` to a
``ssbench-master run-scenario`` command and the scenario will be "run" but
the ``ssbench-worker`` processes will not actually talk to the Swift cluster.

In this manner, you may determine your maximum requests per second if talking
to the Swift cluster were free.

The reported "Average requests per second:" value in the "TOTAL" section of
the report should be higher than you expect to get out of the Swift cluster
itself.

With an older version of ``ssbench`` which used a beanstalkd server to manage
master/worker communication, my 2012 15" Retina Macbook Pro could get **~2,700
requests per second** with ``--noop`` using a local beanstalkd, one
``ssbench-worker``, and a user count (concurrency) of 4.

With ZeroMQ sockets (no beanstalkd involved), the same laptop can get between
**7,000 and 8,000 requests per second** with ``--noop``.


Contributing To ssbench
=======================

First, please use the Github Issues for the project when submitting bug reports
or feature requests.

Code submissions should be submitted as pull requests and all code should be
PEP8 (v. 1.4.2) compliant.  Current unit test line coverage is not 100%, but
code contributions should not *lower* the code coverage (so please include
new tests or update existing ones as part of your change).  Running tests will
probably require Python 2.7 and a few additional modules like ``flexmock`` and
``nose``.

Regarding test tools, I started out using ``flexmock``, but plan to mostly add
new tests using the ``mock`` library since that's been included in the stdlib
and the Python community seems to be converging on it.  So please use ``mock``
instead of ``flexmock`` for new tests.

If contributing code which implements a feature or fixes
a bug, please ensure a Github Issue exists prior to submitting the pull request
and reference the Issue number in your commit message.

When submitting your first pull request, please also update AUTHORS to include
yourself, maintaining alphabetical ordering by last name.

If any of the file(s) you change do not yet have a copyright line with your
name, please add one at the bottom of the others, above the license text (but
never remove any existing copyright lines).  Your copyright line should look
something like::

  # Copyright (c) 2013 FirstName LastName
