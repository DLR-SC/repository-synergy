=================
Benchy
=================
A lightweight benchmarking framework written in Python focused on performing memory consumption and runtime performance comparison for Python programs.

The goal of this framework is to help scientific developers to perform
benchmarkings of several algorithmical approaches written in Python.

It's has the `memory_profiler <http://pypi.python.org/pypi/psutil>`_ ,
`numpy <http://pypi.python.org/pypi/psutil>`_  and
`matplotlib <http://pypi.python.org/pypi/psutil>`_ as dependencies.


==============
 Installation
==============
To install through easy_install or pip::

    $ easy_install -U benchy # pip install -U benchy

To install from source, download the package, extract and type::

    $ python setup.py install


=======
 Usage
=======
To use the benchy framework, you must first define the functions you would
like to benchmark. In this example, we create three versions of a simple
function ``create_list`` that allocates the list ``a`` with 100000 elements::

    from benchy.api import Benchmark

    common_setup = ""
    statement = "lst = ['i' for x in range(100000)]"
    benchmark1 = Benchmark(statement, common_setup, name= "range")

    statement = "lst = ['i' for x in xrange(100000)]"
    benchmark2 = Benchmark(statement, common_setup, name= "xrange")

    statement = "lst = ['i'] * 100000"
    benchmark3 = Benchmark(statement, common_setup, name= "range")


With all benchmarks created, we could test a simple benchmark by
calling the method ``run``::

    print benchmark1.run()

The output will follow the structure below::

    {'memory': {'repeat': 3,
                'success': True,
                'units': 'MB',
                'usage': 2.97265625},
     'runtime': {'loops': 100,
                 'repeat': 3,
                 'success': True,
                 'timing': 7.5653696060180664,
                 'units': 'ms'}}


The dict associated to the key *memory* represents the memory performance
results. It gives you the number of calls *repeat* to the statement, the average
consumption *usage* in *units* . In addition, the key 'runtime' indicates
the runtime performance in timing results. It presents the number of calls
*repeat* following the average time to execute it *timing* in *units*.

Do you want see a more presentable output ? It is possible calling the method ``to_rst`` with the results as parameter::

    rst_text = benchmark1.to_rst(results)


The output

    **Benchmark setup**

    .. code-block:: python



    **Benchmark statement**

    .. code-block:: python

        lst = ['c' for x in range(100000)]

    +-----------------+--------+--------+-------+-------+
    |            name | repeat | timing | loops | units |
    +=================+========+========+=======+=======+
    | list with range |      3 |  6.739 |   100 |    ms |
    +-----------------+--------+--------+-------+-------+



Now let's check which one is faster and which one consumes less memory. Let's
create a ``BenchmarkSuite``. It is referred as a container for benchmarks.::

     from benchy.api import BenchmarkSuite
     suite = BenchmarkSuite()
     suite.append(benchmark1)
     suite.append(benchmark2)
     suite.append(benchmark3)

Finally, let's run all the benchmarks together with the ``BenchmarkRunner``.
This class can load all the benchmarks from the suite and run each individual
analysis and print out interesting reports::

    from benchy.api import BenchmarkRunner
    runner = BenchmarkRunner(benchmarks=suite, tmp_dir='.', name= 'List Allocation Benchmark')


Let's run the suite::

    n_benchs, results = runner.run()

Output will follow::

    {Benchmark('list with "*"'):
        {'runtime': {'timing': 0.47582697868347168, 'repeat': 3, 'success': True, 'loops': 1000, 'timeBaselines': 1.0, 'units': 'ms'},
        'memory': {'usage': 0.3828125, 'units': 'MB', 'repeat': 3, 'success': True}},

    Benchmark('list with xrange'):
        {'runtime': {'timing': 5.623779296875, 'repeat': 3, 'success': True, 'loops': 100, 'timeBaselines': 11.818958463504936, 'units': 'ms'},
        'memory': {'usage': 0.71484375, 'units': 'MB', 'repeat': 3, 'success': True}},

    Benchmark('list with range'): {
        'runtime': {'timing': 6.5933513641357422, 'repeat': 3, 'success': True, 'loops': 100, 'timeBaselines': 13.856615239384636, 'units': 'ms'},
        'memory': {'usage': 2.2109375, 'units': 'MB', 'repeat': 3, 'success': True}}}

Next, we will plot the relative timings. It is important to measure how faster the other benchmarks are compared to reference one. By calling the method ``plot_relative``::


    def plot_relative(self, results, ref_bench=None, fig=None,
                    horizontal=True, colors=list('bgrcmyk'), logy=False):
        """Relative plot.
            Parameters:
            -----------
            results: The benchmark results from BenchmarkRunner.
            ref_bench: The Benchmark object that will be the baseline, optional
            fig: matplotlib figure object, optional
            horizontal: The plot will be horizontal or vertical, optional
            colors:  the colormap for the plots, optional
            logy:  log scale, optional

            Returns:
            --------
            fig: matplotlib figure
        """
        ...

Going back to the list allocation, let's save the plot::

    fig = runner.plot_relative(results, horizontal=True)
    plt.savefig('%s_r.png' % runner.name, bbox_inches='tight')


.. image:: https://dl.dropbox.com/u/1977573/List%20Creation_r.png


As you can see the graph aboe the xrange method is 12x slower and the range approach is 13x.  Let's see the absolute timings. Just call the method ``plot_absolute`::

    def plot_absolute(self, results, fig=None, horizontal=True,
            colors=list('bgrcmyk'), logy=False):
        """Absolute Timing plot.
            Parameters:
            -----------
            results: The benchmark results from BenchmarkRunner.
            fig: matplotlib figure object, optional
            horizontal: The plot will be horizontal or vertical, optional
            colors:  the colormap for the plots, optional
            logy:  log scale, optional

            Returns:
            --------
            fig: matplotlib figure
        """
        ...

Showing the plot now::

    runner.plot_absolute(results, horizontal=False)
    plt.savefig('%s.png' % runner.name) # bbox_inches='tight')

.. image:: https://dl.dropbox.com/u/1977573/ListCreation.png

You may notice besides the bar representing the timings, the line plot
representing the memory consumption for each statement. There is a positive
correlation between the memory consumption and the runtime performance.

Finally, benchy also provides a full repport for all benchmarks by calling
the method ``to_rst``::

    rst_text = runner.to_rst(results, runner.name + 'png',
            runner.name + '_r.png')
    with open('teste.rst', 'w') as f:
            f.write(rst_text)

The expected output (the configuration I added manually):


Performance Benchmarks
======================

These historical benchmark graphs were produced with `benchy
<http://github.com/python-recsys/benchy>`__.

Produced on a machine with

  - Intel Core i5 950 processor
  - Mac Os 10.6
  - Python 2.6.5  64-bit
  - NumPy 1.6.1


list with "*"
-------------

**Benchmark setup**

.. code-block:: python



**Benchmark statement**

.. code-block:: python

    lst = ['c'] * 100000

+---------------+--------+--------+-------+-------+
|          name | repeat | timing | loops | units |
+===============+========+========+=======+=======+
| list with "*" |      3 | 0.4788 |  1000 |    ms |
+---------------+--------+--------+-------+-------+

list with xrange
----------------

**Benchmark setup**

.. code-block:: python



**Benchmark statement**

.. code-block:: python

    lst = ['c' for x in xrange(100000)]

+------------------+--------+--------+-------+-------+
|             name | repeat | timing | loops | units |
+==================+========+========+=======+=======+
| list with xrange |      3 |  5.772 |   100 |    ms |
+------------------+--------+--------+-------+-------+

list with range
---------------

**Benchmark setup**

.. code-block:: python



**Benchmark statement**

.. code-block:: python

    lst = ['c' for x in range(100000)]

+-----------------+--------+--------+-------+-------+
|            name | repeat | timing | loops | units |
+=================+========+========+=======+=======+
| list with range |      3 |  7.037 |   100 |    ms |
+-----------------+--------+--------+-------+-------+

Final Results
-------------
+------------------+--------+--------+-------+-------+---------------+
|             name | repeat | timing | loops | units | timeBaselines |
+==================+========+========+=======+=======+===============+
|    list with "*" |      3 | 0.4788 |  1000 |    ms |             1 |
+------------------+--------+--------+-------+-------+---------------+
| list with xrange |      3 |  5.772 |   100 |    ms |         12.05 |
+------------------+--------+--------+-------+-------+---------------+
|  list with range |      3 |  7.037 |   100 |    ms |          14.7 |
+------------------+--------+--------+-------+-------+---------------+

**Performance Relative graph**

.. image:: https://dl.dropbox.com/u/1977573/List%20Creation_r.png
   :width: 6in
**Performance Absolute graph**

.. image:: https://dl.dropbox.com/u/1977573/ListCreation.png
   :width: 6in



============================
 Frequently Asked Questions
============================
    * Q: How accurate are the results ?
    * A: This module gets the memory consumption by querying the
      operating system kernel about the amount of memory the current
      process has allocated, which might be slightly different from
      the amount of memory that is actually used by the Python
      interpreter. Also, because of how the garbage collector works in
      Python the result might be different between platforms and even
      between runs. The runtime performance is obtained by calling the
      python standard library `timeit <http://docs.python.org/2/library/timeit.html>`_
      module. So it also can lead to different results between platforms and
      even runs.

    * Q: Does it work under windows ?
    * A: I didn't test yet. It will be a issue in the Github's issue tracker.



===========================
 Support, bugs & wish list
===========================
Send issues, proposals, etc. to `github's issue tracker <https://github.com/python-recsys/benchy/issues>`_ .

If you've got questions regarding development, you can email me
directly at marcel@pingmind.com


=============
 Development
=============
Latest sources are available from github:

    https://github.com/python-recsys/benchy


=========
 Authors
=========
This module was written by `Marcel Caraciolo <http://aimotion.blogspot.com>`_

Inspired by Wes Mckinney `vbench <https://github.com/pydata/vbench>`_.




=========
 License
=========
Simplified BSD