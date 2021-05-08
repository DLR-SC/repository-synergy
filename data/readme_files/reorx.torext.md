Description
-----------

Torext is an utilities bundle for tornado, aimed at easy development & deployment of tornado application.

Tornado is a great library, but sometimes I found it not that convenient to use, for example,
I have to manually import handlers for Application initialization while there are more than one modules
that hold request handlers, I have to write ``define('myoption')`` for a lot of lines, they are unsightly and inconvenient to manipulate.
Each time I encounter those problems, my developing process is disturbed, I have to either consult the code
I wrote in old project, or type lengthy repetitive code. Tornado is elegant, so I think developing with tornado
should also be elegant.

That's what torext is created for, it contains features that most web frameworks commonly have:

* database integration and models

* url routing

* validator for request arguments and everything

* error handling dispatch

* project scaffold

* invoke settings from file

* unit testing
