# Deep-Atrous-CNN-Text-Network: End-to-end word level model for sentiment analysis and other text classifications

A Deep Atrous CNN architecture suitable for text (sentiment) classification with variable length.

The architecture substitutes the typical CONV->POOL->CONV->POOL->...->CONV->POOL->SOFTMAX architectures, instead to speed up computations it uses atrous convolutions which are resolution perserving. Another great property of these type of networks is the short travel distance between the first and last words, where the path between them is bounded by C*log(d) steps, where C is a constant and d is the length of the input sequence.

The architecture is inspired by the [Neural Machine Translation in Linear Time](https://arxiv.org/abs/1610.10099) and [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882).

Where the Atrous CNN layers are similar to the ones in the bytenet encoder in [Neural Machine Translation in Linear Time](https://arxiv.org/abs/1610.10099) and the max-over-time pooling idea was inspired from the [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882) paper.

<p align="center">
  <img src="https://raw.githubusercontent.com/randomrandom/deep-atrous-cnn-sentiment/master/png/architecture.png" width="1024"/>
</p>

The network support embedding initialization with pre-trained GloVe vectors ([GloVe: Gloval Vectors for Word Representations](https://nlp.stanford.edu/pubs/glove.pdf)) which handle even rare words quite well compared to word2vec.

To speed up training the model pre-processes any input into "clean" file, which then utilizes for training. The data is read by line from the "clean" files for better memory management. All input data is split into the appropriate buckets and dynamic padding is applied, which provides better accuracy and speed up during training. The input pipeline can read from multiple data sources which makes addition of more data sources easy as long as they are preprocessed in the right format. The model can be trained on multiple GPUs if the hardware provides this capability.

<p align="center">
  <img src="https://raw.githubusercontent.com/randomrandom/deep-atrous-cnn-sentiment/master/png/queue_example.gif" width="1024"/>
</p>

(Some images are cropped from [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499), [Neural Machine Translation in Linear Time](https://arxiv.org/abs/1610.10099) and [Tensorflow's Reading Data Tutorial](https://www.tensorflow.org/programmers_guide/reading_data)) 

## Version

Current version : __***0.0.0.1***__

## Dependencies ( VERSION MUST BE MATCHED EXACTLY! )
1. python3.5
1. arrow==0.10.0
1. numpy==1.13.0
1. pandas==0.20.2
1. protobuf==3.3.0
1. python-dateutil==2.6.0
1. pytz==2017.2
1. six==1.10.0
1. sugartensor==1.0.0.2
1. tensorflow==1.2.0
1. tqdm==4.14.0

## Installation
1. python3.5 -m pip install -r requirements.txt
1. install tensorflow or tensorflow-gpu, depending on whether your machine supports GPU configurations

## Dataset & Preprocessing 
Currently the only supported dataset is the one provided by the [Bag of Words Meets Bags of Popcorn](https://www.kaggle.com/c/word2vec-nlp-tutorial/rules) challenge, instructions how to obtain and preprocess it can be found [here](https://github.com/randomrandom/deep-atrous-cnn-sentiment/tree/master/data/datasets/kaggle_popcorn_challenge)

The Kaggle dataset contains 25,000 labeled examples of movie reviews. Positive movie reviews are labeled with 1, while negative movie reviews are labeled with 0. The dataset is split into 20,000 training and 5,000 validation examples.
## Training the network

The model can be trained across multiple GPUs to speed up the computations. In order to start the training:

Execute
<pre><code>
python train.py ( <== Use all available GPUs )
or
CUDA_VISIBLE_DEVICES=0,1 python train.py ( <== Use only GPU 0, 1 )
</code></pre>

Currently the model achieves up to 97% accuracy on the validation set.

## Monitoring and Debugging the training
In order to monitor the training, validation losses and accuracy and other interesting metrics like gradients, activations, distributions, etc. across layers do the following:


```
# when in the project's root directory
bash launch_tensorboard.sh
```

then open your browser [http://localhost:6008/](http://localhost:6008/)

<p align="center">
  <img src="https://raw.githubusercontent.com/randomrandom/deep-atrous-cnn-sentiment/master/png/tensorboard.png" width="1024"/>
</p>

(kudos to [sugartensor](https://github.com/buriburisuri/sugartensor) for the great tf wrapper which handles all the monitoring out of the box)

## Testing
This version of the model provides interactive testing, in order to start it, execute:

<pre><code>
python test.py ( <== Use all available GPUs )
or
CUDA_VISIBLE_DEVICES=0,1 python test.py ( <== Use only GPU 0, 1 )
</code></pre>

The console will ask for input, some sample manual test over examples of the dataset:

```
>this is an intimate movie of a sincere girl in the real world out of hollywoods cheap fantasy is a very good piece of its class , and ashley judd fills the role impeccably . it may appear slo
w for thrill seekers though . cool movie for a calm night . br br
> Sentiment score:  0.538484

>the silent one - panel cartoon henry comes to fleischer studios , billed as the worlds funniest human in this dull little cartoon . betty , long past her prime , thanks to the production code
 , is running a pet shop and leaves henry in charge for far too long - - five minutes . a bore .
> Sentiment score:  0.0769837

>in her first nonaquatic role , esther williams plays a school teacher whos the victim of sexual assault . she gives a fine performance , proving she could be highly effective out of the swimm
ing pool . as the detective out to solve the case , george nader gives perhaps his finest performance . and he is so handsome it hurts ! john saxon is the student under suspicion , and althoug
h he gets impressive billing in the credits , its edward andrews as his overly - protective father who is the standout . br br bathed in glorious technicolor , the unguarded moment is irresist
ible hokum and at times compelling drama .
> Sentiment score:  0.832277
```

## Future works
1. Increase the number of supported datasets
1. Put everything into Docker
1. Create a REST API for an easy deploy as a service

## My other repositories
1. [Deep-Atrous-CNN-NER](https://github.com/randomrandom/deep-atrous-ner)

## Citation

If you find this code useful please cite me in your work:

<pre><code>
George Stoyanov. Deep-Atrous-CNN-Text-Network. 2017. GitHub repository. https://github.com/randomrandom.
</code></pre>

## Authors
George Stoyanov (georgi.val.stoyan0v@gmail.com)
