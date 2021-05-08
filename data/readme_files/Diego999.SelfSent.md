# SelfAttentiveSentenceEmbedding
Implementation in Tensorflow of [A Structured Self-attentive Sentence Embedding](https://arxiv.org/abs/1703.03130) with the sentiment analysis task.

The code organization is similar to [NeuroNER](https://arxiv.org/abs/1705.05487).

# Requirements
SelfSent relies on Python 3.5 and TensorFlow 1.0+.
For the package `stanford_corenlp_pywrapper`, just install it from https://github.com/mpagli/stanford_corenlp_pywrapper.

# Data
You need to create a `data` folder next to the `src` folder.
Then for each dataset, you have to create a separate folder. In this folder, you just need to put a file `all.json` where each line correspond to a json sample with its attributes. 

Here a sample of Yelp dataset:
<pre>{"review_id":"IYE_M_cRsk-AhVYeYvnADg","user_id":"r-zUIQPaHzvIyL93wQaoiQ","business_id":"HE23DlZWAO_JF1VIHA60TQ",**"stars":3**,"date":"2012-10-09",**"text":"This is the Capitol Square branch."**,"useful":0,"funny":0,"cool":0,"type":"review"}</pre>

In the case of review star prediction, the needed attributes are `text` and `stars`. 
<pre>{"review_id":"IYE_M_cRsk-AhVYeYvnADg",<b>"stars":3</b>,"date":"2012-10-09",<b>"text":"This is the Capitol Square branch."</b>,"user_id":"r-zUIQPaHzvIyL93wQaoiQ","business_id":"HE23DlZWAO_JF1VIHA60TQ""useful":0,"funny":0,"cool":0,"type":"review"}</pre>

The parameters `do_split` (force to split even if the pickle files exist), `training`, `valid`, `test` in `parameters.ini` will split the dataset accordingly.

# Word Embedding
It also needs some word embeddings, which should be downloaded from http://neuroner.com/data/word_vectors/glove.6B.100d.zip, unzipped and placed in `/data/word_vectors`. This can be done on Ubuntu and Mac OS X with:

```
# Download some word embeddings
mkdir -p SelfSent-master/data/word_vectors
cd SelfSent-master/data/word_vectors
wget http://neuroner.com/data/word_vectors/glove.6B.100d.zip
unzip glove.6B.100d.zip
```

# Training

Be sure that `use_pretrained_model = false` and have at least `all.json` in the data folder.

# Deployment

You need to have a pretrained model, which is composed of:
- dataset.pickle
- model.ckpt.data-00000-of-00001
- model.ckpt.index
- model.ckpt.meta
- parameters.ini

Don't forget to put `use_pretrained_model = true` and the path to the pretrained model folder.

    
# Issues/Pull Requests/Feedbacks

Don't hesitate to contact for any feedback or create issues/pull requests.
