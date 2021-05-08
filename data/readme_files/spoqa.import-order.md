import-order
==============

.. image:: https://pypip.in/wheel/import_order/badge.svg
    :target: https://pypi.python.org/pypi/import_order/
    :alt: Wheel Status

.. image:: https://pypip.in/py_versions/import_order/badge.svg
   :target: https://pypi.python.org/pypi/import_order/
   :alt: Supported Python versions

.. image:: https://badge.fury.io/py/import-order.svg
    :target: https://badge.fury.io/py/import-order
    :alt: pypi packages

.. image:: https://travis-ci.org/spoqa/import-order.svg
    :target: https://travis-ci.org/spoqa/import-order
    :alt: travis-ci status

CLI that check the ordering of imports. ordering follow a below rules.

1. Module order: ``__future__`` , standard libraries, site-packages, local.
2. ``CONSTANT_NAMES`` must be the first.
3. ``ClassNames`` must be the second.
4. Rest must be in alphabetical order.


Requirements
--------------

- Python 2.7.x or Python 3.3+


How to install
----------------

Via pip

.. code-block::

   $ pip install -U import-order

Or clone source code from repository and install it.

.. code-block::

   $ git clone https://github.com/spoqa/import-order.git
   $ cd import_order
   $ python setup.py install # or pip install .


How to use
-----------

Use ``import-order`` to check your python codes. If you want to check your
local package named ``foo`` in root directory of package.

.. code-block::

   $ import-order foo

If you check your directory ``bar`` with local packages ( ``foo`` , ``baz`` ).

.. code-block::

   $ import-order foo ./bar baz

Or you can check your directory ``bar`` , file ``some.py`` without
local packages (if ``--only-file`` is missing, it will raise ``ValueError`` ).

.. code-block::

   $ import-order --only-file ./bar some.py

For more information, look around help command.

.. code-block::

   $ import-order --help

When you ignore order on purpose, simply add ``# no import order`` at the
import statement.

.. code-block:: python

   from foo.bar import b, a, c  # no import order


Author and license
-------------------

import-order is maintained by Spoqa_, and licensed
under GPL3_ or later.


.. _GPL3: https://www.gnu.org/licenses/gpl.txt
.. _Spoqa: http://http://www.spoqa.com/
