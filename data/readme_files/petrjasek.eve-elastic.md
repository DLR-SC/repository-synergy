Eve-Elastic
===========

.. image:: https://travis-ci.org/petrjasek/eve-elastic.png?branch=master
        :target: https://travis-ci.org/petrjasek/eve-elastic

Eve-Elastic is `elasticsearch <http://www.elasticsearch.org>`_ data layer for `eve REST framework <http://python-eve.org>`_.

Features
--------

- fulltext search
- filtering via elasticsearch filter dsl
- facets support
- aggregations support
- elasticsearch mapping generator for schema

License
-------
Eve-Elastic is `GPLv3 <http://www.gnu.org/licenses/gpl-3.0.txt>`_ licensed.

Supported elastic versions
--------------------------

It supports ``1.7`` and ``2.x`` versions. If you limit your queries to those which work
with both you can have single codebase for both.


Install
-------

.. code-block:: bash

    $ pip install Eve-Elastic

Usage
-----
Set elastic as your eve data layer.

.. code-block:: python

    import eve
    from eve_elastic import Elastic

    app = eve.Eve(data=Elastic)
    app.run()

Config
------
There are 2 options for Eve-Elastic taken from ``app.config``:

- ``ELASTICSEARCH_URL`` (default: ``'http://localhost:9200/'``) - this can be either single url or list of urls
- ``ELASTICSEARCH_INDEX`` - (default: ``'eve'``)
- ``ELASTICSEARCH_INDEXES`` - (default: ``{}``) - ``resource`` to ``index`` mapping
- ``ELASTICSEARCH_FORCE_REFRESH`` - (default: ``True``) - force index refresh after every modification
- ``ELASTICSEARCH_AUTO_AGGREGATIONS`` - (default: ``True``) - return aggregates on every search if configured for resource

Query params
------------
Eve-Elastic supports eve like queries via ``where`` param which work as `term <http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-term-filter.html>`_ filter.

On top of this, there is a predefined `query_string <http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html>`_ query which does fulltext search.

.. code-block:: bash

    $ curl http://localhost:5000/items?q=foo&df=name

- ``q`` - query (default: ``*``)
- ``df`` - default field (default: ``_all``)


Filtering
---------
For more sophisticated filtering, you can use ``filter`` query param which will be used as filter for the query,
using elastic `filter dsl <http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-filters.html>`_.

Facets
------
To add a facets support for specific resource, add ``facets`` into its ``datasource``:

.. code-block:: python

    DOMAIN = {
        'contacts': {
            'datasource':
                'facets': {
                    'urgency': {'terms': {'field': 'urgency'}},
                    'versioncreated': {'date_histogram': {'field': 'versioncreated', 'interval': 'hour'}}
                }
            }
        }

You will find more info about facets in `elasticsearch docs <http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-facets.html>`_.
