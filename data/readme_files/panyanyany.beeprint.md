beeprint
========

make your debug printing more friendly

Features
========

-  **dict:** print elegantly with ordered keys
-  **text:** auto break into lines, auto clip long text
-  **multi language:** supports English, Chinese
-  outstanding mark to class and instance
-  supports user-defined `__repr__`
-  **recursion** aware
-  compatible with py2 py3

Contents
========

.. contents:: 

Examples
========

A Real World Example
--------------------

.. figure:: https://github.com/panyanyany/beeprint/raw/master/docs/images/a_real_world_example.png
   :alt: A Real World Example


Import beeprint as pp
---------------------

::

    from beeprint import pp

Print dict
----------

**pprint:**

::

    {'entities': {'hashtags': [],
                  'urls': [{'display_url': 'tumblr.com/xnr37hf0yz',
                            'expanded_url': 'http://tumblr.com/xnr37hf0yz',
                            'indices': [107, 126],
                            'url': 'http://t.co/cCIWIwg'}],
                  'user_mentions': []}}

**beeprint:**

::

    {
      'entities': {
        'hashtags': [],
        'urls': [
          {
            'display_url': 'tumblr.com/xnr37hf0yz',
            'expanded_url': 'http://tumblr.com/xnr37hf0yz',
            'indices': [107, 126],
            'url': 'http://t.co/cCIWIwg',
          },
        ],
        'user_mentions': [],
      },
    }

Print class
-----------

**pprint:**

::

    <class 'definition.NormalClassNewStyle'>

**beeprint:**

::

    class(NormalClassNewStyle):
      dicts: {
      },
      lists: [],
      static_props: 1,
      tupl: (1, 2)

Print instance
--------------

**pprint:**

::

    <definition.NormalClassNewStyle object at 0x7f338e5a9dd0>

**beeprint:**

::

    instance(NormalClassNewStyle):
      dicts: {
      },
      lists: [],
      say_hi: 'hello world',
      static_props: 1,
      tupl: (1, 2)

Print long text
---------------

**pprint:**

::

    [['\nThe sky and the earth were at first one blurred entity like an egg. Pangu was born into it.\n \n\tThe separation of the sky and the earth took eighteen thousand years-the yang which was light and pure rose to become the sky, \tand the yin which was heavy and murky\xef\xbc\x88\xe6\x9c\xa6\xe8\x83\xa7\xe7\x9a\x84\xef\xbc\x89 sank to form the earth. Between them was Pangu, who went through nine \tchanges every day, his wisdom greater than that of the sky and his ability greater than that of the earth. Every day the sky rose ten feet higher, the earth became ten feet thicker, and Pangu grew ten feet taller.\n \nAnother eighteen thousand years passed, and there was an extremely high sky, an extremely thick earth, and an extremely tall Pangu. After Pangu died, his head turned into the Five Sacred Mountains (Mount Tai, Mount Heng, Mount Hua, Mount Heng, Mount Song), his eyes turned into the moon and the sun, his blood changed into water in river and sea, his hair into grass.\n \nIn all, the universe and Pangu combine in one.\n',
      '\n\xe6\x8d\xae\xe6\xb0\x91\xe9\x97\xb4\xe7\xa5\x9e\xe8\xaf\x9d\xe4\xbc\xa0\xe8\xaf\xb4\xe5\x8f\xa4\xe6\x97\xb6\xe7\x9b\x98\xe5\x8f\xa4\xe7\x94\x9f\xe5\x9c\xa8\xe9\xbb\x91\xe6\x9a\x97\xe5\x9b\xa2\xe4\xb8\xad\xef\xbc\x8c\xe4\xbb\x96\xe4\xb8\x8d\xe8\x83\xbd\xe5\xbf\x8d\xe5\x8f\x97\xe9\xbb\x91\xe6\x9a\x97\xef\xbc\x8c\xe7\x94\xa8\xe7\xa5\x9e\xe6\x96\xa7\xe5\x8a\x88\xe5\x90\x91\xe5\x9b\x9b\xe6\x96\xb9\xef\xbc\x8c\xe9\x80\x90\xe6\xb8\x90\xe4\xbd\xbf\xe5\xa4\xa9\xe7\xa9\xba\xe9\xab\x98\xe8\xbf\x9c\xef\xbc\x8c\xe5\xa4\xa7\xe5\x9c\xb0\xe8\xbe\xbd\xe9\x98\x94\xe3\x80\x82\n\t\xe4\xbb\x96\xe4\xb8\xba\xe4\xb8\x8d\xe4\xbd\xbf\xe5\xa4\xa9\xe5\x9c\xb0\xe4\xbc\x9a\xe9\x87\x8d\xe6\x96\xb0\xe5\x90\x88\xe5\xb9\xb6\xef\xbc\x8c\xe7\xbb\xa7\xe7\xbb\xad\xe6\x96\xbd\xe5\xb1\x95\xe6\xb3\x95\xe6\x9c\xaf\xe3\x80\x82\xe6\xaf\x8f\xe5\xbd\x93\xe7\x9b\x98\xe5\x8f\xa4\xe7\x9a\x84\xe8\xba\xab\xe4\xbd\x93\xe9\x95\xbf\xe9\xab\x98\xe4\xb8\x80\xe5\xb0\xba\xef\xbc\x8c\xe5\xa4\xa9\xe7\xa9\xba\xe5\xb0\xb1\xe9\x9a\x8f\xe4\xb9\x8b\xe5\xa2\x9e\xe9\xab\x98\xe4\xb8\x80\xe5\xb0\xba\xef\xbc\x8c\n\t\xe7\xbb\x8f\xe8\xbf\x871.8\xe4\xb8\x87\xe5\xa4\x9a\xe5\xb9\xb4\xe7\x9a\x84\xe5\x8a\xaa\xe5\x8a\x9b\xef\xbc\x8c\xe7\x9b\x98\xe5\x8f\xa4\xe5\x8f\x98\xe6\x88\x90\xe4\xb8\x80\xe4\xbd\x8d\xe9\xa1\xb6\xe5\xa4\xa9\xe7\xab\x8b\xe5\x9c\xb0\xe7\x9a\x84\xe5\xb7\xa8\xe4\xba\xba\xef\xbc\x8c\xe8\x80\x8c\xe5\xa4\xa9\xe7\xa9\xba\xe4\xb9\x9f\xe5\x8d\x87\xe5\xbe\x97\xe9\xab\x98\xe4\xb8\x8d\xe5\x8f\xaf\xe5\x8f\x8a\xef\xbc\x8c\xe5\xa4\xa7\xe5\x9c\xb0\xe4\xb9\x9f\xe5\x8f\x98\xe5\xbe\x97\xe5\x8e\x9a\xe5\xae\x9e\xe6\x97\xa0\xe6\xaf\x94\xe3\x80\x82\xe7\x9b\x98\xe5\x8f\xa4\xe7\x94\x9f\xe5\x89\x8d\xe5\xae\x8c\xe6\x88\x90\xe5\xbc\x80\xe5\xa4\xa9\xe8\xbe\x9f\xe5\x9c\xb0\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe4\xb8\x9a\xe7\xbb\xa9\xef\xbc\x8c\xe6\xad\xbb\xe5\x90\x8e\xe6\xb0\xb8\xe8\xbf\x9c\xe7\x95\x99\xe7\xbb\x99\xe5\x90\x8e\xe4\xba\xba\xe6\x97\xa0\xe7\xa9\xb7\xe6\x97\xa0\xe5\xb0\xbd\xe7\x9a\x84\xe5\xae\x9d\xe8\x97\x8f\xef\xbc\x8c\xe6\x88\x90\xe4\xb8\xba\xe4\xb8\xad\xe5\x8d\x8e\xe6\xb0\x91\xe6\x97\x8f\xe5\xb4\x87\xe6\x8b\x9c\xe7\x9a\x84\xe8\x8b\xb1\xe9\x9b\x84\xe3\x80\x82\n']]

**beeprint:**

::

    [
      [
        '\nThe sky and the earth were at first one blurred entity like an egg. Pangu
         was born into it.\n \n\tThe separation of the sky and the earth took
         ...(12 hidden lines)',
        '\n????????????????????????????????????????????????????????????????????????????????????????????????????????????
         ?????????????????????????????????\n\t????????????????????????????????????????????????????????????????????????
         ...(3 hidden lines)',
      ],
    ]

Installation
============

.. code:: shell

    pip install beeprint

Settings
========

    more on `config.py <./beeprint/config.py>`__
