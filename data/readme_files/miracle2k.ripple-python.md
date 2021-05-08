Python utilities to work with the Ripple payment network.

For now, this contains:

ripple.sign
    Offline signing for transactions. Supports fully-canonical signatures.
    [very new, but seems to work so far]

ripple.serialize
    Encode data structures transactions to binary.
    [not 100% complete, but most things you'll need for transactions]

ripple.client
    High-level client library. [very much a work in progress]

ripple.datastructures
    Helps extracting information from Ripple transaction data, like
    how balances changed during a payment. [very much a work in progress]


Installation
------------

Runs on Python 2.7 and Python 3.3. PyPy is also supported.

To install on 2.7, or PyPy:

    $ pip install ripple-python

To install on 3.3:

    $ pip install --process-dependency-links ripple-python
