Dtree - A simple pure-Python decision tree construction algorithm
=================================================================

[![](https://img.shields.io/pypi/v/dtree.svg)](https://pypi.python.org/pypi/dtree) [![Build Status](https://img.shields.io/travis/chrisspen/dtree.svg?branch=master)](https://travis-ci.org/chrisspen/dtree) [![](https://pyup.io/repos/github/chrisspen/dtree/shield.svg)](https://pyup.io/repos/github/chrisspen/dtree)

Overview
--------

Given a training data set, it constructs a decision tree for classification or
regression in a single batch or incrementally.

It loads data from CSV files. It expects the first row in the CSV to be a
header, with each element conforming to the pattern "name:type:mode".
Mode is optional, and denotes the class attribute. Type identifies the
attribute as either a continuous, discrete, or nominal.

The module is loosely based on code published by Christopher Roach in his
article [Building Decision Trees in Python](http://onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html).
I refactored his code to be more object-oriented, and extended it to support
basic regression.

The class attribute can be either continuous, discrete or nominal, but all
other attributes can only be discrete or nominal.

Installation
------------

Download the code and then run:

    python setup.py build
    sudo python setup.py install
    
You can also install from PyPI using pip via:

    sudo pip install dtree
    
Or upgrade from an earlier version via:

    sudo pip install --upgrade dtree

Usage
-----

Classification and regression are handled through the same interface, and
differ only in the object returned by the predict() method and how the result
from test() is interpreted.

With classification, this object will always be a DDist instance, representing
a probability distribution over a set of discrete or nominal classes. In this
case, the result from test() will be a CDist instance representing the
classification accuracy.

With regression, this object will always be a CDist instance, representing a
mean and variance. In this case, the result from test() will be a CDist
instance representing the mean absolute error.

    from dtree import Tree, Data
    
    tree = Tree.build(Data('classification-training.csv'))
    result = t.test(Data('classification-testing.csv'))
    print 'Accuracy:',result.mean
    prediction = tree.predict(dict(feature1=123, feature2='abc', feature3='hot'))
    print 'best:',prediction.best
    print 'probs:',prediction.probs
    
    tree = Tree.build(Data('regression-training.csv'))
    result = t.test(Data('regression-testing.csv'))
    print 'MAE:',result.mean
    prediction = tree.predict(dict(feature1=123, feature2='abc', feature3='hot'))
    print 'mean:',prediction.mean
    print 'variance:',prediction.variance

Features
--------

- building a classification or regression tree using batch or incremental/online methods

Todo
----

Does not yet support:

- sparse training data
- sparse query vector

History
-------

0.1.0 - 2012.01.24
Initial development.

0.2.0 - 2012.02.08
Refactored to support incremental/online tree construction and forests.

1.0.0 - 2016.10.30
Added support for Python 3.
