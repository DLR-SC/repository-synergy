# drivebot

for more general info see [the blog post](http://matpalm.com/blog/drivebot/)

for more advanced RL experiments (with less of a focus on sim-real transfer learning) see [cartpoleplusplus](https://github.com/matpalm/cartpoleplusplus)

for info on the physical rover build see [this google+ collection](https://plus.google.com/u/0/collection/kMWoSB)

## building drivebot ROS package

drivebot has two ROS specific components that need to be built.

* a `ActionGivenState.srv` service definition that describes how bots (real or simulated) interface with the NN policy
* a `TrainingExample.msg` msg definition that describes training examples sent to the NN policy`

```
# build msg and service definitions
cd $ROOT_OF_CHECKOUT  # whatever this is...
cd ros_ws
catkin_make

# add various ROS related paths to environment variables
# (add this to .bashrc if required)
source $ROOT_OF_CHECKOUT/ros_ws/devel/setup.bash
```

## running ros env

stdr sim

```
roslaunch stdr_launchers server_no_map.launch
```

load map and add three bots...

```
rosservice call /stdr_server/load_static_map "mapFile: '$PWD/maps/track1.yaml'"
rosrun stdr_robot robot_handler add $PWD/maps/pandora_robot.yaml 5 5 0
rosrun stdr_robot robot_handler add $PWD/maps/pandora_robot.yaml 5 5 0
rosrun stdr_robot robot_handler add $PWD/maps/pandora_robot.yaml 5 5 0
```

optionally run gui (for general sanity) and rviz (for odom visulations)

```
roslaunch stdr_gui stdr_gui.launch
roslaunch stdr_launchers rviz.launch
```

## running sim

### start external policy

the policy represents the decision making process for bots.

policy is run in seperate process so it can support >1 bots. given stdr's limitations
of not being able to run faster-than-real time the quickest way to train (apart from
experience replay) is having multiple bots running.

```
$ ./policy_runner.py --help
usage: policy_runner.py [-h] [--policy POLICY] [--state-size STATE_SIZE]
                        [--q-discount Q_DISCOUNT]
                        [--q-learning-rate Q_LEARNING_RATE]
                        [--q-state-normalisation-squash Q_STATE_NORMALISATION_SQUASH]
                        [--gradient-clip GRADIENT_CLIP]
                        [--summary-log-dir SUMMARY_LOG_DIR]
                        [--summary-log-freq SUMMARY_LOG_FREQ]
                        [--target-network-update-freq TARGET_NETWORK_UPDATE_FREQ]
                        [--target-network-update-coeff TARGET_NETWORK_UPDATE_COEFF]

optional arguments:
  -h, --help            show this help message and exit
  --policy POLICY       what policy to use; Baseline / DiscreteQTablePolicy /
                        NNQTablePolicy
  --state-size STATE_SIZE
                        state size we expect from bots (dependent on their
                        sonar to state config)
  --q-discount Q_DISCOUNT
                        q table discount. 0 => ignore future possible rewards,
                        1 => assume q future rewards perfect. only applicable
                        for QTablePolicies.
  --q-learning-rate Q_LEARNING_RATE
                        q table learning rate. different interp between
                        discrete & nn policies
  --q-state-normalisation-squash Q_STATE_NORMALISATION_SQUASH
                        what power to raise sonar ranges to before
                        normalisation. <1 => explore (tends to uniform), >1 =>
                        exploit (tends to argmax). only applicable for
                        QTablePolicies.
  --gradient-clip GRADIENT_CLIP
  --summary-log-dir SUMMARY_LOG_DIR
                        where to write tensorflow summaries (for the
                        tensorflow models)
  --summary-log-freq SUMMARY_LOG_FREQ
                        freq (in training examples) in which to write to
                        summary
  --target-network-update-freq TARGET_NETWORK_UPDATE_FREQ
                        freq (in training examples) in which to flush core
                        network to target network
  --target-network-update-coeff TARGET_NETWORK_UPDATE_COEFF
                        affine coeff for target network update. 0 => no
                        update, 0.5 => mean of core/target, 1.0 => clobber
                        target completely
```

### run one bot

```
$ ./sim.py --help
usage: sim.py [-h] [--robot-id ROBOT_ID] [--max-episode-len MAX_EPISODE_LEN]
              [--num-episodes NUM_EPISODES]
              [--episode-log-file EPISODE_LOG_FILE]
              [--max-no-rewards-run-len MAX_NO_REWARDS_RUN_LEN]
              [--sonar-to-state SONAR_TO_STATE]
              [--state-history-length STATE_HISTORY_LENGTH]

optional arguments:
  -h, --help            show this help message and exit
  --robot-id ROBOT_ID
  --max-episode-len MAX_EPISODE_LEN
  --num-episodes NUM_EPISODES
  --episode-log-file EPISODE_LOG_FILE
                        where to write episode log jsonl
  --max-no-rewards-run-len MAX_NO_REWARDS_RUN_LEN
                        early stop episode if no +ve reward in this many steps
  --sonar-to-state SONAR_TO_STATE
                        what state tranformer to use; FurthestSonar /
                        OrderingSonars / StandardisedSonars
  --state-history-length STATE_HISTORY_LENGTH
                        if >1 wrap sonar-to-state in a StateHistory
```

common config includes 

### baseline

just go in direction of furthest sonar.

state is simply which sonar reads the furthest distance (0 for F, 1 for L and 2 for R) e.g. [0]

```
./policy_runner.py --policy Baseline
```

```
./sim.py --robot-id 0 --sonar-to-state FurthestSonar
./sim.py --robot-id 1 --sonar-to-state FurthestSonar
```

![lap](blogish/lap_and_half_simple_policy.png?raw=true "lap")

### discrete state q table

q table with discrete states based on which sonar is reporting the furthest distance.

state is concat of history of last 4 readings; eg [0, 0, 1, 1]

```
./policy_runner.py --policy DiscreteQTablePolicy --q-state-normalisation-squash=50
```

```
./sim.py --robot-id 0 --sonar-to-state FurthestSonar 
./sim.py --robot-id 1 --sonar-to-state FurthestSonar 
```

### continous state q learnt function

train a single layer NN using standardised sonar readings (mu and stddev derived from sample data for `discrete state q table`

```
./policy_runner.py --policy=NNQTablePolicy
--q-learning-rate=0.01 --q-state-normalisation-squash=50 --state-size=3
--summary-log-dir=summaries
```

```
./sim.py --robot-id=0 --sonar-to-state=StandardisedSonars
```

## cookbook

### state history variants

all sims.py can be run with `--state-history-length=N` to maintain state as a history of the last N sonar readings. 
(i.e. stat is 3N floats, not just 3)

in the case of `NNQTablePolicy` we need to pass 3N as `--state-size`

### training config

some config is expressed as ros parameters. these params are refreshed periodically by sim / trainer..

```
$ rosparam get /q_table_policy
{ discount: 0.9,                    # bellman RHS discount
  learning_rate: 0.1,               # sgd learning rate
  state_normalisation_squash: 1.0,  # action choosing squash; <1.0 (~0.01) => random choice, >1 (~50) => arg max
  summary_log_freq: 100,            # frequency to write tensorboard summaries
  target_network_update_freq: 10}   # frequency to clobber target network params
```

### episode / event hacking for replay

( when `--episode-log-file` is not specified to `sim.py` we can extract it from recorded stdout. )

```
$ cat runs/foo.stdout | ./log_to_episodes.py
```

extract event jsonl from a log (one event per line)

```
$ cat runs/foo.log | ./log_to_episodes.py | ./episode_to_events.py
```

use previous date to calculate mean/std of ranges

```
$ cat runs/foo.log | ./log_to_episodes.py | ./calculate_range_standardisation.py
(68.56658770018004, 30.238156000781927)
```

rewrite the states for a run. every simualtion involves mapping from ranges -> states that are specific
for the policy being trained. by using `./rewrite_event_states.py` we can rewrite the ranges (which are always the
same) to be a different state sequence. this can be used to build cirruculum style training data from
one policy (say a discrete q table) to be used by another policy (say an nn q table). 


```
# rewrite an sequence of episodes so that events retain history of 10 states.
cat runs/foo.log \
 | ./log_to_episodes.py \
 | ./rewrite_event_states.py 10 \
 > runs/foo_episodes_with_new_states.episode.jsonl
```

this data can then be piped through `./episode_to_events.py` and shuffled to build batch experience replay training data.

e.g. replay a sequence of events (one per line) to the `/drivebot/training_egs` ros topic

```
# replay events in random order
cat runs/foo.episode.jsonl | ./episode_to_events.py | shuf | ./publish_events_to_topic.py --rate 1000
```

```
# rewrite episodes to have a history length of 5 then replay events in random order ad infinitum
cat runs/foo.episode.jsonl | ./log_to_episodes.py | ./episode_to_events.py > events.jsonl
while true; do shuf events.jsonl | ./publish_events_to_topic.py --rate=1000; done
```

### stats

```
cat runs/foo.episode.jsonl | ./episode_stats.py > episode_id.num_events.total_reward.tsv
```






