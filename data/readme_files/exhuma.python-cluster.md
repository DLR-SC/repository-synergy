DESCRIPTION
===========

.. image:: https://readthedocs.org/projects/python-cluster/badge/?version=latest
    :target: http://python-cluster.readthedocs.org
    :alt: Documentation Status

python-cluster is a "simple" package that allows to create several groups
(clusters) of objects from a list. It's meant to be flexible and able to
cluster any object. To ensure this kind of flexibility, you need not only to
supply the list of objects, but also a function that calculates the similarity
between two of those objects. For simple datatypes, like integers, this can be
as simple as a subtraction, but more complex calculations are possible. Right
now, it is possible to generate the clusters using a hierarchical clustering
and the popular K-Means algorithm. For the hierarchical algorithm there are
different "linkage" (single, complete, average and uclus) methods available.

Algorithms are based on the document found at
http://www.elet.polimi.it/upload/matteucc/Clustering/tutorial_html/

.. note::
    The above site is no longer avaialble, but you can still view it in the
    internet archive at:
    https://web.archive.org/web/20070912040206/http://home.dei.polimi.it//matteucc/Clustering/tutorial_html/


USAGE
=====

A simple python program could look like this::

   >>> from cluster import HierarchicalClustering
   >>> data = [12,34,23,32,46,96,13]
   >>> cl = HierarchicalClustering(data, lambda x,y: abs(x-y))
   >>> cl.getlevel(10)     # get clusters of items closer than 10
   [96, 46, [12, 13, 23, 34, 32]]
   >>> cl.getlevel(5)      # get clusters of items closer than 5
   [96, 46, [12, 13], 23, [34, 32]]

Note, that when you retrieve a set of clusters, it immediately starts the
clustering process, which is quite complex. If you intend to create clusters
from a large dataset, consider doing that in a separate thread.

For K-Means clustering it would look like this::

    >>> from cluster import KMeansClustering
    >>> cl = KMeansClustering([(1,1), (2,1), (5,3), ...])
    >>> clusters = cl.getclusters(2)

The parameter passed to getclusters is the count of clusters generated.


.. image:: https://readthedocs.org/projects/python-cluster/badge/?version=latest
    :target: http://python-cluster.readthedocs.org
    :alt: Documentation Status
