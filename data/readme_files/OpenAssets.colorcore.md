Colorcore
=========

Colorcore is an open source colored coin wallet compatible with the `Open Assets Protocol <https://github.com/OpenAssets/open-assets-protocol/blob/master/specification.mediawiki>`_. It supports two modes: a command line interface, and a JSON/RPC server. The command line interface is suitable for managing a local wallet without going through any third-party service. The JSON/RPC interface is suitable for server-side implementations of colored coins and programmatic colored coins wallet management.

Open Assets is a protocol for issuing and transferring custom digital tokens in a secure way on the Bitcoin blockchain (or any compatible blockchain).

Use `Coinprism <https://www.coinprism.com>`_ for a web-based and user-friendly colored coins wallet.

Requirements
============

The following items are required to run Colorcore in the default mode:

* `Python 3.4 <https://www.python.org/downloads/>`_
* The following Python packages: `openassets <https://github.com/openassets/openassets>`_, `python-bitcoinlib <https://github.com/petertodd/python-bitcoinlib>`_, `aiohttp <https://github.com/KeepSafe/aiohttp>`_
* An operational Bitcoin Core wallet with JSON/RPC enabled and full transaction index

Installation
============

Clone the source code from GitHub::

    $ git clone https://github.com/OpenAssets/colorcore.git
    
Update the requirements::

    $ cd colorcore
    $ pip install --upgrade -r requirements.txt

Configuration
=============

Make sure your have a Bitcoin Core server running, with the following arguments: ``-txindex=1 -server=1``. You may need to have a username and password configured in the configuration file for Bitcoin Core (``bitcoin.conf``).

All the configuration for Colorcore is done though the ``config.ini`` file::

    [general]
    # Defines what provider to use to retrieve information from the Blockchain
    blockchain-provider=bitcoind

    [bitcoind]
    # Replace username, password and port with the username, password and port for Bitcoin Core
    # The default port is 8332 in MainNet and 18332 in TestNet
    rpcurl=http://<username>:<password>@localhost:<port>

    [environment]
    dust-limit=600
    default-fees=10000

    [cache]
    # Path of the cache file (use :memory: to disable)
    path=cache.db

    [rpc]
    # The port on which to expose the Colorcore RPC interface
    port=8080

Usage
=====

The general syntax for executing Colorcore is the following::

    python colorcore.py <command> <arguments>
    
All the commands are documented. Use the following command to show the documentation::

    python colorcore.py --help

The currently supported commands are the following:

* **getbalance**: Returns the balance in both bitcoin and colored coin assets for all of the addresses available in your Bitcoin Core wallet.
* **listunspent**: Returns an array of unspent transaction outputs, augmented with the asset ID and quantity of each output.
* **sendbitcoin**: Creates a transaction for sending bitcoins from an address to another.
* **sendasset**: Creates a transaction for sending an asset from an address to another.
* **issueasset**: Creates a transaction for issuing an asset.
* **distribute**: Creates a batch of transactions used for creating a token and distributing it to participants of a crowd sale.

RPC server
----------

Use the following command to start the RPC server::

    python colorcore.py server

Colorcore will then start listening on the port specified in the configuration file.

To call the RPC server, issue a HTTP POST request to http://localhost:<port>/<operation>. The list of valid operations is the same as the list of commands available via command line.

The arguments must be passed to the server in the body of the request, using the ``application/x-www-form-urlencoded`` encoding. Argument names are the same as for the command line interface.

Issue an asset
--------------

Issuing an asset is done through a standard Bitcoin transaction. The following command can be used to issue one million units of an asset::

    python colorcore.py issueasset <address> 1000000

The ``<address>`` placeholder represents the issuing address. You must own the private key for this address in your Bitcoin Core wallet, and you must have at least 0.000006 BTC on that address in order to successfully issue the asset. If the operation is successful, this command will return the transaction hash of the issuing transaction. You can then use a `color-aware block explorer <https://www.coinprism.info>`_ to see the details of the transaction.

Get your balance
----------------

Getting the balance of the wallet stored on the Bitcoin Core instance can be done by using the following command::

    python colorcore.py getbalance

Send an asset
-------------

Use the ``sendasset`` operation to send an asset to another address::

    python colorcore.py sendasset <from> <asset> <quantity> <to>

Crowdsales
----------

Crowdsales can be operated from Colorcore using the ``distribute`` command. It is not vulnerable to double spends, and allows the issuer to change the price of their tokens over time.

Remarks
-------

Fees can be specified through the ``--fees`` argument, and the default amount for fees can be changed through the ``config.ini`` file.

Once you have colored coins on one address, make sure you use the ``sendbitcoin`` operation to send uncolored bitcoins from that address. If you use Bitcoin Core to send bitcoins, Bitcoin Core might spend your colored outputs as it is not aware of colored coins.

If RPC is enabled, it is highly recommended to use a firewall to prevent access to Colorcore from an unauthorized remote machine.

Blockchain Providers
====================

Colorcore supports several modes. The mode can be defined using the ``blockchain-provider`` setting under ``[general]``. The following values are supported:

* ``bitcoind``: Colorcore connects only to a Bitcoin Core instance. For this to work, you need an operational Bitcoin Core wallet with JSON/RPC enabled and full transaction index.
  The following setting must be configured: ``rpcurl`` under ``[bitcoind]``.
* ``chain.com``: This is the lightweight mode. Colorcore connects to the `chain.com <https://chain.com/>`_ API. You must have a valid API Key and API secret. Using this mode, you will only be able to perform read operations such as ``getbalance`` and ``listunspent``. Any operation requiring to sign a transaction will fail. Bitcoin Core is not required when using this mode.
  The following settings must be configured: ``base-url``, ``api-key-id`` and ``secret`` under ``[chain.com]``.
* ``chain.com+bitcoind``: Colorcore connects to the chain.com API for obtaining blockchain data, but signs transactions using Bitcoin Core. All operations are supported.
  The following settings must be configured: ``base-url``, ``api-key-id`` and ``secret`` under ``[chain.com]`` and ``rpcurl`` under ``[bitcoind]``.

License
=======

The MIT License (MIT)

Copyright (c) 2014 Flavien Charlon

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
