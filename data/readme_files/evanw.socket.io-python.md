# A socket.io bridge for Python

This gives Python users access to socket.io, a node.js library. This library provides simple and efficient bidirectional communication between browsers and servers over a message-oriented socket. Transport is normalized over various technologies including WebSockets, Flash sockets, and AJAX polling.

## Installation

This bridge requires [node.js](http://nodejs.org) and [socket.io](http://socket.io). Install node.js and [npm](http://npmjs.org/), then run `npm install .` in this directory to install the correct version of socket.io (the newer versions have changed their API).

## Usage

This bridge is designed to be self-contained, so `socket_io.py` is the only file you need. A server is created by subclassing `socket_io.Socket` and overriding the `on_connect`, `on_message`, and/or `on_disconnect` methods:

    import socket_io as io
    
    class Server(io.Server):
        def on_connect(self, client):
            print client, 'connected'
            self.broadcast(str(client) + ' connected')
            print 'there are now', len(self.clients), 'clients'
        
        def on_message(self, client, message):
            print client, 'sent', message
            client.send(message)
        
        def on_disconnect(self, client):
            print client, 'disconnected'
            self.broadcast(str(client) + ' disconnected')
            print 'there are now', len(self.clients), 'clients'
    
    Server().listen(5000)

The client in the browser just uses the same interface that regular socket.io clients use:

    <script type="text/javascript" src="http://localhost:5000/socket.io/socket.io.js"></script>
    <script type="text/javascript">

    function log(html) {
        document.body.innerHTML += html + '<br>';
    }

    var socket = new io.Socket('localhost', { port: 5000 });
    socket.on('connect', function() {
        log('connect');
    });
    socket.on('message', function(data) {
        log('message: ' + data);
    });
    socket.on('disconnect', function() {
        log('disconnect');
    });
    socket.connect();

    </script>
