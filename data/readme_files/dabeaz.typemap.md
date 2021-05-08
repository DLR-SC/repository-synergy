Typemap - The Annotator (TM)
============================

Typemap is a module that allows you to apply Python type annotations
by name, using simple "type quantifier" operators.  Here's a simple
example::

    # sample1.py

    ᗄx: int
    ᗄy: int

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y 

    import typemap; typemap()

In this case, the "for all" type quantifier attaches the given type
annotation to all occurrences of a given name.  You can see this
if you import your module and look at the annotations::

    >>> import sample1
    >>> sample1.add.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>}
    >>> sample1.sub.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>}
    >>> 

Sweet!  You can also apply typemaps to name prefixes using
the "there exists" type quantifier.  If there exists a
given prefix, then it gets a type annotation.  For example::

    # sample2.py

    Ǝi: int

    def add(ix, iy):
        return ix + iy

    def sub(ix, iy):
        return ix - iy

    import typemap; typemap()

It's one less line of typing (sic) and it still works::

    >>> import sample2
    >>> sample2.add.__annotations__
    {'ix': <class 'int'>, 'iy': <class 'int'>}
    >>>

Naturally, you can also use typemaps in class definitions::

    # sample3.py

    class Spam:
        ᗄx: int
        ᗄy: int
        def __init__(self, x,  y):
            self.x = x
            self.y = y

        def yow(self, x):
            pass

    import typemap; typemap()

Typemaps are inherited.  Thus, this class gets the same typemaps as
the parent class::

    class Child(Spam):
        def bar(self, x, y):
            pass

    import typemap; typemap()

Look at some of the annotations::

    >>> import sample3
    >>> sample3.Spam.__init__.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>}
    >>> sample3.Child.bar.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>}
    >>>

See the file ``sample.py`` for more examples.

FAQ
---

**How do you type ᗄ and Ǝ?**

The ᗄ character is U+15C4. The Ǝ character is U+018E.
The easiest way to get these is probably to cut and paste them out
of a document that shows them displayed correctly.   If you absolutely must, you
can use ``all_`` and ``prefix_`` as substitutes.  However, keep in mind that
good type annotations should be hard to type. 

**Can you use the mathematical characters ∀ (U+2200) and ∃ (U+2203)?**

Yes, but ``typemap`` needs to already be imported (from elsewhere) and
you need to use the special "typemap" source encoding.  For example::

    # somefile.py
    # -*- coding: typemap -*-

    # Define some typemaps
    ∀x: int
    ∀y: int
    ...

    import typemap; typemap()

**Why do the special characters look garbled or incorrect?**

Maybe your fonts aren't advanced enough to use typemap. 

**Why do you have to call ``import typemap; typemap()`` at the bottom?**

Reasons.  

**Are there any unit tests?**

No, not tests, types.

**Is there any more documentation?**

No, not documentation, types.

**How do you deploy typemap in production?**

Rather than calling overt attention to its use, the best practice is
to copy the ``typemap.py`` file into your own project and to quietly
use it internally. No need to add an additional dependency to your
requirements file.

**WHY?**

Is it not obvious?

**Who?**

Typemap - The Annotator (TM) is the brainchild of David Beazley (@dabeaz) 
who disavows all knowledge of it and who should probably be working on
his book instead.

**P.S.**

You should come take a `course <https://www.dabeaz.com/courses.html>`_.