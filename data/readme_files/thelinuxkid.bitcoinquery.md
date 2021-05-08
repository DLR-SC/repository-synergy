============
bitcoinquery
============

bitcoinquery stores the Bitcoin blockchain in a MongoDB database to
allow querying of block and transaction data

Usage
=====

In order to use bitcoinquery you need a Bitcoind RPC server. The
server must maintain a full index in order to retrieve all
transactions. To do this, run the server with the -txindex option or
set txindex=1 in the server's conf file. If you are already running a
server without a full index you must reindex the server with the
-reindex option.

Once the Bitcoind server is setup properly you can start collecting
data using the service described in the Collection_ section. You can
start making queries right away but it will take a while to store the
whole blockchain.

Installation
============

System dependencies
-------------------

    - Python 2.7
    - MongoDB 2.4.0
    - Bitcoind 0.8.1.0

Python external dependencies
----------------------------

    - python-setuptools
    - python-virtualenv

Setup
-----

To install bitcoinquery run the following commands from the project's
base directory. You can download the source code from github_::

    virtualenv .virtual
    .virtual/bin/python setup.py install
    # At this point, bitcoinquery will already be in easy-install.pth.
    # So, pip will not attempt to download it
    .virtual/bin/pip install bitcoinquery[test]

    # The test requirement installs all the dependencies. But,
    # depending on the service you wish to run you might want to
    # install only the appropriate dependencies as listed in
    # setup.py. For example to run blockchain-collect you only need
    # the mongo and bitcoin requirements which install the pymongo and
    # python-bitcoinrpc dependencies
    .virtual/bin/pip install bitcoinquery[mongo,bitcoin]

Services
========

It is recommended that you use an init daemon such as upstart_ or
runit_ to run the bitcoinquery services.

Collection
----------

To start the service which collects and stores block and transaction
data call the ``blockchain-collect`` cli with the ``CONFIG``
argument::

    .virtual/bin/blockchain-collect collect.conf

where ``collect.conf`` looks like::

    [bitcoind]
    url = http://<username>:<password>@<host>:<port>

    [mongodb]
    host = <host>:<port>
    database = bitcoinquery
    collections = blocks,transactions,errors

You can also specify a MongoDB replica set with the replica-set
option.

Querying
========

Block data is stored in the ``blocks`` MongoDB collection with the
block height as the document _id. Transaction data is stored in
``transactions`` with the transaction hash as the document _id. Errors
encountered during transaction retrieval are stored in the ``errors``
collection.

Example
-------

Find the number of public keys::

    import pymongo

    db = pymongo.Connection().bitcoinquery
    def fn():
        for t in db.transactions.find():
            for v in t['vout']:
                if v['scriptPubKey']['type'] == 'pubkey':
                    for a in v['scriptPubKey']['addresses']:
                        yield a

    keys = set([i for i in fn()])
    print 'There are {count} public keys'.format(count=len(keys))

Developing
==========

To start developing follow the instructions in the Installation_
section but replace::

    .virtual/bin/python setup.py install

with::

    .virtual/bin/python setup.py develop

If you like to use IPython you can install it with the dev
requirement::

    .virtual/bin/pip install bitcoinquery[dev]

.. _runit: http://smarden.org/runit/
.. _upstart: http://upstart.ubuntu.com/
.. _github: https://github.com/thelinuxkid/bitcoinquery
