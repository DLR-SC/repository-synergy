# Heroku Python Skeleton

This repository has all the base files ready for deploying a Python application on Heroku. It includes the following features:

 - Flask HTTP application
 - SQLAlchemy model that binds to a Heroku Postgres database
 - RESTful API based on Flask-RESTful and the Marshmallow serialization framework

## Usage

### Initial

```bash
$ git clone https://github.com/yuvadm/heroku-python-skeleton.git
$ cd heroku-python-skeleton
$ heroku create
$ git push heroku master
```

### Database

```bash
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku run python
```

and in the Python REPL:

```python
>>> from app import db
>>> db.create_all()
```

For a detailed introduction see [http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/](http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/).
