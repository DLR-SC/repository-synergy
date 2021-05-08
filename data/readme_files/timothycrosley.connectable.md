![connectable](https://raw.github.com/timothycrosley/connectable/develop/logo.png) 

A simple, yet powerful, implementation of QT's signal / slots pattern for Python3
===================

[![PyPI version](https://badge.fury.io/py/connectable.svg)](http://badge.fury.io/py/connectable)
[![Build Status](https://travis-ci.org/timothycrosley/connectable.svg?branch=master)](https://travis-ci.org/timothycrosley/connectable)
[![Coverage Status](https://coveralls.io/repos/timothycrosley/connectable/badge.svg?branch=master&service=github)](https://coveralls.io/github/timothycrosley/connectable?branch=master)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/connectable/)
[![Join the chat at https://gitter.im/timothycrosley/connectable](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timothycrosley/connectable?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Connectable enables you to quickly and effeciently attach actions preformed by one object, to actions of another:

```py
from connectable import Connectable


class Person(Connectable):
    signals = ('says_hello', )

    def __init__(self, name):
        self.name = name

    def say_hello(self, to=None):
        if to:
            print("Hi {to}, this is {name}".format(to=to, name=self.name))
        else:
            print("Hi! This is {name}".format(name=self.name))
        self.emit('says_hello', self.name)


speaker = Person('Tim')
room = (Person('Amanda'), Person('Bob'), Person('Ted'), Person('Sue'))
heckler = Person('The *Real* Timothy')

for person in room:
    speaker.connect('says_hello', person.say_hello)
speaker.connect('says_hello', heckler.say_hello, transform='you horrible imposter')

speaker.say_hello()
```

Would output:

```bash
Hi! This is Tim
Hi Tim, this is Bob
Hi Tim, this is Sue
Hi Tim, this is Ted
Hi Tim, this is Amanda
Hi you horrible imposter, this is The *Real* Timothy
```

QT has a pretty good [write up](http://doc.qt.io/qt-4.8/signalsandslots.html) on the general merits of a signal / slots approach.


Making an object *Connectable*
===================

To make an object Connectable, all you have to do is inherit from the Connectable class and define your signals at the class level:
```py
from connectable import Connectable

class MyConnectable(Connectable):
    signals = ['something_changed']
```
Then to signal any of your defined signals, simply emit the signal name, optionally with a value:
```py

def action(self):
    self.emit('something_changed', 'Forever.')
    # or simply self.emit('something_changed')
```
Then any Python method or function can be connected to that action, via the connect command:
```py
my_object = MyConnectable()
my_object.connect('something_changed', print)
```
If you emitted a value and the provided slot method accepts one it will be passed as the first argument to that method.


Unique Features of Connectable
===================

Connectable adds some additional benefits over a vanilla port of the signal / slots pattern
- You can pass a custom value to the slot:
```py
    order_button.connect('clicked', status_label.set_text, 'Order Submitted Succesfully')
```
- You can add a conditional to the connection:
```py
    edit_mode_button.connect('toggled', input_field.set_editable, True, condition=False)
    edit_mode_button.connect('toggled', input_field.set_editable, False, condition=True)
```


Installing connectable
===================

Installing connectable is as simple as:

```bash
pip3 install connectable --upgrade
```

Ideally, within a virtual environment.


Why connectable?
===================

I've always loved the simplicity and expressiveness of QT's take on the observer pattern, and wanted to bring a similar
experience to Python.

--------------------------------------------

Thanks and I hope you find this *connection* helpful!

~Timothy Crosley
