# mnist-tensorboard-embeddings
[![Build Status](https://travis-ci.org/normanheckscher/mnist-tensorboard-embeddings.svg?branch=master)](https://travis-ci.org/normanheckscher/mnist-tensorboard-embeddings)

TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs. The TensorFlow documentation isn't extremely
explicit with the how-to visualizations. The code within `mnist_t-sne.py`
is a working example of how to implement a 3-dimensional visualization
with the MNIST dataset and it's embedded images.

The full tutorial is on the [TensorFlow website](https://www.tensorflow.org/how_tos/embedding_viz/).

By default, the Embedding Projector performs 3-dimensional
[principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis),
meaning it takes high-dimensional data and tries to find a
structure-preserving projection onto three dimensional space. Basically, it does
this by rotating the data so that the first three dimensions reveal as much of
the variance in the data as possible. There's a nice visual explanation
[here](http://setosa.io/ev/principal-component-analysis/). Another extremely
useful projection is
[t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding).

# Requirements
- [Tensorflow](http://www.tensorflow.org) r1.0

# Sample output

<video autoplay loop style="max-width: 100%;">
  <source src="https://www.tensorflow.org/images/embedding-mnist.mp4" type="video/mp4">
  Sorry, your browser doesn't support HTML5 video in MP4 format.
</video>

Run the `mnist_t-sne.py` file from within its directory to generate the
embeddings and visualisation.

Once you have event files, run TensorBoard and provide the log directory. If
you're using a precompiled TensorFlow package (e.g. you installed via pip), run:

```
tensorboard --logdir=path/to/logs
```

This should print that TensorBoard has started. Next, connect to http://localhost:6006.

TensorBoard requires a `logdir` to read logs from. For info on configuring
TensorBoard, run `tensorboard --help`.

TensorBoard can be used in Google Chrome or Firefox. Other browsers might
work, but there may be bugs or performance issues.

The second file, ` mnist_with_summaries.py`, is a full example of the
embedding,visualization and a subsequent model generation. This second
file mostly mirrors the official TensorFlow tutorial file.

# Contribution
Your comments (issues) and PRs are always welcome.
