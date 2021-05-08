Safe
====

Is your password safe? **Safe** will check the password strength for you.

.. image:: https://travis-ci.org/lepture/safe.png?branch=master
   :target: https://travis-ci.org/lepture/safe

How it works
------------

**Safe** will check if the password has a simple pattern, for instance:

1. password is in the order on your QWERT keyboards.
2. password is simple alphabet step by step, such as: abcd, 1357

**Safe** will check if the password is a common used password.
Many thanks to Mark Burnett for the great work on `10000 Top Passwords <https://xato.net/passwords/more-top-worst-passwords/>`_.

**Safe** will check if the password has mixed number, alphabet, marks.

Installation
------------

Install Safe with pip::

    $ pip install Safe

If pip is not available, try easy_install::

    $ easy_install Safe

Usage
-----

It's very simple to check the strength of a password::

    >>> import safe
    >>> safe.check(1)
    terrible
    >>> safe.check('password')
    simple
    >>> safe.check('is.safe.password')
    medium
    >>> safe.check('x*V-92Ba')
    strong
    >>> strength = safe.check('x*V-92Ba')
    >>> bool(strength)
    True
    >>> repr(strength)
    'strong'
    >>> str(strength)
    'password is perfect'
    >>> strength.valid
    True
    >>> strength.strength
    'strong'
    >>> strength.message
    'password is perfect'


Environ Variables
-----------------

1. **PYTHON_SAFE_WORDS_CACHE**: cache words in this file, default is a tempfile
2. **PYTHON_SAFE_WORDS_FILE**: words vocabulary file, default is the 10k top passwords

Other Implementations
---------------------

1. **JavaScript**: `lepture/safe.js <https://github.com/lepture/safe.js>`_
