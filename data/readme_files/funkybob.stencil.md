stencil
=======

A minimalist template engine for Python3

The goal of Stencil is to provide just enough of a template engine in a single file.

Currently weighs in at 550 LoC (414 according to sloccount).

Quick Start
-----------

1. Make a directory for our templates:

   .. code-block:: bash

      $ mkdir tmpl

2. Create a simple template:

   .. code-block:: html

      Good morning, {{ name }}!

3. Write a script to use it

   .. code-block:: python

      import stencil

      loader = stencil.TemplateLoader(['tmpl/'])

      t = loader['index.html']
      c = stencil.Context({'name': 'Ruprect'})

      print t.render(c)
      # Should output "Good morning, Ruprect!"


Python support
--------------

As of stencil v4, there is a new expression syntax that is not backward
compatible.

As of stencil v2.1, only Python 3.6+ is supported.
As of stencil v2, only Python 3.4+ is supported.

Stencil 1.2.3 is the last stable Python 2.7 version.

See the `documentation <https://stencil-templates.readthedocs.io/en/latest/>`_ to see more details.
