=================
 Welcome to Owyl!
=================

You have Pyglet.  You've got Rabbyt.  But who do your sprites go to
for advice?  Owyl, of course.


Goals
=====

The goal of Owyl: provide a fast and flexible Behavior Tree library
implemented in python. Owyl trees use nested generators to iterate
through your behaviors. The root of the tree always works just like a
normal python iterator. If you know how to work with iterators, you
know how to work with an Owyl tree. Because Owyl is small and behavior
trees are easy to grasp, it's easy to control and extend your AI
behaviors.


Trees as Iterators
==================

Trees as iterators give you total control over how a behavior tree
integrates with your code: use a for loop, a list comprehension, a
generator expression, or manual calls to tree.next(). Run the tree one
step, five, or fifty with every frame.


Extending
=========

Writing new behaviors is simple and easy (and soon to be
documented!). Any object that corresponds to python's iterator
interface and a few simple rules for yielded values will work. Owyl's
core behaviors are written as simple generator functions.


More information
================

For more information on Behavior Trees, see
[http://aigamedev.com/hierarchical-logic these articles]. Remember: AI
isn't about math, it's about getting things done.

Owyl has been tested on python 2.5. It will probably work on 2.6. It
definitely WILL NOT work on 2.4 without adaptation. Please let me know
if you have any trouble with it.

David Eyk
owyl@eykd.net


Installation
============

See INSTALL.


Documentation
=============

API documentation can be found at <http://worlds.eykd.net/owyl/api/>.

For more information about Owyl, please visit the project site at
<http://code.google.com/p/owyl/>.


Problems? Questions?
====================

If you run into trouble, or have a question, visit the discussion
group at <http://groups.google.com/group/owyl-discuss/>.


