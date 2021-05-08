<div align="center">
  <img src="img/logo.png">
</div>

# tensorflow-qnd

[![PyPI version](https://badge.fury.io/py/tensorflow-qnd.svg)](https://badge.fury.io/py/tensorflow-qnd)
[![Python versions](https://img.shields.io/pypi/pyversions/tensorflow-qnd.svg)](setup.py)
[![Build Status](https://travis-ci.org/raviqqe/tensorflow-qnd.svg?branch=master)](https://travis-ci.org/raviqqe/tensorflow-qnd)
[![License](https://img.shields.io/badge/license-unlicense-lightgray.svg)](https://unlicense.org)

Quick and Dirty TensorFlow command framework

tensorflow-qnd is a TensorFlow framework to create commands to train and
evaluate models and make inference with them.
The framework is built on top of
[tf.contrib.learn module](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn).
Especially if you are working on research projects using TensorFlow, you can
remove most of boilerplate code with the framework.
All you need to do is to define a model constructor `model_fn` and input
producer(s) `input_fn` to feed a dataset to the model.

## Features

-   Command creation for:
    -   Training and evaluation of models
    -   Inference of labels or regression values with trained models
-   Configuration of command line options to set hyperparameters of models etc.
-   [Distributed TensorFlow](https://www.tensorflow.org/how_tos/distributed/)
    -   Just set an optional argument `distributed` of `def_train_and_evaluate()`
        as `True` (i.e. `def_train_and_evaluate(distributed=True)`) to enable it.
    -   Supports only data parallel training
    -   Only for training but not for inference

## Installation

Python 3.5+ and TensorFlow 1.1+ are required.

```
pip3 install --user --upgrade tensorflow-qnd
```

## Usage

1.  Add command line arguments with `add_flag` and `add_required_flag` functions.
2.  Define a `train_and_evaluate` or `infer` function with
    `def_train_and_evaluate` or `def_infer` function
3.  Pass `model_fn` (model constructor) and `input_fn` (input producer) functions
    to the defined function.
4.  Run the script with appropriate command line arguments.

For more information, see [documentation](https://raviqqe.github.io/tensorflow-qnd/qnd).

## Examples

`train.py` (command script):

```python
import logging
import os

import qnd

import mnist


train_and_evaluate = qnd.def_train_and_evaluate(
    distributed=("distributed" in os.environ))


model = mnist.def_model()


def main():
    logging.getLogger().setLevel(logging.INFO)
    train_and_evaluate(model, mnist.read_file)


if __name__ == "__main__":
    main()
```

`mnist.py` (module):

```python
import qnd
import tensorflow as tf


def _preprocess_image(image):
    return tf.to_float(image) / 255 - 0.5


def read_file(filename_queue):
    _, serialized = tf.TFRecordReader().read(filename_queue)

    def scalar_feature(dtype): return tf.FixedLenFeature([], dtype)

    features = tf.parse_single_example(serialized, {
        "image_raw": scalar_feature(tf.string),
        "label": scalar_feature(tf.int64),
    })

    image = tf.decode_raw(features["image_raw"], tf.uint8)
    image.set_shape([28**2])

    return _preprocess_image(image), features["label"]


def serving_input_fn():
    features = {
        'image': _preprocess_image(tf.placeholder(tf.uint8, [None, 28**2])),
    }

    return tf.contrib.learn.InputFnOps(features, None, features)


def minimize(loss):
    return tf.train.AdamOptimizer().minimize(
        loss,
        tf.contrib.framework.get_global_step())


def def_model():
    qnd.add_flag("hidden_layer_size", type=int, default=64,
                 help="Hidden layer size")

    def model(image, number=None, mode=None):
        h = tf.contrib.layers.fully_connected(image,
                                              qnd.FLAGS.hidden_layer_size)
        h = tf.contrib.layers.fully_connected(h, 10, activation_fn=None)

        predictions = tf.argmax(h, axis=1)

        if mode == tf.contrib.learn.ModeKeys.INFER:
            return predictions

        loss = tf.reduce_mean(
            tf.nn.sparse_softmax_cross_entropy_with_logits(labels=number,
                                                           logits=h))

        return predictions, loss, minimize(loss), {
            "accuracy": tf.contrib.metrics.streaming_accuracy(predictions,
                                                              number)[1],
        }

    return model
```

With the code above, you can create a command with the following interface.

```
usage: train.py [-h] [--output_dir OUTPUT_DIR] [--train_steps TRAIN_STEPS]
                [--eval_steps EVAL_STEPS]
                [--min_eval_frequency MIN_EVAL_FREQUENCY]
                [--num_cores NUM_CORES] [--log_device_placement]
                [--save_summary_steps SAVE_SUMMARY_STEPS]
                [--save_checkpoints_steps SAVE_CHECKPOINTS_STEPS]
                [--keep_checkpoint_max KEEP_CHECKPOINT_MAX]
                [--batch_size BATCH_SIZE]
                [--batch_queue_capacity BATCH_QUEUE_CAPACITY]
                [--num_batch_threads NUM_BATCH_THREADS] --train_file
                TRAIN_FILE [--filename_queue_capacity FILENAME_QUEUE_CAPACITY]
                --eval_file EVAL_FILE [--hidden_layer_size HIDDEN_LAYER_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --output_dir OUTPUT_DIR
                        Directory where checkpoint and event files are stored
                        (default: output)
  --train_steps TRAIN_STEPS
                        Maximum number of train steps (default: None)
  --eval_steps EVAL_STEPS
                        Maximum number of eval steps (default: 100)
  --min_eval_frequency MIN_EVAL_FREQUENCY
                        Minimum evaluation frequency in number of train steps
                        (default: 1)
  --num_cores NUM_CORES
                        Number of CPU cores used. 0 means use of a default
                        value. (default: 0)
  --log_device_placement
                        If specified, log device placement information
                        (default: False)
  --save_summary_steps SAVE_SUMMARY_STEPS
                        Number of steps every time of which summary is saved
                        (default: 100)
  --save_checkpoints_steps SAVE_CHECKPOINTS_STEPS
                        Number of steps every time of which a model is saved
                        (default: None)
  --keep_checkpoint_max KEEP_CHECKPOINT_MAX
                        Max number of kept checkpoint files (default: 86058)
  --batch_size BATCH_SIZE
                        Mini-batch size (default: 64)
  --batch_queue_capacity BATCH_QUEUE_CAPACITY
                        Batch queue capacity (default: 1024)
  --num_batch_threads NUM_BATCH_THREADS
                        Number of threads used to create batches (default: 2)
  --train_file TRAIN_FILE
                        File path of train data file(s). A glob is available.
                        (e.g. train/*.tfrecords) (default: None)
  --filename_queue_capacity FILENAME_QUEUE_CAPACITY
                        Capacity of filename queues of train, eval and infer
                        data (default: 32)
  --eval_file EVAL_FILE
                        File path of eval data file(s). A glob is available.
                        (e.g. eval/*.tfrecords) (default: None)
  --hidden_layer_size HIDDEN_LAYER_SIZE
                        Hidden layer size (default: 64)
```

Explore [examples](examples) directory for more information and see how to run
them.


## Caveats

### Necessary update of a global step variable

As done in [examples](examples), you must get a global step variable with
`tf.contrib.framework.get_global_step()` and update (increment) it in each
training step.

### Use streaming metrics for `eval_metric_ops`

When non-streaming metrics such as `tf.contrib.metrics.accuracy` are used in a
return value `eval_metric_ops` of your `model_fn` or as arguments of
`ModelFnOps`, their values will be ones of the last batch in every evaluation
step.

## Contributing

Please send issues about any bugs, feature requests or questions, or pull
requests.

## License

[The Unlicense](https://unlicense.org)
