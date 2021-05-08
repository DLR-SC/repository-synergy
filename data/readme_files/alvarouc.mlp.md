# Keras Multilayer Perceptron for scikit-learn

Keras makes  it very easy  to implement deep-learning  models, however
these are not compatible with scikit-learn out-of-the-box. This
prohibits our models to be tested using sciki-learn's methods GridSearchCV
and cross_val_score. 

I  created this  MLP class  to  be compatible  with scikit-learn  that
contains the fit, predict, and predict_proba methods.

Install
```bash
pip install mlp
```

Quick guide

Initialize your classifier
```python
from mlp import MLP
clf = MLP(n_hidden=10, n_deep=3, l1_norm=0, drop=0.1, verbose=0)
```

Now evaluate your classifier with scikit-learn's cross_val_score
```python
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(clf, data, label, cv=5, n_jobs=-1, scoring='f1_weighted')
print(scores)
```

See a complete example in https://github.com/alvarouc/mlp/blob/master/examples/moon_sklearn.ipynb


