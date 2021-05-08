> (Note: if anybody is interested in **becoming the maintainer of this package**, let me know.  I really don't do much Python any more so I'm not at all current on it.  I would happily let somebody else take charge of this project.)

What is This?
=============

I've heard a lot about deferreds, futures and promises in working with
Python, Scala and Javascript and I worked with deferreds in Python in
conjunction with some work I did using Twisted.  But then, I came
across [this
talk](http://marakana.com/s/post/1453/redemption_from_callback_hell_michael_jackson_domenic_denicola_video)
(which is really great, you should watch it) about Promises and
specifically
[Promises/A+](http://promises-aplus.github.io/promises-spec/) and I
really wanted to have similar functionality in Python.

But...
------

I can already hear Python users saying "But what about [Deferred in
Twisted](https://twistedmatrix.com/documents/8.2.0/api/twisted.internet.defer.Deferred.html)?"
or "But what about [PEP
3148](http://www.python.org/dev/peps/pep-3148/)/[PEP
3156](http://www.python.org/dev/peps/pep-3156/)
/[concurrent.futures](http://docs.python.org/dev/library/concurrent.futures.html)?"

Yes, I'm aware of those (and even the fact that futures have been
backported to 2.x).  But those implementations aren't really the same
as Promises/A+.  Not only are the APIs different, they also make
certain assumptions about where the asyncronicity comes from which I
thought was too specific.  Also, because I'm doing stuff that involves
both Python and Javascript, I thought it would be useful to have
implementations of Promises on both sides that were conceptually the
same.  Finally, I liked the fact that Promises/A+ was a specification
with a test suite so you can really support claims of conformance.

Getting Started
===============

I'm not even going to begin to explain what I find so interesting
about promises.  As I said above, go watch [this
video](http://promises-aplus.github.io/promises-spec/) and it will do
a much better job than me of demonstrating the various use cases.

To use the `aplus` package, all you need to do is just type:

```
from aplus import Promise
```

From there, you can start creating promises (which will presumably be
fulfilled or rejected in some asyncronous way).  Note that this
library doesn't constrain you at all as to how such promises are
actually fulfilled or rejected.  They could happen in threads, in
responses to messages in a message queue, when an HTTP request gets a
response, etc.  The important part is that you can chain together
these promises to notify you when they are completed or to chain
together further computations.

Note, when a promise is rejected, it is necessary that the value
passed to the rejection **is a subclass of** `Exception`.

Extras
======

I've added just a few extras beyond the Promises/A+ spec.

Blocking
--------

The first is that I added `wait` and `get` methods.  This way, if you
want to block (although I'm not sure why you would, apart from
testing), you can.  These methods also includea `timeout` argument so
you can limit the amount of time you block.

Python Datatypes
----------------

I've also added to useful utility functions called `listPromise` and
`dictPromise`.  The `listPromise` function takes arguments that are
`Promise` objects and returns to you a `Promise` for a list of values.
In other words, it takes a list of promises for values and returns a
promise for a list of values.  Got that? :-)

Not surprisingly, the `dictPromise` method works in a similar way.  It
takes a dictionary of promises (as *values*, not keys) and returns a
promise for a dictionary of values.

One could try and apply a monadic approach to such cases, but I just
focused on these two collection types.  If you feel that a monadic
approach is required, I look forward to your pull request. :-)

Callbacks
---------

It is possible to add callbacks to promises for pure notification
purposes.  To do this, use the `addCallback(...)` or `addErrback(...)`
methods.  These methods expect a function that takes a single argument
(the fulfilled value in the case of callbacks and the reason for
rejection in the case of errbacks).

Testing
=======

Test Suite and Coverage
-----------------------

I attempted to create a test suite based on the Promises/A+ spec.  I
couldn't really reuse the existing Javascript test suite, so I pretty
much made my own from scratch.  It's possible that it is not a
completely accurate reflection of the specification semantics, but I
tried.

The good news is that the library passes the entire test suite (plus
some extra tests for extended functionality).  Furthermore, the test
suite provides 100% coverage of the package source code.

One more thing...
-----------------

The Promises/A+ specification includes a section numbered `3.2.4`.
This section is problematic when it comes to Python.  It basically
says that the `then` method should return a promise but that any
callbacks triggered by the relationships that are being defined when
calling the `then` method shouldn't fire until after the `then` method
returns.  This is possible in Javascript because there is a built-in
event-loop/deferral mechanism in the language.  This is not the case
for Python.  As such, I could not build a generic Python package that
could conform to that section.  The next best thing would be to use
something like `twisted` which provides something like that.  But I
didn't want to chain people down to one particular asyncronous
framework to utilize an otherwise general purpose capability.

Acknowledgments
===============

Special thanks to Adrian Kuendig for putting in considerable effort to
ensure that this library functions properly in the face of
concurrency.
