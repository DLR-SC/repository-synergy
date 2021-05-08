# Temporal Tessellation: A Unified Approach for Video Analysis


Implementation of video captioning from the paper ["Temporal Tessellation: A Unified Approach for Video Analysis"](https://arxiv.org/abs/1612.06950)

Before going further please watch this:
[ICCV 2017 spotlight](https://www.youtube.com/watch?v=XPcvNxhoh58)

This method has won the Large Scale Movie Description and Understanding Challenge at ECCV 2016. 

## Dependencies

This code is written in python. To use it you will need:

* Python 2.7
* tensorflow 0.8

### Getting data
Getting the data:
https://sites.google.com/site/describingmovies/lsmdc-2016/download

## Preparing the data

Suppose you have video descriptors and the matching cpations in a shared space. 
Please refer to:

    my_reader.py

For a detailed exaplantaion of how to prepare the data for training.

Note that you will need to set the data directory in 

    constants.py

## Training  models

To train your own models, simply run 

    python driver.py

As the model trains, it will periodically evaluate on the development set and save predicted captions to file. 

`rnn.Mpiiconfig` has many hyperparameters;
Descriptions of each hyperparameter follow:


#### Architecture
* **init_scale**: weights initial scale.
* **num_layers**: the LSTM number of layers
* **keep_prob**: dropout probability of keeping weights.
* **hidden_size**: LSTM number of units
* **input_feature_num**: The size of the input to the LSTM

#### Training
* **learning_rate**: learning rate initial value
* **batch_size**: the size of a minibatch.
* **max_epoch**: number of epochs that were trained with the initial learning rate
* **grad_clip**: magnitude at which to clip the gradient

## Reference

If you found this code useful, please cite the following paper:

Dotan kaufman, Gil levi, Tal Hassner, Lior wolf. **"Temporal Tessellation: A Unified Approach for Video Analysis."** 
