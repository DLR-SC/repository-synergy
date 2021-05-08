<p align="center">
 <img src="./assets/logo.png" alt="Drawing", width=40%>
</p>

Tune the hyperparameters of your PyTorch models with **HyperSearch**.

## Requirements

* Python 3.5+
* [PyTorch](http://pytorch.org/) 0.4+
* tqdm

## API

**Note:** We currently only support FC networks. ConvNet support coming soon!

* Install requirements using:

```
pip install -r requirements.txt
```
* Define your model in `model.py`. This should return a `nn.Sequential` object. Take note of the last layer, i.e. using `nn.LogSoftmax()` vs. `nn.Softmax()` will require possible changes in the training method. For example, let's define a 4 layer FC network as follows:
```
Sequential(
  (0): Linear(in_features=784, out_features=512)
  (1): ReLU()
  (2): Linear(in_features=512, out_features=256)
  (3): ReLU()
  (4): Linear(in_features=256, out_features=128)
  (5): ReLU()
  (6): Linear(in_features=128, out_features=10)
  (7): LogSoftmax()
)
```
* Write your own `data_loader.py` if you **do not** have a dataset that is supported by `torchvision.datasets`. Else, slightly edit `data_loader.py` to suit your dataset of choice: `CIFAR-10`, `CIFAR-100`, `Fashion-MNIST`, `MNIST`, etc.
* Create your hyperparameter dictionary in `main.py`. You must follow the following syntax:

```python
params = {
    '2_hidden': ['quniform', 512, 1000, 1],
    '4_hidden': ['quniform', 128, 512, 1],
    'all_act': ['choice', [[0], ['choice', ['selu', 'elu', 'tanh']]]],
    'all_dropout': ['choice', [[0], ['uniform', 0.1, 0.5]]],
    'all_batchnorm': ['choice', [0, 1]],
    'all_l2': ['uniform', 1e-8, 1e-5],
    'optim': ['choice', ["adam", "sgd"]],
}
```
Keys are of the form `{layer_num}_{hyperparameter}` where `layer_num` can be a layer from your `nn.Sequential` model or `all` to signify all layers. Values are of the form `[distribution, x]` where `distribution` can be one of `uniform`, `quniform`, `choice`, etc.

For example, `2_hidden: ['quniform', 512, 1000, 1]` means to sample the hidden size of layer 2 of the model (`Linear(in_features=512, out_features=256)`) from a quantile uniform distribution with lower bound 512, upper bound 1000 and `q = 1`.

`all_dropout: ['choice', [[0], ['uniform', 0.1, 0.5]]]` means to choose whether to apply dropout or not to all layers. `choice` means pick from elements in a list and `[0]` means False while the other choice, implicitly implied to mean true, means to sample Dropout probability from a uniform distribution with lower bound 0.1 and upper bound 0.5.

* Edit the `config.py` file to suit your needs. Concretely, you can edit the hyperparameters of HyperBand, the default learning rate, the dataset of choice, etc. There are 2 parameters that control the HyperBand algorithm:
  * `max_iter`: maximum number of iterations allocated to a given hyperparam config
  * `eta`: proportion of configs discarded in each round of successive halving.
  * `epoch_scale`: a boolean indicating whether `max_iter` should be computed in terms of mini-batch iterations or epochs. This is useful if you want to speed up HyperBand and don't want to evaluate a full pass on a large dataset.

Set `max_iter` to the usual amount you would train neural networks for. It's mostly a rule fo thumb, but something in the range `[80, 150]` epochs. Larger values of `nu` correspond to a more aggressive elimination schedule and thus fewer rounds of elimination. Increase to receive faster results at the cost of a sub-optimal performance. Authors advise a value of `3` or `4`.

* As a last step, depending on the last layer in your model, you may wish to edit the `train_one_epoch()` method in the `hyperband.py` file. The default uses `F.nll_loss` because it assumes the user used `LogSoftmax` but feel free to edit the loss to tailor to your needs.

Finally, you can run the algorithm using:

```
python main.py
```

## Hyperparameter Support

- [x] Activation
    - [x] all
    - [x] per layer
- [x] L1/L2 regularization (weights & biases)
    - [x] all
    - [x] per layer
- [x] Add Batch Norm
    - [x] sandwiched between every layer
- [x] Add Dropout
    - [x] sandwiched between every layer
- [ ] Add Layers
    - [ ] conv Layers
    - [ ] fc Layers
- [ ] Change Layer Params
    - [x] change fc output size
    - [ ] change conv params
- [x] Optimization
    - [x] batch size
    - [x] learning rate
    - [x] optimizer (adam, sgd)

## Todo

- [ ] **conv nn support**
- [ ] max exploration option (`s = s_max`)
- [ ] input error checking
- [ ] improve plotting and logging
- [ ] multi-gpu and multi-cpu support

## References

- [zygmuntz's hyperband](https://github.com/zygmuntz/hyperband)
- [Demo by kgjamieson](https://people.eecs.berkeley.edu/~kjamieson/hyperband.html)
