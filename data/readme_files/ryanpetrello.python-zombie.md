A Python driver for `Zombie.js <http://zombie.labnotes.org/>`_, a headless browser
powered by `node.js <http://nodejs.org/>`_. ::

    from zombie import Browser
    b = Browser()
    b.visit('http://pypi.python.org/').fill('term', 'Zombie').pressButton('submit')
    assert "A Python driver for Zombie.js" in b.body.text

    brew install node
    curl https://www.npmjs.org/install.sh | sh
    npm install zombie

.. _travis: http://travis-ci.org/ryanpetrello/python-zombie
.. |travis| image:: https://secure.travis-ci.org/ryanpetrello/python-zombie.png

|travis|_

Installing
==========
To install Zombie from PyPI::

    $ pip install zombie

...or, for the latest (unstable) tip::

    $ git clone https://github.com/ryanpetrello/python-zombie -b next
    $ cd python-zombie && python setup.py develop

Development
===========

Source hosted at `GitHub <https://github.com/ryanpetrello/python-zombie>`_.
Report issues and feature requests on `GitHub
Issues <https://github.com/ryanpetrello/python-zombie/issues>`_.

To fix bugs or add features to zombie, a GitHub account is required.

The general practice for contributing is to `fork zombie
<https://help.github.com/articles/fork-a-repo>`_ and make changes in the
``next`` branch. When you're finished, `send a pull request
<https://help.github.com/articles/using-pull-requests>`_ and your patch will
be reviewed.

Tests require ``tox`` and can be run with ``python setup.py test``.

All contributions must:

* Include accompanying tests.
* Include API documentation if new features or API methods are changed/added.
* Be (generally) compliant with PEP8.  One exception is that (for consistency,
  and to demonstrate their analogous nature) API methods on
  ``zombie.Browser`` should follow the camel case formatting set forth in
  the zombie.js API (e.g., ``Browser.pressButton``, not
  ``Browser.press_button``).
* Not break the tests or build. Before issuing a pull request, ensure that all
  tests still pass across multiple versions of Python.
* Add your name to the (bottom of the) ``AUTHORS`` file.
