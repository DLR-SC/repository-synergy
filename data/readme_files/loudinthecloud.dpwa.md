# Distributed P2P Learning Implementation

## Introduction

Performs distributed learning using a peer-to-peer parameter averaging approach. The method is described in [How to scale distributed deep learning?](https://arxiv.org/abs/1611.04581) and [Gossip training for deep learning](https://arxiv.org/abs/1611.09726). The library is named **distributed pair-wise averaging (dpwa)**, as it is generic enough to be used with multiple optimizers or training methods.

This implementation can be used as a starting point for people who want to experiment with async p2p training algorithms. Please see the papers above to learn more.

## PyTorch Integration (How-To)

Integration is very simple, simply call 2 functions before and after each training batch. The following shows a pythonic pseudo-code of how it would work:

```python
# Create a connection to the cluster
# the config file contains the list of named nodes in the cluster, and name identifies which node are we.
conn = DpwaPyTorchAdapter(net, name, config_file)

# Training loop
for batch in training_samples:
    # 1. Updates the local server with the latest model parameters
    # 2. Initiate an asynchronous fetch parameters request to a random peer
    conn.update_send(loss)

    # Train the model as usual
    loss = train_batch(batch)

    # 1. Wait for the fetch parameters request to complete (blocking)
    # 2. Average the model's parameters with the peer's parameters
    conn.update_wait(loss)
```

Please see the [pytorch-cifar](examples/pytorch-cifar) training script for an integration example.

## Implemetation Details

Each node in the cluster creates two threads:

1. The `RxThread` is serving the current parameters + state to any other peer
2. The `TxThread` request a random peer's parameters.

Where both recieving and sending is done asynchronousely to training the network.

The state is composed of the current `loss` and `clock` and is sent with the parameters. The `clock` is a sequence number that represents the age of the model, in term of training samples trained so far. The `loss` is provided by the user in calls to `update_send` and `update_wait`.

The `clock` and `loss` values may be used to calculate the value of the averaging/interpolation factor according to the interpolation method used.

## Configuration

Configuration is supplied using a `.yaml` file. A sample configuration file can be copied from the `samples/` directory (see [here](samples/config.yaml)).

The configuration file holds the following information:

* `nodes`: a list of nodes participating in the cluster
* `fetch_probability`: probability of initiating a fetch parameters request from a random peer
* `timeout_ms`: the timeout of each socket send/recv. A simple flow control mechanism is used for selecting the target peer, combined with a random term. In each timeout, we decrease the flow control score of the peer so it'll be less likely to get picked up in the next iteration, we increase the flow control score otherwise.
* `interpolation`: the name of the method to be used to set the interpolation factor.
* `divergence_threshold`: controls the threshold loss value to start diverging the models, if not zero, and the `loss` is below the threshold, it'll decrease the interpolation factor by `(loss / divergence_threshold)`, regardless of the interplation method.
* The rest of the configuration is for setting individual interpolation methods configuration.

Here's a sample configuration file:

```yaml
# Sample configuration file for a multi-core machine
# Each worker is running on a seperate core
---
- nodes:
  - {name: w1, host: localhost, port: 45000}
  - {name: w2, host: localhost, port: 45001}
  - {name: w3, host: localhost, port: 45002}
  - {name: w4, host: localhost, port: 45003}

# The probability of initiating a fetch parameter request
- fetch_probability: 1

# The timeout value is used for flow-control
- timeout_ms: 2500

# Choose interpolation method: clock, loss or constant
- interpolation: constant

# Diverge models when loss is reaching the value specified here (use 0 to disable)
- divergence_threshold: 0.2

# Individual interpolation methods configuration:

- constant: { value: 0.5 }

- clock: 0

- loss: 0
```

### Interpolation Methods

The interpolation methods controls how the interpolation/averaging factor is calculated. Averaging is done using the following equation: `params = factor * peer_params + (1 - factor) * params`. currently the following methods are supported:

* `Constant`: The factor is constant, the papers above used a constant factor value derived theoretically.
* `Clock`: Uses the following equation `factor = peer_clock / (clock + peer_clock)`, the factor increase when the peer's clock is larger.
* `Loss`: Same as clock, but uses the loss value instead of the clock value.

**NOTE:** The `Clock` and `Loss` interpolation methods are not published, nor backed by experiments and comparisons yet, they are here only for reference but you may try to see how they work for your model.

## Training pytorch-cifar

Do the following to start a local cluster where each node is running on a different cpu core.

1. Clone repository
2. Install requirements: `pip install -r requirements.txt`
3. `cd examples/pytorch-cifar`
4. `./prepare.sh`
5. Start training: `./run.sh`
6. Stop (kill python3): `./stop.sh`
