This project explores the implementation of concurrent, distributed data
structures and related building blocks on top of memcache.


MANIFEST

The following are implemented in the form of a Python client library (see
memcache_collections.py).  They are intended to work with any implementation of
the common memcache API (including python-memcached, App Engine, and pylibmc)
and with any server configuration (i.e. multiple backends).  See below for
specific limitations.


1) Lock-free double-ended queue

This is a fast, concurrent queue with constant-time access which can grow
to unlimited size.  Values can be nearly as large as the memcache entry limit.
An example use is as a communication channel between remote processes.  It's
only suitable where you can tolerate low durability or have tight control
over memcache server uptime and evictions.

Synopsis:

    >>> import memcache
    >>> from memcache_collections import deque
    >>> mc = memcache.Client(['127.0.0.1:11211'], cache_cas=True)
    >>> d = deque.create(mc, 'my_deque')
    >>> d.appendleft(5)
    >>> d.appendleft('hello')

  Then from some other process or machine:

    >>> d = deque.bind(mc, 'my_deque')
    >>> d.pop()
    5
    >>> d.pop()
    'hello'


2) Lock-free, multi-entry compare and set (MCAS)

Like memcache's native operation, this provides atomic compare-and-set-- except
it works atomically across any number of entries.  The catch is you have to
use a specific function (mcas_get) for read access of any location that may be
involved in an MCAS transaction.  MCAS is a building block for concurrent
structures which otherwise would be overwhelmingly complicated to implement
with single CAS.

Synopsis:

    >>> import memcache
    >>> from memcache_collections import mcas
    >>> mc = memcache.Client(['127.0.0.1:11211'], cache_cas=True)
    >>> # initialize a doubly-linked list with two elements
    >>> mc.set_multi({
    ...     'foo': {'next': 'bar'},
    ...     'bar': {'prev': 'foo'}})
    >>> # always use mcas_get to access entries potentially in MCAS operations
    >>> # (each call returns an object representing a memcache entry snapshot)
    >>> foo_entry, bar_entry = mcas_get(mc, 'foo'), mcas_get(mc, 'bar')
    >>> foo_entry.key, foo_entry.value
    ('foo', {'next': 'bar'})
    >>> # atomically insert new node in our doubly linked list via MCAS
    >>> mc.add('baz', {'prev': 'foo', 'next': 'bar'})
    >>> mcas(mc, [
    ...     (foo_entry, {'next': 'baz'}),
    ...     (bar_entry, {'prev': 'baz'})])

The pylibmc client is not supported by MCAS since the implementation has no
no way to access memcache CAS ID's.


GENERAL CAVEATS

The implementations presented make heavy use of memcache's CAS operation.
CAS over a network (as opposed to against local memory) is susceptible
to fairness issues.  When entries are under high contention, a client can
be at a disadvantage due to slowness of its machine or implementation or
network proximity relative to other clients.

The implementations make use of Python-specific serialization, precluding
interoperation with potential clients in other languages.  A more robust
implementation would employ some platform-independent, extensible data format
such as protocol buffers.

The common Python memcache API suffers from a mis-design regarding implicit
management of CAS ID's.  This causes memory management issues as client
implementations need to hold these ID's definitely, as well as thread safety
issues.  Ports of memcache-collections to other languages won't have this
issue since the corresponding memcache API's support explicit CAS ID
management.  As for Python, I'm attempting to work with owners of the Python
memcache clients to improve the API.


DISCLAIMERS

Although Google, Inc. holds the copyright, memcache-collections is not a
Google product.

The included mockcache.py is derived from work by Hong MinHee, with various
paches for set_multi (Tony Bajan) and CAS support.


CONTRIBUTIONS

Contributions such as porting the client library to other languages are welcome,
assuming they are of high quality.  You'll need to sign a contributor license
agreement with Google.

    http://developers.google.com/open-source/cla/individual
    http://developers.google.com/open-source/cla/corporate


John Belmonte <john@neggie.net>
