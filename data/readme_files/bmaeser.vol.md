===============
vol
===============

************
Installation
************

with pip as easy as: ::

    $ pip install vol

or checkout the latest version from github: ::

    $ git clone https://github.com/bmaeser/vol.git
    $ cd vol
    $ python setup.py install

*****
What?
*****

vol lets you control your mac's audio volume from the commandline. It also has support for profiles.

****
Why?
****

Because i want to have profiles, and want to change my audio-volume via commandline.
So i can ssh into the box in my livingroom and change the volume while sitting on the couch.

****
How?
****

::

    vol (in|out|alert) <volume>
    vol mute
    vol unmute
    vol load <profile>
    vol info

    vol (-h | --help)
    vol --version

    Options:
        -h --help     Show this screen.
        --version     Show version.

*********
Examples
*********

set output volume to 50 (of 100 max): ::

    vol out 50

set input (mic) volume to 10: ::

    vol in 10

mute and unmute: ::

    vol mute
    vol unmute

load a profile from ``$HOME/.vol`` - file: ::

    vol load party

********
Profiles
********

vol looks for profiles in ``.vol`` in your home.

If your username is 'bob' vol will parse ``/Users/bob/.vol``

a short example for ``.vol``: ::

    [party]
    in= 0
    alert= 0
    out= 100

    [silence]
    out = 0
    in = 0
    alert = 0
    mute=True

``.vol`` uses ini-style syntax. Please see the full example configfile in ./conf/



.. image:: https://d2weczhvl823v0.cloudfront.net/bmaeser/vol/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

