Git-play
========

Git-play is a custom git command for deploying an application server very easily from a remote git repository. It checks the remote git repository every minute and if something has changed, it will restart the application server automatically.


Installation
------------

You can simply install git-play from PyPI by using ``pip`` or ``easy_install``:

.. code-block:: console

   $ pip install git-play

 
Getting started
---------------

Git-play is made for people who hate complicated configurations, thus basically it doesn't require you to do much except for ``.git-play.yml``.


Configuring your git-play deployment with ``.git-play.yml``
-----------------------------------------------------------

Git-play uses the ``.git-play.yml`` file in the root of your repository to configure how you want your application to be executed.
``.git-play.yml`` file has three parts: ``app``, ``setup``, ``teardown``.

For your convenience, there are several examples of ``.git-play.yml`` file.

Django
------

.. code-block:: yaml

   app:
     workdir: ./mysite
     respawn: yes
     exec: python manage.py runserver

   setup:
     - pip install -r requirements.txt  
     - cd mysite
     - python manage.py syncdb

   teardown:
     - echo "The server is going down for maintanance..."


Express
-------

.. code-block:: yaml

   app:
     respawn: yes
     env:
      PORT: 80
     exec: node app.js

   setup:
     - npm install

   teardown:
     - echo "The server is going down for maintanance..."


Spray and pray!
---------------

Lastly, all you have to do is simply type the following in your terminal:

.. code-block:: console

   $ git play http://github.com/foo/bar --remote origin --branch master
   Spawned!

For an existing repository, type the following:

.. code-block:: console

   $ git play bar -r origin -b master
   Spawned! 

.. code-block:: console 

   $ ls -F
   bar/
   $ cd bar 
   $ git play 
   Spawned!

Contributing
------------
Just fork and request pulls. Any help or feedback is appreciated.
