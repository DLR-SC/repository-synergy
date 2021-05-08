# Tars

[![Build Status](https://travis-ci.com/masa-su/Tars.svg?branch=master&token=Tzd7hmaLjunaLnEja81y)](https://travis-ci.com/masa-su/Tars)
[![Python Version](https://img.shields.io/badge/python-2.7-blue.svg)](https://github.com/masa-su/Tars)
[![Documentation Status](https://readthedocs.org/projects/tars-generative-models/badge/?version=latest)](http://tars-generative-models.readthedocs.io/en/latest/?badge=latest)

[New] We are developing a **PyTorch version of Tars** made with more sophisticated API (which is named [**Pixyz**](https://github.com/masa-su/pixyz)). It is released now!

Tars is a deep generative models library. It has the following features:
* Various distributions
  * Gaussian, Bernoulli, Laplace, Gamma, Beta, Dirichlet, Bernoulli, Categorical, and so on.
  * Hierarchical latent distributions (New!).
  * We can draw samples from these distributions by **the reparameterization trick** .
* Various models
  * Autoencoder
  * VAE
     * Conditional VAE
     * Importance weighted autoencoder
     * [JMVAE](https://arxiv.org/abs/1611.01891v1)
     * Multiple latent layers
  * GAN, Conditional GAN
  * VAE-GAN, conditional VAE-GAN
    * [JMVAE-GAN](https://arxiv.org/abs/1611.01891v1)
  * VAE-RNN
    * Variational RNN
    * DRAW, Convolutional DRAW
* Various lower bounds
  * The evidence lower bound (ELBO, which is the same as the original lower bound)
  * The importance sampling lower bound 
  * The variational R'enyi bound

* Note: Some of the implementations of the above models have not yet been released in this version. If you want to use such models, please use the old version (v0.0.2).
* For a more detailed explanation of this library, please refer to [this page](http://qiita.com/mms/private/c548ac3268e5a325b129) (in Japanese).

## Installation
```
$ git clone https://github.com/masa-su/Tars.git
$ pip install -e Tars --process-dependency-links
```
or
```
$ pip install -e git://github.com/masa-su/Tars --process-dependency-links
```
When you execute this command, the following packages will be automatically installed in your environment:
* Theano
* Lasagne
* progressbar2
* matplotlib
* sklearn

## Examples
Please go to the examples directory and try to run some examples.
