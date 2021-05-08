Weka - Python wrapper for Weka classifiers
==========================================

[![](https://img.shields.io/pypi/v/weka.svg)](https://pypi.python.org/pypi/weka) [![Build Status](https://img.shields.io/travis/chrisspen/weka.svg?branch=master)](https://travis-ci.org/chrisspen/weka) [![](https://pyup.io/repos/github/chrisspen/weka/shield.svg)](https://pyup.io/repos/github/chrisspen/weka)

Overview
--------

Provides a convenient wrapper for calling Weka classifiers from Python.

Installation
------------

First install the Weka and LibSVM Java libraries. On Debian/Ubuntu this is simply:

    sudo apt-get install weka libsvm-java

Then install the Python package with pip:

    sudo pip install weka

Usage
-----

Train and test a Weka classifier by instantiating the Classifier class,
passing in the name of the classifier you want to use:

    from weka.classifiers import Classifier
    c = Classifier(name='weka.classifiers.lazy.IBk', ckargs={'-K':1})
    c.train('training.arff')
    predictions = c.predict('query.arff')

Alternatively, you can instantiate the classifier by calling its name directly:

    from weka.classifiers import IBk
    c = IBk(K=1)
    c.train('training.arff')
    predictions = c.predict('query.arff')

The instance contains Weka's serialized model, so the classifier can be easily
pickled and unpickled like any normal Python instance:

    c.save('myclassifier.pkl')
    c = Classifier.load('myclassifier.pkl')
    predictions = c.predict('query.arff')

Development
-----------

Tests require the Python development headers to be installed, which you can install on Ubuntu with:

    sudo apt-get install python-dev python3-dev python3.4-dev

To run unittests across multiple Python versions, install:

    sudo apt-get install python3.4-minimal python3.4-dev python3.5-minimal python3.5-dev

To run all [tests](http://tox.readthedocs.org/en/latest/):

    export TESTNAME=; tox

To run tests for a specific environment (e.g. Python 2.7):
    
    export TESTNAME=; tox -e py27

To run a specific test:
    
    export TESTNAME=.test_IBk; tox -e py27
