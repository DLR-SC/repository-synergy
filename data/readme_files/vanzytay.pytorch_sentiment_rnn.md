# Sentiment Analysis with Pytorch [WIP]

**UPDATE/NOTE: Hi all, I do not work on this repository anymore! Please use at your own discretion since I would consider it strongly deprecated. In fact, this was just me testing Pytorch when it first came out. As I fundamentally code in TF, I wouldn't be able to answer any questions on this repo. Plus, I coded this about more than a year ago. Thanks!** 

Pytorch Example For Aspect-based Sentiment Analysis with RNN / GRUs / LSTMs on SemEval 2014. 

Currently we implemented a baseline LSTM/RNN/GRU model with a linear layer on the *last* output along with a target-dependent, TD-LSTM (Tang et al 2015) model for Aspect based sentiment analysis (ABSA). 

The sequences are padded with zeros *from the front* so that the last vector is not zero. We pad these in the prepare script using keras pad sequences. Nothing is masked so far and we pad to the max length. 

There are two modes of prediction, namely `term` and `aspect`. Aspect refers to aspect **categories** while term refers to, well, **terms** which are sequences that **can** be found in the text itself. There are two datasets, Laptop and Restaurants. There are both term and aspect settings for Laptop but only aspect setting for restaurants.

# Usage

Before running prepare.py you need a folder `../embedding/` one directory higher than project root. (That is where my glove embeddings to avoid copying them in every single project)

## Data Preperation

1) Download glove embeddings from paper. 

```
Jeffrey Pennington, Richard Socher, and Christopher D
Manning. 2014. Glove: Global vectors for word representation.
Proceedings of the Empiricial Methods
in Natural Language Processing (EMNLP 2014),
12:1532–1543.
```

2) Make directory
```
mkdir ../glove_embeddings
```

3) place glove.840B.300d.txt into ../glove_embeddings

```
python prepare.py         # Will take awhile.
```
This should build into `./store` and `./embeddings/`. The former is the environment object that `train.py` reads while the file written into embeddings is just a smaller concised version of glove so  that I can rerun prepare.py fast. 

For training and evaluation, run the following script. Evaluates accuracy every epoch. (Note, it takes awhile for the model to stop predicting all the same class)

```
python train.py --batch-size 20 --rnn_type GRU --cuda --gpu 1 --lr 0.0001 --mdl RNN --clip_norm 1 --opt Adam
```

This should give
```
[Epoch 50] Train Loss=0.680990989366
Test loss=0.810974478722
Output Distribution={0: 158, 1: 158, 2: 804}
Accuracy=0.733035714286
```
After 50 epoches.

We also support TD-LSTM (target-dependent LSTM)

```
python train.py --batch-size 20 --rnn_type GRU --cuda --gpu 1 --lr 0.0001 --mdl TD-RNN --clip_norm 1 --opt Adam
```

```
[Epoch 50] Train Loss=0.641238689423
Test loss=0.838252484798
Output Distribution={0: 178, 1: 122, 2: 820}
Accuracy=0.70625
```

Seems like TD-LSTM does nothing to improve the results on this dataset. 

## Notes

1) Basic LSTM/RNN/GRU works! Testing on SemEval (Term Category + Restaurants) give about 73-75% accuracy around epoch 20. This is the same result I previously got using TensorFlow. The algorithm constantly predicts the same class (2) for the first 10+ iterations though. 

2) Handling Gradiet Clipping is done as follows:

```
if(self.args.clip_norm>0):
    coeff = clip_gradient(self.mdl, self.args.clip_norm)
    for p in self.mdl.parameters():
        p.grad.mul_(coeff)
self.optimizer.step()
```
Not sure if this is correct or not.

3) It seems like RNNs in pyTorch are batch-minor, i.e, seq length is dim 0 and batch is dim 1. Let's wait for more variable length support.

4) Pretrained embeddings are supported. (I loaded GloVe)

5) I wonder how to make the embedding layer non-trainable?


#### Additional Notes on Dataset Pre-processing

1) I fixed 3 aspect terms in the restaurant dataset which are **clearly** typos.

```
====================
[384, 4494, 358, 2389, 2569, 964, 4686, 182, 2817, 2580, 322, 3501, 303, 3387, 4065, 940, 2]
['good', 'atmosphere', 'combination', 'of', 'all', 'the', 'hottest', 'music', 'dress', 'code', 'is', 'relatively', 'strict', 'except', 'on', 'fridays', '']
['dress', 'cod']
[Warning] Target not found in text!
====================
[1632, 5071, 4437, 1065, 2865, 1419, 3900, 1380, 903, 119, 2930, 1844, 3201, 4002, 2]
['interesting', 'other', 'dishes', 'for', 'a', 'change', 'include', 'chicken', 'in', 'curry', 'sauce', 'and', 'salmon', 'caserole', '']
['chicken', 'in', 'curry', 'sauc']
[Warning] Target not found in text!
====================
[368, 4523, 4426, 3782, 897, 2044, 2465, 1496, 4558, 384, 4997, 2865, 3860, 4264, 4044, 2671, 964, 1674, 719, 2]
['they', 'should', 'have', 'called', 'it', 'mascarpone', 'with', 'chocolate', 'chips', 'good', 'but', 'a', 'far', 'cry', 'from', 'what', 'the', 'name', 'implies', '']
['mascarpone', 'with', 'chocolate', 'chip']
[Warning] Target not found in text!
```






