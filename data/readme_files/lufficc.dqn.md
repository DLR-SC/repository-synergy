# Deep Q Network

An implementation of q algorithm of Reinforcement Learning.

## Installation Dependencies:

1. Python 3
1. TensorFlow 1.0.1
1. pygame
1. gym

## How to Run?

```
git clone https://github.com/lufficc/dqn.git
cd dqn
python run.py
```

## Tricks for flappybird

Remove background image:
![remove-bg](https://github.com/lufficc/images/blob/master/dqn/remove-bg.png)

clip useless part:
![clip](https://github.com/lufficc/images/blob/master/dqn/clip.png)

resize and using binary image:
![bin](https://github.com/lufficc/images/blob/master/dqn/bin.png)

**decayed ε-greedy exploration, and when exploration, 0.95 probability to do nothing(because in flappy bird, most time wo do nothing). This is very important. It makes model converge in less than 2 hours.**

```
def egreedy_action(self, state):
    #Exploration
    if random.random() <= self.epsilon:
        if random.random() < 0.95:
            action_index = 0
        else:
            action_index = 1
        # action_index = random.randint(0, self.num_actions - 1)
    else:
        #Exploitation
        action_index = self.action(state)
    if self.epsilon > self.final_epsilon:
        self.epsilon *= self.decay_factor
    return action_index
```

## Thanks

1. [DeepLearningFlappyBird](https://github.com/yenchenlin/DeepLearningFlappyBird)
1. [Guest Post (Part I): Demystifying Deep Reinforcement Learning](https://www.nervanasys.com/demystifying-deep-reinforcement-learning/)
1. [UCL Course on RL](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
1. [A Painless Q-Learning Tutorial](http://mnemstudio.org/path-finding-q-learning-tutorial.htm)
1. [DQN 从入门到放弃1 DQN与增强学习](https://zhuanlan.zhihu.com/p/21262246)