## Python EOS Api Client
This is an unofficial API wrapper by [@furion](https://steemit.com/@furion)

## Installation
```
pip install -U git+https://github.com/Netherdrake/py-eos-api
```

## Usage
```python
>>> from eosapi import Client
>>> c = Client(nodes=['http://localhost:8888'])

>>> c.get_info()

    {'head_block_id': '0000652e92c1f73e14503383ee18c28901dd301ff5be0b94c77d846d799d5050',
     'head_block_num': 25902,
     'head_block_producer': 'initi',
     'head_block_time': '2017-09-16T04:25:18',
     'last_irreversible_block_num': 25884,
     'participation_rate': '1.00000000000000000',
     'recent_slots': '1111111111111111111111111111111111111111111111111111111111111111'}

>>> c.get_account?

    Signature: c.get_account(name) -> dict
    Docstring: Fetch a blockchain account
    File:      ~/GitHub/EOS/py-eos-api/eosapi/api.py
    Type:      method

>>> c.get_account('inita')

    {'eos_balance': '1000000.0000 EOS',
     'last_unstaking_time': '1969-12-31T23:59:59',
     'name': 'inita',
     'permissions': [{'name': 'active',
       'parent': 'owner',
       'required_auth': {'accounts': [],
        'keys': [{'key': 'EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV',
          'weight': 1}],
        'threshold': 1}},
      {'name': 'owner',
       'parent': 'owner',
       'required_auth': {'accounts': [],
        'keys': [{'key': 'EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV',
          'weight': 1}],
        'threshold': 1}}],
     'staked_balance': '0.0000 EOS',
     'unstaking_balance': '0.0000 EOS'}
```

You can also use a lower level `HttpClient` directly:
```python
from eosapi import HttpClient

h = HttpClient(["http://localhost:8888"])

print(h.exec('chain', 'get_block', '{"block_num_or_id": 5}'))
print(h.exec('chain', 'get_block', {"block_num_or_id": 5}))
print(h.exec('chain', 'get_info'))
```

You can also stream raw blocks (polling indefinitely):
```python
from eosapi import Client
c = Client()

for block in c.stream_blocks(start_block=100, mode='head'):
    print(block)
```

### TODO
 - add support for type hints _(Union[NativeType, PythonType])_
 - split api into submodules to avoid potential collisions
 - apigen: load from json spec files once they are finalized

### License
MIT
