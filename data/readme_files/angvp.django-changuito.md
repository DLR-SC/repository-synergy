django-changuito
=================

[![Build Status](https://travis-ci.org/angvp/django-changuito.png)](https://travis-ci.org/angvp/django-changuito)
[![Coverage Status](https://coveralls.io/repos/angvp/django-changuito/badge.svg?branch=master&service=github)](https://coveralls.io/github/angvp/django-changuito?branch=master)


# Introduction

django-changuito, is a simple cart based on django-cart, it allows you to have
a session cart for logged and not logged users, it's born from the need of features
that weren't available on django-cart and the previous main developer seems to
doesn't have more free time, we are very thankful for his work but we don't
want to maintain our own version of django-cart, so we forked and did our changes
and make everything open source on a public repo and uploaded to PyPI.

We are already using it on production and we want to encourage old users
of django-cart or forked projects of django-cart to migrate to changuito instead.

## Prerequisites

- Django 1.7, 1.8, 1.9, 1.10, 1.11
- Python 2.7 and Python 3.4+
- django content type framework in your INSTALLED_APPS

## Installation

To install this just type:

```
python setup.py install
```

or

```
pip install django-changuito
```

## Testing

For running the test suite please do:

```
python setup.py test 
```

Or simply run tox (if you want to test all the envs)

After installation is complete:

1. add 'changuito' to your INSTALLED_APPS directive and
2. Syncronize the DB: `./manage.py migrate`

## Usage

A basic usage of django-changuito could be (example):

```python
#settings.py
MIDDLEWARE_CLASES += ('changuito.middleware.CartMiddleware', )
```


```python
# views.py
from myproducts.models import Product

def add_to_cart(request, product_id, quantity=1):
    product = Product.objects.get(id=product_id)
    cart = request.cart 
    cart.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    cart = request.cart 
    cart.remove_item(product_id)

def get_cart(request):
    return render_to_response('cart.html', dict(cart=CartProxy(request)))
```

```django
# templates/cart.html
{% extends 'base.html' %}

{% block body %}
    <table>
        <tr>
            <th>Product</th>
            <th>Description</th>
            <th>Quantity</th>
            <th>Total Price</th>
        </tr>
        {% for item in cart %}
        <tr>
            <td>{{ item.product.name }}</td>
            <td>{{ item.product.description }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.total_price }}</td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}
```

## Some Info

This is from the original project that I've forked, I just renamed the project since
is not officialy dead and continued my work on this project

```
This project was abandoned and I got it and added tests and South migrations, 
and I will be maintaining it from now on. 
```

## A note on the authors of this project

This project is a fork of django-cart which was originally started by Eric Woudenberg and followed up by Marc Garcia <http://vaig.be>, and then continued by Bruno Carvalho, which adds a lot of stuff and then wasn't much aware of the status of the project.
The last change ocurred in Jan 29 2012. Bruno and other authors added tests and cool stuff and we are thankful for that, and we will continue with that spirit.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/angvp/django-changuito/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
