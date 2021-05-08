todo.py
=======

.. image:: https://secure.travis-ci.org/sigmavirus24/Todo.txt-python.png?branch=development
    :alt: Build Status

A port of the `popular todo.txt-cli project
<https://github.com/ginatrapani/todo.txt-cli>`_ from bash to python.

Dependencies
------------

This only requires GitPython_ if you want to have todo.py also manage a git
repository which tracks the related files. Running the script once will give
you the URL to download it. Please note that GitPython is written for ``git
--version`` 1.7.2+.

If you're on Windows and running the script out of cmd.exe, install 
colorama for 'termcolor' support.

.. _GitPython: https://github.com/gitpython-developers/GitPython

Installation
------------

From the repo
`````````````
If you want to install the copy locally (i.e. to a personal directory) you can
simply download one of the packages_ and run the ``install.sh`` script.

.. _packages: https://github.com/sigmavirus24/Todo.txt-python/downloads

Be sure to run ``./install.sh -h`` first. You can decide where you would like
the script installed (the default is ``$HOME/bin/``) and where you would like an
alias for the script, e.g., ``t`` or ``tpy``, written (the default is
``$HOME/.bashrc``).

Using pypi
``````````

If you would prefer a system-wide installation, you can use install ``todo.py``
from PyPi like so:

::

    $ pip install todo.py

Be aware that making a system-wide installation will not automattically create
an alias for your use. You will have to edit either your ``.bashrc`` or
``.bash_profile`` (or respective shell configuration filse) to include something
along the lines of:

::

    alias t='$HOME/bin/todo.py'

Hacking
-------

Enjoy, contribute, and feel free to clone. I'm doing this blind [1]_ as best as
possible for fun.

Important Information
---------------------

- License: GPLv3_
- Build Status: TravisCI_

.. _GPLv3: https://raw.github.com/sigmavirus24/Todo.txt-python/master/LICENSE
.. _TravisCI: http://travis-ci.org/sigmavirus24/Todo.txt-python

--------

.. [1] By blind, I mean without looking at the source of the original todo.txt-cli
    project. I'm working solely from my experiences with the script and
    experimenting with the functionality while adding things I should probably write
    as patches and send upstream... I'll wait to finish my version of the project
    first though.
