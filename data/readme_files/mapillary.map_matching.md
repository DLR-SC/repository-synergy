# map_matching

`map_matching` is a Python library that associates a sequence of
locations (e.g. GPS trajectory) to the underlying road network. The
matching considers both road network topology and spatial
relations. The library provides a simple interface for use, and above
that it is also intended to work nicely with PostGIS and OSM road
network to build real-world applications.


## Features

- Provide both offline and online matching
- Support PostGIS with OSM road network loaded
- Designed to be fast, even in Python


## Getting Started

See [Getting Started](https://github.com/mapillary/map_matching) for
more information.


## Tests

We use [nose](https://nose.readthedocs.org/en/latest/) to run unit
tests.

Currently we put code and tests together for the sake of
convenience. To test a single module, for example, `shortest_path.py`,
simply:

```bash
$ nosetest map_matching/shortest_path.py
```

To run all unit tests:

```bash
$ nosetest map_matching/*.py
```


## License

`map_matching` is under BSD license. See `LICENSE` file for full
license text.
