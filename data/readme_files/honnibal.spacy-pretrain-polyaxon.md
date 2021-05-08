# Using Language Models with Approximate Outputs to pre-train spaCy

**NB: This describes work in progress. It reflects expected results, not
necessarily things that are already true.**

This repository contains experiments on spaCy's new "pretrain" command, which
uses a ULMFit/Elmo/BERT/etc-like process for pre-training. We employ a novel
trick which we term Language Modelling with Approximate Outputs (LMAO).
Normally language models have to softmax (or hierarchical softmax) over the
output vocabulary, which requires large hidden layers. We want to train small
hidden layers, as we want spaCy to be cost-effective to run.

Instead of outputting numeric IDs, we predict points in a vector space that's
been pre-trained using an algorithm like GloVe or FastText. This lets the model
learn large target vocabularies, without requiring extra parameters.

## Update 05-12-18: Good results Universal Dependencies English

I compared accuracy on the development data of the English-EWT portion of the
universal dependencies data for four models:

1. No GloVe, no LMAO: Only the training data was used, with no pre-training in
  the word vectors or the CNN. This is the `sm` configuration in spaCy.
2. GloVe: Pre-trained word vectors were used as one of the input features. This
  is the `lg` configuration in spaCy.
3. No GloVe, LMAO: Like 1, but the CNN and hash embeddings were pretrained with LMAO cloze task.
4. GloVe, LMAO:  Like 2, but the CNN and hash embeddings were pretrained with the LMAO cloze task. 

| Model        | LAS  | 
| ------------ | ---- | 
| -GloVe,-LMAO | 79.1 |
| -GloVe,+LMAO | 81.0 |
| +GloVe,-LMAO | 81.0 |
| +GloVe,+LMAO | 82.4 |
| Stanford '17 | 82.3 |
| Stanford '18 | 83.9 |

All the models had the same number of learnable parameters: token vector width
96, hidden width 64, 2000 embedding rows. The model is very small --- like,
3 MB if total. The pre-training was done on the January 2017 portion of the
Reddit comments corpus (about 2 billion words). The pre-training objective is
like the BERT cloze task, but instead of predicting word IDs, we predict the
pre-trained GloVe vector of the word. This means the output layer is very small
(only 300 dimensions). A non-linear layer is used in between the CNN and the
output layer. This non-linear layer is a layer-normalized Maxout layer.

The two Stanford models are shown for comparison, to show these are overall
quite solid scores given the size of the model. We're achieving comparable
accuracy to the Stanford system that won the CoNLL 2017 shared task. The
Stanford 2018 results were near state-of-the-art in August 2018, but don't
utilise BERT-style pre-training, which I guess would push their results
into the high 80s.

## Update 02-12-18: Good results for small models, low data

The `spacy pretrain` command now uses a BERT-style masked language model, but
instead of predicting the word IDs, we predict the GloVe vector of the target
words. I've used this objective to pre-train spaCy's small CNN model on
2 billion words of text from Reddit (the January 2017 portion of the Reddit
comments corpus). The pre-trained CNN is very small: it's depth 4, width 96,
and has only 2000 rows in the hash embeddings table. Weights for the serialized
model are only 3.2 MB.

## Parsing results

Here's how pretraining affects parser unlabelled accuracy on different sized subsets of
the training data.

| #Docs | #Words | Baseline | Pretrain |
| ----- | ------ | -------- | -------- |
| 1     | 69     | 41.8     | 60.5     |
| 10    | 311    | 47.4     | 66.4     |
| 100   | 2947   | 61.3     | 79.0     |
| 1000  | 31097  | 78.5     | 84.7     |
| 10000 | 255000 | 87.0     | 87.8     |

The effect size here is pretty strong. The pretraining is very effective in the
low and medium data cases, but the impact fades as more training data becomes
available. One caveat with these results is that static vectors weren't used in
the input --- the vectors were trained from scratch. This is a bit unfair to
the baseline, since pre-trained vectors are a simple and effective existing way
to get some pretrained knowledge into the model. As a quick datapoint, the result
for baseline+GloVe vectors for the 1000 document case is 82.0%. So the static vectors
aren't as good as the pretraining. We can also use static vectors
together with pretraining, but I need to rerun the pretraining for that.

## Text classification results

I've also run some text classification experiments, using the same pretrained
weights as the parsing experiments. The evaluation is the IMDb task, but with
only 1000 training samples available. The GloVe vectors greatly improve
results on this task, so the current results aren't so interesting. The
pre-training improves over the baseline, but the absolute numbers are too low
to be informative. We'll see what happens when we have a pretrained weights file
also uses the GloVe vectors as input.

The CNN is very sensitive to hyper-parameters on small text classification
tasks. In order to get a valid comparison, we therefore have to do
hyper-parameter search separately for each experiment configuration. To do
this. I'm using [Polyaxon](https://polyaxon.com). The experiment code is in the
`lmao-imdb-1k` directory. See `gke-terraform-polyaxon` for setup instructions.

I ran 100 configurations with and without pre-training. Without pre-training,
the best accuracy achieved was 78.4%; with pre-training, the best accuracy
achieved was 81.3%. With GloVe vectors, the baseline goes up to 87%. We'll have
to wait and see how the pretraining+GloVe model performs.

## A few thoughts

Low and medium data use-cases are very important, because they help you perform
rapid prototyping. When doing practical NLP, there are an enormous number of
decisions to make in how you break down the application requirements into
statistical models. To make good decisions, you need to try things out and see
how well models perform with different approaches. If you have models which
take huge quantities of data before they yield reasonable performance, you have
to do a lot of annotation just to find out an idea doesn't work.

A reasonable interpretation of the current results is that pretraining lets you
use a larger model than your training data could otherwise support. The
previous work has shown that pretraining lets us make very large models, and
those models will let us hit state-of-the-art accuracies even when the training
corpus is quite large. It wasn't clear from the previous work whether
pretraining would also improve results for a small model. My results so far
suggest it does, but so far only when the training data is small.

I'm now pre-training a larger CNN, to check that my results match up with
previous work in finding that this improves accuracy on the full dataset. This
could also be a nice option for spaCy users, who want more accuracy even if it
means slower runtimes.


