# Tweet2Vec
Please Cite: [Soroush Vosoughi, Prashanth Vijayaraghavan and Deb Roy. (2016). Tweet2Vec: Learning Tweet Embeddings using Character-level CNN-LSTM Encoder-Decoder. In Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2016). Pisa, Italy.](http://dx.doi.org/10.1145/2911451.2914762)
##Requirements
1. numpy
2. Theano
3. joblib


##Training:
Create subdirectories to store logs and models. However you can specify your own dir from command line:
logs/
all_data/


Use the following command to see all the options & hyperparameters for training that can be specified from command line:

```THEANO_FLAGS=mode=FAST_RUN,device=gpu1,floatX=float32 PYTHONPATH=. python model/train.py -h```

Using default parameters, training can be performed by :
```THEANO_FLAGS=mode=FAST_RUN,device=gpu1,floatX=float32 PYTHONPATH=. python model/train.py -t -i ./train_file.json -m "new_model" -E 3```

Training data format is provided in sample.json. However, the tweet1 & tweet2 need to be a modified version. It could either be replies to tweets which have similar meaning or just synonym modified version of the tweet.


NOTE: Training takes a long time!  The cost is the total sum of the log probabilities across each batch, timestep and decoder.  Note that the Cost will fluxuate a lot. You could experiment with other loss functions as in loss.py.
It takes more than a week to get good vectors.

##Embeddings

Use the following command to see all the options & parameters for getting embeddings that can be specified from command line:


```THEANO_FLAGS=mode=FAST_RUN,device=gpu1,floatX=float32 PYTHONPATH=. python model/embeddings.py -h```

Get embedding using the following command:
```THEANO_FLAGS=mode=FAST_RUN,device=gpu1,floatX=float32 PYTHONPATH=. python model/embeddings.py -R -i /res/tweets.json -m "new_model" -e 3 -o "/res/emb.npy"```




