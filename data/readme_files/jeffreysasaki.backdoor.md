Linux Backdoor
================================================================================
COMP 8505 - Assignment 3

By: Jeffrey Sasaki

May 25, 2015

Description:
--------------------------------------------------------------------------------
This program features a Linux Backdoor implementation where an attacker is able
to remotely access a targeted machine and gain control of executable commands.

Files:
--------------------------------------------------------------------------------
**server.py**
The server is to be ran by the victim's machine. It will conceal itself and
masquerade the process.

**client.py**
The client program is to be ran by the attacker's machine. It will allow access
to the victim's machine, allowing the attacker to execute any Linux commands.
The privilege is based on who executed the server program.

Executables:
--------------------------------------------------------------------------------
On the target's machine, type:

$ python server.py -p (port) &

On the attacker's machine, type:

$ python client.py -d (host ip) -p (port)

Note:
Both program requires pycrypto library to be installed Additionally, the server
requires the setproctitle library to be installed

You may download the libraries from the links below:
- https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz
- https://pypi.python.org/packages/source/s/setproctitle/setproctitle-1.1.8.tar.gz#md5=728f4c8c6031bbe56083a48594027edd

Documentations:
---------------------------------------------------------------------------------
Documentation and testing documentation can be found in Documentation.pdf
