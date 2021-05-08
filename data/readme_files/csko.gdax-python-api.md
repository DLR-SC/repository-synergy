# GDAX Python API

[![Build Status](https://travis-ci.org/csko/gdax-python-api.svg?branch=master)](https://travis-ci.org/csko/gdax-python-api)
[![PyPI](https://img.shields.io/pypi/pyversions/gdax-python-api.svg)](https://pypi.python.org/pypi/gdax-python-api)
[![PyPI](https://img.shields.io/pypi/v/gdax-python-api.svg)](https://pypi.python.org/pypi/gdax-python-api)
[![codecov](https://codecov.io/gh/csko/gdax-python-api/branch/master/graph/badge.svg)](https://codecov.io/gh/csko/gdax-python-api)

Unofficial GDAX API client written in Python3 using async/await

## API
The implementation supports the following GDAX endpoints:
* Market Data REST API
* Private REST API
* Public and private Websocket feeds

See the official API documentation at https://docs.gdax.com/ for more documentation.

## Examples
### Market Data
```python
import asyncio
import gdax

async def main():
    trader = gdax.trader.Trader(product_id='BTC-USD')
    res = await asyncio.gather(
        trader.get_products(),
        trader.get_product_ticker(),
        trader.get_time(),
    )
    print(res)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

### Private Endpoint
```python
import asyncio
import gdax

async def main():
    trader = gdax.trader.Trader(
        product_id='BTC-USD',
        api_key='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        api_secret='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa==',
        passphrase='aaaaaaaaaaa')
    res = await trader.get_account()
    print(res)

    res = await trader.buy(type='limit', size='0.01', price='2500.12')
    print(res)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

### Order book
```python
import asyncio
import gdax

async def run_orderbook():
    async with gdax.orderbook.OrderBook(['ETH-USD', 'BTC-USD']) as orderbook:
        while True:
            message = await orderbook.handle_message()
            if message is None:
                continue
            print('ETH-USD ask: %s bid: %s' %
                  (orderbook.get_ask('ETH-USD'),
                   orderbook.get_bid('ETH-USD')))
            print('BTC-USD ask: %s bid: %s' %
                  (orderbook.get_ask('BTC-USD'),
                   orderbook.get_bid('BTC-USD')))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_orderbook())
```

## Installation
Install from PyPI:

    pip install gdax-python-api

You can [download the latest release from Github](https://github.com/csko/gdax-python-api/archive/master.zip) and install it manually:

    python setup.py install

## Requirements

* Python 3.6 (async/await, f-strings)
* aiohttp
* aiofiles
* async_timeout
* sortedcontainers


## Acknowledgements
Parts of this software are based on [GDAX-Python](https://github.com/danpaquin/GDAX-Python) by Daniel Paquin. See also https://github.com/danpaquin/GDAX-Python/blob/master/contributors.txt.
