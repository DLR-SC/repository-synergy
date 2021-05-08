# carl

[![Build Status](https://travis-ci.org/diana-hep/carl.svg)](https://travis-ci.org/diana-hep/carl) [![Coverage Status](https://coveralls.io/repos/diana-hep/carl/badge.svg?branch=master&service=github)](https://coveralls.io/github/diana-hep/carl?branch=master) [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.47798.svg)](http://dx.doi.org/10.5281/zenodo.47798) [![JOSS](http://joss.theoj.org/papers/26a9ffd9e7b98b1911d89d2ceb268f37/status.svg)](http://joss.theoj.org/papers/26a9ffd9e7b98b1911d89d2ceb268f37)

`carl` is a toolbox for likelihood-free inference in Python.

The likelihood function is the central object that summarizes the information
from an experiment needed for inference of model parameters. It is key to many
areas of science that report the results of classical hypothesis tests or
confidence intervals using the (generalized or profile) likelihood ratio as a
test statistic. At the same time, with the advance of computing technology, it
has become increasingly common that a simulator (or generative model) is used to
describe complex processes that tie parameters of an underlying theory and
measurement apparatus to high-dimensional observations. However, directly
evaluating the likelihood function in these cases is often impossible or is
computationally impractical.

In this context, the goal of this package is to provide tools for the
likelihood-free setup, including likelihood (or density) ratio estimation
algorithms, along with helpers to carry out inference on top of these.
It currently supports:

- Composition and fitting of distributions;
- Likelihood-free inference from classifiers;
- Parameterized supervised learning;
- Calibration tools.

_This project is still in its early stage of development. Join us if you feel
like contributing!_


## Documentation

* [Static documentation](http://diana-hep.org/carl).

* Extensive details regarding likelihood-free inference with calibrated
  classifiers can be found in the companion paper _"Approximating Likelihood
  Ratios with Calibrated Discriminative Classifiers", Kyle Cranmer, Juan Pavez,
  Gilles Louppe._
  [http://arxiv.org/abs/1506.02169](http://arxiv.org/abs/1506.02169)


## Installation

The following dependencies are required:

- Numpy >= 1.11
- Scipy >= 0.17
- Scikit-Learn >= 0.18-dev
- Theano >= 0.8

Once satisfied, `carl` can be installed from source using the following
commands:

```
git clone https://github.com/diana-hep/carl.git
cd carl
python setup.py install
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions to start
developing and contributing to `carl`.


## Citation

```
@misc{carl,
  author       = {Gilles Louppe and Kyle Cranmer and Juan Pavez},
  title        = {carl: a likelihood-free inference toolbox},
  month        = mar,
  year         = 2016,
  doi          = {10.5281/zenodo.47798},
  url          = {http://dx.doi.org/10.5281/zenodo.47798}
}
```
