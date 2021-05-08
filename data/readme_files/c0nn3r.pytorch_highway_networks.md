# PyTorch Highway Networks
[Highway networks](https://arxiv.org/abs/1505.00387) implemented in [PyTorch](http://www.pytorch.org).

![Highway Equation](images/highway.png)

Just the [MNIST example](https://github.com/pytorch/examples/tree/master/mnist) from [PyTorch](http://www.pytorch.org) hacked to work with Highway layers.

## Todo
- ~~Make the Highway `nn.Module` reuseable and configurable.~~
- Why does softmax work better than sigmoid? This shouldn't be the case...
- Make training graphs on the MNIST dataset.
- Add convolutional highway networks.
- Add recurrent highway networks.
- Experiment with convolutional highway networks for character embeddings.

## Notes
- ELU doesn't work better than RELU for the layer activation.
- Softmax seems to work better than sigmoid for the gate function?!
