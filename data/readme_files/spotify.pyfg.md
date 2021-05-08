PyFG
====

PyFG is a Python (2.7 tested, may work on other versions) package.

API for FortiOS or how to turn FortiOS into JunOS

Introduction
============

This API allows you to interact with a device runnine FortiOS in a sane way. With this API you can:

* Connect to the device, retrieve the running config (the entire config or some blocks, whatever you want) and build a model
* Build the same model from a file
* Do changes in the candidate configuration locally
* Create a candidate configuration from a file
* Do a diff between the running config and the local candidate config
* Generate the necessary commands to go from the running configuration to the candidate configuration

Documentation
=============

You can find the documentation on [Read the Docs](https://pyfg.readthedocs.io/en/latest/index.html).

Installation
============

To install the library execute:

```
pip install pyfg
```

Examples
========

In the examples directory you will find different file with examples on how to use the API:

* example1 - How to retrieve the configuration of a VDOM
* example2 - How to get BGP information and navigate through it
* example3 - How to load BGP configuration from a file (running.conf is emulating this step), load the candidate configuration from a file and then check the differences and show to get to the candidate configuration from the running one.
* example4 - Similar as example3 but this time the changes are done programmatically instead of using a text file.
* example5 - This example will do some changes, will try to commit them, will detect that something went wrong and it will finally rollback the changes.
