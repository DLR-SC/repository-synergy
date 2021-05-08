rst2epub2
===============

This code consists of two tools:

* a binary, ``rst2epub``, to convert rst files into epub2 compliant
  files (ie that pass epub check, can be loaded into Apple, BN, Kobo,
  etc. Or converted to mobi and thrown into AMZN)
* a library, ``epublib``, that has the ability to programatically
  create epub files. See the ``test`` function in ``epublib/epub.py``
  for more details. There is experimental support for KF8 fixed layout
  as well.


Install
============

running::

  make dev

will create a virtualenv in ``env``. The ``rst2epub.py`` binary will be
located in the ``env/bin/`` directory.

Known to work on linux systems. (Should work on apple, cygwin, MS with
some futzing).

Docs
======

There are a few rst tweaks to support features such as metadata. See
the sample doc for examples of a complete book and how to generate
both epub and mobi files.

Feel free to interact via github for support.

Thanks
========

timtambin@gmail.com wrote the original epublib and hosted it on google
code. I've tweaked (pep8'd) it and imported into github.
