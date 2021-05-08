# Tensorflow Seq2Seq For Conversations
## Build conversation Seq2Seq models with TensorFlow

Takes dialog data and trains a model to make responses for a conversation input.

## Dependencies 
* [Tensorflow](https://github.com/tensorflow/tensorflow)
* [Numpy](https://github.com/numpy/numpy)

## Data format
Data must be formated as *input text,output text* for each exchange. File must be named \[dialogs.csv\]. **note: no space between the input text or ouput text in relation to the comma.**

Example data:  
hi,hello  
how are you?,i'm well  
what is your name?,my name is john  

Before TensorFlow builds the model we compile a dictionary of all the words in the training set to convert them to vectors. The code has a word frequency minimum by default, but you can uncomment one line to use every word in the dataset. The function is create_dictionary() near the bottom if you wish to do so.

Once the dictionary is built(This can take a few hours!) TensorFlow makes the model and starts training.  

## train.py
`python train.py -dialog_path -units -layers -training_iterations -batch_size --restore --display_out --load_dictionary`

Required to build:
- dialog_path: path to the dialog csv ex: /user/dialog_folder/
- units: number of neurons per GRU cell
- layers: number of layers deep for the recurrent model (min. 1)
- training_iteration: number of mini-batches to train on
- batch_size: number of dialog pairs per mini-batch

Not required:
- --restore: restores the model from a past save
- --display_out: displays a feed-forward of the model to the console
- --load_dictionary: uses a pre-built dictionary. Use this once you have built the model at least once. It save computing time.

All of the **Not Required** args are booleans that are entered automatically.

Example:
`python train.py ~/adam/tensorflow_seq2seq/ 512 4 1000000 32`
Makes a new model where the data is at "~/adam/tensorflow_seq2seq/". The model has 512 neurons per GRU cell and is 4 layers deep. The program will run for 1,000,000 iterations with a batch size of 32. 

`python train.py ~/adam/tensorflow_seq2seq/ 512 4 1000000 32 --restore --display_out --load_dictionary`
This command will build the same model above and restore from a past save. This command will display a feed-forward pass after each training iteration. Also this command will use a past dictionary that is generated after the first run of the model. 

## test.py
`python test.py -dialog_path -units -layers`

Required to build:
- dialog_path: use the same path as used to train the model
- units: use the same number of neurons as when training
- layers: use the same number of layers as when training

Example:
`python train.py ~/adam/tensorflow_seq2seq/ 512 4`
This will use the model above after training. Once you run this a "> " will appear. Type in anything you want to see the output of the model. 


## Notes:  

FYI: To train this model you need something like a GTX TITAN X or a cluster computer and a lot of time. Not for the Deep Learning weary. 
