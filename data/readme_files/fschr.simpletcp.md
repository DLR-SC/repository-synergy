# simpleTCP
simpleTCP is a minimal non-blocking TCP server written for Python 3. It is licensed under the GNU Affero General Public License, Version 3.

### Installation

**simpleTCP is no longer available on PyPI.** To install, run `python3 setup.py install`.

simpleTCP is written in pure Python 3. It has no external dependencies.

### Quick Start

simpleTCP just requires that you specify:

* the mode (local or public) of your server
  * your server can also be bound to a specific IP address
* the port of your server
* what happens when your server receives data

For example, here's an echo server:

```
from simpletcp.tcpserver import TCPServer

def echo(ip, queue, data):
    queue.put(data)

server = TCPServer("localhost", 5000, echo)
server.run()
```

#### Callback functions

`echo` is the server's callback function. This function is called whenever the server receives data.

Callback functions should take three arguments:

1. `ip`: The IP address that the data was received from.
2. `queue`: This is a `queue.Queue` object. Any data put into this queue will be asynchronously sent back to the socket it was received from. In this case, our server echoes all data it receives, so we just put all received data right back into this queue with `queue.put(data)`.
3. `data`: This is the data that the server received. It is a string of bytes. Its type is `bytes`.

#### The `TCPServer` itself

The `TCPServer` constructor takes three arguments:

1. The `mode`. There are two special `modes`: `"localhost"` and `"public"`. They are aptly named --- `"localhost"` means run the server on `127.0.0.1`. Therefore, the server is only visible on the machine on which it is running. `"public"` means run the server on `0.0.0.0` --- make it visible to anything that can see the machine on which it is running. If mode is not `"localhost"` or `"public"`, then it is interpreted as an IP address.
2. The port. For development, pick a high (four-digit) number.
3. The callback function. This function is called whenever the server receives data.

#### Sending data to the server

To send data to the server, create a `ClientSocket` and send away!

```
from simpletcp.clientsocket import ClientSocket

s1 = ClientSocket("localhost", 5000, single_use=False)
response = s1.send("Hello, World!")
```

### Examples

Examples can be found in the `/examples` folder.
