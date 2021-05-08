# neural-sentiment
A sentiment analyzer using deep rnns, built with TensorFlow.

### Installation & Dependency Instructions

1. Python 2 or 3
2. Install [TensorFlow 1.2]https://www.tensorflow.org/install/)
3. `$ pip install nltk`

Next you will need to download the nltk tokenizer dataset:

1. run a python session in terminal `$ python`
2. `>>> import nltk`
3. `>>> nltk.download()`
4. type 'd', then hit enter
5. type 'punkt' then hit enter

You can exit the python terminal once the download is done, your dependencies will be all setup.

### Usage Instructions

To run with preset hyper-parameters just run:

`$ python train.py`

To try other hyper-parameters, you can change them in the config file. If you want to provide your own:

`$ python train.py --config_file="path_to_config"`

Descripton of hyper parameters:

|   Name               | Type          |     Description                            |
| :-------------------:|:-------------:|:-------------------------------------------|
| hidden_size          | int           | number of hidden units in hidden layers    |
| num_layers           | int           |   number of hidden layers                  |
| batch_size           | int           |    size of batchs in training              |
| max_epoch            | int           |    max number of epochs to train for       |
| learning_rate        | float         |    beggining learning rate                 |
| steps_per_checkpoint | int           |    number of steps before running test set |
| lr_decay_factor      | float         |    factor by which to decay learning rate  |
| batch_size           | int           |    size of batchs in training              |
| max_seq_length       | int           |    maximum length of input token sequence  |
| checkpoint_dir       | string        |    directory to store/restore checkpoints  |
| dropout              | float         | probability of hidden inputs being removed |
| grad_clip            | int           |    max gradient norm                       |


When you first run train.py, it will download the data set, unzip, and process it. This will take several minutes. The training will begin automatically after this is done.

After your model is trained you can run:

`$ python sample.py --text="Your text to sample here"`

It will return 0 or 1. This number corresponds to a positive (1), or a negative (0) score.

### Model

The model is: embedding layer -> LSTMCells -> logistic regression output layer. I'll provide a picture in the future.

The hidden state averaged across all time steps is what is passed to the logistic regression layer.

### Tensorboard Usage

I've begun to implement tensorboard variables and histograms.

You can access tensorboard with this application by using:

`$ tensorboard --logdir=/tmp/tb_logs/`

Then copy and paste the localhost url your terminal window gives you, into your browser of choice.

There isn't much to see right now except an overview of the graph. I will include screenshots of this down the road as I add more tensorboard functionality to this project.

### Results

Pre-trained model will be committed soon. Currently with defaults, it gets about 70%.
I would like to get it to about 80-85% before committing the model.

### Attribution
Thanks to reddit user /u/LeavesBreathe for the help with getting the last hidden state

The dataset used was the [Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/).

I also referred to this [tutorial](http://deeplearning.net/tutorial/lstm.html) as a starting point
