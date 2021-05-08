Django Data Importer
====================

[![Build Status](https://travis-ci.org/valdergallo/data-importer.png?branch=master)](https://travis-ci.org/valdergallo/data-importer)
[![Latest Version](http://img.shields.io/pypi/v/data-importer.svg)](https://pypi.python.org/pypi/data-importer)
[![Coverage Status](https://coveralls.io/repos/valdergallo/data-importer/badge.png)](https://coveralls.io/r/valdergallo/data-importer)
[![BSD License](http://img.shields.io/badge/license-BSD-yellow.svg)](http://opensource.org/licenses/BSD-3-Clause)
[![PyPi downloads](https://img.shields.io/pypi/dm/data-importer.svg)](https://pypi.python.org/pypi/data-importer)


**Django Data Importer** is a tool which allow you to transform easily a `CSV, XML, XLS and XLSX` file into a python object or a django model instance. It is based on the django-style declarative model.

Features
--------

* Support to Django Customer User
* (beta) QuerysetToWorkbook
* Ignore empty line
* Accept custom clean_fields
* Accept post_clean
* Accept post_save
* Accept post_save_all_lines
* Accept pre_clean
* Accept pre_commit
* Accept save with transaction
* Auto generate async importers
* Auto Importer CSV
* Auto Importer XLS
* Auto Importer XLSX
* Auto Importer XML
* Check import status on Django Admin
* Convert text values by default as unicode
* Default FormView
* Django Admin integration to download files in File History
* Easy interface to create Importers
* Easy interface to create Readers
* File History integrated with FormView
* GenericImporter to import files (CSV, XLS, XLSX, XML)
* Get fields from Django Models
* Ignore First Row
* Integrated with Celery
* Integrated with Django Models
* Integrated with Django Models Validators
* Open file to read
* Read source as File, cStringIO, Text, FileField
* Set starting_row
* Set XLS/XLSX importer by sheet_index
* Set XLS/XLSX importer by sheet_name
* Support to user a JSON descriptor with Fields
* Fields as OrderedDict with text position


Installation
------------

Use either ``easy_install``:

    easy_install data-importer

or ``pip``:

    pip install data-importer


Settings
--------

Customize data_importer decoders

>**DATA_IMPORTER_EXCEL_DECODER**<br/>
>    Default value is cp1252

>**DATA_IMPORTER_DECODER**<br/>
>    Default value is UTF-8


Add support to South Migrations and Django Migrations


```
    SOUTH_MIGRATION_MODULES = {
        'data_importer': 'data_importer.south_migrations',
    }

    MIGRATION_MODULES = {
        'data_importer': 'data_importer.django_migrations'
    },
```


Basic example
-------------

Consider the following:

```
>>> from data_importer.importers import CSVImporter
>>> class MyCSVImporterModel(CSVImporter):
...     fields = ['name', 'age', 'length']
...     class Meta:
...         delimiter = ";"
```

You declare a ``MyCSVImporterModel`` which will match to a CSV file like this:

    Anthony;27;1.75

To import the file or any iterable object, just do:

```
>>> my_csv_list = MyCSVImporterModel(source="my_csv_file_name.csv")
>>> row, first_line = my_csv_list.cleaned_data[0]
>>> first_line['age']
27
```

Without an explicit declaration, data and columns are matched in the same
order:

    Anthony --> Column 0 --> Field 0 --> name
    27      --> Column 1 --> Field 1 --> age
    1.75    --> Column 2 --> Field 2 --> length


Using Fields as Dict
---------------------

You can use diferents ways to define the fields as dicts


```
>>> class TestMetaDict(XLSImporter):
...     fields = OrderedDict((
...         ('business_place', 'A'),
...         ('doc_number', 'b'),
...         ('doc_data', 'C'),
...     ))
```

or

```
>>> class TestMetaDict(XLSImporter):
...     fields = OrderedDict((
...         ('business_place', 0),
...         ('doc_number', 1),
...         ('doc_data', 2),
...     ))
```

or

```
>>> class TestMetaDict(XLSImporter):
...     fields = OrderedDict((
...         ('business_place', '0'),
...         ('doc_number', 1,)
...         ('doc_data', 'C'),
...     ))
```

Using declaration, data and columns are matched in the same
order:

    New York   --> Column 0 --> Field 0 --> business_place
    664736     --> Column 1 --> Field 1 --> doc_number
    2015-01-01 --> Column 2 --> Field 2 --> doc_data


Django Model
------------

If you now want to interact with a django model, you just have to add a **Meta.model** option to the class meta.

```
>>> from django.db import models
>>> class MyModel(models.Model):
...     name = models.CharField(max_length=150)
...     age = models.CharField(max_length=150)
...     length = models.CharField(max_length=150)

>>> from data_importer.importers import CSVImporter
>>> from data_importer.model import MyModel
>>> class MyCSVImporterModel(CSVImporter):
...     class Meta:
...         delimiter = ";"
...         model = MyModel
```

That will automatically match to the following django model.

*The django model should be imported in the model*

>**delimiter**<br/>
>    define the delimiter of the csv file.<br/>
>    If you do not set one, the sniffer will try yo find one itself.

>**ignore\_first_line**<br/>
>    Skip the first line if True.

>**model**<br/>
>    If defined, the importer will create an instance of this model.

>**raise_errors**<br/>
>    If set to True, an error in a imported line will stop the loading.

>**exclude**<br/>
>    Exclude fields from list fields to import

>**transaction**<br/>
>    Use transaction to save objects


Django XML
------------

If you now want to interact with a django model, you just have to add a **Meta.model** option to the class meta.

XML file example:

```
<encspot>
    <file>
        <Name>Rocky Balboa</Name>
        <Age>40</Age>
        <Height>1.77</Height>
    </file>
    <file>
        <Name>Chuck Norris</Name>
        <Age>73</Age>
        <Height>1.78</Height>
    </file>
</encspot>

>>> from django.db import models
>>> class MyModel(models.Model):
...     name = models.CharField(max_length=150)
...     age = models.CharField(max_length=150)
...     height = models.CharField(max_length=150)

>>> from data_importer.importers import XMLImporter
>>> from data_importer.model import MyModel
>>> class MyCSVImporterModel(XMLImporter):
...     root = 'file'
...     class Meta:
...         model = MyModel
```

That will automatically match to the following django model.

*The django model should be imported in the model*

> **model**<br/>
>    If defined, the importer will create an instance of this model.

>**raise_errors**<br/>
>    If set to True, an error in a imported line will stop the loading.

>**exclude**<br/>
>    Exclude fields from list fields to import

>**transaction**<br/>
>    Use transaction to save objects


Django XLS/XLSX
----------------

My XLS/XLSX file can be imported too


| Header1 | Header2 | Header3 | Header4
| ------- | ------- | ------- | -------
| Teste 1 | Teste 2 | Teste 3 | Teste 4
| Teste 1 | Teste 2 | Teste 3 | Teste 4



This is my model

```
>>> from django.db import models
>>> class MyModel(models.Model):
...     header1 = models.CharField(max_length=150)
...     header2 = models.CharField(max_length=150)
...     header3 = models.CharField(max_length=150)
...     header4 = models.CharField(max_length=150)
```

This is my class
```
>>> from data_importer import XLSImporter
>>> from data_importer.model import MyModel
>>> class MyXLSImporterModel(XLSImporter):
...     class Meta:
...         model = MyModel
```


If you are using XLSX you will need use `XLSXImporter` to made same importer
```
>>> from data_importer import XLSXImporter
>>> from data_importer.model import MyModel
>>> class MyXLSXImporterModel(XLSXImporter):
...     class Meta:
...         model = MyModel
```


> **ignore\_first_line**<br/>
> Skip the first line if True.

>**model** <br/>
>    If defined, the importer will create an instance of this model.

>**raise_errors**<br/>
>    If set to True, an error in a imported line will stop the loading.

>**exclude**<br/>
>    Exclude fields from list fields to import

>**transaction** <br/>
>    Use transaction to save objects


Descriptor
----------

Using file descriptor to define fields for large models.


import_test.json

```
{
  'app_name': 'mytest.Contact',
    {
    // field name / name on import file or key index
    'name': 'My Name',
    'year': 'My Year',
    'last': 3
    }
}
```

model.py

```
class Contact(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    laster = models.CharField(max_length=5)
    phone = models.CharField(max_length=5)
    address = models.CharField(max_length=5)
    state = models.CharField(max_length=5)
```

importer.py

```
class MyImpoter(BaseImpoter):
    class Meta:
        config_file = 'import_test.json'
        model = Contact
        delimiter = ','
        ignore_first_line = True
```

content_file.csv

```
name,year,last
Test,12,1
Test2,13,2
Test3,14,3
```

Default DataImporterForm
------------------------

`DataImporterForm` is one `django.views.generic.edit.FormView`
to **save file** in `FileUpload` and parse content on success.

Example
-------

```
class DataImporterCreateView(DataImporterForm):
    extra_context = {'title': 'Create Form Data Importer',
                     'template_file': 'myfile.csv'
                    }
    importer = MyCSVImporterModel
```

TEST
----

Acentuation with XLS    | Excel MAC 2011    |   **OK**
----------------------- | ----------------- | --------
Acentuation with XLS    | Excel WIN 2010    |   **OK**
Acentuation with XLSX   | Excel MAC 2011    |   **OK**
Acentuation with XLSX   | Excel WIN 2010    |   **OK**
Acentuation with CSV    | Excel Win 2010    |   **OK**


Python |  3.4+
-------|------
Python |  2.7+
Django |  1.8+
