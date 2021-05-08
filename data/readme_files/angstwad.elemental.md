Elemental
=========

A Flask MVC-style application base.

## Purpose

Elemental was written to provide my most basic needs in public-facing Flask apps.  A quick rundown of what it provides:

1. A signup, login, logout and hello world view
2. User-related code is dependent on flask-login and uses bcrypt for passwords
3. MongoDB as a backend with MongoEngine as the ODM
4. flask-admin to provide quick admin views of MongoDB collections
5. flask-wtf for forms
6. A common ancestor template (`header.html`) to inherit, which provides Bootstrap (and a navbar) and jQuery
7. A basic, logical separation of the application inspired by the MVC software pattern.

## Use

**Be sure to edit the elemental/config/config.py file to settings that suit your environment.**  Primarily, be sure to change the `MONGO_SETTINGS['host']` setting in config.py.

The Flask development server can be invoked from a Python environment that has installed the requirements in `requirements.txt`.

```
$ python runapp.py
```

I wrote Elemental with the intent of running derivative apps with Gunicorn in production.

#### Dependencies:
* flask-login
* flask-admin
* flask-debugtoolbar
* flask-mongoengine
* flask-bcrypt
* flask-wtf

## License

Apache 2.0



