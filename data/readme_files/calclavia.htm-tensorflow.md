# Hierarchical Temporal Memory in Tensorflow
An implementation of Numenta's HTM algorithm in Tensorflow with GPU support.
API design based on Keras API.

## Setup
Install Python 3.5 and PIP. Then run the following command to install all project
dependencies.

```
pip install -r requirements.txt
```

See Tensorflow's documentation on GPU setup.

## Experiments
### MNIST
Experiment with MNIST dataset using an HTML spatial pooler and 1 layer neural
network softmax classifier.

Ensure that the MNIST dataset is placed into the data folder in its zipped format.

http://yann.lecun.com/exdb/mnist/

```
python mnist.py
```

Results using the provided hyperparameters achieve ~95% validation accuracy.
