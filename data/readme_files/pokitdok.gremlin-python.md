.. image:: https://travis-ci.org/pokitdok/gremlin-python.svg?branch=master
    :target: https://travis-ci.org/pokitdok/gremlin-python


gremlin-python
==============

gremlin-python (gremthon) allows you to use Python syntax when traversing property graphs...

Quick Start
-----------

Take a test drive locally (expects curl, java, and unzip commands to be available):

.. code-block:: bash

    $ ./test_drive/setup.sh && ./test_drive/run.sh


This will download the necessary components, start titan, and run the rexster console with
python scripting support enabled.

If you prefer to use Docker, you can pull the pokitdok/gremlin-python-test-drive container and run it
to quickly evaluate gremlin-python:

.. code-block:: bash

    $ docker run -i -t pokitdok/gremlin-python-test-drive


Compile, test and package the gremlin-python jar:

.. code-block:: bash

    $ mvn clean package

rexster
-------

To utilize Python syntax from within a rexster console, you'll need to drop in a couple of jar files
and edit some xml configuration.

Edit conf/rexster-cassandra-es.xml (or the configuration file you're using) in your titan distribution directory to include:

.. code-block:: xml

        <script-engine>
            <name>gremlin-python</name>
        </script-engine>


See the rexster-test-drive.xml file for an example configuration that's used when you take a test drive.

You'll also need to put the files gremlin-python-{version}.jar and jython-standalone-{version}.jar
into your titan lib directory.   gremlin-python has been tested with jython-standalone-2.7.0.jar.
You can find a gremlin-python jar file for each release at https://github.com/pokitdok/gremlin-python/releases
The jython standalone jar can be found at http://www.jython.org/downloads.html

After (re)starting titan + rexster, you should see python available in your rexster console. We also included a sample graph to explore.

.. code-block:: bash

    $ ./bin/rexster-console.sh -l python
            (l_(l
    (_______( 0 0
    (        (-Y-) <woof>
    l l-----l l
    l l,,   l l,,
    opening session [127.0.0.1:8184]
    ?h for help

    rexster[python]> g = rexster.getGraph("graph")
    ==>null
    rexster[python]> g.V.has('vertex_type','doctor').count()
    ==>25
    rexster[python]> g.V.has('vertex_type','consumer').count()
    ==>1000
    rexster[python]> g.E.has('edge_type','viewed').count()
    ==>3470
    rexster[python]> g.E.has('edge_type','scheduled_with').count()
    ==>1000

Exploring the properties of this graph a bit more... (note: the people in this example are fake)

.. code-block:: bash

    rexster[python]> list(g.V.has('vertex_type','doctor').map())[0]
    ==>last_name=Moen
    ==>first_name=Shana
    ==>full_name=Dr. Shana Moen
    ==>specialty=family doctor
    ==>age=60
    ==>vertex_type=doctor
    rexster[python]> list(g.V.has('vertex_type','consumer').map())[0]
    ==>last_name=Rogahn
    ==>first_name=Ozella
    ==>full_name=Ozella Rogahn
    ==>age=32
    ==>vertex_type=consumer
    rexster[python]> list(g.V.has('age',55).full_name)[:5]
    ==>Enrico Homenick
    ==>Vincenzo Ebert
    ==>Dr. Annetta McGlynn
    ==>Bertram Jaskolski
    ==>Mitchel Quitzon

This example was set up to mimick a network of consumers viewing and scheduling appointments with doctors. For example:

.. code-block:: bash

    rexster[python]> g.V.has('full_name','Myriam Daugherty').out_e('viewed').in_v().full_name
    ==>Dr. Alfred Dibbert
    ==>Dr. Abraham Casper
    ==>Dr. Cristobal Leffler
    ==>Dr. Avis Crona
    rexster[python]> g.V.has('full_name','Myriam Daugherty').out_e('scheduled_with').in_v().full_name
    ==>Dr. Nellie Heidenreich

Next, let us take a look at how to rank the providers according to how many consumers have viewed them.

.. code-block:: bash

    rexster[python]> ranked_by_viewed = {}
    rexster[python]> g.E.has('edge_type','viewed').in_v().group_count(ranked_by_viewed, lambda it: it.full_name, lambda it: it.b+1.0)
    rexster[python]> sorted_viewed_results = sorted(ranked_by_viewed.items(), key=lambda x:x[1], reverse=True)
    ==>null
    rexster[python]>sorted_viewed_results[:10]
    ==>(u'Dr. Cristobal Leffler', 369.0)
    ==>(u'Dr. Avis Crona', 366.0)
    ==>(u'Dr. Shana Moen', 350.0)
    ==>(u'Dr. Nellie Heidenreich', 337.0)
    ==>(u'Dr. Donny Schaefer', 266.0)
    ==>(u'Dr. Annetta McGlynn', 221.0)
    ==>(u'Dr. Israel Kiehn', 201.0)
    ==>(u'Dr. Roxanne Quigley', 196.0)
    ==>(u'Dr. Elton Zboncak', 184.0)
    ==>(u'Dr. Alfred Dibbert', 153.0)


Next, let us take a look at how to rank the providers according to how many consumers have scheduled with them.

.. code-block:: bash

    rexster[python]> ranked_by_scheduled = {}
    rexster[python]> g.E.has('edge_type','scheduled_with').in_v().group_count(ranked_by_scheduled, lambda it: it.full_name, lambda it: it.b+1.0)
    rexster[python]> sorted_scheduled_results = sorted(ranked_by_scheduled.items(), key=lambda x:x[1], reverse=True)
    ==>null
    rexster[python]> sorted_scheduled_results[:10]
    ==>(u'Dr. Nellie Heidenreich', 111.0)
    ==>(u'Dr. Donny Schaefer', 104.0)
    ==>(u'Dr. Anna Collier', 100.0)
    ==>(u'Dr. Avis Crona', 83.0)
    ==>(u'Dr. Elton Zboncak', 78.0)
    ==>(u'Dr. Roxanne Quigley', 68.0)
    ==>(u'Dr. Constance Kihn', 58.0)
    ==>(u'Dr. Emmalee Ondricka', 57.0)
    ==>(u'Dr. Annetta McGlynn', 54.0)
    ==>(u'Dr. Kip Stoltenberg', 45.0)


Troubleshooting
---------------

If you have problems connecting to a remote titan graph (that's using elasticsearch) when you're working
within an interactive jython session, try placing the names.txt file from elasticsearch somewhere on
the path or in your current working directory.  It seems that some class loader differences exist
between an interactive jython session and working within rexster.  names.txt can be found properly
within rexster but not when working with jython.  You can grab a copy of names.txt here:
https://github.com/elasticsearch/elasticsearch/blob/master/src/main/resources/config/names.txt
or from within the elasticsearch jar file.


Supported JVM Versions
----------------------

This library aims to support and is tested against these JVM versions:

* openjdk7
* oraclejdk7
* oraclejdk8


License
-------

Copyright (c) 2015 PokitDok, Inc.  The MIT License (MIT) (See LICENSE_ for details.)
