# [Zatt](https://github.com/simonacca/zatt)

Zatt is a distributed storage system built on the [Raft](https://raft.github.io/)
consensus algorithm.

By default, clients share a `dict` data structure, although every python object
is potentially replicable with the `pickle` state machine.

Zatt was developed as part of my thesis work at the University of Trento, Italy. See [Slides](https://acca.science/slides/thesis/) and [Thesis](https://acca.science/thesis.pdf).

![Zatt Logo](docs/logo.png?raw=true "Zatt Logo")

Please note that the **client** is compatible with both `python2` and `python3`,
while the **server** makes heavy use of the asynchronous programming library
`asyncio` and is therefore python3-only. This won't affect compatibility with
legacy code since the server is standalone.

## Structure of the project

The most relevant part of the code concerning Raft is in the [states](https://github.com/simonacca/zatt/blob/develop/zatt/server/states.py) and in the [log](https://github.com/simonacca/zatt/blob/develop/zatt/server/log.py) files.

TODO: extend

## Installing
Both the server and the client are shipped in the same
[package](https://pypi.python.org/pypi/raft/)
(Note: this link won't work until the project is public).

Zatt can be installed by several means:

### Pypi
`$ pip3 install zatt`. (Note: this won't work until the project is public).

### Pip and Git
`$ pip3 install git+ssh://github.com/simonacca/zatt.git@develop`

### Cloning
```
$ git clone git@github.com:simonacca/zatt.git
$ cd zatt
$ git checkout develop
$ python3 setup.py install
```

Regardless of the installation method, `$ zattd --help` should work at this point.

## Examples

This screencast shows a basic usage of the code. The code run can be found below.

[![asciicast](https://asciinema.org/a/7o8bpyfxh0r1uaxvpfi7u8tjl.png)](https://asciinema.org/a/7o8bpyfxh0r1uaxvpfi7u8tjl)


### Spinning up a cluster of servers

A server can be configured with command-line options or with a config file,
in this example, we are going to use both.

First, create an empty folder and enter it:
`$ mkdir zatt_cluster && cd zatt_cluster`.

Now create a config file `zatt.conf` with the following content:
```
{"cluster": {
    "0": ["127.0.0.1", 5254],
    "1": ["127.0.0.1", 5255],
    "2": ["127.0.0.1", 5256]
 }
}
```

You can now run the first node:

`$ zattd -c zatt.conf --id 0 -s zatt.0.persist --debug`

This tells zattd to run the node with `id:0`, taking the info about address and port from the config file.

Now you can spin up a second node: open another terminal, navigate to `zatt_cluster` and issue:

`$ zattd -c zatt.conf --id 2 -s zatt.2.persist --debug`

Repeat for a third node, this time with `id:2`

### Client

To interact with the cluster, we need a client. Open a python interpreter (`$ python`) and run the following commands:

```
In [1]: from zatt.client import DistributedDict
In [2]: d = DistributedDict('127.0.0.1', 5254)
In [3]: d['key1'] = 0
```

Let's retrieve `key1` from a second client:

Open the python interpreter on another terminal and run:

```
In [1]: from zatt.client import DistributedDict
In [2]: d = DistributedDict('127.0.0.1', 5254)
In [3]: d['key1']
Out[3]: 0
In [4]: d
Out[4]: {'key1': 0}
```

### Notes

Please note that in order to erase the log of a node, the corresponding `zatt.{id}.persist` folder has to be removed.

Also note that JSON, currently used for serialization, only supports keys of type `str` and values of type `int, float, str, bool, list, dict `.

## Tests
In order to run the tests:

* clone the repo if you haven't done so already: `git clone git@github.com:simonacca/zatt.git`
* navigate to the test folder: `cd zatt/tests`
* execute: `python3 run.py`

## Contributing

TODO

## License

TODO
