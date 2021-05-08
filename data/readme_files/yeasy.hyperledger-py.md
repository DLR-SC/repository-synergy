# hyperledger-py

[![Build Status](https://travis-ci.org/yeasy/hyperledger-py.svg?branch=master)](https://travis-ci.org/yeasy/hyperledger-py)
[![PyPI Version](http://img.shields.io/pypi/v/hyperledger.svg)](https://pypi.python.org/pypi/hyperledger)

**The project has been accepted by Hyperledger Community as [fabric-sdk-py](https://gerrit.hyperledger.org/r/#/admin/projects/fabric-sdk-py).**

Python SDK for [Hyperledger fabric](https://github.com/hyperledger/fabric).

Currently, we support two branches: 
* [restful](https://github.com/yeasy/hyperledger-py/tree/restful)(Stable) : implementated based on restful APIs.
* [grpc](https://github.com/yeasy/hyperledger-py/tree/grpc)(Under development): implementated based on grpc.

This restful branch will follow the [Hyperledger API](https://github.com/hyperledger/fabric/tree/master/docs/API) to let users use those APIs by importing a simple python library. e.g.,

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.peer_list()
{u'peers': [{u'type': 1, u'ID': {u'name': u'vp1'}, u'address': u'172.17.0.2:7051'}, {u'type': 1, u'ID': {u'name': u'vp2'}, u'address': u'172.17.0.3:7051'}]}
```

If you want a quick start with a hyperledger cluster without any local 
configuration and vagrant setup, please use this 
[compose-file](https://github.com/yeasy/docker-compose-files#hyperledger).

## Installation
The stable version is always available on PyPi.

```sh
$ pip install hyperledger --upgrade
```

The latest version is on [github](https://github.com/yeasy/hyperledger-py).
```sh
$ git clone https://github.com/yeasy/hyperledger-py.git
$ cd hyperledger-py
$ pip install -r requirements.txt
$ python setup.py install
```

## Change Logs
See [change log](docs/change_log.md).

## Documentation
The source is available in the [docs](docs) directory.

* [API Usage](docs/api.md)

## Testing
All testing code is under [tests](tests) directory.

After installation, you can run a quick full-functional testing (deploy,
invoke, query chaincode, etc.) with your hyperledger cluster by

```python
$ python tests/function_test.py HYPERLEDGER_API_URL
```

## Contribution
Please see [Contribution Instruction](docs/contribution.md).

## Acknowledgement

This work is highly inspired by the following projects:

 * [Hyperledger](https://github.com/hyperledger/hyperledger)
 * [requests](https://pypi.python.org/pypi/requests)
 * [docker-py](https://github.com/docker/docker-py)

## License

This work is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full license text.
