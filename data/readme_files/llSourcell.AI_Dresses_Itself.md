## Overview

This is the code for [this](https://youtu.be/vcYBiwvauA4) video on Youtube by Siraj Raval. This is an implementation of the Trust Region Policy Optimization algorithm that was used by the researchers in the video. They did not, however, make their full code public. So here is the technique applied to game environments. Someone can use it as a starting point to recreate their code. Meanwhile -- hey researchers :) go ahead and release it the community would appreciate it.

# PyTorch implementation of TRPO

Try this implementation of [PPO](github.com/ikostrikov/pytorch-a2c-ppo-acktr/) (aka newer better variant of TRPO), unless you need to you TRPO for some specific reasons.

##

This is a PyTorch implementation of ["Trust Region Policy Optimization (TRPO)"](https://arxiv.org/abs/1502.05477).

This is code mostly ported from [original implementation by John Schulman](https://github.com/joschu/modular_rl). In contrast to [another implementation of TRPO in PyTorch](https://github.com/mjacar/pytorch-trpo), this implementation uses exact Hessian-vector product instead of finite differences approximation.

## Contributions

Contributions are very welcome. If you know how to make this code better, don't hesitate to send a pull request.

## Usage

```
python main.py --env-name "Reacher-v1"
```

## Recommended hyper parameters

InvertedPendulum-v1: 5000

Reacher-v1, InvertedDoublePendulum-v1: 15000

HalfCheetah-v1, Hopper-v1, Swimmer-v1, Walker2d-v1: 25000

Ant-v1, Humanoid-v1: 50000


## Credits

Credits for this code go to [ikostrikov](https://github.com/ikostrikov). I've merely created a wrapper to get people started. 
