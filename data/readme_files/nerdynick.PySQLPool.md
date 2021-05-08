=================
What is PySQLPool
=================

PySQLPool is at the heart a MySQL Connection Pooling library for use with the MySQLDB Python bindings.

Part of the PySQLPool is the MySQL Query class that handles all the thread safe connection locking, 
connection management in association with the Connection Manager, and cursor management. 
Leaving all the work you have to do in your code is write MySQL Queries. Saving you hours of work.

============
Installation
============

Linux/Mac OS X::

    cd PySQLPool
    python setup.py build
    sudo python setup.py install
    
    - or -
    
    sudo easy_install PySQLPool

Windows::

    cd PySQLPool
    python setup.py build 
    python setup.py install 

====================
Documentation
====================

The documentation for PySQLPool is constructed using Sphinx. You can view the raw text files in
doc/*, or if you wish to view an html version in doc/html/* or via the web at 
http://packages.python.org/PySQLPool/

=======
License
=======

PySQLPool is licensed under the LGPL. You can find out more in the included LICENSE file.

=================================================
Got a Bug, Question, or Idea to Improve PySQLPool
=================================================

Bugs can be submitted at https://bugs.launchpad.net/pysqlpool
Blueprints/Ideas can be submitted at https://blueprints.launchpad.net/pysqlpool
Questions/Answers can be submitted at https://answers.edge.launchpad.net/pysqlpool

=====
Links
=====

Homepages: 

- https://github.com/nerdynick/PySQLPool (Primary Site)
- http://code.google.com/p/pysqlpool/ (Legacy Site)
- https://launchpad.net/pysqlpool/ (Soon to be Legacy Site)
          
Documentation:
 
- http://packages.python.org/PySQLPool/


===========
Development
===========

Contributing
============

If you would like to contribute back to PySQLPool. Fill free to fork a branch and ask for a pull, or just submit me a patch. 
Eather via 'git format-patch' if you want true tracked credit or just a normal diff patch.


Basic Folder Structure
======================

/doc           - RST based documentation
/src           - Base Source Code
/src/PySQLPool - Actual Source Code
/test          - Unittest via PyUnit
