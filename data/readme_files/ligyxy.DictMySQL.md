DictMySQL
=========

PyPI page: https://pypi.python.org/pypi/dictmysql

Documentation: https://git.io/dictmysql

Introduction
------------

DictMySQL is a MySQL query builder on the top of
`PyMySQL <https://github.com/PyMySQL/PyMySQL>`__. It allows convenient
database manipulation with Python dictionary.

DictMySQL simplifies and unifies the input/output of MySQL queries, by
allowing passing values and conditions in dictionary into database. With
DictCursor, you can even have a dict-in, dict-out mysql connector.

To install:

.. code:: bash

    pip install dictmysql

Quick example:

.. code:: python

    from dictmysql import DictMySQL
    db = DictMySQL(db='occupation', host='127.0.0.1', user='root', passwd='')

    db.select(table='jobs',
              columns=['id','value'],
              where={'$OR': [{'value': {'$LIKE': 'Artist%'}}, {'id': 10}]})
    # SELECT `id`, `value` FROM `jobs` WHERE (`value` LIKE "Artist%") OR (`id` = 10);

With DictCursor:

.. code:: python

    from dictmysql import DictMySQL, cursors
    db = DictMySQL(db='occupation', host='127.0.0.1', user='root', passwd='', 
                   cursorclass=cursors.DictCursor)

    db.select(table='jobs',
              columns=['id','value'],
              limit=2)
    # returns [{u'id': 1, u'value': u'Artist'}, {u'id': 2, u'value': u'Engineer'}]

Future Works
------------

1. Full support of CRUD
2. Better documents


License
-------

DictMySQL uses the MIT license, see ``LICENSE`` file for the details.
