# mnist-bn
Using slim to perform batch normalization

Run `python mnist_bn.py --phase=train` to train.
Run `python mnist_bn.py --phase=test` to test.

It should achieve an accuracy of ~99.3% or higher on test set.

I've added accuracy, cross_entropy and batch normalization paramters into summary. Use **tensorboard --logdir=/log** to explore the learning curve and parameter distributions!
