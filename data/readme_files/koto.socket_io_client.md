A simple malicious Socket.IO client as a Python script. 

http://blog.kotowicz.net/2011/03/html5-websockets-security-new-tool-for.html

It can:
 - Handshake with a Socket.io server
 - Ignore all Origin restrictions
 - Transparently handle all socket.io heartbeats
 - Send arbitrary messages - from a prompt or an input file. Messages could be raw or
   properly formatted according to socket.io protocol
 - Receive/log all server messages

I also included a few exemplary payloads which can crash servers I encountered. 
You can test the client against my vulnerable chat application (try XSS).

1. Connect (with Chrome or other browser supporting websockets) to 
   http://vuln.nodester.com/chat.html
2. Run the command line client
   ./socket_io_client.py vuln.nodester.com 80
3. Start conversation
4. Try to inject XSS from the command line client

You could also use my prepared payloads like so:

   ./socket_io_client.py vuln.nodester.com 80 < payloads.txt

Or save all server reponses like so:
   ./socket_io_client.py vuln.nodester.com 80 > output.txt

