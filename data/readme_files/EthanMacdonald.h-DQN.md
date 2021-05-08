# h-DQN

Reproduction of "Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation" by Kulkarni et al. (2016) in Python: https://arxiv.org/abs/1604.06057

## Disclaimer

This is a work in progress. I haven't been able to replicate the results yet.

Also, I haven't started on Montezuma's revenge yet. I intend to do this eventually, but I'm not sure when. Pull requests are welcomed and encouraged!

Comments/criticisms/suggestions/etc welcome, as always.

## Progress

### MDP Environment
- Create MDP Environment **[Done]**
- Create a non-hierarchical actor-critic agent as a baseline **[Done]**
- Evaluate the non-hierachical actor-critic by plotting which states it visits **[Done]**
- Create a h-DQN agent **[Done]**
- Evaluate the h-DQN agent by plotting which states it visits **[Done]**

### Montezuma's Revenge

TODO (This might be a while. Pull requests welcome.)

## Results

### Stochastic MDP Environment

#### h-DQN

The h-DQN agent is located in `./agent/hDQN.py`. Below is our replication of Figure 4 from the paper:

![Figure 4](https://github.com/EthanMacdonald/h-DQN/raw/master/fig/r4.png)

## Requirements

- numpy
- tensorflow
- keras
- h5py
- matplotlib
