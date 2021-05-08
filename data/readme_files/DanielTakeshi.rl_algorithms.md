Note: this repository has not been updated in years and I don't have plans to do so. I recommend using rlpyt for future RL research.

# Reinforcement Learning Algorithms

I will use this repository to implement various reinforcement learning
algorithms (also imitation learning), because I'm sick of reading about them but
not really understanding them.  Hence, hopefully this repository will help me
understand them better. I will also implement various supporting code as needed,
such as for simple custom scenarios like GridWorld. Or I can use OpenAI gym.
Click on the links to get to the appropriate algorithms. Each sub-directory will
have its own READMEs with results there, along with usage instructions.

Here are the algorithms currently implemented or in progress:

- [Q-Learning, tabular version](https://github.com/DanielTakeshi/rl_algorithms/tree/master/q_learning) (should be correct)
- [G-Learning](https://github.com/DanielTakeshi/rl_algorithms/tree/master/g_learning) (in progress ...)
- [Behavioral Cloning](https://github.com/DanielTakeshi/rl_algorithms/tree/master/bc) (should be correct)
- [Natural Evolution Strategies](https://github.com/DanielTakeshi/rl_algorithms/tree/master/es) (should be correct)
- [Deep-Q Networks](https://github.com/DanielTakeshi/rl_algorithms/tree/master/dqn) (should be correct)
- [Vanilla Policy Gradients](https://github.com/DanielTakeshi/rl_algorithms/tree/master/vpg) (should be correct)
- [Deep Deterministic Policy Gradients](https://github.com/DanielTakeshi/rl_algorithms/tree/master/ddpg) (in progress ...)
- [Trust Region Policy Optimization](https://github.com/DanielTakeshi/rl_algorithms/tree/master/trpo) (in progress ...)

Note: "Vanilla Policy Gradients" refers to the REINFORCE algorithm, also known
as Monte Carlo Policy Gradient. Sometimes it's called an actor-critic method
and other times it's not. Even if it's considered an actor-critic method, the
usual way we think of actor-critic involves a TD update rather than waiting
until the end of an episode to get returns.


# Requirements

Right now the code is designed for Python 2.7, but it *should* be compatible
with Python 3.5+, with the possible exception of if the bash scripts can't tell
the difference between which Python versions I'm using.

In short:

- Python 2.7.x
- Tensorflow 1.2.0


# GPU and TensorFlow 

(Update 06/16/17, these are out of date ... just install with pip and preferably
virtualenv. It's so much easier.)

I installed TensorFlow 1.0.1 from source.  For the configuration script, I used
CUDA 8.0, cuDNN 5.1.5, and compute capability 6.1.

Compiling from source means I can get faster CPU instructions. This requires
`bazel` plus extra compiler options. I used:

```
bazel build -c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --copt=-msse4.2 --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
```

This resulted in ton of warning messages but I ended up with:

```
Target //tensorflow/tools/pip_package:build_pip_package up-to-date:
  bazel-bin/tensorflow/tools/pip_package/build_pip_package
INFO: Elapsed time: 884.276s, Critical Path: 672.19s
```

and things seem to be working. Then run the command:

```
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
```

To get a wheel, which we then do a pip install. But be careful due to pip on
anaconda vs pip with default python. I use anaconda. And make sure you're not in
either the `tensorflow` or the `bazel` directories!

Track the GPU usage with `nvidia-smi`. Unfortunately, that's only for one
time-step, but we can instead run:

```
while true; do nvidia-smi --query-gpu=utilization.gpu --format=csv >> gpu_utilization.log; sleep 10; done;
```

Or something like that. It will record the output every 10 seconds and dump it
into the log file. Ideally, GPU usage should be as high as possible (100% or
close to it).

# References

I have read a number of reinforcement learning paper references to help me out.
A list of papers and summaries (for a few of them) are [in my paper notes
repository](https://github.com/DanielTakeshi/Paper_Notes).
