TextClassification
==================

Simple practice for text classification using Python

| File  | Content|
|-------|--------|
|Rocchio.py | Text classification using Rocchio's algorithm. Each document is represented in a vector space. In the training phase, centroids for each class of documents are found. In the testing phase, test document's distance to each centroid is calculated and document is assigned to the closest centroid's class.|
|NaiveBayes.py | Text classification using Naive Bayes' algorithm. Each document in represented in a vector space. In the training phase, class priors and class conditional probabilities for every term of dictionary are learnt. In the testing phase, document is assigned to the class having the maximum posterior probability given the test document.|
|[sklearn-text classification.ipynb](http://nbviewer.ipython.org/github/erfannoury/TextClassification/blob/master/sklearn-text%20classification.ipynb) | This is an IPython notebook showing a complete, though simple, text classification pipeline using scikits-learn machine learning library. Pipeline starts with text cleaning and tokenization, then each document is projected into a vector space. Tfidf weighting is used to nornalize vectors. Then some classifiers are tested; using their default parameters. Finally using 10-fold cross validation over a brute force parameter grid search, best paramters for some of the classifiers are found and classification is performed using the newly-found parameters. |
