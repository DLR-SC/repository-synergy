Open Assets Reference Implementation
====================================

The ``openassets`` Python package is the reference implementation of the colored coins `Open Assets Protocol <https://github.com/OpenAssets/open-assets-protocol>`_.

Open Assets is a protocol for issuing and transferring custom digital tokens in a secure way on the Bitcoin blockchain (or any compatible blockchain).

Requirements
============

The following items are required for using the ``openassets`` package:

* Python 3.4
* The `python-bitcoinlib <https://github.com/petertodd/python-bitcoinlib>`_ package

Installation
============

Linux, OSX
----------

Using pip::

    $ pip install openassets

Or manually from source, assuming all required modules are installed on your system::

    $ python ./setup.py install

Windows
-------

1) Make sure you have `Python 3.4 and pip <http://www.anthonydebarros.com/2011/10/15/setting-up-python-in-windows-7/>`_ installed
2) Open the command prompt: Start Menu > Accessories > Command Prompt
3) Run the following command::

    pip install openassets

Overview
========

The ``openassets`` package contains two submodules: the ``protocol`` submodule and the ``transactions`` submodule.

``protocol`` submodule
----------------------

The ``protocol`` submodule implements the specification in order to interpret Bitcoin transactions as Open Assets transactions.

Usage
^^^^^

This example requires a Bitcoin Core instance running with RPC enabled and the ``-txindex=1`` parameter::

    import asyncio
    import bitcoin.rpc
    import openassets.protocol

    @asyncio.coroutine
    def main():
        bitcoin.SelectParams('testnet')

        # Create a RPC client for Bitcoin Core
        rpc_client = bitcoin.rpc.Proxy('http://user:pass@localhost:18332')
        # OutputCache implements the interface required for an output cache provider, but does not perform any caching
        cache = openassets.protocol.OutputCache()
        # The transaction provider is a function returning a transaction given its hash
        transaction_provider = asyncio.coroutine(rpc_client.getrawtransaction)
        # Instantiate the coloring engine
        coloring_engine = openassets.protocol.ColoringEngine(transaction_provider, cache, loop)

        transaction_hash = bitcoin.core.lx('864cbcb4b5e083a98aaeaf94443815025bdfb0d35a6fd00817034018b6752ff5')
        output_index = 1
        colored_output = yield from coloring_engine.get_output(transaction_hash, output_index)

        print(colored_output)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

``transactions`` submodule
--------------------------

The ``transactions`` submodule contains functions that can be used to build unsigned Open Assets transactions for various purposes.

Usage
^^^^^

This example requires a Bitcoin Core instance running with RPC enabled and the ``-txindex=1`` parameter::

    import asyncio
    import bitcoin.rpc
    import openassets.protocol
    import openassets.transactions

    @asyncio.coroutine
    def main():
        bitcoin.SelectParams('testnet')

        # Create a RPC client for Bitcoin Core
        rpc_client = bitcoin.rpc.Proxy('http://user:pass@localhost:18332')

        # Output script corresponding to address myLPe3P8SE2DyqRwABRwqezxdZxhkYxXYu (in testnet)
        output_script = bitcoin.core.x('76a914c372d85bc2c54384dbc2cb9ef365eb7f15d4a9b688ac')

        # Initialize the coloring engine
        transaction_provider = asyncio.coroutine(rpc_client.getrawtransaction)
        engine = openassets.protocol.ColoringEngine(transaction_provider, openassets.protocol.OutputCache(), loop)

        # Obtain the unspent output for the local wallet
        unspent_outputs = []
        for output in rpc_client.listunspent():
            if output['scriptPubKey'] == output_script:
                unspent_outputs.append(openassets.transactions.SpendableOutput(
                    bitcoin.core.COutPoint(output['outpoint'].hash, output['outpoint'].n),
                    (yield from engine.get_output(output['outpoint'].hash, output['outpoint'].n))
                ))

        # The minimum valid value for an output is set to 600 satoshis
        builder = openassets.transactions.TransactionBuilder(600)

        # Create the issuance parameters
        issuance_parameters = openassets.transactions.TransferParameters(
            unspent_outputs=unspent_outputs,    # Unspent outputs the coins are issued from
            to_script=output_script,            # The issued coins are sent back to the same address
            change_script=output_script,        # The bitcoin change is sent back to the same address
            amount=1500)                        # Issue 1,500 units of the asset

        # Create the issuance transaction
        # The metadata is left empty and the fees are set to 0.0001 BTC
        transaction = builder.issue(issuance_parameters, metadata=b'', fees=10000)

        print(transaction)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

License
=======

The MIT License (MIT)

Copyright (c) 2014 Flavien Charlon

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
