# Skeletor [![Build Status](https://travis-ci.org/noahgolmant/skeletor.svg?branch=master)](https://travis-ci.org/noahgolmant/skeletor)

Skeletor is a lightweight wrapper for research code. It is meant to enable fast, parallelizable prototyping without sacrificing reproducibility or ease of experiment analysis.

You can install it with: `pip install skeletor-ml`

## Why use skeletor?

Tracking and analyzing experiment results is easy. Skeletor uses [track](https://github.com/richardliaw/track), which provides a simple interface to log metrics throughout training and to view those metrics in a pandas DataFrame afterwards. It can log locally and to S3. Compared to other logging tools, track has minimal overhead and a very simple interface. No longer do you need to decorate every function or specify a convoluted experiment pipeline.

Orchestrating many experiments in parallel is simple and robust. Almost every experiment tracking framework implements its own scheduling and hyperparameter search algorithms. Luckily, I don't trust myself to do this correctly. Instead, skeletor uses [ray](https://github.com/ray-project/ray), a high-performance distributed execution framework. In particular, it uses [ray tune](https://ray.readthedocs.io/en/latest/tune.html) for scalable hyperparameter search. 

## Setup

Necessary packages are listed in `setup.py`.
Just run `pip install skeletor-ml` to get started.

## Basic Usage

A basic example `train.py` might look like:

```
import skeletor
from skeletor.models import build_model
from skeletor.datasets import build_dataset
from skeletor.optimizers import build_optimizer
import track

def add_args(parser):
    parser.add_argument('--arch', default='resnet50')
    parser.add_argument('--lr', default=0.1, type=float)

def train(epoch, trainloader, model, optimizer):
    ...
    return avg_train_loss

def test(epoch, testloader, model):
    ...
    return avg_test_loss

def experiment(args):
    trainloader, testloader = build_dataset('cifar10')
    model = build_model(args.arch, num_classes=10)
    opt = build_optimizer('SGD', lr=args.lr)
    for epoch in range(200):
        track.debug("Starting epoch %d" % epoch)
        train_loss = train(epoch, trainloader, model, opt)
        test_loss = test(epoch, testloader, model)
        track.metric(iteration=epoch,
                     train_loss=train_loss,
                     test_loss=test_loss)

skeletor.supply_args(add_args)
skeletor.execute(experiment)
```

You just have to supply (1) a function that adds your desired arguments to an `ArgumentParser` object, and (2) a function that runs the experiment using the parsed arguments. You can then use `track` to log statistics during training.

You can supply a third function to run analysis after training. `skeletor.supply_postprocess(postprocess_fn)` takes in a user-defined function of the form `postprocess_fn(proj)`. `proj` is a `track.Project` object.

Internally, the basic experiment flow is:

`run add_args(parser) -> parse the args -> run experiment_fn(args) -> optionally run postprocess_fn(proj)`

## Launching experiments

To launch an experiment in `train.py`, you just do `python train.py <my args> <experimentname>`. The results will go in `<logroot>/<experimentname>`. For example, you can do something like

`CUDA_VISIBLE_DEVICES=0 python train.py --arch ResNet50 --lr .1 resnet_cifar`


The same code can be used to launch several experiments in parallel. Suppose I have a config called `config.yaml` that looks like:

```
arch: ResNet50
lr:
  grid_search: [.001, .01, .1, 1.0]
```

I can test out all of these learning rates at the same time by running:

`CUDA_VISIBLE_DEVICES=0,1 python train.py --config=config.yaml --self_host=2 resnet_cifar`

Ray will handle scheduling the jobs across all available resources.

Logs (`track` records) will be stored in `<args.logroot>/<args.experimentname>`.
See the `track` docs for how to access these records as DataFrames.

## Examples

You can find an example of running a grid search for training a residual network on CIFAR-10 in PyTorch in `examples/train.py`.


## Getting experiment results

I added a utility in `skeletor.proc` for converting all `track` trial records for an experiment into a single Pandas DataFrame. It can also pickle it.

That means if I run an experiment like above called `resnet_cifar`, I can access all of the results for all the trials as a single DataFrame by calling `skeletor.proc.proj('resnet_cifar', './logs')`.

## Registering custom models, dataloaders, and optimizers

Registering custom classes allows you to construct an instance of the specified class by calling `build_model`, `build_dataset`, or `build_optimizer` with the class string name. This is useful for hyperparameter searching because you can search over these choices directly by class name.

I try to provide a simple interface for registering custom implementations with skeletor. For example, I can register a custom `Model` class by calling `skeletor.models.add_model(Model)`. This allows me to create models through `skeletor.models.build_model('Model')`. You can also register entire modules full of definitions at once. There are analogous functions `add_dataset, add_optimizer` for datasets and optimizers.

```
class MyNetwork(Module):
    ...

skeletor.models.add_model(MyNetwork)

arch_name = 'MyNetwork'
model = skeletor.models.build_model(arch_name)
```

## Help me out / Things to Do

We have active [issues](https://github.com/noahgolmant/skeletor/issues)! Feel free to suggest new improvements or add PRs to contribute.

[...](https://www.youtube.com/watch?v=g20_8-TPyTQ)
