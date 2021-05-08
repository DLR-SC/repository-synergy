# tf-a3c-gpu

Tensorflow implementation of A3C algorithm using GPU (haven't tested, but it would be also trainable with CPU).

On the original paper, ["Asynchronous Methods for Deep Reinforcement Learning"](https://arxiv.org/abs/1602.01783),
suggests CPU only implementations, since environment can only be executed on CPU which causes unevitable communication
overhead between CPU and GPU otherwise.

However, we can minimize communication up to 'current state, reward' instead of whole parameter sets by storing all parameters
for a policy and a value network inside of a GPU. Furthermore, we can achieve more utilization of a GPU by having multiple agent for a single thread.
The current implementation (and with minor tuned-hyperparameters) uses 4 threads while each has 64 agents. With this setting, I was able to achieve 2 times of speed up. (huh, a little bit disappointing, isn't it?)

Therefore, this implementation is not quietly exact re-implementation of the paper, and
the effect of having multiple batch for each thread is worth to be examined. (different # of threads and agents per thread).
(However, I am still curious about how A3C can achieve such a nice results. Is the asynchrnous update is the only key? I couldn't find other explanations of effectiveness of this method.)
Yet, it gave me a quiet competitive result (3 hours of training on breakout-v0 for reasonable playing), so it could be a good base for someone to start with.

Enjoy :)

## Requirements

- Python 2.7
- Tensorflow v1.2
- OpenAI Gym v0.9
- scipy, pip (for image resize)
- tqdm(optional)
- better-exceptions(optional)

## Training Results

- Training on Breakout-v0 is done with nVidia Titan X Pascal GPU for 28 hours
- With the hyperparameter I used, one step corresponds to 64 * 5 frames of inputs(64 * 5 * average 3 game framse).
- Orange Line: with reward clipping(reward is clipped to -1 to 1) + Gradient Normalization, Purple Line: wihtout them
    - by the number of steps

        ![](/assets/per_iteration.PNG)

    - by the number of episodes

        ![](/assets/per_eps.PNG)

    - by the time

        ![](/assets/per_time.PNG)

- Check the results on [my results page](https://gym.openai.com/evaluations/eval_DKtoUiYuSESwmJOOUWekw)

    [![Watch the video](/assets/output.gif)](https://openai-kubernetes-prod-scoreboard.s3.amazonaws.com/v1/evaluations/eval_DKtoUiYuSESwmJOOUWekw/training_episode_batch_video.mp4)

## Training from scratch

- All the hyperparmeters are defined on `a3c.py` file. Change some hyperparameters as you want, then execute it.
```
python ac3.py
```

## Validation with trained models

- If you want to see the trained agent playing, use the command:
```
python ac3-test.py --model ./models/breakout-v0/last.ckpt --out /tmp/result
```


## Notes & Acknowledgement

- Here is other implementations and code I refer to.
    - [ppwwyyxx's implementation](https://github.com/ppwwyyxx/tensorpack/tree/master/examples/A3C-Gym)
    - [carpedm20's implementation of DQN](https://github.com/carpedm20/deep-rl-tensorflow)
