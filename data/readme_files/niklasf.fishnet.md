fishnet: distributed Stockfish analysis for lichess.org
=======================================================

.. image:: https://badge.fury.io/py/fishnet.svg
    :target: https://pypi.python.org/pypi/fishnet

.. image:: https://travis-ci.org/niklasf/fishnet.svg?branch=master
    :target: https://travis-ci.org/niklasf/fishnet

.. image:: https://coveralls.io/repos/github/niklasf/fishnet/badge.svg?branch=master
    :target: https://coveralls.io/github/niklasf/fishnet?branch=master

Installation
------------

1. Request your personal fishnet key: https://lichess.org/get-fishnet
2. Install the fishnet client.

   **Via pip**

   To install or upgrade to the latest version do:

   ::

       pip install --upgrade --user fishnet

   Example usage:

   ::

       python -m fishnet --auto-update

   Optional: Generate a systemd service file:

   ::

       python -m fishnet systemd

   **Via Docker**

   There is a `Docker container <https://hub.docker.com/r/mklemenz/fishnet/>`_
   courtesy of `@mklemenz <https://github.com/mklemenz>`_. For example you can
   simply do:

   ::

       docker run mklemenz/fishnet --key MY_APIKEY --auto-update

lichess.org custom Stockfish
----------------------------

fishnet is using
`lichess.org custom Stockfish <https://github.com/niklasf/Stockfish/tree/fishnet>`__
by `@ddugovic, @ianfab et al <https://github.com/ddugovic/Stockfish>`_.

You can build Stockfish yourself (for example with ``./build-stockfish.sh``)
and provide the path using ``python -m fishnet --stockfish-command``. Otherwise
a precompiled binary will be downloaded for you.

Overview
--------

.. image:: https://raw.githubusercontent.com/niklasf/fishnet/master/doc/sequence-diagram.png

See `protocol.md <https://github.com/niklasf/fishnet/blob/master/doc/protocol.md>`_ for details.

License
-------

fishnet is licensed under the GPLv3+ license. See LICENSE.txt for the full
license text.
