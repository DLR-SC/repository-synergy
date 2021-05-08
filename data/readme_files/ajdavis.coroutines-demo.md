How Do Python Coroutines Work?
==============================

Script for live-coding an implementation of Python async coroutines
analogous to asyncio.coroutine in the Python 3.4 standard library:

    https://pygotham.org/2015/talks/162/how-do-python-coroutines/

tornado.gen.coroutine is an earlier inspiration for the same idea.

The example program is a "web crawler" that fetches only two URLs.
Files are named in order.

10. The first version does a blocking fetch of the two URLs, one at a time.
20. Then it puts its sockets in non-blocking mode and uses an event loop and
    callbacks to connect asynchronously. Still fetches serially.
30. Add more callbacks to fetch asynchronously.
40. Add a "Future" to abstract callbacks.
50. Introduce "Task" and replace callbacks with generators. The combination
    of Task, Future, and generators is a coroutine implementation.

To run the examples, first start server.py in a separate terminal session.
(It requires Flask.) server.py is designed to be slow - each URL takes about
a second to download. This provides a good example of async's strength suit.

The material for this demo is adapted from a chapter I wrote with Guido van
Rossum for an upcoming book in the Architecture of Open Source Applications
series:

https://github.com/aosabook/500lines/blob/master/crawler/crawler.markdown

The chapter presents a far more sophisticated code example than is demo'ed
here, and covers the relevant ideas in much greater depth and detail.
