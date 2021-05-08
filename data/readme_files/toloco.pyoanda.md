# PYOANDA

[![Documentation Status](https://readthedocs.org/projects/pyoanda/badge/?version=latest)](https://readthedocs.org/projects/pyoanda/?badge=latest)
[![Build Status](https://travis-ci.org/toloco/pyoanda.svg?branch=master)](https://travis-ci.org/toloco/pyoanda)
[![Coverage Status](https://coveralls.io/repos/toloco/pyoanda/badge.svg)](https://coveralls.io/r/toloco/pyoanda)
[![PyPi version](https://img.shields.io/pypi/v/pyoanda.svg)](https://pypi.python.org/pypi/pyoanda)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyoanda.svg)](https://pypi.python.org/pypi/pyoanda)
[![Code Health](https://landscape.io/github/toloco/pyoanda/master/landscape.svg?style=flat)](https://landscape.io/github/toloco/pyoanda/master)

Oanda’s API python wrapper. Robust and Fast API wrapper for your Forex bot
Python library that wraps [Oanda](http://oanda.com) API. Built on top of requests, it’s easy to use and makes sense.

Pyoanda is released under the [MIT license](https://raw.githubusercontent.com/toloco/pyoanda/master/LICENSE). The source code is on [GitHub](https://github.com/toloco/pyoanda/) and [issues are also tracked on GitHub](https://github.com/toloco/pyoanda/issues). Works well with python  __2.7, 3, 3.1, 3.2, 3.3, 3.4 and pypy__.

### Install
#### Pypi
```bash
pip install pyoanda
```

#### Manual
```bash
git clone git@github.com:toloco/pyoanda.git
cd pyoanda
python setup.py install
```

##### Run the tests 
```bash
python setup.py test
```


### Code example

```python
    from pyoanda import Client, PRACTICE

    client = Client(
        environment=PRACTICE,
        account_id="Your Oanda account ID",
        access_token="Your Oanda access token"
    )

    client.get_instrument_history(
        instrument="EUR_GBP",
        candle_format="midpoint",
        granularity="S30"
    )
```

Note that if you are indenting to use the sandbox environment, you should first use the  API to create an account then use the account_id to run the example above.

```python
    from pyoanda import Client, SANDBOX

    client = Client(environment=SANDBOX)

    # Create an account
    user = client.create_account()

    # Retrieve the username and accountId values for future use
    print "username: %s\naccount_id: %d" % (user['username'], user['accountId'])
```

### Examples

Check out the [examples gallery](examples) (Working progress)

Please feel free to send or post new examples! everybody will love to see them.



See [Pypi](https://pypi.python.org/pypi/pyoanda) project page.

See [Docs](http://pyoanda.readthedocs.org/) project page.
