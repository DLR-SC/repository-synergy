# deep_rl_ale
This repo contains an implementation of [this paper](http://home.uchicago.edu/~arij/journalclub/papers/2015_Mnih_et_al.pdf) in TensorFlow.  It also contains the option to use the [double dqn](http://arxiv.org/pdf/1509.06461v3.pdf) loss function, as well as a parallel version that acts and learns simultaneously to speed up training.

[Watch it play Pong, Breakout, Space Invaders, and Seaquest here](https://youtu.be/gQ9FsAGb148)

The code is still a little messy in some places, and will be cleaned up in the future, but there will probably not be any significant updates or changes until mid-May.

## Dependencies/Requirements

1. An nVidia GPU with GDDR5 memory to train in a reasonable amount of time
2. [Python 3](https://www.python.org/)
3. [The Arcade Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment) for the emulator framework.
4. [Tensorflow](https://www.tensorflow.org/) for gpu numerical computions and symbolic differentiation.
5. Linux/OSX, because Tensorflow doesn't support Windows.
6. [Matplotlib](http://matplotlib.org/) and [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/) for visualizations.
7. [OpenCV](http://opencv.org/) for image scaling.  Might switch to SciPy since OpenCV was a pain for me to install.
8. Any dependencies of the above software, of course, like NumPy.

## How to run

From the top directory of the repo (dir with python files):
### Training
`$ python3 ./run_dqn.py <name_of_game> <name_of_algorithm/method> <name_of_agent_instance>`

For example:

`$ python3 ./run_dqn.py breakout dqn brick_hunter`

### Watching
`$ python3 ./run_dqn.py <name_of_game> <name_of_algorithm/method> <name_of_saved_model> --watch`
Where \<name_of_saved_model\> is the \<name_of_agent_instance\> used during training.  If you used any non-default settings, make sure to use the same ones when watching as well.

## Running Notes

You can change many hyperparameters/settings by entering optional arguments.
To get a list of arguments:

`$ python3 ./run_dqn.py --h`

By default rom files are expected to be in a folder titled 'roms' in the parent directory of the repo.  You can pass a diferent directory as an argument or change the default in run_dqn.py.

Statistics and saved models are saved in the parent directory of the repo as well.

The default settings are very similar to those used in the DeepMond Nature paper.  There are only a few small differences of which I am aware.

A full training run takes between 3 and 4 days on my nVidia GTX 970, depending on whether or not the parallel option is used.  Parallel training speeds up training by ~30%, but I'm still testing how different things impact speed.
