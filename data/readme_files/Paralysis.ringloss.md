# Ring Loss
Modified based on:
**Ring loss: Convex Feature Normalization for Face Recognition**
https://arxiv.org/abs/1803.00130

## Getting Started
Install PyTorch and Python.
Download ringloss.py to your working directory. 

## Training for MNIST example script
In terminal type:
```
python mnist_example.py
```

## Usage of RingLoss module
Initialize a RingLoss module
```
ringloss_block = RingLoss(type='auto', loss_weight=1.0)
```
During forward
```
ringloss = ringloss_block(feature) # your feature should be (batch_size x feat_size)
```
During backward, be sure to use ringloss as an augmentation of your classification loss. e.g.
```
total_loss = softmax_loss + ringloss
total_loss.backward()
```

## Training
During training, a pretrained model is suggested, since Ring loss may be unstable in the beginning. 

## Results
