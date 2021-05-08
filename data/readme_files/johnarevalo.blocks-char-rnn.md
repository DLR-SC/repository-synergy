# char-rnn in Blocks
This code is a python implementation of [Torch char-rnn](https://github.com/karpathy/char-rnn)
project using the [Blocks](http://blocks.readthedocs.org/) framework.

## Requirements

* Install Blocks. Please see the
[documentation](http://blocks.readthedocs.org/) for more information.

## Usage

* Set `text_file` parameter in the config.py file. You can try the
[input.txt](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt)
file used in the original code.
* run `make_dataset.py` to create the [Fuel](http://fuel.readthedocs.org/) dataset.
* run `train.py` file to train a Gated RNN ([Cho et al.](http://arxiv.org/abs/1409.1259)). 'rnn' and 'lstm' are also supported.
* run `sample.py` to sample characters using a trained model.

`train.py` and `sample.py` scripts follow most of the parameters from the
original [char-rnn](https://github.com/karpathy/char-rnn) project.  Please take
a look on it to train your own models.
