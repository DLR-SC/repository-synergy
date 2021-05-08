CodernityDB pure python, NoSQL, fast database
=============================================

CodernityDB is opensource, pure python (no 3rd party dependency), fast (really fast check Speed in documentation if you don't believe in words), multiplatform, schema-less, NoSQL_ database. It has optional support for HTTP server version (CodernityDB-HTTP), and also Python client library (CodernityDB-PyClient) that aims to be 100% compatible with embeded version.


You can call it a more advanced key-value database. With multiple key-values indexes in the same engine. Also CodernityDB supports functions that are executed inside database.


.. note::
   Bitbucket repo is a public release repo, we will sync it time to time with our main repo. But really feel free to make pull requests / forks etc from this repo.


.. image:: https://bitbucket.org/codernity/codernitydb/raw/tip/docs/CodernityDB.png
  :align: center



Visit `Codernity Labs`_ to see documentation (included in repo).

Key features
~~~~~~~~~~~~

* Native python database
* Multiple indexes
* Fast (more than 50 000 insert operations per second see Speed in documentation for details)
* Embeded mode (default) and Server (CodernityDB-HTTP), with client library (CodernityDB-PyClient) that aims to be 100% compatible with embeded one.
* Easy way to implement custom Storage


Install
~~~~~~~

Because CodernityDB is pure Python you need to perform standard installation for Python applications::

   pip install CodernityDB

or using easy_install::

   easy_install CodernityDB

or from sources::

   hg clone ssh://hg@bitbucket.org/codernity/codernitydb
   cd codernitydb
   python setup.py install


Contribute & Bugs & Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CodernityDB is one of projects developed and released by Codernity_, so you can contact us directly in any case.

Do you want to contribute? Great! Then just fork this repository on Bitbucket and do a pull request. It can't be more easy!

To fill a bug please also use Bitbucket.


.. _codernity: http://codernity.com


Support
~~~~~~~

In case of any problems, feature request you can also contact us directly.

Do you want customized version of CodernityDB ? No problem, just contact us.



.. _NoSQL: http://en.wikipedia.org/wiki/NoSQL
.. _KnockoutJS: http://knockoutjs.com/
.. _Codernity Labs: http://labs.codernity.com/codernitydb
