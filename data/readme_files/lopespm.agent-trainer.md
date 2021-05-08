# Agent Trainer


<p align="center">
    <a href="https://www.youtube.com/watch?v=spzYVhOgKBA">
      <img align="center" src="http://i.ytimg.com/vi/spzYVhOgKBA/mqdefault.jpg" alt="Agent playing Out Run (no time limit, no traffic, 2X time lapse)">
    </a>
</p>

Through [Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf), this agent can autonomously train itself to play [Out Run](https://en.wikipedia.org/wiki/Out_Run) and potentially be modified to play other games or perform tasks other than gaming.

More details about the training process [in this blogpost](http://lopespm.github.io/machine_learning/2016/10/06/deep-reinforcement-learning-racing-game.html).

Built with Python and Tensorflow.


## Setup

### Build cannonball's (Out Run game emulator) SO file

1. Clone [the custom Cannonball fork](https://github.com/lopespm/cannonball), which contains the changes needed to access the emulator externally.

2. Build Cannonball:

    ```bash
    # On Cannonball's root folder do:
    $ mkdir build
    $ cd build
    # Building on OSX / MacOS
    $ cmake -G "Unix Makefiles" -DTARGET:STRING=sdl2_macosx ../cmake
    # If building on Linux, execute this commented line instead:
    # $ cmake -G 'Unix Makefiles' -DTARGET:STRING=sdl2 ../cmake
    $ make
    ```
3. Copy the built shared object file (libcannonball.so) to agent-trainer's lib folder:

    ```bash
    $ cp <cannonball-folder>/build/libcannonball.so <agent-trainer-folder>/lib/libcannonball.so
    ```

### Out Run Game Roms

Copy your game roms to `<agent-trainer-folder>/roms/`. More details [here](https://github.com/lopespm/agent-trainer/blob/master/roms/roms.txt).

### Set the training results folder

Set the `train_results_root_folder` parameter in [config.py](https://github.com/lopespm/agent-trainer/blob/master/agent/config.py). This will be the default folder used to write and read training results (can be overriden, see below)

### Install python dependencies

On the root folder, run:

```bash
$ make
```

This installs the depencies via [pip](https://pypi.python.org/pypi/pip). Feel free to use [virtual env wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) (for example) to contain these.

**Dependencies on a GPU enabled Linux machine**

If you are running a Linux machine and want to make use of its GPU for training, use the following flag when installing dependencies:

```bash
$ USE_GPU=true make
```

## Usage

You can use the trainer via [make](https://www.gnu.org/software/make/) tasks:

```bash
# Run all the tests
$ make test

# Start new training session
$ make train-new

# Resume training session
$ SESSION_ID="201609272034" make train-resume

# Play a previously trained session
$ SESSION_ID="201609272034" make play

# Create a t-Distributed Stochastic Neighbor Embedding (t-SNE) visualization, placed on `<train-results-root-folder>/<session-id>/visualizations/t-SNE.png`
# Example output: https://github.com/lopespm/agent-trainer-results/blob/master/201609171218_175eps/visualizations/t-SNE_no_time_mode.png
$ SESSION_ID="201609272034" make visualize-tsne

# Export the metrics of the given session, as PNG images files. These will be placed on `<train-results-root-folder>/<session-id>/metrics-session/`
# Example output: https://github.com/lopespm/agent-trainer-results/tree/master/201609171218_175eps/metrics-session
$ SESSION_ID="201609272034" make metrics-export

# Show the session's metrics on-screen
$ SESSION_ID="201609272034" make metrics-show
```


For finer control, you can run the library module as a script. For example:

```bash
python -m agent play --ec2spot --resultspath /example/alternative-results-folder -s 201609261533
```

Actions: `train-new`, `train-resume`, `play`, `visualize-tsne`, `metrics-show` or `metrics-export`

Options:
 - `-s`: define the session ID
 - `--ec2spot`: when used, it will check on which episode if the spot instance is [scheduled for termination](https://aws.amazon.com/blogs/aws/new-ec2-spot-instance-termination-notices/), acting accordingly by saving the current session and halting training
 - `--resultspath`: overrides the default [`train_results_root_folder`](https://github.com/lopespm/agent-trainer/blob/master/agent/config.py) parameter


## Deploy to Remote Machine / AWS EC2 Instance

You can deploy the agent to a generic remote Linux machine or to an AWS EC2 instance with the help of [agent-trainer-deployer](https://github.com/lopespm/agent-trainer-deployer)