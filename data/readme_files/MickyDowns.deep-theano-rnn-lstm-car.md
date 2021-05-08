# Pack of Drones: Layered reinforcement learning for complex behaviors

## Overview

This project introduces key concepts around Q-learning (reinforcement learning), using sensor data, writing objective functions and layering networks. The result is a digital, 2-D implementation of learning drones that:

    *   Avoid: Turn, accelerate, decelerate to avoid obstacles

    *   Acquire: Locate and touch a target object (pixels) in the environment

    *   Hunt: Acquire target objects while avoiding obstacles

    *   Pack: Accelerate and improve hunt results by directing >1 drones

Here's a 3-min video that shows the final Pack model and lower layer training: [![layered reinforcement learning for complex behaviors](https://img.youtube.com/vi/FgZPu2XWAnU/0.jpg)](https://www.youtube.com/watch?v=FgZPu2XWAnU)

## About the networks

Drone movement and coordination are learned thru five independently-trained neural networks in four categories of operation. Specifically:

* **avoid**: The first two neural networks enable the drone to avoid obstacles. 

    -   The **turn RNN** trains a drone moving at constant speed to avoid stationary and moving obstacles. Inputs are a set of five sonar sensor readings that emanate from the front of the drone. Outputs are turn actions including: going straight, turning right (2 levels), and turning left (2 levels). Its objective function is to avoid collisions by maximizing the length of its sensor readings. It receives rewards for long readings and penalties for short readings (crashes).

    -   The **speed RNN** trains the drone to speed up or slow down to avoid obstacles. This network is trained on-top of the "turn" network. Inputs are the minimum distance measured by the sonar sensors AND the turn decision of the "turn" model. Output is one of three speed options: 30, 50, 70. It's trained using a 3-dimensional objective function blending speed and distance from obstacles. Basically, it's rewarded for slowing down in traffic and speeding up on the open road.

* **acquire RNN**: The third network trains the drone to search the 1000x700 pixel surface to locate and "touch" a target pixel. Its inputs are the target pixel heading and distance. So, when it sees (-180, 150), it learns to turn around (until heading = 0), then travel forward 150 pixels. It has the same five "turn" model outputs (straight, 2 right, 2 left). It is rewarded for moving efficiently to and then acquiring the pixel. Note: This model has no distance sensors and no memory of wall locations. It avoids crashes only to the extent it can plot a straight path to the target.

* **hunt RNN**: The fourth network merges avoid and acquire capabilities, selectively employing those networks to achieve a complex "hunting" objective. It searches the target area acquiring target pixels while avoiding obstacles. Its inputs are the full array of sonar sensor readings and the heading and distance to target. Its outputs are either the "acquire" or "avoid" network actions. It selectively accepts one or the other's action based on its appraisal of the inputs and its objective function. That objective function is a normalized composite of defensive (avoiding obstacles) and offensive (acquiring target pixels) move efficiency. Note: This model developed complex hunting behaviors including circling the target pixel to find the best angle of attack and a waiting for obstacles to clear its path before proceeding. 

* **pack LSTM**: The fifth network **illustrates the power of LSTM**. It coordinates the "hunting" activities of multiple drones by modifying their target headings. **Think of it like directing sheep dogs with hand signals.** Its inputs are the x, y coordinates of the target pixel, the other drones and the obstacles. It learns to direct the drones using nine output commands ranging from 0,0 (no command, follow "hunt" model), to -1,+1 (adjust drone 1 heading right 0.8 radians, adjust drone 2  heading left 0.8 radians). It uses an objective function that values movement towards the target (70\%) and away from obstacles (30\%). Couple notes:

    -   Given noise at this level (due to randomized obstacle movements), the model evaluates progress every 5 moves. So, the LSTM involves: a. Taking 10 drone moves (2 drones, 5 moves ea), b. assembling them into a set of 5 frame states, c. waiting an additional 5 frames to score the result, d. feeding the combined 5 frames, the action taken and the reward received as a single batch into the LSTM.

    -   This model outperforms a naive approach (i.e., same 2 drones using the hunt RNN to acquire pixels in an uncoordinated fashion) by about 20\% as measured by both average time to acquire a pixel (250 frames) and survival time (80 frames between crashes).

## Technology

The project technology is Python3, Jupyter notebook, Pygame, Pymunk, Keras and Theano. See "installing" below to get started though be ready to do some problem solving as, given differences in environments, components like Pymunk and Pygame can be challenging. **I'll soon put this project into a Docker container to reduce configuration issues.** In the meantime, I've commented the code. So, even if you don't install and run the code, you'll understand the approach.

### Key files:

* pack-o-drones.ipynb: This notebook has everything you need to run the game, train and run the networks. Further, it loads pre-trained models. So, while you'll have to acquiaint yourself with some of the variables, you can work sequentially through the models from least to most complex. If you're inclined, you can choose from alternative neural nets trained at each level to understand some of the tradeoffs. 

    -   The "common variables" section controls all downstream processing. Set the model you want to train (turn, avoid, acquire, hunt, pack) and whether you want to train from scratch or use_existing_model. Also, specify the number of obstacles, drones, etc. here. Finally, determine whether you want the game output to the screen (show_sensors, draw_screen). 

    -   The "learning" section trains the neural network based based on predictions/decisions, states and rewards. Each of the five networks are trained in similar fashion. Some number of random training samples are generated and evaluated against the objective function. A "state" (of the game world) is generated for each sample move and its efficacy is evaluated against the objective function for that network. These states are stacked (up to 100k), sampled and the submitted in microbatches of 100 to the nets for training. Gradually, they improve after seeing a variety of states with corresponding rewards.

    -   The "game" section controls the game play. It receives drone turn and speed commands from learning.py and playing.py. It effects those moves in the game and returns a set of training mode-specific (e.g., turn, speed, acquire, hunt) states. Those states communicate key information about obstacle distances, crashes, rewards, etc. used in training the models. Look in this file if you want to know how the drone and obstacles work, how state is maintained and how rewards are calculated.

    -   The "define neural net" section holds the neural network schema. The "load models" sections will load either an initialized model (if common var use_existing_model == False) or an existing model (if use_existing_model == True and a valid model name is supplied).

    -   The "playing" section runs the trained neural networks receiving states from game, getting predictions, translating those to actions, effecting the move, etc. It is activated by executing the calling function in the next cell. 

### installing

1. Clone this repo
1. Install numpy ```pip3 install numpy```
2. Install Pygame. I used these instructions: http://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3 but with ```pip3 install hg+http://bitbucket.org/pygame/pygame```
3. Install pymunk ```pip3 install pymunk```
4. Update pymunk to python3 by CDing into its directory and running ```2to3 -w *.py```
5. Install Keras ```pip3 install keras```
6. Upgrade Theanos ```pip3 install git+git://github.com/Theano/Theano.git --upgrade --no-deps```
7. Install h5py for saving models ```pip3 install h5py```

## Credits

This project extends work begun by **Matt Harvey** in his Github repository entitled **Using reinforcement learning to train an autonomous vehicle to avoid obstacles** located here: https://github.com/harvitronix/reinforcement-learning-car. He trained an digital autonomous car to avoid obstacles using reinforcement learning. His ultimate goal is to embed the resulting neural network onto a chip and into a a car that will, hopefully, avoid his cats while cruising his house. I highly recommend his Medium posts on the topic beginning here: https://medium.com/@harvitronix/using-reinforcement-learning-in-python-to-teach-a-virtual-car-to-avoid-obstacles-6e782cc7d4c6.

Note: It is possible that the tasks performed herein could be performed by a single, deep, deep neural net. The folks at DeepMind (of Go fame) used Q-learning to train a single network to win Atari games (https://t.co/liV9sJFoCp). However, I have specifically avoided giving the drones a down-sampled, convnet view of the entire environment. Instead, they learn it thru exploration as I will eventually flash this network to real drones and want the learning to continue onboard. 

## Related Concepts

**Layered learning** is used when mapping directly from inputs to outputs is not tractable e.g., too complex for current algorithms, networks, hardware. It starts with bottoms-up, hierarchical task decomposition. It then uses machine learning algorithms to exploit data at each level training function-specific models. The output of learning in one layer feeds into the next layer building complex behaviors. More here: http://www.cs.cmu.edu/~mmv/papers/00ecml-llearning.pdf.

**Reinforcement learning** is used when you don't have a correct solution ("y") value for each observation ("X"). The model learns-as-it-goes by balancing exploration of the solution space (thru random variation) and exploitation of what it has previously learned.

**Q-Learning** is model-free reinforcement learning. It samples historical game states (e.g., the distance to obstacles, targets, etc.), actions taken and rewards received to iteratively refine network weights. It gradually learns what action to take based on expected (probability-weighted) reward. 

**LSTM (long-short term memory)** is RNN with memory. Each neural network layer can be thought of as a composite of four types of neurons with specialized memory, input, output and forget functions. The net effect is a network that can learn not just from the input array, but a sequence of input arrays arranged in batches over time. Chris Olah provides a great overview here: http://colah.github.io/posts/2015-08-Understanding-LSTMs/. 

## Learnings

Coursework in statistical and computational methods helped here. However, in academic cases the dots are often pre-connected... you know a positive outcome is possible. That's not true here. That gap was instructive for me. So, I'll pass along some of the key learnings:

* Importance of tight linkage between inputs, outputs, objecive function, and cost function. Seems obvious to say that the networks can only learn from stimuli they can observe, can only change levers they control, and can only improve if they understand what's valuable. So, when designing the network for a layer **think like a machine**. Would you know what lever to pull based on the incoming data stream and a numeric reward?

* **Frames speed learning.** The current networks do are not using LSTM (Long Short Term Memory). LSTM was specifically developed to enable networks to learn from prior experience. The networks used here have short term memory in that each prediction is based on joining states from the last two or three moves. This roughly halved training time. 

* Run the **cost-benefit on network depth**. Initial "speed" and "hunt" models using two-hidden layers couldn't handle the complexity of a. reading sensors, b. reading lower model decisions, c. deciphering 3-D objective functions. Performance declined. Adding a third hidden layer enabled these models (at some cost to processing speed) to improve survivability. In contrast, 3 hidden layer "turn" and "acquire" models overfit the data. Increasing regularization in these models by a. dropping hidden layers and b. introducing dropout, improved survivability. 

* **Use domain experience.** In a layered network like this the simplier the objective function at each layer the better chance you'll have of the layers working together. However, that's not always the case. The "speed" model was implemented first with a simple survival goal (i.e., same as turn: reward = min(sensor_lengths)), second with a more complex 3D goal for slowing in traffic. Given training < 700k frames, the more complex objective function significantly outperformed (2x) the simplier. 
