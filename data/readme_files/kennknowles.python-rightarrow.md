```
 _          _       _     _                               
 \\        (_)     | |   | |                              
  \\   _ __ _  __ _| |__ | |_ __ _ _ __ _ __ _____      __
   \\ | '__| |/ _` | '_ \| __/ _` | '__| '__/ _ \ \ /\ / /
    \\| |  | | (_| | | | | || (_| | |  | | | (_) \ V  V / 
     \\_|  |_|\__, |_| |_|\__\__,_|_|  |_|  \___/ \_/\_/  
              __/ |                                      
             |___/                                       
```

==========================

https://github.com/kennknowles/python-rightarrow

[![Build status](https://travis-ci.org/kennknowles/python-rightarrow.png)](https://travis-ci.org/kennknowles/python-rightarrow)

This library provides a language for concise higher-order annotations for Python programs, inspired
by the syntax for higher-order contracts and types in advanced languages. Functionality such as run-time
checking, static checking, inference of annotations, and documentation generation all exist here in
various stages of completeness.

This project has a "duck-typed" status: Whatever you can use it for, it is ready for :-)

Here is a more concrete list of implemented and intended features:

 - _yes_      - Definition of the language.
 - _yes_      - Parsing and printing.
 - _yes_      - Run-time monitoring of adherence for monomorphic annotations.
 - _upcoming_ - Monitoring of adherence for polymorphic annotations.
 - _upcoming_ - Documentation generation.
 - _upcoming_ - Generation of constraints between annotations in a program.
 - _upcoming_ - Best-effort inference of suitable annotations.
 - _upcoming_ - More precise annotations to support full higher-order design-by-contract.


The Annotations
---------------

This language is built from the following concepts:

 - Named types: `int`, `long`, `float`, `complex`, `str`, `unicode`, `file`, `YourClassNameHere`, ...
 - Lists: `[int]`, `[[long]]`, ...
 - Tuples: `(int, long)`, `(float, (int, Regex))`, ...
 - Dictionaries: `{string: float}`, `{ (str, str) : [complex] }`, ...
 - Unions: `int|long|float`, `str|file`, ...
 - "Anything goes": `??`
 - Functions, after which this library is named :-)
    - `str -> int`
    - `(int) -> int`
    - `(int, int) -> int`
    - `( (int, int) ) -> int`
    - `( str|file ) -> SomeClass`
    - `(int, *[str]) -> [(str, int)]`
    - `(int, *[int], **{int: str}) -> str`
 - Objects: `object(self_type, field1: int, field2: str, ...)`
 - Polymorphic types (where `~a`, `~b`, `~c` range over any other type. Syntax subject to change; no preference really)
    - `~a -> ~a`
    - `[~a] -> [~a]`
    - `( (~a, ~b) ) -> ~a`


Run-time checking
-----------------

The module `rightarrow.enforce` contains functions for using these annotations as run-time monitors.

Applied directly:

```python
>>> check('{string: int}', {"hello" : "there"})
```

Wrapping a function to protect it from funky input is more interesting.
For example, putting better error checking on Python's `unicode`/`str`
interactions (at least in Python 2)

```python
>>> '\xa3'.encode('utf-8')
...
UnicodeDecodeError: 'ascii' codec can't decode byte 0xa3 in position 0: ordinal not in range(128)

>>> @guard('unicode -> str')
... def safe_encode(s):
...    return s.encode('utf-8')

>>> safe_encode(u'hello')
'hello'
>>> safe_encode('\xa3')
TypeError: Type check failed: ? does not have type unicode
```

If you are familiar with notions of "blame" for higher-order contracts, pull-requests welcome :-)


Inferring Annotations
---------------------

Inference is a work-in-progress, definitely planned, and almost certainly will always be "best effort" only.
It works like so:

1. By traversing the code, we can discover a bunch of constraints between different missing annotations.
2. Some of these constraints are going to be very easy to solve, so we can just propagate the results.
3. Some of these constraints are not going to be practical to try to solve, so we
   can just drop them or insert some enforcement code if we like.


More to explore
---------------

There are many other projects that check contracts or types for Python in some way. 
They are all different, many are prototypes or research projects, and none 
seem to serve the need that motivates this library. Still, check them out!

 * [PEP 316](http://www.python.org/dev/peps/pep-0316/) (deferred)
 * [RPython](http://doc.pypy.org/en/latest/translation.html) and [PyPy](http://pypy.org/) (compilation-oriented)
 * [pySonar](http://yinwang0.wordpress.com/2010/09/12/pysonar/) and [mini-pysonar](https://github.com/yinwang0/mini-pysonar)
   (way cool)
 * [Pyntch](http://www.unixuser.org/~euske/python/pyntch/index.html)
 * [typechecker](https://github.com/shomah4a/typechecker)
 * [pycontract](http://www.wayforward.net/pycontract/)
 * [python-dbc](http://code.google.com/p/python-dbc/) 
   and [one pyDBC](http://www.nongnu.org/pydbc/) 
   and [another pydbc](https://github.com/cadrian/pydbc) 
   and [yet another pyDBC](https://github.com/Ceasar/pyDbC)
 * [python-type-inference](http://code.google.com/p/python-type-inference/wiki/Resources) (no code, but has a great list of papers and even more tools)

And there are cool things happening in other dynamic languages! 

 * [Contracts in Racket](http://docs.racket-lang.org/guide/contracts.html) and [Typed Racket](http://docs.racket-lang.org/ts-guide/)
 * [Typescript](http://www.typescriptlang.org/) 
   aka [a slightly gradually-typed Javascript](http://siek.blogspot.com/2012/10/is-typescript-gradually-typed-part-1.html)
   and [Javascript++](http://jspp.javascript.am/) (sort of gradually-typed Javascript)
   and [javascript-contracts](https://github.com/brownplt/javascript-contracts)
   and [cerny](http://www.cerny-online.com/cerny.js/)
 * [Este](https://github.com/Steida/este) (statically-typed coffeescript) 
   and [Uberscript](https://github.com/jstrachan/coffee-script/blob/master/TypeAnnotations.md) (gradually-typed coffeescript)
   and [contracts.coffee](http://disnetdev.com/contracts.coffee/)
 * [Contracts.ruby](https://github.com/egonSchiele/contracts.ruby)

And this library draws inspiration from such a huge amount of academic work it cannot possibly all
be mentioned, but special thanks to these research efforts, which you might enjoy.

 - _Higher-order contracts_. Start with [Contracts for higher-order functions](http://www.eecs.northwestern.edu/~robby/pubs/papers/ho-contracts-icfp2002.pdf)
     by Robert Bruce Findler & Matthias Felleisen, 2002.
 - _Gradual typing_. Start with [Gradual typing for functional languages](http://ecee.colorado.edu/~siek/pubs/pubs/2006/siek06_gradual.pdf)
     by Jeremy Siek & Walid Taha, 2006.
 - _Hybrid Type Checking_. Start with [Hybrid type checking](http://users.soe.ucsc.edu/~cormac/papers/toplas09.pdf)
     by Kenneth Knowles & Cormac Flanagan 2006/2010; 

Contributors
------------

 * [Kenn Knowles](https://github.com/kennknowles) ([@kennknowles](https://twitter.com/KennKnowles))


Copyright and License
---------------------

Copyright 2012- Kenneth Knowles

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
