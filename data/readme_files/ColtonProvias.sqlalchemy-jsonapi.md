# SQLAlchemy-JSONAPI

[![Build Status](https://travis-ci.org/ColtonProvias/sqlalchemy-jsonapi.svg?branch=master)](https://travis-ci.org/ColtonProvias/sqlalchemy-jsonapi)

[JSON API](http://jsonapi.org/) implementation for use with
[SQLAlchemy](http://www.sqlalchemy.org/).

SQLAlchemy-JSONAPI aims to implement the JSON API spec and to make it as simple
to use and implement as possible.

* [Documentation](http://sqlalchemy-jsonapi.readthedocs.org)

## Installation

```shell
pip install sqlalchemy-jsonapi
```

## Quick usage with Flask-SQLAlchemy

```py
# Assuming FlaskSQLAlchemy is db and your Flask app is app:
from sqlalchemy_jsonapi import FlaskJSONAPI

api = FlaskJSONAPI(app, db)

# Or, for factory-style applications
api = FlaskJSONAPI()
api.init_app(app, db)
```

## Quick usage without Flask

```py
# Assuming declarative base is called Base
from sqlalchemy_jsonapi import JSONAPI
api = JSONAPI(Base)

# And assuming a SQLAlchemy session
print(api.get_collection(session, {}, 'resource-type'))
```