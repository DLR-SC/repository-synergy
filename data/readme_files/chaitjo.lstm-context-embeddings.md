# Overview
Presented here is a method to modify the word embeddings of a word in a sentence with its surrounding context using a bidirectional Recurrent Neural Network (RNN). The hypothesis is that these modified embeddings are a better input for performing text classification tasks like sentiment analysis or polarity detection. 

**Read the full blog post here: [chaitjo.github.io/context-embeddings](https://chaitjo.github.io/context-embeddings/)**

---

![Bidirectional RNN layer](res/bidirectional-rnn.png)

# Implementation
The code implements the proposed model as a pre-processing layer before feeding it into a [Convolutional Neural Network for Sentence Classification](https://arxiv.org/pdf/1408.5882v2.pdf) (Kim, 2014). Two implementations are provided to run experiments: one with [tensorflow](https://www.tensorflow.org/) and one with [tflearn](http://tflearn.org/) (A high-level API for tensorflow). Training happens end-to-end in a supervised manner: the RNN layer is simply inserted as part of the existing model's architecture for text classification.

The tensorflow version is built on top of [Denny Britz's implementation of Kim's CNN](https://github.com/dennybritz/cnn-text-classification-tf), and also allows loading pre-trained word2vec embeddings. 

Although both versions work exactly as intended, results in the blog post are from experiments with the tflearn version only.

# Usage
I used Python 3.6 and Tensorflow 0.12.1 for my experiments.
Tensorflow code is divided into `model.py` which abstracts the model as a class, and `train.py` which is used to train the model. It can be executed by running the `train.py` script (with optional flags to set hyperparameters)-
```
$ python train.py [--flag=1]
```
(Tensorflow code for Kim's baseline CNN can be found in `/cnn-model`.)

Tflearn code can be found in the `/tflearn` folder and can be run directly to start training (with optional flags to set hyperparameters)-
```
$ python tflearn/model.py [--flag=1]
```

The summaries generated during training (saved in `/runs` by default) can be used to visualize results using tensorboard with the following command-
```
$ tensorboard --logdir=<path_to_summary>
```
