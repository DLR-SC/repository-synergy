# CNN Image Classifier

## Overview

A Simple Deep Neural Network to classify images made with Keras. This supports binary and multiclass classification.

## Requirements

  * Keras = 2.x (TensorFlow backend)
  * Numpy = 1.x

## Usage

First, collect training and validation data and deploy it like this(for multiclass classification),
```
./data/
  train/
    pizza/
      pizza1.jpg
      pizza2.jpg
      ...
    poodle/
      poodle1.jpg
      poodle2.jpg
      ...
    rose/
      rose1.jpg
      rose2.jpg
      ...
  validation/
    pizza/
      pizza1.jpg
      pizza2.jpg
      ...
    poodle/
      poodle1.jpg
      poodle2.jpg
      ...
    rose/
      rose1.jpg
      rose2.jpg
      ...
```

and then run train script.

```
python src/train-multiclass.py
```

Train script makes model and weights file to `./output/`.

To test another images, run

```
python src/predict-multiclass.py
```

After training, you'll have tensorboard log in `./tf-log/`
So you can see the result

```
tensorboard --logdir=./tf-log
```
