<img src="https://github.com/sisl/Chimp/blob/master/logos/monkey_text.png" width="300">

<br>

Chimp is a general purpose framework for deep reinforcement learning developed at the [Stanford Intelligent Systems Laboratory](http://sisl.stanford.edu/).
Chimp is based on a simple four-part architecture to allow plug-and-play like capabilities for deep reinforcement
learning experiments. 
This package was inspired by the Google DeepMind [paper](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html) (V. Mnih, et al). 
Many of the architectural ideas were taken from DeepMind's
[GORILA](http://arxiv.org/abs/1507.04296) framework and from the
[paper](http://arxiv.org/abs/1508.04186) on distributed Deep Q-Learning by Ong, et al.

# Installation

First clone Chimp:
```
git clone https://github.com/sisl/Chimp
```
Then add the source directory to your `PYTHONPATH`. 

```
cd Chimp
export PYTHONPATH=$(pwd):$PYTHONPATH
```

You will also need numpy and scipy installed, as well as a deep learning backend. Currently only [Chainer](https://github.com/pfnet/chainer) is supported (TensorFlow coming soon). 

Once you have the dependencies installed you should be able to run the framework using a CPU. To use the GPU, you will need CUDA and a supported graphcis card. 

# Getting Started

If you are interested in using it for your own reinforcement learning problems check out the [mountain car tutorial](https://github.com/sisl/Chimp/blob/master/examples/mountain_car.ipynb) to get an idea of how to write your own simulator class. If you would like to use Chimp with the Atari Learning Environemnt check out the [Atari tutorial](https://github.com/sisl/Chimp/blob/master/examples/atari_tutorial.ipynb) to get started.

# Architecture 

Chimp consists of four main modules: Agent, Learner, Simulator, and Memory. Such decomposition leads to a very powerful and flexible framework for reinforcement learning experiments, where one can quickly switch between simulators, replay memory implementations, and various deep learning backends.

Chimp is also powerful in its flexible handling of inputs to the deep neural network. 
The user can specify the history lengths for observations, actions, and even rewards that they want to use as inputs to the model and Chimp will handle the rest. 

The specification of the input size is in the form of a tuple ```(s_size, a_size, r_size)```. For the DeepMind Atari experiments, this setting would look like (4,0,0): they use four image frames per input and no action or reward history. 

# Components

* Memory (implements experience replay)
	* Currently, we support in-memory numpy arrays and HDF5 allocated storage

* Learner ("brain" of the algorithm that does forward and backward passes in a neural net)
	* We support DQN with arbitrary observation/action history lengths as input
	* Planning to add LSTM + actor-critic framework

* Simulator (environment for the agent to interact with)
	* Single-player Arcade Learning Environment
	* MDPs

* Agent (general framework that handles all interactions between a learner, a memory, and a simulator)

# Dependencies

Chimp relies on existing deep learning back-ends. Currently only [Chainer](http://chainer.org/) is supported.

Required Python packages:
* [Chainer](https://github.com/pfnet/chainer)
* NumPy
* SciPy

Recommended libraries (some functionality will be absent without them):
* Pygame
* CUDA
* Arcade Learning Environment

# Authors

The original authors of this software are: Yegor Tkachenko, Max Egorov, Hao Yi Ong.

# License

The software is distributed under the Apache License 2.0
