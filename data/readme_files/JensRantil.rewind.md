**This project is fully functional, but only supports a single event
stream.  I've taken the lessons learnt with Rewind and applied the
knowledge to the next generation of Rewind, Gorewind. The project can be
found here: https://github.com/JensRantil/gorewind**

=======
Rewind
=======

.. image:: https://secure.travis-ci.org/JensRantil/rewind.png?branch=develop
   :target: http://travis-ci.org/#!/JensRantil/rewind

Have you ever been nervous of all those DBMSs schema changes when you
are deploying your applications? They are gonna take too long, or break
backward compatibility? Have you ever thought "Crap, I wish I had stored
that information since earlier"? Have you ever felt your writing
patterns and your reading patterns differ a lot, making things harder to
scale?

CQRS (Command-Query Response Segregation) is an architectural pattern
that aims to solve these issues by splitting up your architectural
system into two parts:

* A *write side* that takes care of validating input and optimizes for
  fast writes. The write side takes commands and outputs corresponding
  events if the command validates correctly.

* A *read side* that listens to incoming events from the write side. The
  read side is optimized for fast reads.

A core concept in CQRS is the *event store* which sits inbetween the
write and the read side. The event store takes care of three things:

* persisting all events to disk.
  
* being a hub/broker replicating all events from the write to the read
  side of things.
  
* it allows fast querying of events so that different parts of the system
  can be synced back on track and new components can be brought back in
  play.

*Rewind* is an event store application that talks ZeroMQ. It is written
in Python and supports multiple storage backends.

Installing
==========

PyPi
----
Rewind `exists on PyPi`_ and can be downloaded by issuing::

    $ pip install rewind

.. _exists on PyPi: http://pypi.python.org/pypi/rewind/

Manual install
--------------
Rewind uses basic ``setuptools``. Installation can be used done as
follows::

    $ git clone https://github.com/JensRantil/rewind.git
    $ cd rewind
    $ python setup.py install

However **NOTE**, that this will install Rewind globally in your Python
environment and is NOT recommended. Please refer to virtualenv_ on how to
create a virtual environment.

.. _virtualenv: http://www.virtualenv.org

Talking to `rewind`
===================
There is a preexisting Python client package, `rewind-client`_. If you
are not writing a new client you might want to skip the following
section below.

.. _rewind-client: https://github.com/JensRantil/rewind-client

Rewind has two different wire protocols. Each is using ZeroMQ as low
level transport protocol. Each wire protocol has one single ZeroMQ
endpoint in Rewind:

* **A request/response socket for Rewind.** It is used for publishing
  new events and querying chronological slices of all events throughout
  time.

* **A streaming socket.** It is used by all clients that are interested
  in all new incoming events.

Each endpoint is configurable through command line when starting
``rewind``. Issue ``rewind --help`` to get a list of the specific
command line arguments ``rewind`` can handle.

*Note that the wire protocol is still under heavy development. Pull
requests and improvement proposals are welcome!*

Request/response socket
-----------------------
The socket for querying Rewind is the one which has the most advanced
wire protocol. The socket is of type RES and takes commands. A typical
converation between a client (C) and Rewind (R) looks like this::

    C: Request
    R: Response
    C: Request
    R: Response
    ...

Request types
`````````````
Each request is a multipart message. The first part is a string that
specifies the type of request. There are multiple request types:

PUBLISH
'''''''
Used for publishing an event. The next message part is a blob of bytes
that is supposed to be a serialized event of some form. Rewind does not
know anything about the serialization format. It always simply stores
the bytes.

Each new incoming/published event triggers that it is to be streamed out
to all listening clients.

On successful reception of an event, Rewind responds with the ASCII
bytes ``PUBLISHED``. See "Error response" below for error response.

QUERY
'''''
Used for querying for older events. For the ``QUERY`` request type the
next two message parts must be:

* Contains an optional event id, or an empty part. Restricts the
  earliest (chronologically) incoming message that we are interested in
  to all messages received after the event with the specified event id.
  Note that this does not include the message with the specified event
  id. If this part of the message is empty, no lower restriction is made
  and messages will be returned starting from the first event ever seen.

* Contains an optional event id, or an empty part. Restricts the latest
  (chronologically) incoming message that we are interested in to all
  messages received before, or including, the event with the specified
  event id. If this part of the message is empty, no upper restriction
  is made and messages will be returned starting from the first event
  ever seen.

If you are a data structure type-of-guy you could view Rewind as a
distributed insert-ordered map (event id => event) that allows querying
of ranges of events based on event ids.

There are two types of responses that can be given upon a query:

* An error. See "Error response" below; or

* a resultset containing events. It's a multipart message containing
  frames like so; eventid #1, event #1, eventid #2, event #2, eventid
  #3, event #3, ... where eventid #X is the event id for event X. At
  most 100 messages will be returned. If Rewind did not cap number of
  events, the result will be appended by a last frame containing the
  ASCII content ``END``. It is up to the client to make requests
  repeatedly if the result set is capped.

Error response
``````````````
If anything goes wrong, a single message starting with the ASCII text
``ERROR`` will be sent with the response. This means an error occured.
The rest of message contains a human readable (ASCII) description of the
actual error that occured. This information can be highly useful for
remote clients to debug any problems that might arise.

Event stream
------------
Every incoming event gets broadcast to all sockets connected to the
streaming socket. The streaming socket a ZeroMQ socket of type PUB.

Every message received automatically gets assigned a unique event id
(UUID, type 1) by Rewind. This event id is used for querying events (see
below). Each sent message from the streaming is a multipart message that
consists of two parts:

1. The event ID. The client should view this as a series of bytes.

2. The previous event ID. This information is useful to know whether
   ZeroMQ high-water mark kicked in while syncing up a client while
   querying for older events. If streaming has just begun, this message
   part can be empty and can thus be ignored.

3. The event content. This is the exact same bytes that were
   correspondingly sent to the receiving socket.

Developing
==========
Getting started developing `rewind` is quite straightforward. The
library uses `setuptools` and standard Python project layout for tests
etcetera.

Checking out
------------
This is how you check out the `rewind` library into a virtual environment::

    cd <your development directory>
    virtualenv --no-site-packages rewind
    cd rewind
    git clone http://<rewind GIT URL> src

Workin' the code
----------------
Every time you want to work on `rewind` you want to change directory
into the source folder and activate the virtual environment scope (so
that you don't touch the global Python environment)::

    cd src
    source ../bin/activate

The first time you've checked the project out, you want to initialize
development mode::

    python setup.py develop

Runnin' them tests
------------------
Running the test suite is done by issuing::

    python setup.py nosetests

. Nose is configured to automagically spit out test coverage information
after the whole test suite has been executed.

As always, try to run the test suite *before* starting to mess with the
code. That way you know nothing was broken beforehand.

Generally, I try to keep a 100% code coverage of the ``rewind.server``
package. Due to some Python 3 support hack, the coverage is around 99%.
for Python 2.

`The Rewind central github repository`_ also has `Travis CI`
integration that can be accessed at
http://travis-ci.org/#!/JensRantil/rewind Every time a pull request is
being made to https://github.com/JensRantil/rewind, Travis CI will make
a comment about whether the pull request breaks the test suite or not.

.. _The Rewind central github repository: https://github.com/JensRantil/rewind
.. _Travis CI: http://travis-ci.org

Helping out
===========
Spelling mistakes, bad grammar, new storage backends, wire format
improvements, test improvements and other feature additions are all
welcome. Please issue pull requests or create an issue if you'd like to
discuss it on Github.

Why the name "Rewind"?
======================
Pick and choose:

* Rewind can look at what happened in the past and replay the events
  since then.

* It's time to rewind and rethink the way we are overusing DBMS's and
  the way we are storing our data.

Author
======

This package has been developed by Jens Rantil <jens.rantil@gmail.com>.
You can also reach me through snailmail at::

    Jens Rantil
    Br??lunden 4
    16774 Bromma
    SWEDEN
