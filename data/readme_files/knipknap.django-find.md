# django-find

[![Build Status](https://travis-ci.org/knipknap/django-find.svg?branch=master)](https://travis-ci.org/knipknap/django-find)
[![Coverage Status](https://coveralls.io/repos/github/knipknap/django-find/badge.svg?branch=master)](https://coveralls.io/github/knipknap/django-find?branch=master)
[![Code Climate](https://lima.codeclimate.com/github/knipknap/django-find/badges/gpa.svg)](https://lima.codeclimate.com/github/knipknap/django-find)
[![Documentation Status](https://readthedocs.org/projects/django-find/badge/?version=latest)](http://django-find.readthedocs.io/en/latest/?badge=latest)

## Summary

**django-find** is a Django app that makes it easy to add complex
search/filter functionality for the models in your project.
It supports two different ways to search your Django models:
Query-based, or JSON-based.

**django-find** is not a full text search engine, it searches the fields
of your models. In other words, it filters on your models and provides
tabular data as a result.

## Features

### Query-based search

By query-based, we mean that you can use statements like these
to search your models:

```
author:"robert frost" and (title:road or chapter:2)
```

### Add a search field to your template using a single tag

```
{% load find_tags %}
{% find object_list %}
{% for obj in object_list %}
  {{ obj.name }}
{% endfor %}
```

(object\_list is a queryset that is passed to the template)

### Query in your code

Just add the Searchable mixin:

```python
from django_find import Searchable

class Author(models.Model, Searchable):
    name = models.CharField("Author Name", max_length=10)
    ...
```

And you are good to go:

```python
# Query-based search returns a standard Django QuerySet that you
# can .filter() and work with as usual.
query = Book.by_query('author:"robert frost" and title:"the road"')

# You can also get a Django Q object for the statements.
q_obj = Book.q_from_query('author:"robert frost" and title:"the road"')
```

### Query using JSON

To make it easy to do complex searches spanning multiple models, JSON-based
query method is provided. It allows your to make custom searches like these:

![Custom Search](https://raw.githubusercontent.com/knipknap/django-find/master/docs/_static/custom.png)

For this, a JSON-based search functionality is provided:

```
{
    "Author":{"name":[[["equals","test"]]]},
    "Book": {"title":[[["notcontains","c"]]]},
    "Chapter": {"content":[[["startswith","The "]]]}
}
```

django-find is smart in figuring out how to join those models
together and return a useful result.
In your code, you can load the JSON and get back the search
result:

```python
# JSON-based search exhausts what Django's ORM can do, so it does
# not return a Django QuerySet, but a row-based PaginatedRawQuerySet:
query, field_list = Book.by_json_raw('''{
    "Chapter": {"title":[[["contains","foo"]]]}
}''')
print('|'.join(field_list))
for row in query:
    print('|'.join(row))
```

## Documentation

Full documentation, including installation instructions, is here:

http://django-find.readthedocs.io
