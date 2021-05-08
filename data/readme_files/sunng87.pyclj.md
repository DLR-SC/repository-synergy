pyclj
=====

A python reader/writer for clojure data literals. 
On clojure's extensible data notations, checkout Rich Hickey's edn spec: https://github.com/richhickey/edn

Install
-------

``pip install pyclj``

Usage
-----

The API is very similar to python's built-in json module.

- dump(data, fileobj)
- dumps(data)
- load(fileobj)
- loads(string)

Clojure -> Python Type Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= ======
Clojure Python
======= ======
list    list
vector  list 
set     set
map     dict
nil     None
string  string
int     int
float   float
boolean boolean
char    string
keyword string
======= ======
 
Python -> Clojure Type Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= =======
Python  Clojure
======= =======
list    vector
set     set
dict    map
None    nil
string  string
int     int
float   float
boolean boolean
======= =======

License
-------

pyclj is distributed under MIT license.



