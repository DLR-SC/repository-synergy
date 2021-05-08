## Given that I haven't been working on this project for a while and Tensorflow is under havy development, my code got oudated. I'm planning to restart working on it at early January (2017). If you're insterestd on it, please check it again later on Jnauary, 2017. 

## Thanks.


These are my experiments re-implementing the "Effective Approaches to Attention-based Neural Machine Translation" 
paper by [Luong et al. (2015)](http://arxiv.org/abs/1508.04025)

We are also integrating some of the techniques described in  "On Using Very Large Target Vocabulary for Neural Machine 
Translation" by [Jean et al. (2015)](http://arxiv.org/abs/1412.2007) using TensorFlow.

I'm heavily relying on [Tensorflow's](https://www.tensorflow.org/) seq2seq interfaces to construct the models.

I'm following the PEP8 conventions for coding with one change: I'm using lines 100 characters long. 
(Sorry python purists). 

**This is a work in progress and include some of my experiments with attentional models (e.g. an hybrid including both 
global and local attention with a feedback gate), and the code is not polished. Should not be used in production.**

###### Features (so far):

* Sequence-to-Sequence model with LSTM or GRU
* Global attention module
* Local attention module (local-p by [Luong et al. (2015)](http://arxiv.org/abs/1508.04025))
* Content-based functions to compute the attention vector:
  * general and dot by [Luong et al. (2015)](http://arxiv.org/abs/1508.04025)
  * attention by [Vinyals & Kaiser et al. (2014)](http://arxiv.org/abs/1412.7449)
* Beam search

###### Dependencies (so far):

* [TensorFlow](http://tensorflow.org/)
