=============
linux-metrics
=============

*System Metrics/Stats Library for Linux*

* 2010-2013 `Corey Goldberg <http://goldb.org>`_
* Dev Home: https://github.com/cgoldberg/linux-metrics
* PyPI: http://pypi.python.org/pypi/linux-metrics
* Free Open Source : `MIT License <http://www.opensource.org/licenses/MIT>`_

----

-----------
Description
-----------

`linux-metrics` is a Python package containing modules for getting OS metrics on systems running the Linux kernel.  It is a pure python library with no external dependencies.

Basic stats for major subsystems are provided (Processor/CPU, Disk, Memory, Network).

-----------------
Install from PyPI
-----------------

* `pip install linux-metrics`
 
------------
Requirements
------------

* Python 2.6/2.7/3.1/3.2/3.3/PyPy
* Linux 2.6+

-------------
Example Usage
-------------

print number of processes running::

    from linux_metrics import cpu_stat

    print cpu_stat.procs_running()

print CPU utilization every 5 secs::

    >>> from linux_metrics import cpu_stat
    >>> 
    >>> while True:
    ...     cpu_pcts = cpu_stat.cpu_percents(5)
    ...     print 'cpu utilization: %.2f%%' % (100 - cpu_pcts['idle'])
    ... 
    cpu utilization: 0.70%
    cpu utilization: 0.50%
    cpu utilization: 24.80%
    cpu utilization: 20.89%
    cpu utilization: 40.04%

---
API
---

::

  * linux_metrics
    * cpu_stat
      * cpu_times()
      * cpu_percents(sample_duration=1)
      * procs_running()
      * procs_blocked()
      * load_avg()
      * cpu_info()
    * disk_stat
      * disk_busy(device, sample_duration=1)
      * disk_reads_writes(device)
      * disk_usage(path)
      * disk_reads_writes_persec(device, sample_duration=1)
    * mem_stat
      * mem_stats()
    * net_stat
      * rx_tx_bytes(interface)
      * rx_tx_bits(interface)
      * rx_tx_dump(interface)

-------
Example
-------

`linux-metrics` package contains an example script:

* `example.py <https://github.com/cgoldberg/linux-metrics/blob/master/example.py>`_

----------
Unit Tests
----------

You can run the included unit tests and verify all cases pass in your environment:

::

    $ nosetests

Note:  you may need to adjust the configuration of the unit tests to match your environment.  They are set by default to use:

::

    DISK_DEVICE = 'sda1'
    
    NETWORK_INTERFACE = 'eth0'

