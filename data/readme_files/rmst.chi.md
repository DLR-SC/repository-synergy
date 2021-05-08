
<img src="./assets/cb.png" width="100%">

### CHI – A high-level framework for advanced deep learning with TensorFlow

Chi provides high-level operations for writing and visualizing experiments


---------------------------

### Getting started

__Experiment Scripts__ can also be defined via decorator. When run from the command line the function arguments are translated into command line parameters.
```python
@chi.experiment
def my_experiment(logdir, a=0.5):
  print(logdir)
  ...
```
If no logdir is specified it will generate a new one. See [examples/experiments.py for the full example](examples/experiments.py)

For a more interesting experiment see the [Wasserstein GAN example](/examples/wgan.py).

--------------------------

### Visualization with CHIBOARD
Chiboard is a browser based dashboard for managing experiments. Start it with `chiboard`.

<img src="./assets/cb.png" width="100%">

Clicking on an experiment card leads to a detail page about that experiment which automatically spins up and embeds a TensorBoard:

<img src="./assets/cb1.png" width="100%">

See [chi/board for a full overview](chi/board).

--------------------------

### Installation

Requires Python 3.6

```
git clone git@github.com:rmst/chi.git
pip install -e chi
```

---------------------------


### Acknowledgements

The foundations for this work have been developed during projects at the following institutes.

- Reasoning and Learning Lab (RLLab) at McGill University in Canada
- Montreal Institute for Learning Algorithms (MILA) in Canada
- Intelligent Autonomous Systems Lab (IAS) at TU-Darmstadt in Germany

The structures of this repo and readme were inspired by [Keras-RL](https://github.com/matthiasplappert/keras-rl) and [Keras](https://github.com/fchollet/keras) respectively.

