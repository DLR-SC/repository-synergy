==========================
Using asyncio with Tkinter
==========================

The ``tkapp.py`` and ``tkapp2.py`` examples in this folder demonstrate:

- using an alternative ``asyncio.BaseEventLoop`` subclass on top of the Tkinter event loop;
- leveraging futures and ``yield from`` to escape *callback hell*;
- applying the ``asyncio`` abstractions to GUI programming instead of network programming.

History
=======

The code is adapted from Dino Viehland's (@DinoV) talk `Using futures for async GUI programming in Python 3.3 <http://lanyrd.com/2013/pycon/scdywd/>`_ presented at PyCon US 2013. Dino's example used Tulip because the first release of ``asyncio`` was not available then; some APIs changed later and the ``tkapp.py`` was not working with Python 3.4 and ``asyncio`` from the standard library.

Luciano Ramalho (@ramalho) updated this code to run with Python 3.4 with help and encouragement from Guido van Rossum (@gvanrossum). See relevant thread in the `python-tulip <https://groups.google.com/d/msg/python-tulip/TaSVW-pjWro/QO07gF9dreEJ>`_ group.

Ramalho also wrote the ``tkapp2.py`` which makes it easier to run the three demonstrations from Viehland's talk: sequential processing, asynchronous with callbacks and asynchronous with coroutines.

Alan Cristhian (@AlanCristhian) fixed the hang-on-exit bug by turning the ``asyncio`` event loop thread into a daemon; see ``guievents.py``, method ``GuiEventLoop._start_io_event_loop``.
