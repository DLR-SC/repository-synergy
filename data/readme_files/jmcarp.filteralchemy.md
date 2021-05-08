=============
filteralchemy
=============

.. image:: https://img.shields.io/pypi/v/filteralchemy.svg
    :target: http://badge.fury.io/py/filteralchemy
    :alt: Latest version

.. image:: https://readthedocs.org/projects/filteralchemy/badge/?version=latest
    :target: https://filteralchemy.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/travis/jmcarp/filteralchemy/dev.svg
    :target: https://travis-ci.org/jmcarp/filteralchemy
    :alt: Travis-CI

.. image:: https://img.shields.io/codecov/c/github/jmcarp/filteralchemy/dev.svg
    :target: https://codecov.io/github/jmcarp/filteralchemy
    :alt: Code coverage

**filteralchemy** is a declarative query builder for SQLAlchemy. **filteralchemy** uses marshmallow-sqlalchemy_ to auto-generate filter fields and webargs_ to parse field parameters from the request. Use it to filter data with minimal boilerplate.

For Django users: the design of **filteralchemy** is strongly inspired by django-filter_.

Install
-------

.. code-block::

    pip install filteralchemy
    
Quickstart
----------

.. code-block:: python

    import flask
    from models import Album, session
    from webargs.flaskparser import parser

    from filteralchemy import FilterSet
    from filteralchemy.operators import Equal, Less, Greater

    class AlbumFilterSet(FilterSet):
        class Meta:
            model = Album
            query = session.query(Album)
            operators = (Equal, Less, Greater)
            parser = parser

    app = flask.Flask(__name__)

    @app.route('/albums')
    def get_albums():
        query = AlbumFilterSet().filter()
        return flask.jsonify(query.all())

.. code-block::

    http :5000/albums artist==Queen genre==rock sales__gt==1000000

.. _marshmallow-sqlalchemy: https://marshmallow-sqlalchemy.readthedocs.org/
.. _webargs: https://webargs.readthedocs.org/
.. _django-filter: https://github.com/alex/django-filter
