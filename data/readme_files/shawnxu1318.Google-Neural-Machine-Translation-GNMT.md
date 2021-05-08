## Note: The current repository is out-dated, and has not been maintained for a while. It is not a good resource if you want to reproduce GNMT any more. Recently, I plan to work on MT problem again, and our team might re-implement this model in a modern way again. 

# Google-Neural-Machine-Translation-GNMT

It is a tensorflow implementation of [GNMT published by google][1]

Keyword: Machine Translation

Tensorflow Version: 0.11.0

## Abstract 
Neural Machine Translation (NMT) is an end-to-end learning approach for automated translation, with the potential to overcome many of the weaknesses of conventional phrase-based translation systems. Unfortunately, NMT systems are known to be computationally expensive both in training and in translation inference. Also, most NMT systems have difficulty with rare words. These issues have hindered NMT's use in practical deployments and services, where both accuracy and speed are essential. In this work, we present GNMT, Google's Neural Machine Translation system, which attempts to address many of these issues. Our model consists of a deep LSTM network with eight encoder and eight decoder layers using attention and residual connections. To improve parallelism and therefore decrease training time, our attention mechanism connects the bottom layer of the decoder to the top layer of the encoder. To accelerate the final translation speed, we employ low-precision arithmetic during inference computations. To improve handling of rare words, we divide words into a limited set of common sub-word units ("word pieces") for both input and output. This method provides a good balance between the flexibility of "character"-delimited models and the efficiency of "word"-delimited models, naturally handles translation of rare words, and ultimately improves the overall accuracy of the system. Our beam search technique employs a length-normalization procedure and uses a coverage penalty, which encourages a generation of an output sentence that is most likely to cover all the words in the source sentence. On the WMT'14 English-to-French and English-to-German benchmarks, GNMT achieves competitive results to state-of-the-art. Using a human side-by-side evaluation on a set of isolated simple sentences, it reduces translation errors by an average of 60% compared to Google's phrase-based production system.

![demo](https://cloud.githubusercontent.com/assets/10870023/21465785/ef85ceb8-c965-11e6-9e02-3903fc8cc898.gif)

## What is implemented 

- bidirection lstm

- stacked residual lstm

- attention model

- multi-GPU

the structure is something like this:
![model](https://cloud.githubusercontent.com/assets/10870023/21465786/f6f80422-c965-11e6-9b9e-609a5f87fb03.png)


## What will be implemented

- sub-word and one-to-many will be implemented in the future

## References
[MIT][12]

[1]: https://arxiv.org/abs/1609.08144
[12]: https://abhshkdz.mit-license.org/



