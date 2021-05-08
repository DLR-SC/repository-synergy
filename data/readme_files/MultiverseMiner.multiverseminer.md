===============================
Multiverse Miner
===============================

Multiverse Miner

Beta signup and project structure example for multiverse miner game.

Quickstart
----------

::

    git clone https://github.com/nikola-k/multiverseminer
    cd multiverseminer
    pip install -r requirements/dev.txt
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``MULTIVERSEMINER_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commmands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.