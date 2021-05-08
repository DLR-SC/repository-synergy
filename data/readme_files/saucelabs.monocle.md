# monocle
## An async programming framework with a blocking look-alike syntax.

[![pypi](https://img.shields.io/pypi/v/monocle.svg)](https://pypi.python.org/pypi/monocle/)
[![Build Status](https://travis-ci.org/saucelabs/monocle.png?branch=master)](https://travis-ci.org/saucelabs/monocle)

monocle straightens out event-driven code using Python's generators.
It aims to be portable between event-driven I/O frameworks, and
currently supports Twisted and Tornado.

It's for Python 2.7 only; the syntax it uses isn't supported in older
versions of Python. Monocle has not yet been updated for Python 3.

## A Simple Example

Here's a simple monocle program that runs two concurrent lightweight
processes (called "o-routines") using Tornado's event loop.  One is an
HTTP server, and the other makes an HTTP request:
```python
    import monocle
    monocle.init("tornado")

    from monocle import Return
    from monocle.stack import eventloop
    from monocle.stack.network import add_service
    from monocle.stack.network.http import HttpClient, HttpHeaders, HttpServer

    @monocle.o
    def hello_http(req):
        content = "Hello, World!"
        headers = HttpHeaders()
        headers['Content-Length'] = len(content)
        headers['Content-Type'] = 'text/plain'
        yield Return(200, headers, content)

    @monocle.o
    def request():
        resp = yield HttpClient.query('http://127.0.0.1:8088/')
        print resp.code, resp.body

    add_service(HttpServer(8088, hello_http))
    monocle.launch(request)
    eventloop.run()
```
## @_o

It's important that code be dapper and well-dressed, so if you prefer,
you can don the monocle and use this handy shortcut for `@monocle.o`:
```python
    from monocle import _o

    @_o
    def request():
        client = HttpClient()
        resp = yield client.request('http://127.0.0.1:8088/')
        print resp.code, resp.body
```
It's true, this violates Python's convention that underscores indicate
variables for internal use.  But rules are for breaking.  Live a
little.

## The Big Idea

Event-driven code can be efficient and easy to reason about, but it
often splits up procedures in an unpleasant way.  Here's an example of
a blocking function to read a request from a user, query a database,
and return a result:
```python
    def do_cmd(conn):
        cmd = conn.read_until("\n")
        if cmd.type == "get-address":
            user = db.query(cmd.username)
            conn.write(user.address)
        else:
            conn.write("unknown command")
```
Here's the same thing in event-driven style, using callbacks:
```python
    def get_cmd(conn):
        conn.read_until("\n", callback=handle_cmd)

    def handle_cmd(conn, cmd):
        if cmd.type == "get-address":
            # keep track of the conn so we can write the response back!
            def callback(result):
                handle_user_query_result(conn, result)
            db.query(cmd.username, callback)
        else:
            conn.write("unknown command")

    def handle_user_query_result(conn, user):
        conn.write(user.address)
```
What started out as a single function in the blocking code has
expanded here into four functions (counting the `callback` closure
that captures `conn` in `handle_cmd`).  In real event-driven code,
this kind of thing happens a *lot*.  Any time we want to do I/O, we
have to register a new handler and return back out to the event loop
to let other things happen while we wait for the I/O to finish.  It
would be nice if we had some way to tell the event loop to call back
into the *middle* of our function, so we could just continue where we
left off.

Fortunately, Python has a mechanism that lets us do exactly that,
called generators.  Monocle uses generators to straighten out
event-driven code.

Here's the monocle equivalent of the event-based code above:
```python
    @_o
    def do_cmd(conn):
        cmd = yield conn.read_until("\n")
        if cmd.type == "get-address":
            user = yield db.query(cmd.username)
            yield conn.write(user.address)
        else:
            yield conn.write("unknown command")
```
It's event-driven for efficient concurrency, but otherwise looks a lot
like the original blocking code.  Each time you see the word `yield`
in the code above, the o-routine is returning back up to the event
loop and waiting to be called back when the I/O it requested
completes.

This approach is a kind of cooperative concurrency that makes for
simpler code than callback-based event-driven code, but which we think
is easier to reason about than multi-threaded code.

## A word about the word `yield`

In ordinary Python generators, the norm is to think of `yield` as in
*crops*: the generator yields a value.  In monocle o-routines, it's
helpful to think of `yield` as in *traffic*.  `yield conn.read(10)` in
an o-routine means "yield to other o-routines until we finish reading
10 bytes".

## Developer information

To run individual tests on your computer install py.test and the packages for
the backend you’d like to test. Here’s how to do it in a separate virtualenv
with Twisted:

    $ cd monocle/
    $ virtualenv --clear --no-site-package .venv
    $ .venv/bin/pip install pytest twisted
    ...

You run the tests like this:

    $ .venv/bin/python o_test.py twisted tests/

Alternatively you can use tox to run all the tests for the different backends:

    $ .venv/bin/pip install tox
    ...
    $ tox

Check tox.ini to see how the tests are run.


## Who?

Monocle was created by Greg Hazel and Steven Hazel.

## Related Work
monocle is similar to, and takes inspiration from:

 * Twisted's inlineCallbacks
 * BitTorrent's yielddefer (used in the 5.x mainline client)
 * diesel
 * Go's goroutines (and CSP generally)
 * Haskell's I/O monad
 * eventlet
