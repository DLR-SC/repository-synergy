# QRNN

Tensorflow implementation of [Quasi-Recurrent Neural Networks](https://arxiv.org/abs/1611.01576) (QRNN). The QRNN layer is implemented in the qrnn.py file.
The original blog post with code reference can be found [here](http://metamind.io/research/new-neural-network-building-block-allows-faster-and-more-accurate-text-understanding/).

A QRNN layer is composed of a convolutional stage (red blocks in the figure) and a pooling stage (blue blocks in the figure):

* The convolutional stage can perform the different activations in parallel (i.e. layer activations and gate activations) through time, such that each red sub-block is independent.

* The pooling stage imposes the ordering information across time, and although it is a sequential process (as depicted by the arrow) the heavy computation has already been performed in a single forward pass in the convolutional stage!

The figure below shows that QRNN is a mixture between CNN and LSTM, where we get the best of both worlds: make all activation computations in parallel with convolutions and merge sequentially, with no recursive weight operations.

![qrnn_block](assets/qrnn_block.png)

This work contains an implementation of the language model experiment on the Pen TreeBank (PTB) dataset.

To execute the PTB language model experiment w/ train and test stages altogether:

`python train_lm.py`

To re-make the data tensors for any corpus, remove the `vocab.pkl.gz` file generated
within the corpus data dir. That will re-set the vocab and dataset generation.

The following training is done a bit differently than in original paper for PTB task:
A zoneout factor of `0.1` was applied without dropout between hidden layers nor L2 reg.

`python train_lm.py --zoneout 0.1 --dropout 0`

#### Training Loss

![qrnn_loss](assets/qrnn_loss.png)

#### Training Perplexity

![qrnn_pplexity](assets/qrnn_pplexity.png)

#### Learning rate decay

![qrnn_lrdecay](assets/qrnn_lrdecay.png)

## TODO

* Work in the sentiment analysis task too
* Implement a wrapper to stack multiple QRNNs
* Set up the possibility of dense connections within the stack
* Implement a seq2seq wrapper

##  Author

Santi Pdp ( [@santty128](https://twitter.com/santty128) )
