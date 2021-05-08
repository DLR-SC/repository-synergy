# djangorestframework-expander

[![Build Status](https://travis-ci.org/silverlogic/djangorestframework-expander.svg?branch=master)](https://travis-ci.org/silverlogic/djangorestframework-expander)

A serializer mixin for Django REST Framework to expand object representations inline

# Requirements

* Python (2.7, 3.2, 3.3, 3.4, 3.5)
* Django (1.7, 1.8, 1.9)
* Django REST Framework (3.1, 3.2, 3.3)

# Installation

Install using `pip`

```
pip install djangorestframework-expander
```

# Quick Start

* Must inherit from ExpanderSerializerMixin
* Expandable fields are defined using the `expandable_fields` attribute on the serializer Meta class.
    * Key is the field name.
    * Value is the serializer class - e.g. `MenuItemSerializer` **OR**
    * Value is a 3 tuple of (class, args, kwargs) - e.g. `(MenuItemSerializer, (), {'many': True})`
* **NOTE** field does not have to appear in `fields` to appear in `expandable_fields`.
* Expansion is controlled using the `expand` URL paramter. e.g. `/menu-items/?expand=menu`
* Expand multiple fields with a comma.  e.g. `/menu-items/?expand=menu,price_bracket`
* Expand nested fields by using a dot.  e.g. `/menu-items/?expand=menu.restaurant`

# Configuration

The available configuration options using settings.py and their defaults.

- `DRF_EXPANDER_EXPAND_ARG = 'expand'` - The request query param that will be used to indicate which fields to expand.

# Example

```python
from expander import ExpanderSerializerMixin


class RestaurantSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'title')


class MenuSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'restaurant', 'title')
        expandable_fields = {
            'restaurant': RestaurantSerializer,
        }

class PriceBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceBracket
        fields = ('id', 'title')


class MenuItemSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'menu', 'title', 'description', 'price', 'price_bracket')
        expandable_fields = {
            'menu': MenuSerializer,
            'price_bracket': PriceBracketSerializer,
        }
```

Making a request for a menu item returns the usual results to start with.

```
GET /menu-items/1/

{
    "id": 1,
    "menu": 3,
    "title": "Breakfast",
    "description": "",
    "price": "3.50"
}
```

Expand menu

```
GET /menu-items/1/?expand=menu

{
    "id": 1,
    "menu": {
        "id": 3,
        "restaurant": 6,
        "title": "Breakfast"
    },
    "title": "Eggs",
    "description": "",
    "price": "3.50"
}
```

Expand nested

```
GET /menu-items/1/?expand=menu.restaurant

{
    "id": 1,
    "menu": {
        "id": 3,
        "restaurant": {
            "id": 6,
            "title": "Bob's Bed and Breakfast"
        },
        "title": "Breakfast"
    },
    "title": "Eggs",
    "description": "",
    "price": "3.50"
}
```
