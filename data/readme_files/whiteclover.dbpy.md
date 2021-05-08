dbpy
#####



dbpy is database abstration layer wrote by python. The design is inspired by `webpy db <https://github.com/webpy/webpy>`_ and `drupal database <https://www.drupal.org/developing/api/database>`_ . If like the simple db abstration layer like ``tornado db`` or ``webpy db``, it is worth to try.


`中文|chinese <https://github.com/thomashuang/dbpy/blob/master/README_CN.rst>`_

changes
==========

#. Add pymysql adapter



Install the extension with the following command::

    $ easy_install pymysql

or alternatively if you have pip installed::


    $ pip install pymysql

Featues
================

#. silmple and flexible
#. graceful and useful sql query builder.
#. thread-safe connection pool
#. supports read/write master-slave mode
#. supports transaction

The Projects use dbpy
======================


`Lilac (Distributed Scheduler Task System) <https://github.com/thomashuang/Lilac>`_

.. contents::
    :depth: 4




Install
==============

Install the extension with the following command::

    $ easy_install dbpy

or alternatively if you have pip installed::


    $ pip install dbpy


or clone it form github then run the command in shell:

.. code-block:: bash

    cd db # the path to the project
    python setup.py install

Development
===========

Fork or download it, then run:

.. code-block:: bash 

    cd db # the path to the project
    python setup.py develop



Compatibility
=============

Built and tested under Python 2.7+


DB API
========


Have a look:

.. code-block:: python

    config = {
            'passwd': 'test',
            'user': 'test',
            'host': 'localhost',
            'db': 'test',
            'max_idle' : 5*60
        }

    db.setup(config,  minconn=5, maxconn=10,  
        adapter='mysql', key='default', slave=False)

    db.execute('show tables')



setup
---------

:config: the connection basic config, the all of arguements of MySQLDB#connect is acceptable。 the ``max_idle`` is the connect timeout setting that is used to reconnection when connection is timeout, default is 10 seconds.
:minconn: the minimum connections for the connection pool, default is 5.
:maxconn: the maximum connections for the connection pool, default is 10.
:adapter: the database driver adapter name, currently supports mysql (MySQLdb, pymysql) only.
:key: the database idenfify for database,  default database is "default"
:slave: if set to true, the database will be register as a slave database. make sure you setup a master firstly.


.. code-block:: python

    config = {
            'passwd': 'test',
            'user': 'test',
            'host': 'localhost',
            'db': 'test',
            'max_idle' : 5*60
        }

    db.setup(config, key='test')
    config['host'] = 'test.slave'
    # set a slave, and now the master can only to write
    db.setup(config, key='test', slave=True) 

    config['host'] = 'test.slave2'
    # add more slave for 'test'
    db.setup(config, key='test', slave=True)


    config['host'] = 'host2'
    config['db'] = 'social'
    # set another database
    db.setup(config, key='social', slave=True)

query
-------



query api is used for reading database operation, like select..., show tables, if you wanna update your database please use execute api.

query(sql, args=None, many=None, as_dict=False, key='default'):

:sql: the raw sql
:args: the args for sql arguement to prepare execute.
:many: when set to a greater zero integer, it will use fetchmany then yield return a generator, otherwise a list.
:as_dict: when set to true, query api will return the database result as dict row, otherwise tuple row.
:key: the idenfify of database.

.. code-block:: python

    print db.query('SELECT 1')
    # > ((1L,),)

    # use social db
    print db.query('SELECT 1', key='social')
    # > ((1L,),)

    print db.query('SELECT * FROM users WHERE uid=%s and name=%s', (1, 'user_1'))
    # > ((1L, u'user_1'),)

    # Wanna return dict row
    print db.query('SELECT * FROM users WHERE uid=%s and name=%s', 
                (1, 'user_1'), as_dict=True)
    # > ({'uid': 1L, 'name': u'user_1'},)

    # Use fetchmany(many) then yeild, Return generator
    res = db.query('SELECT * FROM users WHERE uid=%s and name=%s', 
                    (1, 'user_1'), many=5, as_dict=True)
    print res
    print res.next()
    # > <generator object _yield at 0x7f818f4b6820>
    # > {'uid': 1L, 'name': u'user_1'}


execute
--------

the api is used for writing database operation, like insert, update, delete.. if you wanna read query your database please use query api.

execute(sql, args=None, key='default'):


:sql: the raw sql
:args: the args for sql arguement to prepare execute.
:key: the idenfify of database.


Return::

  it returns last_insert_id when sql is insert statement, otherwise rowcount

.. code-block:: python
    
    db.execute('DROP TABLE IF EXISTS `users`')
    db.execute("""CREATE TABLE `users` (
             `uid` int(10) unsigned NOT NULL AUTO_INCREMENT,
            `name` varchar(20) NOT NULL,
            PRIMARY KEY (`uid`))""")
    
    # when inset mutil-values，the api will call executemany
    db.execute('INSERT INTO users VALUES(%s, %s)', [(10, 'execute_test'), (9, 'execute_test')])
    # > 9
    db.execute('DELETE FROM users WHERE name=%s', ('execute_test',))
    # > 2


    # use social db
    db.execute('delete from events where created_at<%s', (expired, ), key='social')
    # > 10

select
-----------

the api is used for select sql database query.

select(table, key='default'):

:table: the table name
:key: the idenfify of database 

select all
~~~~~~~~~~~~~~~~

.. code-block:: python

    db.select('users')
    # > SELECT * FROM `users`

specific columns
~~~~~~~~~~~~~~~~~

.. code-block:: python

    db.select('users').fields('uid', 'name')
    # > SELECT `uid`, `name` FROM `users`


execute
~~~~~~~~~~~~~~~~

when you already build your sql, try execute api to fetch your database result.

execute(many=None, as_dict=False):

:many: when set to a greater zero integer, it will use fetchmany then yield return a generator, otherwise a list.
:as_dict: when set to true, query api will return the database result as dict row, otherwise tuple row.

.. code-block:: python

    q = db.select('users').fields('uid', 'name')
    res = q.execute()
    print res
    # > ((1L, u'user_1'), (2L, u'user_2'), (3L, u'user_3'), (4L, u'user_4'), (5L, None))

    res = q.execute(many=2, as_dict=True)
    print res
    print res.next()
    # > <generator object _yield at 0x7f835825e820>
    # > {'uid': 1L, 'name': u'user_1'}


Condition
~~~~~~~~~~~

It is time to try more complex select query.

condition(field, value=None, operator=None):

:field: the field of table 
:value: the value of field, defaul is None ("field is null")
:operator: the where operator like BETWEEN, IN, NOT IN, EXISTS, NOT EXISTS, IS NULL, IS NOT NULL, LIKE, NOT LIKE, =, <, >, >=, <=, <> and so on.


simple 
^^^^^^^^^^^^^^^^

.. code-block:: python

    db.select('users').condition('uid', 1) # condition('uid', 1, '=')
    # > SELECT * FROM `users`
    # > WHERE  `uid` = %s 


in 
^^^^^^^^^^^^^^^^

.. code-block:: python


    db.select('users').condition('uid', (1, 3)) # condition('uid', [1, 3]) 一样
    # > SELECT * FROM `users`
    # > WHERE  `uid` IN  (%s, %s) 

between 
^^^^^^^^^^^^^^^^

.. code-block:: python

    db.select('users').condition('uid', (1, 3), 'between')
    # > SELECT * FROM `users`
    # > WHERE  `uid` BETWEEN %s AND %s 


multi condition
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    db.select('users').condition('uid', 1).condition('name', 'blabla')
    # > SELECT * FROM `users`
    # > WHERE  `uid` = %s AND `name` = %s 

or condition
^^^^^^^^^^^^^^

.. code-block:: python

    or_cond = db.or_().condition('uid', 1).condition('name', 'blabla')
    db.select('users').condition(or_cond).condition('uid', 1, '<>')
    # > SELECT * FROM `users`
    # > WHERE  ( `uid` = %s OR `name` = %s ) AND `uid` <> %s 



order by
~~~~~~~~~

.. code-block:: python

    db.select('users').order_by('name')
    # > SELECT * FROM `users`
    # > ORDER BY `name`

    db.select('users').order_by('name', 'DESC')
    # > SELECT * FROM `users`
    # > ORDER BY `name` DESC

    db.select('users').order_by('name', 'DESC').order_by('uid')
    # > SELECT * FROM `users`
    # > ORDER BY `name` DESC, `uid`



distinct
~~~~~~~~~

.. code-block:: python

    db.select('users').distinct().condition('uid', 1)
    # > SELECT DISTINCT * FROM `users`
    # > WHERE  `uid` = %s 

    db.select('users').fields('uid', 'name').distinct().condition('uid', 1)
    # > SELECT DISTINCT `uid`, `name` FROM `users`
    # > WHERE  `uid` = %s 


group by
~~~~~~~~~

.. code-block:: python

    db.select('users').group_by('name', 'uid')
    # > SELECT * FROM `users`
    # > GROUP BY `name`, `uid`


limit and offset
~~~~~~~~~~~~~~~~~

.. code-block:: python

    db.select('users').limit(2).offset(5)
    # > SELECT * FROM `users`
    # > LIMIT 2 OFFSET 5

null condition
~~~~~~~~~~~~~~~

.. code-block:: python

    db.select('users').is_null('name').condition('uid', 5)
    # > SELECT * FROM `users`
    # > WHERE  `name` IS NULL  AND `uid` = %s 

    db.select('users').is_not_null('name').condition('uid', 5)
    # > SELECT * FROM `users`
    # > WHERE  `name` IS NOT NULL  AND `uid` = %s 

    db.select('users').condition('name', None)
    # > SELECT * FROM `users`
    # > WHERE  `name` IS NULL  


complex conditions
-------------------

using db.and_(), db.or_(), we can build complex where conditions:

.. code-block:: python

    or_cond = db.or_().condition('field1', 1).condition('field2', 'blabla')
    and_cond = db.and_().condition('field3', 'what').condition('field4', 'then?')
    print db.select('table_name').condition(or_cond).condition(and_cond)

    # > SELECT * FROM `table_name`
    # > WHERE  ( `field1` = %s OR `field2` = %s ) AND ( `field3` = %s AND `field4` = %s ) 

expr
------------

if you wanna use the aggregate functions like sum, count, please use ``erpr`` :

.. code-block:: python

    from  db import expr

    db.select('users').fields(expr('count(*)'))
    # > SELECT count(*) FROM `users`

    db.select('users').fields(expr('count(uid)', 'total'))
    # > SELECT count(uid) AS `total` FROM `users`



insert
-----------

The ``insert`` api is used for building insert into sql statement.

insert(table, key='default'):

:table: the table name
:key: the idenfify of database 

.. code-block:: python

    q = db.insert('users').values((10, 'test_insert'))
    # > INSERT INTO `users` VALUES(%s, %s)
    print q._values
    # > [(10, 'test_insert')]


    q = db.insert('users').fields('name').values({'name': 'insert_1'}).values(('insert_2',))
    # > INSERT INTO `users` (`name`) VALUES(%s)
    print q._values
    # > [('insert_1',), ('insert_2',)]


When you use ``execute`` api to get result, it will reutrn the ``last insert id``：

.. code-block:: python
    
    
    print q.execute()
    # > 2



update
-----------

The ``update`` api is used for building update sql statement.

update(table, key='default'):

:table: the table name
:key: the idenfify of database 


mset and set：

:mset: the value must be dict tpye, that sets mutil-fileds at once time.
:set(column, value): set one field one time.

the where conditions please see `select`_ for more information.


.. code-block:: python
    
    
    db.update('users').mset({'name':None, 'uid' : 12}).condition('name','user_1')
    # > UPDATE `users` SET `name` = %s, `uid` = %s WHERE  `name` = %s 

    q = (db.update('users').set('name', 'update_test').set('uid', 12)
        .condition('name', 'user_2').condition('uid', 2)) # .execute()
    print q.to_sql()
    # > UPDATE `users` SET `name` = %s, `uid` = %s WHERE  `name` = %s AND `uid` = %s 
  


When you use ``execute`` api to get result, it will reutrn the ``rowcount``：


.. code-block:: python
    
    
    print q.execute()
    # > 2

limit
~~~~~~~~~



You can use limit api to lim the quantity of update.


.. code-block:: python
    
    db.update('users').mset({'name':None, 'uid' : 12}).condition('name','user_1').limit(5)
    # > UPDATE `users` SET `name` = %s, `uid` = %s WHERE  `name` = %s  LIMIT 5

delete
-----------


The ``delete`` api is used for building DELETE FROM sql statement.

delete(table, key='default'):

:table: the table name
:key: the idenfify of database 

the where conditions please see `select`_ for more information.

.. code-block:: python
    
    db.delete('users').condition('name','user_1')
    # > DELETE FROM `users` WHERE  `name` = %s 
	
When you use ``execute`` api to get result, it will reutrn the ``rowcount``：

.. code-block:: python
    
    
    print q.execute()
    # > 2


to_sql and str
---------------------

you can use to_sql or __str__ method to the objects of  ``select``, ``insert``, ``update``, ``delete`` to print the sql you build.


.. code-block:: python
    

    q = (db.update('users').set('name', 'update_test').set('uid', 12)
            .condition('name', 'user_2').condition('uid', 2))
    print q.to_sql()
    print q
    # > UPDATE `users` SET `name` = %s, `uid` = %s WHERE  `name` = %s AND `uid` = %s 


transaction
------------

transaction(table, key='default'):

:table: the table name
:key: the idenfify of database 


The simple transaction done all or do nothing, you cann't set savepoint. 



.. code-block:: python
    

    # with context
    with db.transaction() as t:
        t.delete('users').condition('uid', 1).execute()
        (t.update('users').mset({'name':None, 'uid' : 12})
            .condition('name','user_1').execute())


    # the normal way
    t = db.transaction()
    t.begin()
    t.delete('users').condition('uid', 1).execute()
    (t.update('users').mset({'name':None, 'uid' : 12})
        .condition('name','user_1').execute())

    #if failed will rollback
    t.commit()

.. note:: when uses begin must be combine with commit，otherwise the connection will not return connection pool.suggets to use ``with context``


simple orm
-----------

the orm demo  `samples <https://github.com/thomashuang/dbpy/blob/master/samples>`_

.. code-block:: python
    
    import model
    from orm import Backend
    import db

    db.setup({ 'host': 'localhost', 'user': 'test', 'passwd': 'test', 'db': 'blog'})


    user = Backend('user').find_by_username('username')
    if user and user.check('password'):
        print 'auth'

    user = model.User('username', 'email', 'real_name', 'password', 
            'bio', 'status', 'role')
    if Backend('user').create(user):
        print 'fine'

    user = Backend('user').find(12)
    user.real_name = 'blablabla....'
    if Backend('user').save(user):
        print 'user saved'

    if Backend('user').delete(user):
        print 'delete user failed'


    post = model.Post('title', 'slug', 'description', 'html', 'css', 'js', 
            'category', 'status', 'comments', 'author')
    if not Backend('post').create(post):
        print 'created failed'

Future
--------


Personal idea:

#. add ``join``  for select api 
#. add a schema class for creating or changing table.
#. add some api for mysql individual sql like ``replace`` or ``duplicate update``
#. improve connection pool.


LICENSE
=======

    Copyright (C) 2014-2015 Thomas Huang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 2 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

