# What's this
Implementation of Appendix A (Neural Architecture Search with Reinforcement Learning) by chainer


# Dependencies

    git clone https://github.com/nutszebra/neural_architecture_search_with_reinforcement_learning_appendix_a.git
    cd neural_architecture_search_with_reinforcement_learning_appendix_a
    git submodule init
    git submodule update

# How to run
    python main.py -p ./ -g 0 


# Details about my implementation
All hyperparameters and network architecture are the same as in [[1]][Paper] except for some parts.  

* Data augmentation  
Train: Pictures are randomly resized in the range of [32, 36], then 32x32 patches are extracted randomly and are normalized locally. Horizontal flipping is applied with 0.5 probability.  
Test: Pictures are resized to 32x32, then they are normalized locally. Single image test is used to calculate total accuracy. 

* Learning rate schedule  
Learning rate is divided by 10 at [150, 170] epochs. The total number of epochs is 200.

* batch  
128

# Cifar10 result

| network              | depth | total accuracy (%)                      |
|:---------------------|-------|----------------------------------------:|
| my implementation    | 15    | 90.35 (I look for bugs)                 |
| [[1]][Paper]         | 15    | 94.5                                    |

<img src="https://github.com/nutszebra/neural_architecture_search_with_reinforcement_learning_appendix_a/blob/master/loss.jpg" alt="loss" title="loss">
<img src="https://github.com/nutszebra/neural_architecture_search_with_reinforcement_learning_appendix_a/blob/master/accuracy.jpg" alt="total accuracy" title="total accuracy">

# References
Neural Architecture Search with Reinforcement Learning [[1]][Paper]

[paper]: https://arxiv.org/abs/1611.01578 "Paper"
