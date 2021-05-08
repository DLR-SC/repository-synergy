Active Learning Library
==
# pyAL
--------------
pyAL is an python library that implements common active learning strategies. The project is currently developed by the members of the Machine Learning Lab at IIT: (http://ml.cs.iit.edu).

This work is supported by NSF CAREER Award #1350337. http://nsf.gov/awardsearch/showAward?AWD_ID=1350337

Currently supported strategies:

1. Random sampling
2. Uncertainty sampling by Lewis and Gale, 1994. A sequential algorithm for training text classifiers. Proceedings of the 17th annual international ACM SIGIR conference on Research and development in information retrieval.
3. Query-by-committee by Seung et al, 1992. Query by committee. Proceedings of the fifth annual workshop on Computational learning theory.
4. Expected error reduction by Roy and McCallum, 2001. Toward optimal active learning through monte carlo estimation of error reduction. Proceedings of the Eighteenth International Conference on Machine Learning.

# Related Links 
--------------
* Machine Learning Lab @ IIT (http://cs.iit.edu/~ml)
* Documentation: (http://iitml.github.io/AL/)


# Dependencies
-----------
pyAL is tested to work under Python 2.7. The required dependencies to build the software are scikit-learn >= 0.15, NumPy >= 1.6.2, and SciPy >= 0.9.


# Installation
----------------
This package uses distutils, which is the default way of installing python modules. To install in your home directory, use:

python setup.py install --user
To install for all users on Unix/Linux:
```
$ python setup.py build
$ sudo python setup.py install
```

# Content of this Repository
This repository is organized as follows:

* ```al```: contains the code
* ```documentation```: contains the documentation of the classes
* ```front_end```: containts the GUI
* ```utils```: contains the utilities

# Development

## Code - GIT

You can check the latest sources with the command:

```
git clone git@github.com:iitml/AL.git
```

# How to use this Library

## GUI Example

* Example about how to use the GUI: (http://iitml.github.io/AL/code.html#id1)

## Module Example
```python
from al.learning_curve import LearningCurve

learning_api = LearningCurve()

training_size, avg_accu, avg_auc = learning_api.run_trials(X_pool, y_pool, X_test, y_test, strategy, classifier, alpha, boot_strap_size, step_size, budget, num_trials)
```
