README for the py_interface
===========================

What is py_interface
====================

The py_interface is a python-implementation of an Erlang node. For
information on the Erlang programming language, visit the web site
http://www.erlang.org/.

Python 3 vs Python 2
====================

The py_interface as of version 2.0 supports only Python 3.
For Python 2, use 1.x versions of py_interface.

The intention for the 1.x is to only do bug fixes and minor work.
Major efforts will target 2.x.

Overview
========

The py_interface provides the possibility to create a node that may be
used for communication with other Erlang nodes.

Some characteristics:
* The Python nodes are hidden, like the Java nodes
* The Python node supports
  - registering the Python node in the epmd
  - sending and receiving message
  - executing remote procedure calls (the rpc:call(M,F,A) mechanism)
* The Python node does currently _not_ do:
  - linking
  - tracing
* The Python node translates Erlang types to Python types as far as
  there is a reasonable Python counterpart. If there is not, then
  a class is used.
* The Python node is a single threaded callback-driven process.
* The Python node is released under LGPL, see the file COPYING.LIB.
* Work originally begain with Erlang R7 and Python 1.5
* It was recently tested with Erlang 19.2 as well as R15B03 and Python 3.5
* The source of information for this Python node has been the files
  `distribution_handshake.txt' and `erl_ext_dist.txt' together with
  the Java node source files, the `net_kernel.erl' and the
  `dist_util.erl' files in the Erlang source code distribution.
  Nowadays, this is all documented here:
  http://erlang.org/doc/apps/erts/erl_ext_dist.html
  http://erlang.org/doc/apps/erts/erl_dist_protocol.html


General programming model
=========================

When using the py_interface, the general principle is to register a
callback for different purposes, such as incoming messages to the pid,
an return from an rpc-call, or a timeout. The callback will get called
whenever the message or return value arrives or when the timer times
out.

Erlang types vs Python types
============================

  Erlang type   Corresponding Python type
  ------------------------------------------------------------------
  int           int
  float         float
  atom          erl_term.ErlAtom instance
  tuple         tuple

  list          list or str or erl_term.ErlImproperList,
                see below for more info

  map           erl_term.ErlMap instance, which implements a custom
                dictionary type, see below for more info

  pid           erl_term.ErlPid instance
  binary        bytes
  bitstring     erl_term.ErlBitBinary instance

  fun           erl_term.ErlFun or erl_term.ErlFunExport instance
  reference     erl_term.ErlRef instance
  port          erl_term.ErlPort instance
  

About strings and types for data transfer Erlang --> Python
-----------------------------------------------------------

In Erlang, there are no strings, only lists of integers, such as lists of
Unicode code-points.  When the Erlang side serializes a list of integers,
it may encode it as STRING, if it looks like it could be a string.  But it
may also be serialized as a list of integers, depending on its content.
But the heuristic may result in both false positives and false negatives.

If the Erlang side has guessed that the list of integers may in fact be a
string, it will be unpacked as a Python string.  If it has been unpacked as
a list of integers, the function erl_term.IODataToStr can be used to turn
it into a string.  A string can be turned into a list using the function
erl_term.StrToList.

About Erlang maps and Python dicts
----------------------------------

In Erlang, any value can be a key in a map.  In Python, for the corresponding
dict type, only immutable values can be keys; for example lists and class
instances are mutable and thus cannot be used as keys in ordinary dicts.

The way this is done in the py_interface ErlMap, which imitates a dict, is
that for mutable keys, such as lists or ErlAtom instances, a hash of the
serialized value is calculated upon insertion.  Please do not change such
mutable objects used as ErlMap keys, after insertion.  Treat them as if
they had been immutable, or the ErlMap probably won't work as expected.

One more difference between the ErlMap and a normal Python dictionary is
that in ErlMap, 0 and 0.0 are two different keys --- because that is how it
is for Erlang maps, and it is desirable to preserve round-trip consistency
for all terms.  For normal Python dicts, 0 and 0.0 is the same key.


Examples
========

The easiest way to get acquainted with the Python node, run test programs
interactively in two terminal windows:

Example 1: A connection from and Erlang node to a Python node
-------------------------------------------------------------

We will create a Python node named test@127.0.0.1, with cookie x,
it will in turn create and register a process with the name p.
Then it will wait for messages, presumably on the form {Pid::pid(),Msg}
and if it has this format, it will send {self(),Msg} back to Pid.

We will then start an Erlang node which sends such a message and waits
for something to be come back.


In window 1:

  $ cd test
  $ ./pingpong_slave.py -d -n test@127.0.0.1 -c x


In window 2:

  $ erl -name x@127.0.0.1 -setcookie x \
    -eval "{p,'test@127.0.0.1'}"' ! {self(),hello}, receive X -> io:format("Got ~p~n", [X]), halt() end.'


Example 2: An outgoing connection from a Python node to an Erlang node
----------------------------------------------------------------------

We will make an outgoing connection from a Python node to a named
process in an Erlang node. The Erlang side registers a process with name
ppp in a node with name e@127.0.0.1. The Python side connects to this,
and sends a message, the atom mmm.

In window 1:

  $ erl -name e@127.0.0.1 -setcookie x \
    -eval 'register(ppp,self()), receive X -> io:format("Got ~p~n", [X]), halt() end.'

In window 2:

  $ cd test
  $ ./out_connecting.py -d -n t@127.0.0.1 -c x ppp e@127.0.0.1 mmm

Example 3: Make a remote procedure call (rpc) from Python to Erlang
----------------------------------------------------------------------

We will call a function in the Erlang node from the Python side.
The '[[1,2,3]]' is a list of one argument, the list to sum. The single
quotes are to protect it from being interpreted by the shell that we
start it from.

In window 1:

  $ erl -name e@127.0.0.1 -setcookie x

In window 2:

  $ cd test
  $ rpc_caller.py -d -n t@127.0.0.1 -c x e@127.0.0.1 lists sum '[[1,2,3]]'


Contacting the author
=====================
To contact the author, Tomas Abrahamsson: send a mail to:
tab@lysator.liu.se or tomas.abrahamsson@gmail.com

