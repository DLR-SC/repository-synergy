python-bittrex
=

python-bittrex is a Python library for the Bittrex API v1.1.

Use this to sell mined coins, write a trading bot or do whatever your heart desires.


Getting started
=

Get your API keys from https://bittrex.com/Account/ManageApiKey, download bittrex.py and place it in the same directory as your script.

    #!/usr/bin/env python
    from bittrex import bittrex
    
    api = bittrex('key', 'secret')
    
    print api.getticker('BTC-DOGE')


example.py
=

The example program buys 100 DOGE for the current price and sells them for a higher price. It also shows some other functions.  

Check out https://bittrex.com/Home/Api or read the source code for a full list of functions.
