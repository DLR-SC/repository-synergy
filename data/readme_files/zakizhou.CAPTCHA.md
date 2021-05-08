# CAPTCHA
Newbie about Deep Learning and TensorFlow?

Boring with MNIST? 

Want a more interesting and complicated application?

This is for you.
This repo contains a cnn model for recognizing
numbers of captcha



## WHAT IS CAPTCHA
CAPTCHA is kind of images that contains chars and digits for people to recognize, it is used
in website log in to test you whether you are a robot or a person. In this repo we will develop
a small convolutional neural network with TensorFlow to recognize it.

For simplicity, images will only contain four digits with noise

**we say a image is classified correctly if and only if four digits inside this image are all classified correctly**

Two sample images are listed below

![image1](https://raw.githubusercontent.com/zakizhou/CAPTCHA/master/2_2704.png)

![image2](https://raw.githubusercontent.com/zakizhou/CAPTCHA/master/3_5723.png)

## requirements
python 2.7 with following packages installed should work fine
1. numpy
2. TensorFlow(verison >= 1.4) (because we will use `tf.data`)
3. captcha(you can install it with `pip install captcha`)

(anaconda environment is strongly recommended for managing these packages)

windows and python 3.X are not tested but should be OK.

GPU is not a must, but without it, training might be very slow.

## SOME FEATURES
* Train and validation images are generated on the fly, doesn't need to download any big datasets.

* Inputs of model is built on top of `tf.data` instead of old queue-based api, so reading
the code combined with the [official document](https://www.tensorflow.org/programmers_guide/datasets) about `tf.data` will help you understand how 
to write it yourself.

* Very short code, easy to read.

## USAGE
First clone this repo
```
git clone https://github.com/zakizhou/CAPTCHA
```
Before run training, training and validation images should be 
 generated, change to the root dir of this repo and run
 ```
 cd CAPTCHA
 mkdir -p images/train
 mkdir -p images/validation
 mkdir -p tfrecords
 mkdir -p save
python captcha_producer.py -n 30000 -p images/train
 ```
This will generate 30000 training images in the images/train/ and also convert infomation about 
these images into `tfrecords/train.tfrecords` file.

for validation set:
 ```
python captcha_producer.py -n 3000 -p "images/validation"
 ```

Now you can run this model with
 ```
python captcha_train.py
 ```

## Result
After 10000 steps (you can manually change num of steps in `captcha_train.py` file) training on single GTX1060, this model achieved 
around 70% accuracy, adjusting the scale of parameters or adding dropout
should still improve this performance

## Details about files
* `images/train` and `images/validation` will contains generated train and validation images
* `tfrecords` will contains about generated tfrecords(`train.tfrecords`, `validation.tfrecords`)
* `save` will contains saved model after training
* `captcha_producer.py` is used to generate images and tfrecords
* `captcha_model.py` contains utils functions for defining the model
* `captcha_data.py` is used for build input for model
* `captcha_config.py` contains configs for model
* `captcha_train.py` is used for training model
## TODO
* add multi gpu training code
* add tensorboard code
* add functions for keep on training after shutdown
