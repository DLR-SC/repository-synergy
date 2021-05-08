Welcome to Clyther's documentation!
===================================

CLyther is a Python tool similar to Cython and PyPy. CLyther is a just-in-time specialization engine for OpenCL. 
The main entry points for CLyther are its :class:`clyther.task` and :class:`clyther.kernel` decorators.
Once a function is decorated with one of these the function will be compiled to OpenCL when called. 

CLyther is a Python language extension that makes writing OpenCL code as easy as Python itself. 
CLyther currently only supports a subset of the Python language definition but adds many new features to OpenCL. 

CLyther exposes both the OpenCL C library as well as the OpenCL language to python.

Objectives:
    * Make it easy for developers to take advantage of OpenCL
    * Take advantage existing Python numerical algorithms
    * Accelerate my code!


Philosophy:
    * Enable users to have 100% control via Python. Access one to one mapping from Python to OpenCL.
    * Endorse native Python abstractions for convenience. e.g. Slice an array, pass a function as an argument.

.. warning::
    
    This is a brand new version of CLyther. I have not released this yet. 
    
    * If you do decide to use it then please think about :ref:`contribute`.
    * The best place to add your input to the `Issue Tracker <https://github.com/srossross/Clyther/issues/>`_.
    
Links:
+++++++++++

* `Homepage <http://srossross.github.com/Clyther/>`_
* `Issue Tracker <https://github.com/srossross/Clyther/issues/>`_

* `Development documentation <http://srossross.github.com/Clyther/develop/>`_
* `PyPi <http://pypi.python.org/pypi/Clyther/>`_
* `Github <https://github.com/srossross/Clyther/>`_
* `OpenCL 1.1 spec <http://www.khronos.org/registry/cl/specs/opencl-1.1.pdf>`_

.. seealso::
    
    * `OpenCL for Python <http://srossross.github.com/oclpb>`_: Python bindings for OpenCL.
    * `Meta <http://srossross.github.com/meta>`_: Metaprogramming utilities for Python.


