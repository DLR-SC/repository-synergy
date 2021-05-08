# Morphological Priors for Probabilistic Neural Word Embeddings
=================================
Implementation of [Morphological Priors for Probabilistic Neural Word Embeddings](https://arxiv.org/abs/1608.01056).

![model_demo](./assets/arch.png)

# VarEmbed in Blocks
This is the implementation for the following paper, to appear at EMNLP 2016:
Morphological Priors for Probabilistic Neural Word Embeddings.  Parminder Bhatia, Robert Guthrie, Jacob Eisenstein.

Using LSTM's for word embeddings that incorporate word-level and morpheme-level information using Blocks and Fuel.
LSTM code modified from https://github.com/johnarevalo/blocks-char-rnn.git.

## Requirements

* Install Blocks. Please see the
[documentation](http://blocks.readthedocs.org/) for more information.

* Install Fuel.  Please see the
[documentation](http://fuel.readthedocs.org/) for more information.

* Install the Morfessor Python package.

Results
-----


![histogram](./assets/results.png)

## Usage

The input can be any raw, pre-tokenized text.  This will walk through how to generate the Morfessor model, preprocess and package the data as NDArrays, and train the model.

You will need to train a Morfessor model on your data.  A script for this has been provided.  It will output a serialized Morfessor model for later use.

```python train_morfessor.py --training-data <input.txt> --output <output.bin>```

The data set needs to be preprocessed and formatted, using preprocess_data.py and make_dataset.py.
The -h flag will give the arguments needed.
Preprocessing is downcasing so that capitalization doesn't affect Morfessor.

```python preprocess_data.py <textfile>.trn -o <output_file> -n <unks all but top N words>```

```python make_dataset.py <textfile>.trn -mf <morfessor_model.bin>```

Next, run train.py to train the model.
It will print statistics after each mini-batch.

```python train.py <filename>.hdf5```

Parameters like batch size, embedding dimension, and the number of epochs can be changed in the config.py file.

Last, word vectors can be output in the format word dim1 dim2 ..., with 1 word per line, via the output_word_vectors.py script.
Provide it a vocab of vectors to output, as well as a serialized network from training.
