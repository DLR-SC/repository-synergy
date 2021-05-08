## Unofficial Python interface for Diaspora\* social network

[![Diaspy on PyPI](https://badge.fury.io/py/diaspy-api.png)](https://pypi.python.org/pypi/diaspy-api)

`diaspy` is a set of modules which form an Python interface to the API of
Diaspora\* social network. 

Test suite will cause problems when run with 2.x so testing should be done 
using python3 interpreter.

Object oriented design of `diaspy` makes it easily reusable by other 
developers who want to use only part of the interface and create derivative
works from it.

Developers who don't like the design of `diaspy` and want to create something better
can use only `diaspy.connection.Connection()` object as it is capable of
doing everything. Other modules are just layers that provide easier access to
parts of the Diaspora\* API.

----

### Dependencies

List of software `diaspy` requires to run.
Versions used by maintainer are the ones available in stock Arch x86\_64 repositories.

**`python`**

Version: 3.3.3
[Website](https://www.python.org/)


**`python-requests`**

Version: 2.1.0
[Website](http://docs.python-requests.org/en/latest/)

**`python-dateutil`**

Version: >= 2.2
[Website](https://github.com/dateutil/dateutil)

*Optional:* **`python-beautifulsoup4`**
[Website](https://www.crummy.com/software/BeautifulSoup/)


----

#### Quick intro

#### 1. Posting text to your stream

You only need two objects to do this: `Stream()` and `Connection()`. 

    >>> import diaspy
    >>> c = diaspy.connection.Connection(pod='https://pod.example.com',
    ...                                  username='foo',
    ...                                  password='bar')
    >>> c.login()
    >>> stream = diaspy.streams.Stream(c)
    >>> stream.post('Your first post')

----

#### 2. Reference implementation

There is no official reference implementation of D\* client using `diaspy`.
The `diaspy.client` module is no longer maintained and will be removed in the future.

However, there is a small script written that uses `diaspy` as its backend.
Look for `diacli` in marekjm's repositories on GitHub.

----

To get more information about how the code works read 
documentation (`./doc/` directory) and manual (`./manual/` directory).
