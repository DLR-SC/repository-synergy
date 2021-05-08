DeepMind : Teaching Machines to Read and Comprehend
=========================================

This repository contains an implementation of the two models (the Deep LSTM and the Attentive Reader) described in *Teaching Machines to Read and Comprehend* by Karl Moritz Hermann and al., NIPS, 2015. This repository also contains an implementation of a Deep Bidirectional LSTM. 

The three models implemented in this repository are:

- `deepmind_deep_lstm` reproduces the experimental settings of the DeepMind paper for the LSTM reader
- `deepmind_attentive_reader` reproduces the experimental settings of the DeepMind paper for the Attentive reader
- `deep_bidir_lstm_2x128` implements a two-layer bidirectional LSTM reader

## Our results

We trained the three models during 2 to 4 days on a Titan Black GPU. The following results were obtained:


<table width="416" cellpadding="2" cellspacing="2">
<tr>
<td valign="top" align="center"> </td>
<td colspan="2" valign="top" align="center">DeepMind </td>
<td colspan="2" valign="top" align="center">Us </td>
</tr>
<tr>
<td valign="top" align="center"> </td>
<td colspan="2" valign="top" align="center">CNN </td>
<td colspan="2" valign="top" align="center">CNN </td>
</tr>
<tr>
<td valign="top" align="center"> </td>
<td valign="top" align="center">Valid </td>
<td valign="top" align="center">Test </td>
<td valign="top" align="center">Valid </td>
<td valign="top" align="center">Test </td>
</tr>
<tr>
<td valign="top" align="center">Attentive Reader </td>
<td valign="top" align="center"><b>61.6</b> </td>
<td valign="top" align="center"><b>63.0</b> </td>
<td valign="top" align="center">59.37 </td>
<td valign="top" align="center">61.07 </td>
</tr>
<tr>
<td valign="top" align="center">Deep Bidir LSTM </td>
<td valign="top" align="center">- </td>
<td valign="top" align="center">- </td>
<td valign="top" align="center"><b>59.76</b> </td>
<td valign="top" align="center"><b>61.62</b> </td>
</tr>
<tr>
<td valign="top" align="center">Deep LSTM Reader</td>
<td valign="top" align="center">55.0</td>
<td valign="top" align="center">57.0</td>
<td valign="top" align="center">46</td>
<td valign="top" align="center">47</td>
</tr>
</table>

Here is an example of attention weights used by the attentive reader model on an example:

<img src="https://raw.githubusercontent.com/thomasmesnard/DeepMind-Teaching-Machines-to-Read-and-Comprehend/master/doc/attention_weights_example.png" width="816px" height="652px" />


## Requirements

Software dependencies:

* [Theano](https://github.com/Theano/Theano) GPU computing library library
* [Blocks](https://github.com/mila-udem/blocks) deep learning framework 
* [Fuel](https://github.com/mila-udem/fuel) data pipeline for Blocks

Optional dependencies:

* Blocks Extras and a Bokeh server for the plot

We recommend using [Anaconda 2](https://www.continuum.io/downloads) and installing them with the following commands (where `pip` refers to the `pip` command from Anaconda):

    pip install git+git://github.com/Theano/Theano.git
    pip install git+git://github.com/mila-udem/fuel.git
    pip install git+git://github.com/mila-udem/blocks.git -r https://raw.githubusercontent.com/mila-udem/blocks/master/requirements.txt

Anaconda also includes a Bokeh server, but you still need to install `blocks-extras` if you want to have the plot:

    pip install git+git://github.com/mila-udem/blocks-extras.git

The corresponding dataset is provided by [DeepMind](https://github.com/deepmind/rc-data) but if the script does not work (or you are tired of waiting) you can check [this preprocessed version of the dataset](http://cs.nyu.edu/~kcho/DMQA/) by [Kyunghyun Cho](http://www.kyunghyuncho.me/).


## Running

Set the environment variable `DATAPATH` to the folder containing the DeepMind QA dataset. The training questions are expected to be in `$DATAPATH/deepmind-qa/cnn/questions/training`.

Run:

    cp deepmind-qa/* $DATAPATH/deepmind-qa/

This will copy our vocabulary list `vocab.txt`, which contains a subset of all the words appearing in the dataset.

To train a model (see list of models at the beginning of this file), run:

    ./train.py model_name

Be careful to set your `THEANO_FLAGS` correctly! For instance you might want to use `THEANO_FLAGS=device=gpu0` if you have a GPU (highly recommended!)


## Reference

[Teaching Machines to Read and Comprehend](https://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend.pdf), by Karl Moritz Hermann, Tomáš Kočiský, Edward Grefenstette, Lasse Espeholt, Will Kay, Mustafa Suleyman and Phil Blunsom, Neural Information Processing Systems, 2015.


## Credits

[Thomas Mesnard](https://github.com/thomasmesnard)

[Alex Auvolat](https://github.com/Alexis211)

[Étienne Simon](https://github.com/ejls)


## Acknowledgments

We would like to thank the developers of Theano, Blocks and Fuel at MILA for their excellent work.

We thank Simon Lacoste-Julien from SIERRA team at INRIA, for providing us access to two Titan Black GPUs.


