.. log_calls Readme documentation master file, created by
   sphinx-quickstart on Tue Feb  9 05:14:29 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
    :hidden:
    :maxdepth: 1
    :titlesonly:


.. role:: raw-html(raw)
   :format: html

.. |br| raw:: html

   <br />

.. |release| replace:: 0.3.2



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`log_calls` — A Decorator for Debugging and Profiling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Readme (release |release|)
############################################################

`log_calls` is a Python 3.3+ decorator that can print a lot of useful information
about calls to decorated functions, methods and properties. The decorator can
write to ``stdout``, to another stream or file, or to a logger. `log_calls`
provides methods for writing your own debug messages, and for easily "dumping"
variables and expressions paired with their values. It can decorate individual
functions, methods and properties; but it can also programmatically decorate
callable members of entire classes and class hierarchies, even of entire modules,
with just a single line — which can greatly expedite learning a new codebase.

In short, `log_calls` can save you from writing, rewriting, copying, pasting and
tweaking a lot of *ad hoc*, debug-only, boilerplate code — and it can keep *your*
codebase free of that clutter.

For each call to a decorated function or method, `log_calls` can show you:

* the caller (in fact, the complete call chain back to another `log_calls`-decorated caller,
  so there are no gaps in chains displayed)
* the arguments passed to the function or method, and any default values used
* nesting of calls, using indentation
* the number of the call (whether it's the 1\ :superscript:`st` call, the 2\ :superscript:`nd`,
  the 103\ :superscript:`rd`, ...)
* the return value
* the time it took to execute
* and more!

These and other features are optional and configurable settings, which can be specified
for each decorated callable via keyword parameters, as well as *en masse* for a group of
callables all sharing the same settings. You can examine and change these settings
on the fly using attributes with the same names as the keywords, or using a dict-like
interface whose keys are the keywords.

`log_calls` can also collect profiling data and statistics, accessible at runtime, such as:

* the number of calls to a function
* total time taken by the function
* the function's entire call history (arguments, time elapsed, return values, callers,
  and more), available as text in CSV format and, if `Pandas <http://pandas.pydata.org>`_
  is installed, as a `DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`_.

The package contains two other decorators:

* `record_history`, a stripped-down version of `log_calls`,
  only collects call history and statistics, and outputs no messages;
* `used_unused_keywords` lets a function or method easily determine, per-call,
  which of its keyword parameters were actually supplied by the caller,
  and which received their default values.

This document introduces `log_calls` and shows you a few ways to use it. To learn more,
see `the complete documentation  <http://www.pythonhosted.org/log_calls/index.html>`_
for the definitive, detailed account.

The test suites in ``log_calls/tests/``, which provide 96+% coverage, contain
many additional examples, with commentary.

--------------------------------------------------------------------

.. _requirements:

Requirements
##################

The *log_calls* package has no dependencies — it requires no other packages.
All it requires is a standard distribution of Python 3.3 or higher (Python 3.4+ recommended).
The package won't install on earlier versions.

.. _installation:

Installation
##################

Installing `log_calls` is as simple as running the command

       ``$ pip install log_calls``

to install `log_calls` from PyPI (the Python Package Index). Here,
``$`` indicates your command prompt, whatever it may be.

The complete distribution of `log_calls` (available as a  ``tar.gz`` or a ``zip``
from PyPI or github) contains three subdirectories: ``log_calls``, the package
proper; ``docs``, the documentation source files; and ``tests``, mentioned above.
These last two subdirectories are *not* installed by pip, so to obtain those
files you'll have to download an archive and unpack the archive to a fresh directory.
You can then install `log_calls` by changing to that directory and running
the following command:

        ``$ python3 setup.py install``


Whichever method you choose, ideally you'll install `log_calls` in a virtual
environment (a *virtualenv*).
It's easy to set up a virtual environment using tools included in the standard
distribution: in Python 3.3 - 3.5, use
`pyvenv <https://docs.python.org/3/using/scripts.html?highlight=pyvenv#pyvenv-creating-virtual-environments>`_
; in Python 3.6, which deprecates ``pyvenv``, use

       ``$ python3.6 -m venv /path/to/virtualenv``

as per `the relevant docs <https://docs.python.org/3/library/venv.html?highlight=venv#creating-virtual-environments>`_.

--------------------------------------------------------------------

.. _quickstart:

Quick Start
############

.. _Basic-usage:

Basic usage
==================================================

First, let's import the `log_calls` decorator from the package of the same name:

    >>> from log_calls import log_calls

In code, ``log_calls`` now refers to the decorator, a class (an object of type ``type``),
and not to the module:

    >>> type(log_calls)
    type

The decorator has many options, and thus can take many parameters,
but let's first see the simplest examples possible, using no parameters at all.

.. _quickstart-functions:

Decorating functions
---------------------

If you decorate a function with `log_calls`, each call to the function is generally
preceded and followed by some reportage. The decorator first writes messages announcing
entry to the function and what arguments it has received; the decorator calls the function
with those arguments, and the function executes; upon its return, the decorator finishes up
and announces the return of the function:

    >>> @log_calls()
    ... def f(a, b, c):
    ...     print("--- Hi from f")
    >>> f(1, 2, 3)
    f <== called by <module>
        arguments: a=1, b=2, c=3
    --- Hi from f
    f ==> returning to <module>

Adding another decorated function to the call chain presents useful information too. Here,
``g`` calls the decorated ``f`` above. Observe that (by default) the `log_calls` output for the
nested call to ``f`` is indented to align with the inner lines of the `log_calls` output for ``g``:

    >>> @log_calls()
    ... def g(n):
    ...     print("*** Hi from g")
    ...     f(n, 2*n, 3*n)
    ...     print("*** Bye from g")
    >>> g(3)
    g <== called by <module>
        arguments: n=3
    *** Hi from g
        f <== called by g
            arguments: a=3, b=6, c=9
    --- Hi from f
        f ==> returning to g
    *** Bye from g
    g ==> returning to <module>

`log_calls` gives informative output even when call chains include undecorated functions.
In the next example, a decorated function ``h`` calls an undecorated ``g2``, which calls
an undecorated ``g1``, which, finally, calls our original decorated ``f``:

    >>> def g1(n): f(n, 2*n, 3*n)
    >>> def g2(n): g1(n)
    >>> @log_calls()
    ... def h(x, y): g2(x+y)

Now let's call ``h``:

    >>> h(2, 3)
    h <== called by <module>
        arguments: x=2, y=3
        f <== called by g1 <== g2 <== h
            arguments: a=5, b=10, c=15
    --- Hi from f
        f ==> returning to g1 ==> g2 ==> h
    h ==> returning to <module>

Notice that when writing entry and exit messages for ``f``, `log_calls` displays
the entire active call chain *back to the nearest decorated function*, so that there
aren't "gaps" in the chain of functions it reports on. If it didn't do this, we'd
see only ``f <== called by g1``, and then ``f ==> returning to g1`` followed by
``h ==> returning to <module>``, which wouldn't tell us the whole story about how
control reached ``g1`` from ``h``.

See the `Call Chains <http://www.pythonhosted.org/log_calls/call_chains.html>`_
chapter of the documentation contains for examples and finer points.


.. _quickstart-methods:

Decorating methods
-------------------

Similarly, you can decorate methods (and properties) within a class:

    >>> class A():
    ...     def __init__(self, n):
    ...         self.n = n
    ...
    ...     @log_calls()
    ...     def ntimes(self, m):
    ...         return self.n * m

Only the ``ntimes`` method is decorated:

    >>> a = A(3)            # __init__ called
    >>> a.ntimes(4)                 # doctest: +ELLIPSIS
    A.ntimes <== called by <module>
        arguments: self=<__main__.A object at 0x...>, m=4
    A.ntimes ==> returning to <module>
    12

---------------------------------------------------------------------------------------------

.. _quickstart-classes:

Decorating classes
==================================================

To decorate all methods and properties of a class, simply decorate the class itself:

    >>> @log_calls()
    ... class C():
    ...     def __init__(self, n):
    ...         self.n = n if n >= 0 else -n
    ...
    ...     @staticmethod
    ...     def revint(x): return int(str(x)[::-1])
    ...
    ...     @property
    ...     def revn(self): return self.revint(self.n)

All methods of ``C`` are now decorated. Creating an instance logs the call to ``__init__``:

    >>> c = C(123)                    # doctest: +ELLIPSIS
    C.__init__ <== called by <module>
        arguments: self=<__main__.C object at 0x...>, n=123
    C.__init__ ==> returning to <module>

Accessing its ``revn`` property calls the staticmethod ``revint``, and both calls are logged:

    >>> c.revn                        # doctest: +ELLIPSIS
    C.revn <== called by <module>
        arguments: self=<__main__.C object at 0x...>
        C.revint <== called by C.revn
            arguments: x=123
        C.revint ==> returning to C.revn
    C.revn ==> returning to <module>
    321

If you want to decorate only some of the methods of a class, you *don't* have to
individually decorate all and only all the ones you want: the ``only`` and ``omit``
keyword parameters to the class decorator let you concisely specify which methods
will and won't be decorated. The following section introduces ``omit``.

Decorating *most* methods, overriding the settings of one method
----------------------------------------------------------------------

Suppose you have a class ``D`` that's just like ``C`` above, but adds a ``double()`` method.
(For the sake of example, never mind that in practice you might subclass ``C``.)
Suppose you want to decorate all callables in ``D`` *except* ``revint``,
and furthermore, you want `log_calls` to report values returned by the property getter
``revn``. Here's how to do it:

    >>> @log_calls(omit='revint')
    ... class D():
    ...     def __init__(self, n):
    ...         self.n = n if n >= 0 else -n
    ...
    ...     @staticmethod
    ...     def revint(x): return int(str(x)[::-1])
    ...
    ...     def double(self): return self.n + self.n
    ...
    ...     @property
    >>>     @log_calls(log_retval=True)
    ...     def revn(self): return self.revint(self.n)

By default, `log_calls` does *not* display return values, and the outer, class-level
decorator uses that default. The explicit decorator of ``revn`` overrides that,
specifying the desired setting. Note that ``@log_calls`` follows ``@property``:
in general, when decorating a callable in a class, ``@log_calls``
should come *after* any ``@property``, ``@classmethod`` or ``@staticmethod`` decorator.

Let's see this class in action:

    >>> d = D(71)                                           # doctest: +ELLIPSIS
    D.__init__ <== called by <module>
        arguments: self=<__main__.D object at 0x...>, n=71
    D.__init__ ==> returning to <module>

The return value of ``d.double()`` is *not* logged:

    >>> d.double()                                          # doctest: +ELLIPSIS
    D.double <== called by <module>
        arguments: self=<__main__.D object at 0x...>
    D.double ==> returning to <module>

However, the return value of ``revn`` *is* logged, and ``revint`` has *not* been decorated:

    >>> print('~~~\\nMy favorite number plus 3 is', d.revn + 3)   # doctest: +ELLIPSIS
    D.revn <== called by <module>
        arguments: self=<__main__.D object at 0x...>
        D.revn return value: 17
    D.revn ==> returning to <module>
    ~~~
    My favorite number plus 3 is 20

For more information
----------------------

The chapter `Decorating Classes <http://www.pythonhosted.org/log_calls/decorating_classes.html>`_
covers that subject thoroughly — basics, details,
subtleties and techniques.
In particular, ``only`` and ``omit`` are documented there, in the
section `the omit and only keyword parameters  <http://www.pythonhosted.org/log_calls/decorating_classes.html#the-omit-and-only-keyword-parameters-default-tuple>`_
.

---------------------------------------------------------------------------------------------

Writing `log_calls`-aware debugging messages
=====================================================

Printing statements to an output device or file is one of the oldest forms of debugging.
These statements (let's call them `debugging messages`, `aka` "print statements") track
a program's progress, display the values of variables, announce milestones, report on
the consistency of internal state, and so on.

The ``@log_calls`` decorator automates the boilerplate aspects of this reportage:
who calls whom, when, how, and with what result. `log_calls` also provides the methods

    * ``log_calls.print()`` and
    * ``log_calls.print_exprs()``

as attractive alternatives to the ``print`` function for writing other debugging messages.

One common kind of debugging message reports the values of variables as a program runs,
taking snapshots at strategic places at the top level of the code, or within a loop as an
algorithm executes. Writing such statements becomes tedious quickly — they're all alike
though in details all different too. The ``log_calls.print_exprs`` method lets you easily
display the values of variables and expressions within a decorated function.

All other debugging messages require a method as general as ``print``: the ``log_calls.print``
method is that counterpart.

Both methods write to the same output destination as the decorator,
whether that's the console, a file or a logger, and their output is properly synced and aligned with
the decorator's output:

    >>> @log_calls()
    ... def gcd(a, b):
    ...     log_calls.print("At bottom of loop:")
    ...     while b:
    ...         a, b = b, (a % b)
    ...         log_calls.print_exprs('a', 'b', prefix="\\t", suffix= '\\t<--')
    ...     return a
    >>> gcd(48, 246)            # doctest: +NORMALIZE_WHITESPACE
    gcd <== called by <module>
        arguments: a=48, b=246
        At bottom of loop:
        	a = 246, b = 48	<--
        	a = 48, b = 6	<--
        	a = 6, b = 0	<--
    gcd ==> returning to <module>
    6

If you delete, comment out or otherwise disable the decorator, the ``print*`` methods will do nothing
(except waste a little time). To illustrate this, we could just repeat the above function with the
decorator omitted or commented out; but we can also disable the decorator dynamically, and the
``print*`` methods will be silent too:

    >>> gcd.log_calls_settings.enabled = False
    >>> gcd(48, 246)
    6

You can pass expressions to ``print_exprs``:

    >>> @log_calls()
    ... def f():
    ...     x = 42
    ...     log_calls.print_exprs('x', 'x//6', 'x/6')
    >>> f()
    f <== called by <module>
        x = 42, x//6 = 7, x/6 = 7.0
    f ==> returning to <module>

``print`` and ``print_exprs`` properly indent even multiline messages:

    >>> @log_calls()
    ... def f(a):
    ...     log_calls.print("Even multiline messages\\n"
    ...                     "are properly indented.")
    ...     return g(a, 2*a)
    >>> @log_calls()
    ... def g(x, y):
    ...     retval = x + y + 1
    ...     log_calls.print_exprs('retval',
    ...                           prefix="So are multiline\\n"
    ...                                  "prefixes --\\n",
    ...                           suffix="\\n-- and suffixes.")
    ...     return retval
    >>> f(2)
    f <== called by <module>
        arguments: a=2
        Even multiline messages
        are properly indented.
        g <== called by f
            arguments: x=2, y=4
            So are multiline
            prefixes --
            retval = 7
            -- and suffixes.
        g ==> returning to f
    f ==> returning to <module>
    7

You can specify multiple lines for ``print`` either with one string that has explicit newlines,
as above, or by using the ``sep`` keyword parameter together with multiple positional string arguments:

    >>> @log_calls()
    ... def h():
    ...     log_calls.print("Line 1 of 3", "line 2 of 3", "line 3 of 3",
    ...                     sep='\\n')
    >>> h()
    h <== called by <module>
        Line 1 of 3
        line 2 of 3
        line 3 of 3
    h ==> returning to <module>


The behavior of the ``print*`` methods is configurable in a few ways:

    * their output can be "allowed through" while muting the output of the decorators;
    * their output doesn't *have* to be indented, it can be flush left (``extra_indent_level=-1000``);
    * optionally the methods can raise an exception if called from within a function or method that
      isn't decorated, so that development-only code doesn't sneak into production.

In the main documentation, the chapter
`Appendix I: Keyword Parameters Reference <http://www.pythonhosted.org/log_calls/writing_log_calls_aware_debug_messages.html>`_
details
the ``print()`` and ``print_exprs()`` methods; the chapter
`Appendix I: Keyword Parameters Reference <http://www.pythonhosted.org/log_calls/dynamic_control_of_settings.html>`_
documents the ``log_calls_settings`` attribute of a decorated callable.

---------------------------------------------------------------------------------------------

Decorating "external" code
==================================================

Sometimes it's enlightening and instructive to decorate objects in a package or module
that you import. It might be in a new codebase you're getting to know, your own nontrivial
code from a while ago which you now wish you had documented more, or even a function, class
or module in Python's standard library.

We'll illustrate techniques with a simple example: decorating the fractions class
``fractions.Fraction`` in the standard library, to examine how it works. Along the way
we'll illustrate using `log_calls` settings to filter the output, forming hunches about
how ``Fraction`` works based on the information the decorator presents, and consulting
the source code to confirm or refute those hunches.

First, let's import the class, decorate it and create an instance:

    >>> from log_calls import log_calls
    >>> from fractions import Fraction as Frac
    >>> log_calls.decorate_class(Frac)
    >>> print(Frac(3,4))
    Fraction.__new__ <== called by <module>
        arguments: cls=<class 'fractions.Fraction'>, numerator=3, denominator=4
        defaults:  _normalize=True
    Fraction.__new__ ==> returning to <module>
    Fraction.__str__ <== called by <module>
        arguments: self=Fraction(3, 4)
    Fraction.__str__ ==> returning to <module>
    3/4

(**Note**: *In this section, the expected output shown is from Python 3.6 and 3.5.
The output of Python ≤ 3.4 differs slightly: in places it's less efficient, and* __new__,
*indirectly called below, had no* _normalize *parameter.*)

Now create a couple of fractions, using the `log_calls` global mute to do it in silence:

    >>> log_calls.mute = True
    >>> fr56 = Frac(5,6)
    >>> fr78 = Frac(7,8)
    >>> log_calls.mute = False

Before using these, let's redecorate to improve `log_calls` output.
After trying other examples at the command line it becomes apparent that
``__str__`` gets called a lot, and the calls become just noise, so let's
``omit`` that. To eliminate more clutter, let's suppress the exit lines
("... returning to..."). We'll also display return values. Here's how to
accomplish all of that, with another call to ``decorate_class``, which won't
wrap the `log_calls` wrappers already created but will instead just update their settings:

    >>> log_calls.decorate_class(Frac,
    ...                          omit='__str__', log_exit=False, log_retval=True)

Finally, let's do some arithmetic on fractions:

    >>> print(fr78 - fr56)      # doctest: +SKIP
    Fraction._operator_fallbacks.<locals>.forward (__sub__) <== called by <module>
        arguments: a=Fraction(7, 8), b=Fraction(5, 6)
        Fraction.denominator <== called by _sub <== Fraction._operator_fallbacks.<locals>.forward (__sub__)
            arguments: a=Fraction(7, 8)
            Fraction.denominator return value: 8
        Fraction.denominator <== called by _sub <== Fraction._operator_fallbacks.<locals>.forward (__sub__)
            arguments: a=Fraction(5, 6)
            Fraction.denominator return value: 6
        Fraction.numerator <== called by _sub <== Fraction._operator_fallbacks.<locals>.forward (__sub__)
            arguments: a=Fraction(7, 8)
            Fraction.numerator return value: 7
        Fraction.numerator <== called by _sub <== Fraction._operator_fallbacks.<locals>.forward (__sub__)
            arguments: a=Fraction(5, 6)
            Fraction.numerator return value: 5
        Fraction.__new__ <== called by _sub <== Fraction._operator_fallbacks.<locals>.forward (__sub__)
            arguments: cls=<class 'fractions.Fraction'>, numerator=2, denominator=48
            defaults:  _normalize=True
            Fraction.__new__ return value: 1/24
        Fraction._operator_fallbacks.<locals>.forward (__sub__) return value: 1/24
    1/24

The topmost call is to an inner function ``forward`` of the method ``Fraction._operator_fallbacks``,
presumably a closure. The ``__name__`` of the callable is actually ``__sub__`` (its ``__qualname__``
is ``Fraction._operator_fallbacks.<locals>.forward``). We know that classes implement
the infix subtraction operator ``-`` with "dunder" methods ``__sub__`` and ``__rsub__``,
so it appears that in ``Fraction``, the closure `is` the value of the attribute ``__sub__``:

    >>> Frac.__sub__      # doctest: +ELLIPSIS
    <function Fraction._operator_fallbacks.<locals>.forward...>
    >>> Frac.__sub__.__qualname__
    'Fraction._operator_fallbacks.<locals>.forward'
    >>> Frac.__sub__.__name__
    '__sub__'

The closure calls an undecorated function or method ``_sub``. Because
``_sub`` isn't decorated we don't know what its arguments are, and the call chains for
the decorated ``numerator``, ``denominator`` and ``__new__`` chase back to ``__sub__``.
It appears to know about both operands, so we might guess that it takes two arguments.
A look at the source code for ``fractions``,
`fractions.py <https://hg.python.org/cpython/file/3.6/Lib/fractions.py>`_
confirms that guess (``_sub`` is on line 433).

Why isn't ``_sub`` decorated?
------------------------------

Let's check that:

    >>> print(Frac._sub(fr78, fr56))
    Fraction._sub <== called by <module>
        arguments: a=Fraction(7, 8), b=Fraction(5, 6)
        Fraction.denominator <== called by Fraction._sub
            arguments: a=Fraction(7, 8)
            Fraction.denominator return value: 8
        Fraction.denominator <== called by Fraction._sub
            arguments: a=Fraction(5, 6)
            Fraction.denominator return value: 6
        Fraction.numerator <== called by Fraction._sub
            arguments: a=Fraction(7, 8)
            Fraction.numerator return value: 7
        Fraction.numerator <== called by Fraction._sub
            arguments: a=Fraction(5, 6)
            Fraction.numerator return value: 5
        Fraction.__new__ <== called by Fraction._sub
            arguments: cls=<class 'fractions.Fraction'>, numerator=2, denominator=48
            defaults:  _normalize=True
            Fraction.__new__ return value: 1/24
        Fraction._sub return value: 1/24
    1/24

Aha: it *is* decorated after all, and the `log_calls` output certainly looks familiar.

Consulting the source code makes clear what's going on.
When ``Fraction`` is created, on line 439 ``__sub__`` is set equal to a closure
returned by ``_operator_fallbacks(_sub, operator.sub)``, defined on line 318.
The closure is an instance of its inner function ``forward`` on line 398, which
implements generic dispatch based on argument types to one of the two functions
passed to ``_operator_fallbacks``. When called with two ``Fraction``\ s, ``__sub__``
calls ``_sub`` and not ``operator.sub``. On line 407, ``_operator_fallbacks`` sets
the name of the closure to ``__sub__``.

So, the closure ``forward`` that implements ``__sub__`` has a nonlocal variable bound
to the real ``_sub`` at class initialization, before the methods of the class were decorated.
The closure calls the inner, decorated ``_sub``, not the `log_calls` wrapper around it.

How the code works
-------------------

Ultimately, then, subtraction of fractions is performed by a function ``_sub``,
to which ``__sub__`` i.e. ``Fraction._operator_fallbacks.<locals>.forward`` dispatches.
``_sub`` uses the public properties ``denominator`` and ``numerator``
to retrieve the fields of the ``Fraction``\ s, and returns a new ``Fraction``, with a
numerator of 2 (= 7 * 6 - 8 * 5) and denominator of 48 (= 6 * 8). ``__new__`` (line 124
of the source code) reduces the returned ``Fraction`` to lowest terms just before
returning it (because its parameter ``_normalize`` is true, its default value, which
gives Python 3.4 behavior).

Scrolling through ``fractions.py`` reveals that other operators are implemented
in exactly the same way.

For more information
----------------------------

The ``decorate_*`` methods are presented in the
main documentation chapter `Bulk (Re)Decoration, (Re)Decorating Imports <http://www.pythonhosted.org/log_calls/decorating_functions_class_hierarchies.html>`_.

---------------------------------------------------------------------------------------------

Changing "settings" dynamically
================================

When `log_calls` decorates a callable (a function, method, property, ...), it "wraps" that
callable in a function — the *wrapper* of the callable. Subsequently, calls to the decorated
callable actually call the wrapper, which delegates to the original, in between its own
pre- and post-processing. This is simply what decorators do.

`log_calls` gives the wrapper a few attributes pertaining to the wrapped callable, notably
``log_calls_settings``, a dict-like object that contains the `log_calls` state of the callable.
The keys of ``log_calls_settings`` are `log_calls` keyword parameters, such as ``enabled`` and
``log_retval`` — in fact, most of the keyword parameters, though not all of them.

What is a "setting"?
---------------------------

**The** *settings of a decorated callable* **are the key/value pairs of its**
``log_calls_settings`` **object, which is an attribute of the callable's wrapper.**
The settings comprise the `log_calls` state of the callable.

.. _the_settings:

The following keyword parameters are (keys of) settings:

    ``enabled``
    ``args_sep``
    ``log_args``
    ``log_retval``
    ``log_exit``
    ``log_call_numbers``
    ``log_elapsed``
    ``indent``
    ``prefix``
    ``file``
    ``mute``
    ``logger``
    ``loglevel``
    ``record_history``
    ``max_history``

The other keyword parameters are *not* "settings":

    ``NO_DECO``
    ``settings``
    ``name``
    ``override``
    ``omit``
    ``only``

These are directives to the decorator telling it how to initialize itself. Their initial values
are not subsequently available via attributes of the wrapper, and cannot subsequently be changed.

Lifecycle of a "setting"
------------------------------
Initially the value of a setting is the value passed to the `log_calls` decorator for
the corresponding keyword parameter, or the default value for that parameter if no
argument was supplied for it:

    >>> @log_calls(args_sep = ' / ')
    ... def f(*args, **kwargs): return 91

You can access and change the settings of ``f`` via its ``log_calls_settings`` attribute,
which behaves like a dictionary whose keys are the `log_calls` settings keywords:

    >>> f.log_calls_settings['args_sep']
    ' / '
    >>> f.log_calls_settings['enabled']
    True

All of a decorated callable's settings can be accessed through ``log_calls_settings``,
and almost all can be changed on the fly:

    >>> f.log_calls_settings['enabled']
    True
    >>> f.log_calls_settings['enabled'] = False

You can also use the same keywords as attributes of ``log_calls_settings``
instead of as keys to the mapping interface — they're completely equivalent:

    >>> f.log_calls_settings.enabled
    False

`log_calls` is disabled for ``f``, hence no output here:

    >>> _ = f()                   # no output (not even 91, because of "_ = ")

Let's reenable `log_calls` for ``f``, turn on call numbering and display of return values.
We could do this with three separate assignments to settings, but it's easier to use
the ``log_calls_settings.update()`` method:

    >>> f.log_calls_settings.update(
    ...     enabled=True, log_call_numbers=True,log_retval=True)

Now call ``f`` again:

    >>> _ = f()                   # output
    f [1] <== called by <module>
        arguments: <none>
        f [1] return value: 91
    f [1] ==> returning to <module>

and again:

    >>> _ = f(17, 19, foo='bar')                 # output
    f [2] <== called by <module>
        arguments: *args=(17, 19) / **kwargs={'foo': 'bar'}
        f [2] return value: 91
    f [2] ==> returning to <module>


For more information
----------------------------

The chapter `Dynamic Control of Settings <http://www.pythonhosted.org/log_calls/dynamic_control_of_settings.html>`_
of the documentation presents the ``log_calls_settings`` attribute and its API in detail, with many examples.

---------------------------------------------------------------------------------------------

The ``settings`` keyword parameter
==================================================

The ``settings`` parameter lets you collect common values for settings keyword parameters
in one place, and pass them to `log_calls` with a single parameter.
``settings`` is a useful shorthand if you have, for example, a module with several
`log_calls`-decorated functions, all with multiple, mostly identical settings
which differ from `log_calls`'s defaults. Instead of repeating multiple identical
settings across several uses of the decorator, a tedious and error-prone practice,
you can gather them all into one ``dict`` or text file, and use the ``settings``
parameter to concisely specify them *en masse*. You can use different groups
of settings for different sets of functions, or classes, or modules — you're
free to organize them as you please.

When not ``None``, the ``settings`` parameter can be either a ``dict``, or a ``str``
specifying the location of a *settings file* — a text file containing *key=value* pairs and optional comments.
In either case, the valid keys are the keyword parameters that are "settings", listed :ref:`above <the_settings>`,
plus, as a convenience, ``NO_DECO``. *Invalid keys are ignored.*

The values of settings specified in a settings dict or settings file override `log_calls`'s
default values for those settings, and any of the resulting settings are in turn overridden
by corresponding keywords passed directly to the decorator. Of course, you *don't* have to provide
a value for every valid key.

``settings`` as a ``dict``
--------------------------------------

The value of ``settings`` can be a ``dict``, or more generally any object
``d`` for which it's true that ``isinstance(d, dict)``. Here's a settings
``dict`` and two `log_calls`-decorated functions that use it:

    >>> d = dict(
    ...     args_sep=' | ',
    ...     log_args=False,
    ...     log_call_numbers=True,
    ...     NO_DECO=False           # True: "kill switch"
    ... )
    >>> @log_calls(settings=d)
    ... def f(n):
    ...     if n <= 0: return
    ...     f(n-1)
    >>> @log_calls(settings=d, log_args=True)
    ... def g(s, t): print(s + t)

Note that ``g`` overrides the ``log_args`` setting given in ``d``:

    >>> f.log_calls_settings.log_args, g.log_calls_settings.log_args
    (False, True)

Let's call these functions and examine their `log_calls` output:

    >>> f(2)
    f [1] <== called by <module>
        f [2] <== called by f [1]
            f [3] <== called by f [2]
            f [3] ==> returning to f [2]
        f [2] ==> returning to f [1]
    f [1] ==> returning to <module>

    >>> g('aaa', 'bbb')
    g [1] <== called by <module>
        arguments: s='aaa' | t='bbb'
    aaabbb
    g [1] ==> returning to <module>

``settings`` as a pathname (``str``)
------------------------------------------

When the value of the ``settings`` parameter is a ``str``, it must be a path to a
*settings file* — a text file containing *key=value* pairs and optional comments.
If the pathname is just a directory, `log_calls` looks there for a file
named ``.log_calls`` and uses that as a settings file; if the pathname is a file,
`log_calls` uses that file. In either case, if the file doesn't exist then no error
results *nor is any warning issued*, and the ``settings`` parameter is ignored.

.. topic:: Format of a settings file

    A *settings file* is a text file containing zero or more lines of the form

        *setting_name*\ ``=``\ *value*

    Whitespace is permitted around *setting_name* and *value*, and is stripped.
    Blank lines are ignored, as are lines whose first non-whitespace character is ``#``,
    which therefore you can use as comments.

Using ``NO_DECO`` as a global "kill switch"
-------------------------------------------------

The ``NO_DECO`` parameter prevents `log_calls` from decorating a callable or class:
when true, the decorator returns the decorated thing itself, unwrapped and unaltered.
Intended for use at program startup, it provides a single "true bypass" switch.

Using this parameter in a settings dict or settings file lets you
completely bypass `log_calls` decoration for all decorators using that ``settings`` value,
with a single switch, e.g. for production, without having to comment out every decoration.

Use ``NO_DECO=True`` for production
-------------------------------------------

Even even when it's disabled or bypassed, `log_calls` imposes some overhead.
For production, therefore, it's best to not use it at all. One tedious way to guarantee
that would be to comment out every ``@log_calls()`` decoration in every source file.
``NO_DECO`` allows a more humane approach: Use a settings file or settings dict
containing project-wide settings, including an entry for ``NO_DECO``.
For development, use::

    NO_DECO=False

and for production, change that to::

    NO_DECO=True

Even though it isn't actually a "setting", ``NO_DECO`` is permitted in settings files and dicts
in order to allow this.

For example, if we change the ``NO_DECO`` setting in the settings dict ``d`` above and rerun
the script, ``f`` and ``g`` will **not** be decorated:

    >>> d = dict(
    ...     args_sep=' | ',
    ...     log_args=False,
    ...     log_call_numbers=True,
    ...     NO_DECO=True            # True: "kill switch"
    ... )
    >>> @log_calls(settings=d)
    ... def f(n):
    ...     if n <= 0: return
    ...     f(n-1)
    >>> @log_calls(settings=d, log_args=True)
    ... def g(s, t): print(s + t)

    >>> f(2)                # no log_calls output
    >>> g('aaa', 'bbb')     # no log_calls output
    aaabbb

The functions ``f`` and ``g`` aren't just disabled or muted; they're not decorated at all:

    >>> hasattr(f, 'log_calls_settings'), hasattr(g, 'log_calls_settings')
    (False, False)

For more information
----------------------------
See the section
on `the settings parameter <http://www.pythonhosted.org/log_calls/parameters.html#settings-default-none>`_ in
the Keyword Parameters chapter of the documentation.

---------------------------------------------------------------------------------------------

Where To Go From Here
#######################################

These examples have shown just a few of the features that make `log_calls` powerful,
versatile, yet easy to use. They have introduced a few of `log_calls`'s keyword
parameters, the source of much of its versatility, as well as some of its more
advanced capabilities.

In the main documentation, the
chapter `What log_calls Can Decorate <http://www.pythonhosted.org/log_calls/what_log_calls_can_decorate.html>`_
gives general culture and also introduces terminology and concepts subsequently used throughout.
The chapter following it,
`Keyword Parameters <http://www.pythonhosted.org/log_calls/parameters.html>`_,
documents the parameters in detail.
That chapter is a reference, to which you can refer back
as needed; it's not necessary to assimilate its details before proceeding on to further topics.
For an even more concise reference, almost a cheatsheet,
see `Appendix I: Keyword Parameters Reference <http://www.pythonhosted.org/log_calls/appendix_I_parameters_table.html>`_.

`log_calls` provides yet more functionality. The
`full documentation <http://www.pythonhosted.org/log_calls/index.html>`_
covers all of it.

-------------------------------

.. raw:: html

    <p style="font-size: 95%">
    You can show your appreciation and support of <em>log_calls</em> by
    <a href="http://www.paypal.me/logcalls" TARGET="_blank">
        <img src="docs/_static/Donate-BLUE.png" style="vertical-align: middle;" />
    </a>
    .</p>
    <p style="text-align: right">
    Built with <a href="http://sphinx-doc.org/">Sphinx</a> using
    the Alabaster theme.
    </p>
