# non-distributional
Manaal Faruqui, manaalfar@gmail.com

This repository contains data released with the paper on non-distributional
word vector representation (Faruqui & Dyer, 2015). We provide here word vectors
that have been constructed using non-distributional information. This lexical
information has been collected from different linguistic lexicons constrcuted
over time in NLP research. For more details please refer to the paper.

### Data and Tools
####binary-vectors.txt.gz

This is a word vector file which is very high dimensional and is 99.9% sparse.
It contains binary vectors i.e, every word vector has only 1 or 0 as elements.
Its best to use this file in a compressed mode as it expands to around 41 GB
of text file.

Example vector:-

```the 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 ...``` 

####word-feat.txt

Every line of this file contains a word followed by all the features that the
word possesses as collected from the group of lexicons in lexicons/ folder.
This is an un-expanded form of the word vectors in binary-vectors.txt.gz

Example vector:-

```untrustworthiness wn_noun.attribute noun,negative```

####create-vector.py

This script takes a lexicon and converts it into a binary vector. We have created
binary-vectors.txt.gz using this script from all the files in lexicon/ folder. If
you want to create vectors from FrameNet use the following command:-

```python create-vector.py < lexicons/framenet.txt > binary-fn-vectors.txt```

We created binary-vectors.txt using the following command:-

```python create-vector.py < <(cat lexicons/*) > binary-vectors.txt```

####lexicons/

Every file in this directory is a lexicon containing the word and the features that
it possesses.

###Reference

```
@InProceedings{faruqui:2015:non-dist,
  author    = {Faruqui, Manaal and Dyer, Chris},
  title     = {Non-distributional Word Vector Representations},
  booktitle = {Proceedings of ACL},
  year      = {2015},
}
```
