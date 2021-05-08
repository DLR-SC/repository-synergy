======
winsys
======

Enter WinSys: the Python Windows Administrator's Toolkit. A collection
of modules with a consistent approach, wrapping the Windows API
calls already exposed by pywin32, adding some with ctypes, and giving them
all a pythonic feel. There's nothing here you couldn't do yourself with
10 minutes and a copy of the pywin32 and SDK docs. But it's all here already,
and with a more Pythonish feel about it.

Docs available at: http://winsys.readthedocs.org/en/latest/index.html

Design Principles
-----------------

The following principles have directed the design of the modules
and packages wherever possible:

* Make ad-hoc use possible and easy (and even attractive)
* Provide sensible defaults for the common cases, always allowing for more complex scenarios
* Put all constants into one place, grouping them according to their API usage
* Use the pywin32 functionality where available, supplementing it with ctypes where needed
* Assume a recent version of Python (tested on 2.6, 2.7, 3.2, 3.3)
* Make good use of context managers (with-statements)
* Have each object able to dump its contents and that of its children cleanly
* Maintain an object approach, but provide convenient module-level functions
* Have useful factory functions for classes, robustly accepting string or object parameters

Common Features
---------------

Most of the objects in winsys subclass the :class:`core._WinSysObject` class which
offers sensible defaults and defines common functionality such as a dump function.
In addition, the following features are common to many of the modules:

Pythonic Naming
~~~~~~~~~~~~~~~

This is mildly contentious, but the same naming convention has been used
throughout, following the ``lowercase_with_underscores`` convention widely
adopted in the Python community. The most widespread exception to this is
in the :mod:`constants` module, where Windows constants retain their
``UPPERCASE_WITH_UNDERSCORES`` names.

Module-level Functions
~~~~~~~~~~~~~~~~~~~~~~

While a lot of use has been made of Python classes to wrap the function-driven
Windows API, a lot of the functionality has been exposed as module-level
convenience functions. So, for example, in the :mod:`fs` module, the :class:`fs.File`
class offers a :meth:`fs.File.copy` method, but the same functionality is exposed
at the module level as :func:`fs.copy`. That way, you don't have to instantiate
one or more objects simply for the purpose of a single operation.

Factory Functions
~~~~~~~~~~~~~~~~~

Most of the classes have a corresponding factory function (usually with
the same name in lower case) which tries to be more accepting in what
its parameters are and to convert them to what's needed by the class's
own ``__init__`` method. So, for example, the :class:`Principal` class whose
initialiser expects a PySID structure has a corresponding :func:`principal`
function which will take a Sid or a user or group name or None or an existing
:class:`Principal` object.

Dump
~~~~

Each object derived from :class:`core._WinSysObject` has a dump method which
is intended to display its internal structures, possibly recursively where
some of the structures are themselves WinSys objects. This is intended more
for ad-hoc use in the interpreter where it's convenient to see, eg, the
security structure which has been loaded from a file.

Iterators & Generators
~~~~~~~~~~~~~~~~~~~~~~

Where possible and meaningful, lazy iterators have been used, often
implemented by generators. This started in the :mod:`fs` module where
thousands of files were being queried for information, but the approach
has generally been adopted across the package.

Context Managers
~~~~~~~~~~~~~~~~

Where it makes sense, context managers have been used, either by means
of the contextlib contextmanager decorator or by defining an object as
its own context manager by means of ``__enter__`` and ``__exit__`` methods.
Examples of context-managed objects include the :class:`ipc.Mailslot` and
:class:`security.Security` objects. Examples of decorated functions include
the :func:`security.change_privileges` and :func:`security.impersonate` functions.

ToDo
----

Obviously, there's loads to do. The Windows API is vast; even the amount of
it exposed by pywin32 far exceeds my immediate needs and the time at my
disposal. The implementation of this package has been driven largely by the
very specific needs of our Windows sysadmins in their day-to-day work. My
intention is to carry on wrapping Windows functionality in a similar way,
but if anyone has particular needs, or can provide functionality to add in,
let's hear about it.