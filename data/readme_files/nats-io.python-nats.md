# NATS - Tornado based Python 2 Client

A Python async client for the [NATS messaging system](https://nats.io).

[![License Apache 2.0](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Build Status](https://travis-ci.org/nats-io/nats.py2.svg?branch=master)](http://travis-ci.org/nats-io/nats.py2)
[![pypi](https://img.shields.io/pypi/v/nats-client.svg)](https://pypi.org/project/nats-client)

## Supported platforms

Should be compatible with [Python 2.7](https://www.python.org/) using
[Tornado 4.2+](https://github.com/tornadoweb/tornado/tree/v4.2.0) (less than 6.0).

For Python 3, check [nats.py](https://github.com/nats-io/nats.py)

## Getting Started

```bash
pip install nats-client
```

## Basic Usage

```python
import tornado.ioloop
import tornado.gen
import time
from nats.io.client import Client as NATS

@tornado.gen.coroutine
def main():
    nc = NATS()

    # Establish connection to the server.
    yield nc.connect("nats://demo.nats.io:4222")

    @tornado.gen.coroutine
    def message_handler(msg):
        subject = msg.subject
        data = msg.data
        print("[Received on '{}'] : {}".format(subject, data.decode()))

    # Simple async subscriber
    sid = yield nc.subscribe("foo", cb=message_handler)

    # Stop receiving after 2 messages.
    yield nc.auto_unsubscribe(sid, 2)
    yield nc.publish("foo", b'Hello')
    yield nc.publish("foo", b'World')
    yield nc.publish("foo", b'!!!!!')

    # Request/Response
    @tornado.gen.coroutine
    def help_request_handler(msg):
        print("[Received on '{}']: {}".format(msg.subject, msg.data))
        yield nc.publish(msg.reply, "OK, I can help!")

    # Susbcription using distributed queue named 'workers'
    sid = yield nc.subscribe("help", "workers", help_request_handler)

    try:
        # Send a request and expect a single response
        # and trigger timeout if not faster than 200 ms.
        msg = yield nc.request("help", b"Hi, need help!", timeout=0.2)
        print("[Response]: %s" % msg.data)
    except tornado.gen.TimeoutError:
        print("Timeout!")

    # Remove interest in subscription.
    yield nc.unsubscribe(sid)

    # Terminate connection to NATS.
    yield nc.close()

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(main)
```

## Clustered Usage

```python
import tornado.ioloop
import tornado.gen
from datetime import timedelta
from nats.io import Client as NATS
from nats.io.errors import ErrConnectionClosed

@tornado.gen.coroutine
def main():
    nc = NATS()

    # Set pool servers in the cluster and give a name to the client
    # each with its own auth credentials.
    options = {
        "servers": [
            "nats://secret1:pass1@127.0.0.1:4222",
            "nats://secret2:pass2@127.0.0.1:4223",
            "nats://secret3:pass3@127.0.0.1:4224"
            ]
        }

    # Error callback takes the error type as param.
    def error_cb(e):
        print("Error! ", e)

    def close_cb():
        print("Connection was closed!")

    def disconnected_cb():
        print("Disconnected!")

    def reconnected_cb():
        print("Reconnected!")

    # Set callback to be dispatched whenever we get
    # protocol error message from the server.
    options["error_cb"] = error_cb

    # Called when we are not connected anymore to the NATS cluster.
    options["closed_cb"] = close_cb

    # Called whenever we become disconnected from a NATS server.
    options["disconnected_cb"] = disconnected_cb

    # Called when we connect to a node in the NATS cluster again.
    options["reconnected_cb"] = reconnected_cb

    yield nc.connect(**options)

    @tornado.gen.coroutine
    def subscriber(msg):
        yield nc.publish("pong", "pong:{0}".format(msg.data))

    yield nc.subscribe("ping", "", subscriber)

    for i in range(0, 100):
        yield nc.publish("ping", "ping:{0}".format(i))
        yield tornado.gen.sleep(0.1)

    yield nc.close()

    try:
        yield nc.publish("ping", "ping")
    except ErrConnectionClosed:
        print("No longer connected to NATS cluster.")

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(main)
```

## Wildcard Subscriptions

```python
import tornado.ioloop
import tornado.gen
import time
from nats.io import Client as NATS

@tornado.gen.coroutine
def main():
    nc = NATS()

    yield nc.connect("demo.nats.io")

    @tornado.gen.coroutine
    def subscriber(msg):
        print("Msg received on [{0}]: {1}".format(msg.subject, msg.data))

    yield nc.subscribe("foo.*.baz", "", subscriber)
    yield nc.subscribe("foo.bar.*", "", subscriber)
    yield nc.subscribe("foo.>", "", subscriber)
    yield nc.subscribe(">", "", subscriber)

    # Matches all of above
    yield nc.publish("foo.bar.baz", b"Hello World")
    yield tornado.gen.sleep(1)

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(main)
```

## Advanced Usage

```python
import tornado.ioloop
import tornado.gen
from nats.io import Client as NATS
from nats.io.errors import ErrNoServers

@tornado.gen.coroutine
def main():
    nc = NATS()

    try:
        # Setting explicit list of servers in a cluster and
        # max reconnect retries.
        servers = [
            "nats://127.0.0.1:4222",
            "nats://127.0.0.1:4223",
            "nats://127.0.0.1:4224"
            ]
        yield nc.connect(max_reconnect_attempts=2, servers=servers)
    except ErrNoServers:
        print("No servers available!")
        return

    @tornado.gen.coroutine
    def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        for i in range(0, 20):
            yield nc.publish(reply, "i={i}".format(i=i).encode())

    yield nc.subscribe("help.>", cb=message_handler)

    @tornado.gen.coroutine
    def request_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # Signal the server to stop sending messages after we got 10 already.
    yield nc.request(
        "help.please", b'help', expected=10, cb=request_handler)

    # Flush connection to server, returns when all messages have been processed.
    # It raises a timeout if roundtrip takes longer than 1 second.
    yield nc.flush()

    # Drain gracefully closes the connection, allowing all subscribers to
    # handle any pending messages inflight that the server may have sent.
    yield nc.drain()

    # Drain works async in the background.
    yield tornado.gen.sleep(1)

if __name__ == '__main__':
    tornado.ioloop.IOLoop.instance().run_sync(main)
```

### TLS

Advanced [customizations options](https://docs.python.org/2/library/ssl.html#ssl.SSLContext.wrap_socket)
for setting up a secure connection can be done by including them on connect:

```python
# Establish secure connection to the server, tls options parameterize
# the wrap_socket available from ssl python package.
options = {
    "servers": ["nats://127.0.0.1:4444"],
    "tls": {
        "cert_reqs": ssl.CERT_REQUIRED,
        "ca_certs": "./configs/certs/ca.pem",
        "keyfile":  "./configs/certs/client-key.pem",
        "certfile": "./configs/certs/client-cert.pem"
      }
    }
yield nc.connect(**options)
```

The client will also automatically create a TLS context with defaults
in case it detects that it should connect securely against the server:

```python
yield nc.connect("tls://demo.nats.io:4443")
```

## Examples

In this repo there are also included a couple of simple utilities
for subscribing and publishing messages to NATS:

```sh
    # Make a subscription to 'hello'
    $ python examples/nats-sub hello

    Subscribed to 'hello'
    [Received: hello] world

    # Send a message to hello
    $ python examples/nats-pub hello -d "world"
```

## License

Unless otherwise noted, the NATS source files are distributed under
the Apache Version 2.0 license found in the LICENSE file.
