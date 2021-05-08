# stacked_generalization
Python implementation of stacked generalization classifier, as described [here](http://machine-learning.martinsewell.com/ensembles/stacking/). 

Plays nice with sklearn classifiers, or any model classes that have both `.fit` and `.predict` methods.

# Installation 
Currently the package is not on PyPi, but is easy to install directly from github via `pip` using the following command.

	pip install -e 'git+http://github.com/dustinstansbury/stacked_generalization.git#egg=stacked_generalization'

# Example usage

The following example builds a stacked generalizer model to classify the `digits` dataset available in scikits-learn. The three base models (two `RandomForest` classifiers with different optimization criterion, and a `ExtraTreesClassifier`) are estimated with 5-fold cross-validation. The outputs of the fit base models are used as features inputs to the `LogisticRegression` blending model, which is also trained with 5-fold cross-validation. The models are trained on 80 percent of the digits dataset and accuracy is evaluated on the remaining 20 percent.

	from sklearn.datasets import load_digits
	from stacked_generalizer import StackedGeneralizer
	from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
	from sklearn.linear_model import LogisticRegression
	import numpy as np

	VERBOSE = True
	N_FOLDS = 5
	
	# load data and shuffle observations
	data = load_digits()

	X = data.data
	y = data.target

	shuffle_idx = np.random.permutation(y.size)

	X = X[shuffle_idx]
	y = y[shuffle_idx]

	# hold out 20 percent of data for testing accuracy
	train_prct = 0.8
	n_train = int(round(X.shape[0]*train_prct))

	# define base models
	base_models = [RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion='gini'),
	               RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion='entropy'),
	               ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion='gini')]

	# define blending model
	blending_model = LogisticRegression()

	# initialize multi-stage model
	sg = StackedGeneralizer(base_models, blending_model, 
		                    n_folds=N_FOLDS, verbose=VERBOSE)

	# fit model
	sg.fit(X[:n_train],y[:n_train])

	# test accuracy
	pred = sg.predict(X[n_train:])
	pred_classes = [np.argmax(p) for p in pred]

	_ = sg.evaluate(y[n_train:], pred_classes)


           		 precision    recall  f1-score   support

	          0       1.00      1.00      1.00        31
	          1       0.95      1.00      0.97        39
	          2       1.00      1.00      1.00        40
	          3       1.00      0.97      0.99        38
	          4       1.00      0.97      0.99        37
	          5       1.00      0.97      0.99        35
	          6       1.00      1.00      1.00        32
	          7       0.95      1.00      0.97        37
	          8       1.00      0.94      0.97        35
	          9       0.92      0.94      0.93        35

    avg / total       0.98      0.98      0.98       359

	Confusion Matrix:
	[[31  0  0  0  0  0  0  0  0  0]
	 [ 0 39  0  0  0  0  0  0  0  0]
	 [ 0  0 40  0  0  0  0  0  0  0]
	 [ 0  0  0 37  0  0  0  1  0  0]
	 [ 0  0  0  0 36  0  0  0  0  1]
	 [ 0  0  0  0  0 34  0  0  0  1]
	 [ 0  0  0  0  0  0 32  0  0  0]
	 [ 0  0  0  0  0  0  0 37  0  0]
	 [ 0  1  0  0  0  0  0  0 33  1]
	 [ 0  1  0  0  0  0  0  1  0 33]]