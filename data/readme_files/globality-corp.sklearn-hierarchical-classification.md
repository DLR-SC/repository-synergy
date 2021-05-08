# sklearn-hierarchical-classification

![PyPI](https://img.shields.io/pypi/v/sklearn-hierarchical-classification) [![CircleCI](https://circleci.com/gh/globality-corp/sklearn-hierarchical-classification.svg?style=svg&circle-token=6d5d6914ea5a5e2ad92cde6a8166bf25b229ad6a)](https://circleci.com/gh/globality-corp/sklearn-hierarchical-classification)

Hierarchical classification module based on scikit-learn's interfaces and conventions.

See the GitHub Pages hosted documentation [here](http://code.globality.com/sklearn-hierarchical-classification/).


## Installation

To install, simply install this package via pip into your desired virtualenv, e.g:

    pip install sklearn-hierarchical-classification


## Usage

See [examples/](./examples/) for usage examples.


## Testing

To run the included unit-tests, install the test dependencies and then invoke using `nose`:

    pip install -e '.[test]'
    pip install nose
    nosetests


### Jupyter notebooks

Support for interactive development is built in to the `HierarchicalClassifier` class. This will enable progress bars (using the excellent [tqdm](https://pypi.python.org/pypi/tqdm) library) in various places during training and may otherwise enable more visibility into the classifier which is useful during interactive use. To enable this make sure widget extensions are enabled by running:

    jupyter nbextension enable --py --sys-prefix widgetsnbextension

You can then instantiate a classifier with the `progress_wrapper` parameter set to `tqdm_notebook`:

```python
clf = HierarchicalClassifier(
    base_estimator=svm.LinearSVC(),
    class_hierarchy=class_hierarchy,
    progress_wrapper=tqdm_notebook,
)
```


## Documentation

Auto-generated documentation is provided via sphinx. To build / view:

    $ cd docs/
    $ make html
    $ open build/html/index.html


Documentation is published to GitHub pages from the `gh-pages` branch.
If you are a contributor and need to update documentation, a good starting point for getting setup is [this tutorial](https://gohugo.io/hosting-and-deployment/hosting-on-github/#deployment-of-project-pages-from-docs-folder-on-master-branch).


## Further Reading

this module is heavily influenced by the following previous work and papers:

* ["Functional Annotation of Genes Using Hierarchical Text Categorization"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.68.5824&rep=rep1&type=pdf) - Kiritchenko et al. 2005
* ["Classifying web documents in a hierarchy of categories: a comprehensive study"](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.150.8859) - Ceci and Malerba 2007
* ["A survey of hierarchical classification across different application domains"](https://www.researchgate.net/publication/225716424_A_survey_of_hierarchical_classification_across_different_application_domains) - CN Silla et al. 2011
* ["A Survey of Automated Hierarchical Classification of Patents"](https://lirias.kuleuven.be/bitstream/123456789/457904/1/GomezMoens%20Mumia_book_chapter_camera_ready2014.pdf) - JC Gomez et al. 2014
* ["Evaluation Measures for Hierarchical Classification: a unified view and novel approaches"](https://arxiv.org/pdf/1306.6802.pdf) - Kosmopoulos et al. 2013
* ["Bayesian Aggregation for Hierarchical Classification"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.89.3312&rep=rep1&type=pdf) - Barutcuoglu et al. 2008
* ["Kaggle LSHTC4 Winning Solution"](https://kaggle2.blob.core.windows.net/forum-message-attachments/43550/1230/lshtc4.pdf) - Puurula et al. 2014
* ["Feature-Weighted Linear Stacking"](https://arxiv.org/pdf/0911.0460.pdf) - Sill et al. 2009
