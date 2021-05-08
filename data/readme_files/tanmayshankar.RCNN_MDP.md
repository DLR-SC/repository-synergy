# Reinforcement Learning via Recurrent Convolutional Neural Networks

### What is this all about? ###
This repository is code connected to the paper - T. Shankar, S. K. Dwivedy, P. Guha, Reinforcement Learning via Recurrent Convolutional Neural Networks, published at ICPR 2016. 

### Where can I read this cool paper? ###
[Click here to view the paper on ArXiv!](https://arxiv.org/abs/1701.02392) 

### I want a TL;DR of what this repository does. ###
This code base targets the following problems: 

1. Solving Value / Policy Iteration in a standard MDP using feedforward passes of a Value Iteration RCNN. 
2. Representing the Bayes Filter state belief update as feedforward passes of a Belief Propagation RCNN. 
3. Learning the State Transition models in a POMDP setting, using backpropagation on the Belief Propagation RCNN. 
4. Learning Reward Functions in an Inverse Reinforcement Learning framework from demonstrations, using a QMDP RCNN. 

### Is that all? ###
Yes and no. I'm working on two extensions to this framework, you can check them out at https://github.com/tanmayshankar/DeepVectorPolicyFields and https://github.com/tanmayshankar/GraphPlanningNetworks for more! 

### Can I use this code to pretend I did some research? ###
Feel free to use my code, but please remember to cite my paper above (and this repository)! 

### I have a brilliant idea to make this even cooler! ###
Awesome! Feel free to mail me at tanmay.shankar@gmail.com with your suggestions, feedback and ideas! 

### Tell me how to run the code already! ### 
To run any of the code, clone this repository to a local directory, and make sure you have Python >= 2.7 installed. Follow the following instructions to run code specific to any of the given problems. 





**Value Iteration RCNN**

The VI RCNN takes a reward function and a transition model as arguments. Run the appropriate script similar to these examples: 

`./scripts/VI_RCNN/VI_feedforward.py data/VI_Trials/trial_3/reward_function.txt data/learnt_model/actual_transition.txt`

To view the progress of Value Iteration as it goes, run: 

`./scripts/VI_RCNN/VI_live_display.py data/VI_Trials/trial_3/reward_function.txt data/learnt_model/actual_transition.txt`

To run Value Iteration with reward as a function of actions as well, run: 

`./scripts/VI_RCNN/VI_action_reward.py data/VI_Trials/trial_3/reward_function.txt data/learnt_model/actual_transition.txt`

To run Value Iteration with an extended action vector (considering remaining stationary as an action): 

`./scripts/VI_RCNN/VI_extended_actions.py data/QMDP_old_trajectories/trial_9_action_reward/action_reward_function.txt data/learnt_model/actual_transition.txt`

**Displaying Optimal Policy**

Once the feedforward passes of the VI RCNN are run, you may display the policy, reward and value functions by running the following:

`./scripts/Display/display_policy.py output_policy.txt reward_function.txt value_function.txt`

If you used the extended action vector, use this instead: 

`./scripts/Display/display_policy_extended.py output_policy.txt reward_function.txt value_function.txt`

**Learning the Transition Model**

To learn the state transition model of the POMDP by applying backpropagation to the BP RCNN, run any of the codes of BP RCNN: Here's an example for the partially observable case. 

`./scripts/BP_RCNN/BP_PO.py` 

To run backpropagation as convolution of sensitivies instead, run any of the codes from the conv_back_prop folder: 

`./scripts/conv_back_prop/learn_trans_po.py`

You'll notice the convolution version of backpropagation runs much faster. Try replanning (execute value iteration) with the learnt transition model! 

**Following Optimal Policy**

To watch an agent follow the optimal policy from a random position, with the learnt transition values, run: 

`./scripts/Follow_Policy/follow_policy_obs.py data/VI_Trials/trial_3/output_policy.txt data/VI_Trials/trial_3/reward_function.txt data/VI_Trials/trial_3/value_function.txt data/learnt_models/estimated_transition.txt`

**Generating Trajectories using Optimal Policy**

To generate multiple trajectories of an agent following the optimal policy from a random position, run: 

`./scripts/follow_policy/generate_trajectories_extended.py data/VI_Trials/trial_8_bounded/output_policy.txt data/VI_Trials/trial_8_bounded/reward_function.txt data/learnt_models/actual_transition.txt`

**Inverse Reinforcement Learning**

To learn reward functions in an Inverse Reinforcement Learning setting, run the following code. It executes backpropagation on the QMDP RCNN, and uses experience replay across transitions and RMSProp to adapt the learning rate.

`./scripts/QMDP_RCNN/experience_replay_RMSProp.py data/learnt_models/actual_transition.txt data/QMDP_Trials/trial_2/Trajectories.txt data/QMDP_Trials/trial_2/Observed_Trajectories.txt data/QMDP_Trials/trial_2/Actions_Taken.txt`

