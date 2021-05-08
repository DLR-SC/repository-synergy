======
vexbot
======

|readthedocs| |codeclimate|

.. |readthedocs| image:: https://readthedocs.org/projects/vexbot/badge/?version=latest
  :target: http://vexbot.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/c17129f65b11dfef34c0/maintainability.svg
  :target: https://codeclimate.com/github/benhoff/vexbot/badges/gpa.svg
  :alt: Climate Status


Pluggable bot

Under development. Very useable but currently not feature complete.

Requirements
------------

Requires python 3.5 for asyncio and only runs on linux.

If you're a python developer, you can probably get this to run on not linux.

Installation
------------

You will need an active DBus user session bus. Depending on your distro, you might already have one (Arch linux, for example).

For Ubuntu:

.. code-block:: bash

  $ apt-get install dbus-user-session python3-gi python3-dev python3-pip build-essential

For everyone:

.. code-block:: bash

  $ python3 -m venv <DIR>

.. code-block:: bash

  $ source <DIR>/bin/activate

.. code-block:: bash

  $ ln -s /usr/lib/python3/dist-packages/gi <DIR>/lib/python3.5/site-packages/

.. code-block:: bash

  $ pip install vexbot[process_manager]

Configuring
-----------

Make sure your virtual environment is activated. Then run:

.. code-block:: bash

  $ vexbot_generate_certificates

.. code-block:: bash

 $ vexbot_generate_unit_file

.. code-block:: bash

 $ systemctl --user daemon-reload

Your bot is ready to run!

Running
-------

.. code-block:: bash

 $ systemctl --user start vexbot
 
Or

.. code-block:: bash

  $ vexbot_robot

Please note that vexbot has a client/server architecture. The above commands will launch the server. To launch the command line client:

.. code-block:: bash

  $ vexbot

Exit the command line client by typing `!exit` or using `ctl+D`.
