ghdecoy
=======

[![Join the chat at https://gitter.im/tickelton/ghdecoy](https://badges.gitter.im/tickelton/ghdecoy.svg)](https://gitter.im/tickelton/ghdecoy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

ghdecoy is a tool to vandali^H optimize the github contributions calendar. 
It is inspired by [gitfiti](https://github.com/gelstudios/gitfiti) but
with a different use case in mind.

ghdecoy allows you to create a git repository containing commits crafted
in way so that when it is pushed to github periods in the contribution
calendar containing no commits will be filled with a random pattern so your
account looks sufficiently active.

Demo
------------
There are some demo repositories at [ttn-dcy](https://github.com/ttn-dcy)
where you can see what ghdecoy can do for you.

Dependencies
------------

ghdecoy.py only requires a working installation of python 2.7. No
additional packages are required.

Installation
------------

ghdecoy.py can be run as is from the repository.  
If desired it can also be installed using the standard python install command:
```shell
python setup.py install
```

Usage
-----

ghdecoy.py will create a git repository containing fake commits. The
default name for the repository is 'decoy' and by default it will
be located under '/tmp'. Those values can be overridden by command
line arguments. Use the '--help' argument for more detailed information.

When running the script you will typically only have to provide your
github username and the way ghdecoy is supposed to fill your graph.
Currently the following two modes are supported:

 * fill   : fill all occurrences of 5 or more consecutive days without commits with random noise.
 * append : same as fill, but only fills the blank space after the last existing commit.
 * DATE[-DATE][,...] : with DATE being of the format YYYYMMMDD. Randomizes only the given date(s). See man page for details.

EXAMPLE
-------
```shell
python ghdecoy.py -u tickelton append
```
