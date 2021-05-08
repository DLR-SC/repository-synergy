K-means++ in Pandas
===================

An implementation of the [k-means++ clustering algorithm](http://en.wikipedia.org/wiki/K-means%2B%2B) using [Pandas](http://pandas.pydata.org/).

IMPORTANT NOTE
--------------

**This package should not be used in production.** The implementation of k-means++ contained therein is much slower than [that of scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html). Use that instead.

The only reason why I wrote any of this is to teach myself Pandas.

Prerequisites
-------------

* Python 2.7 or lower; this is not Python 3 compatible (yet).
* [Pandas](http://pandas.pydata.org/) (obviously).
* [NumPy](http://numpy.org)

Installation
------------

If you have [pip](http://www.pip-installer.org/en/latest/installing.html), then just do

	pip install k-means-plus-plus

Otherwise,

* Clone the repository:

		git clone https://github.com/jackmaney/k-means-plus-plus-pandas.git

* Enter the newly-created folder containing the repo

		cd k-means-plus-plus-pandas

* And run the installation manually:

		python setup.py install



Usage
-----

Here are the constructor arguments:

* `data_frame`: A Pandas data frame representing the data that you wish to cluster. Rows represent observations, and columns represent variables.

* `k`: The number of clusters that you want.

* `columns=None`: A list of column names upon which you wish to cluster your data. If this argument isn't provided, then all of the columns are selected. **Note:** Columns upon which you want to cluster must be numeric and have no `numpy.nan` values.

* `max_iterations=None`: The maximum number of times that you wish to iterate k-means. If no value is provided, then the iterations continue until stability is reached (ie the cluster assignments don't change between one iteration and the next).

* `appended_column_name=None`: If this value is set with a string, then a column will be appended to your data with the given name that contains the cluster assignments (which are integers from 0 to `k-1`). If this argument is not set, then you still have access to the clusters via the `clusters` attribute.

Once you've constructed a `KMeansPlusPlus` object, then just call the `cluster` method, and everything else should happen automagically. Take a look at the `examples` folder.

TODO:
----

* Add on features that take iterations of k-means++ clusters and compares them via, eg, concordance matrices, Jaccard indices, etc.

* Given a data frame, implement the so-called [Elbow Method](http://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set#The_Elbow_Method) to take a stab at an optimal value for `k`.

* ~~Make this into a proper Python module that can be installed via pip.~~

* Python 3 compatibility (probably via six).
