urltools [![version](https://pypip.in/v/urltools/badge.png?style=flat)](https://pypi.python.org/pypi/urltools) [![Supported Python versions](https://pypip.in/py_versions/urltools/badge.svg?style=flat)](https://pypi.python.org/pypi/urltools/) [![format](https://pypip.in/format/urltools/badge.png?style=flat)](https://pypi.python.org/pypi/urltools) [![downloads](https://pypip.in/d/urltools/badge.png?style=flat)](https://pypi.python.org/pypi/urltools) [![license](https://pypip.in/license/urltools/badge.png?style=flat)](https://pypi.python.org/pypi/urltools)
========

Some functions to parse and normalize URLs.

The main focus of this library is to make it possible to work on all segments of
an URL. Thus a core feature (which is not provided by stdlib) is to split a domain
name correctly by using the Public Suffix List (see below).


## Functions

### Normalize

    >>> urltools.normalize("Http://exAMPLE.com./foo")
    http://example.com/foo

Rules that are applied to normalize a URL:

* tolower scheme
* tolower host (also works with IDNs)
* remove default port
* remove ':' without port
* remove DNS root label
* unquote path, query, fragment
* collapse path (remove '//', '/./', '/../')
* sort query params and remove params without value

`normalize` uses the functions for splitting and normalization which are
descriped below. The hostname is not tolowered by `normalize_host`. It is already
done in the `split_host` step before to make splitting of malformed netlocs
easier.


### Parse

The result of `parse` and `extract` is a `URL` named tuple that contains
`scheme`, `username`, `password`, `subdomain`, `domain`, `tld`, `port`, `path`,
`query`, `fragment` and the original `url` itself.

    >>> urltools.parse("http://example.co.uk/foo/bar?x=1#abc")
    URL(scheme='http', username='', password='', subdomain='', domain='example',
    tld='co.uk', port='', path='/foo/bar', query='x=1', fragment='abc',
    url='http://example.co.uk/foo/bar?x=1#abc')

If the `scheme` is missing `parse` interprets the URL as relative.

    >>> urltools.parse("www.example.co.uk/abc")
    URL(scheme='', username='', password='', subdomain='', domain='', tld='',
    port='', path='www.example.co.uk/abc', query='', fragment='',
    url='www.example.co.uk/abc')


### Extract

`extract` does not care about relative URLs and always tries to extract as much
information as possible.

    >>> urltools.extract("www.example.co.uk/abc")
    URL(scheme='', username='', password='', subdomain='www', domain='example',
    tld='co.uk', port='', path='/abc', query='', fragment='',
    url='www.example.co.uk/abc')


### Additional functions

Besides the already described main functions `urltools` has some more functions
to manipulate segments of a URL or create new URLs.

* `construct` a new URL from parts

        >>> construct(URL('http', '', '', '', 'example', 'com', '/abc', 'x=1',
        ... 'foo', None))
        'http://example.com/abc?x=1#foo'

* `compare` two urls to check if they are the same

        >>> compare("http://examPLe.com:80/abc?x=&b=1",
        ... "http://eXAmple.com/abc?b=1")
        True

* `encode` (IDNA, see RFC 3490)

        >>> urltools.encode("http://müller.de")
        'http://xn--mller-kva.de/'

* `normalize_host` decodes IDNA encoded segments of a DNS name

        >>> normalize_host('xn--mller-kva.de')
        u'müller.de'
        >>> normalize_host('xn--e1afmkfd.xn--p1ai')
        u'пример.рф'

* `normalize_path`

        >>> normalize_path("/a/b/../../c")
        '/c'

* `normalize_query`

        >>> normalize_query("x=1&y=&z=3")
        'x=1&z=3'

* `normalize_fragment` unquotes fragments except for the characters `+#` and
  space
* `unquote` a string. Optional it's possible to specify a list of characters
  which are not unquoted

        >>> unquote('foo%23bar')
        'foo#bar'
        >>> unquote('foo%23bar', ['#'])
        'foo%23bar'

* `split` is basically the same as `urlparse.urlparse` in Python2.7 or
  `urllib.parse.urlparse` in Python3.4. In Python2.7 it handles some malformed
  URLs better than `urlparse`. Differences to `urlparse` in Python3.4 were not
  analyzed.

        >>> split("http://www.example.com/abc?x=1&y=2#foo")
        SplitResult(scheme='http', netloc='www.example.com', path='/abc',
        query='x=1&y=2', fragment='foo')

* `split_netloc` splits a network location (netloc) to username, password, host
  and port

        >>> split_netloc("foo:bar@www.example.com:8080")
        ('foo', 'bar', 'www.example.com', '8080')

* `split_host` uses the Public Suffix List to split a domain name correctly

        >>> split_host("www.example.ac.at")
        ('www', 'example', 'ac.at')



## Public Suffix List

`urltools` uses the Public Suffix List (PSL) to split domain names correctly.
E.g. the TLD of `example.co.uk` would be `.co.uk` and not `.uk`. It is not
possible to decide "how big" the TLD is without a lookup in this list.

A local copy of the PSL is recommended. Otherwise it is downloaded with each
import of `urltools`. The path of the local copy has to be defined in the env
variable `PUBLIC_SUFFIX_LIST`:

    export PUBLIC_SUFFIX_LIST=/path/to/effective_tld_names.dat

For more information about how PSL works see http://publicsuffix.org/



## Installation

You can install `urltools` from the Python Package Index (PyPI):

    pip install urltools

... or get the latest version directly from GitHub:

    pip install -e git://github.com/rbaier/python-urltools.git#egg=urltools


The second option is not recommended because some features might be in an
experimental state.

There is (or should be) a git tag for each version that was released on PyPI.



## Testing

tox and pytest are used for testing. Simply install tox and run it:

    pip install tox
    tox
