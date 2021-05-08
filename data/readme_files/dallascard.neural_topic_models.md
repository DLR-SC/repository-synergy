## neural_topic_models

# NOTE: This repo has been deprecated! It has been replaced with: [www.github.com/dallascard/scholar](https://www.github.com/dallascard/scholar)


The accompanying paper has also been updated to reflect the version published at ACL 2018: "Neural Models for Documents with Metadata" by Dallas Card, Chenhao Tan, and Noah A. Smith

The paper can be found at: [https://arxiv.org/abs/1705.09296](https://arxiv.org/abs/1705.09296)

## Legacy documentation:

### Requirements:

The following requirements can be installed via pip or conda:

* python3
* numpy
* scipy
* theano
* scikit-learn
* spacy

### To run:

If you've never used spaCy before, start by running:

`python -m spacy download en`

Then, run the following commands from the `theano_code` directory:

Download 20 newsgroups data:

`python download_20ng.py`

Preprocess data: 

`python preprocess_data.py ../data/20ng/20ng_all/train.json ../data/20ng/20ng_all/test.json ../data/20ng/20ng_all/ --malletstop`

To test code:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --max_epochs 1 [options]`

### Options:

To recreate the NVDM (Miao et al, 2016), run:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --encoder_layers 2 --generator_layers 0 --train_bias`

To recreate the (e1 g0) model, run:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --encoder_layers 1 --generator_layers 0 --train_bias`

To recreate the (e1s g4s) model, run:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --encoder_layers 1 --encoder_shortcut --generator_layers 4 --generator_shortcut --train_bias`

To train a model with 50% sparsity:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --encoder_layers 1 --encoder_shortcut --generator_layers 4 --generator_shortcut --train_bias --l1_penalty 0.01 --sparsity_target 0.5`

To train a model using topics, labels, and interactions:

`python run_ngtm.py ../data/20ng/20ng_all train output --test test --encoder_layers 1 --encoder_shortcut --generator_layers 4 --generator_shortcut --train_bias --n_topics 5 --n_classes 20 --use_interactions`

### Citation:
If you find this code useful, please cite:
```
@article{card.2017,
  author = {Dallas Card and Chenhao Tan and Noah A. Smith},
  title = {A Neural Framework for Generalized Topic Models},
  year = {2017},
  journal = {arXiv preprint arXiv:1705.09296},
}
```
