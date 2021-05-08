============
Simple Model
============

.. image:: https://badge.fury.io/py/pysimplemodel.svg
    :target: https://pypi.org/project/pysimplemodel/

.. image:: https://img.shields.io/badge/python-3.6,3.7-blue.svg
    :target: https://github.com/lamenezes/simple-model

.. image:: https://img.shields.io/github/license/lamenezes/simple-model.svg
    :target: https://github.com/lamenezes/simple-model/blob/master/LICENSE

.. image:: https://circleci.com/gh/lamenezes/simple-model.svg?style=shield
    :target: https://circleci.com/gh/lamenezes/simple-model

.. image:: https://codecov.io/gh/lamenezes/simple-model/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/lamenezes/simple-model


*SimpleModel* offers a simple way to handle data using classes instead of a
plenty of lists and dicts.

It has simple objectives:

- Define models and its fields easily using class attributes, type annotations or tuples (whatever suits your needs)
- Support for field validation, cleaning and type conversion
- Easy model conversion to dict


Quickstart
==========

Installing
----------

Open your favorite shell and run the following command:

.. code:: shell

    pip install pysimplemodel


Example
-------

Define your models using type annotations:

.. code:: python

    from simple_model import Model


    class Person(Model):
        age: int
        height: float
        is_active: bool = True
        name: str


Simple model automatically creates an initializer for your model and you all set
to create instances:

.. code:: python

    >> person = Person(age=18, height=1.67, name='John Doe')
    >> person.name
    'John Doe'

As you have noticed we haven't informed a value for field `is_active`, but the model
was still created. That's because we've set a default value of `True` for it and
the model takes care of assigning it automatically to the field:

.. code:: python

    >> person.is_active
    True


Simple model also offers model validation. Empty fields are considered invalid and will
raise errors upon validation. Let's perform some tests using the previous `Person` model:

.. code:: python

    >> person = Person()
    >> print(person.name)
    None
    >> person.validate()
    Traceback (most recent call last):
        ...
    EmptyField: 'height' field cannot be empty

Let's say we want the height and age fields to be optional, that can be achieved with
the following piece of code:

.. code:: python

    from simple_model import Model


    class Person(Model):
        age: int = None
        height: float = None
        is_active: bool = True
        name: str


Now let's test it:

.. code:: python

    >> person = Person(name='Jane Doe', is_active=False)
    >> person.is_active
    False
    >> person.validate()
    True

The last line won't raise an exception which means the model instance is valid!
In case you need the validation to return True or False instead of raising an
exception that's possible by doing the following:

.. code:: python

    >> person.validate(raise_exception=False)
    True


You can also add custom validations by writing class methods prefixed by `validate`
followed by the attribute name, e.g.

.. code:: python

    class Person:
        age: int
        height: float
        name: str

        def validate_age(self, age):
            if age < 0 or age > 150:
                raise ValidationError('Invalid value for age {!r}'.format(age))
            
            return age

        def validate_height(self, height):
            if height <= 0:
               raise ValidationError('Invalid value for height {!r}'.format(age))
            
            return height


Let's test it:

.. code:: python

    >> person = Person(name='John Doe', age=190)
    >> person.validate()
    Traceback (most recent call last):
        ...
    ValidationError: Invalid value for age 190
    >> other_person = Person(name='Jane Doe', height=-1.67)
    >> other_person.validate()
    Traceback (most recent call last):
        ...
    ValidationError: Invalid value for height -1.67


It is important to note that models don't validate types. Currently types are used
for field value conversion.

The `validate` method also supports cleaning the field values by defining custom transformations
in the `validate_` methods:

.. code:: python

    class Person:
        age: int
        name: str

        def validate_name(self, name):
            return name.strip()

    >>> person = Person(age=18.0, name='John Doe ')
    >>> person.name
    'John Doe '
    >> person.age
    18.0
    >>> person.validate()
    >>> person.name
    'John Doe'
    >>> person.age  # all attributes are converted to its type before cleaning
    18  # converted from float (18.0) to int (18)


Finally, simple model allows you to easily convert your model to dict type using the function `to_dict()`:

.. code:: python

    >>> to_dict(person)
    {
        'age': 18,
        'name': 'John Doe'
    }


Documentation
=============

Docs on simple-model.rtfd.io_

.. _simple-model.rtfd.io: https://simple-model.readthedocs.io/en/latest/
