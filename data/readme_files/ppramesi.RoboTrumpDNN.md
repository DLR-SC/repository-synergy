# RoboTrumpDNN: Generating Donald Trump Speeches with Word2Vec and LSTM

------------------
*Disclaimer: This is not meant as a political analysis or opinion*

Based on Andrej Karpathy's [article](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) on text generation, I built a model for text generation in Keras. However, instead of using character-level input data, I instead use words Donald Trump uses in his speeches, along with other Republican presidential nominees speeches into Word2Vec (interesting sidenote: if you use the same hyper-parameters and the same speech dictionary, the result of "Obama" - "Strength" analogy comparison results in "Hillary" or "Clinton"), and use Donald Trump's resulting word vectors as the input. His speeches contain ~100k words with a vocabulary of ~4k words. I picked Trump because the transcripts for his speeches are more readily available, and more organic because they are not scripted (to the best of my knowledge). However, because his speeches are stream of consciousness, he tends to repeat phrases over and over again, which sometimes cause the model to get stuck in a loop when generating them, although I'm not sure that's 100% correct.

Nonetheless, I was able to get Donald Trump's speech transcripts since the beginning of his campaign from [what the folly](http://www.whatthefolly.com/). And I think the model is able to generate speeches that have...uh...Trumpian flavors?

------------------

For example:
With feed of "make the country" the model generates:
> rich. it was terrible. but saudi arabia, they make a billion dollars a day. i was the king. i was the king. i was the smartest person in yemen, we have to get to business. i have to say, but he was an early starter. and we have to get to business. i have to say, donald, i can't believe it. it's so important. but this is what they're saying, dad, you're going to be really pro, growth, blah, blah. it's disgusting what's disgusting., and it was a 19 set washer and to go to japan. did you hear that character. we are going to have to think about it. but you know, i've been nice to me. something happens in washington. the beauty of washington. not a good deal. we have to get to business. but i've always said qatar so what i do well. i think we're going to get it back. no, it's true. you know, it's about time that on iraq. he couldn't answer the question, is iraq. think of it. trillion. trillion dollars to the horrible thing he just said, "oh, give you an example. and they say, "we beat china"? you know, people say that's such a hard time even though you know i'm going to do it. remember the poll numbers are horrible. i mean, i can tell you is going to be really pro, growth, seven, 000 people. it was terrible. but saudi arabia, they make a billion dollars a day. i was the smartest person in yemen, we have to get to business. but i've always said qatar so what i do is i build a great wall. and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop and it's got to stop it. and we have to get through these 15 people to another country. and believe me, to the women, it's all about jobs. we have to get to business. i have to tell you, i love people. but i know how to go about making the deal. all of my life. like this. and it's very unfair. i feel it's very sad. now we owe $19 trillion. the budget is so bad. the imbalance is what he should. and you know, we had a really good.

But more interestingly, because I use embedding layer, each word is represented as a vector. So if I feed it to a clustering algorithm (I used KNN), [this](http://pastebin.com/k16wqVuF) is what came out. Although most of the clusters are useless, there are clusters with clear subject (e.g. the words "is", "that's", "it's", "be", "was", "are", "by", "they're", "we're", "only", "what's", "i'm", "you're", "wasn't", "family", "negotiate", "nobody's", "everyone's", "she's", "funding's", "neighbor", "something's", "damn", "understandhe's", "everything's", and "i'm" all belong to the same cluster). The code for this will come later

------------------

You need the following dependencies:

- Keras
- Theano
- numpy, scipy
- pyyaml
- HDF5 and h5py (optional, required if you use model saving/loading functions)
- Gensim Word2Vec Library
- Optional but recommended if you use CNNs: cuDNN.
- Optional for clustering: SciKit Learn 

------------------

You can change the source speech and dictionary to whatever speeches you like to reproduce. But first you'd need to create new word vectors by running
```
python build-dictionary.py
```
To run the script, enter
```
python trumpbot.py
```
to generate the weights, and then run
```
python trumpbot-generate.py
```
to generate new speech. The length of the speech is on line 104, while seed sentence is on line 52. The seed sentence's words has to exist in source.txt
