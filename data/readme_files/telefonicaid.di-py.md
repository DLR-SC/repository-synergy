# di-py

Dependency injection library for python.

[![Version](https://pypip.in/v/di-py/badge.png)](https://crate.io/packages/di-py)
[![Downloads](https://pypip.in/d/di-py/badge.png)](https://crate.io/packages/di-py)
[![Build Status](https://travis-ci.org/telefonicaid/di-py.svg?branch=master)](https://travis-ci.org/telefonicaid/di-py)

# Background

Dependency injection *enables us to write better code*, regardless of doing so
manually or with the help of some library. It helps specially to keep our code
inside the [Law of Demeter](http://en.wikipedia.org/wiki/Law_of_Demeter),
by programming against a known interface without having to worry about
how a concrete implementation is composed.

Python is a highly dynamic language with an "open class" implementation for user
types, thus the need for a full blown dependency injection framework is not
specially needed. For medium to large applications though there is still the
issue of how to actually implement dependency injection in the code using only
Python's standard syntax/library.

This library is designed to be very lightweight and flexible as to allow its use
in a variety of scenarios, including their use to aid with unit testing.
It doesn't form a *framework* but just a set of utilities to keep the dependency
injection needs in a project under control by applying it only where it makes
sense, with minimum overhead and a lean learning curve.

# Scenarios

## Basic example

```py
from http.client import HTTPSConnection
from di import injector

# Create the decorator setting up the dependencies (at configuration time)
inject = injector({
  HTTPSConnection: HTTPSConnection('localhost', '8080')
})

# Apply the decorator to our app logic to inject what we have configured (at runtime)
@inject
def fetch_it(id, http=HTTPSConnection):
  http.request("GET","/?id={0}".format(id))
  return http.getresponse()

# Call the logic without worrying about dependencies :)
print fetch_it(100).status

# Override the dependency if we have some specific use case
print fetch_it(100, http=HTTPSConnect('google.com', '80')).status
```

## Advanced usage with DependencyMap

```py
import hashlib
from di import injector, Key, DependencyMap

# Setup the dependency map
dm = DependencyMap()

# Define a custom Key to map a dependency when it's not a class
HashDep = Key('hash')

# Build a dependency programatically but only the first time it's used
@dm.singleton(HashDep)
def hash(deps):
  return lambda x: hashlib.md5(x).hexdigest()

# Create the decorator and bind it to the dependency map
inject = injector(dm)

# Define our logic defining what should be injected by default
@inject
def hasher(subject, hash=HashDep)
  return hash(subject)

print hasher('foobarbaz')
```

## Explore the unit tests

* [DI at method level](tests/di_tests.py#L32-L104)
* [DI using descriptor protocol](di/main.py#L217-L221)
* [DI using a metaclass](tests/di_tests.py#L107-L143)

# Python interpreters supported

Those are the python interpreters being validated via [travis.ci](https://github.com/juandebravo/di-py/blob/master/.travis.yml#L3) upon every change in the repository.

- python 2.6
- python 2.7
- python 3.3
- python 3.4
- pypy

# Install


### Get the latest stable version

```bash
pip install di-py
```

### Get the edge version directly from github

```bash
pip install git+ssh://git@github.com/telefonicaid/di-py.git@master
```

### Using RPM

Generate RPM from source code

```bash
git clone git@github.com/telefonicaid/di-py.git
cd di-py
python setup.py bdist_rpm
```

# License

See [LICENSE](LICENSE)

# Contributing

Use the GitHub's pull request and issue tracker to provide patches or
report problems with the library. All new functionality must be covered
by unit tests before it can be included in the repository.

The master branch always has the cutting edge version of the code, if
you are using it in your project it would be wise to create a fork of the
repository or target a specific tag/commit for your dependencies.


# Credits

- [Iván -DrSlump- Montes](https://github.com/drslump)
- [Juan de Bravo](https://github.com/juandebravo)
- [Sergi Sorribas](https://github.com/lerovitch)
- [Tomas Montserrat](https://github.com/tomas-mm)
- [Jordi Sesmero](https://github.com/jsmolina)
- [Pau Freixes](https://github.com/pfreixes)
