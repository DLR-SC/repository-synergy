# deep-learning-multipliers

## Requirements

* Theano 0.6 (Bleeding edge version)
* Pylearn2 0.1 
* PyTables (for the SVHN dataset)
* a CUDA capable GPU

## Goal

This code was written to allow anyone to easily reproduce the results 
of the article "Deep learning with low precision multipliers", available at http://arxiv.org/abs/1412.7024 .
The article in question assesses whether it is possible to train Deep Neural Networks with low precision multipliers.

Note that this code only simulates the impact of low precision multipliers.
It does not exploit it in any way.
If you are looking for fast low precision GPU kernels, NervanaSystems made some available https://github.com/NervanaSystems/nervanagpu . 

## How to run it

### Command line

    python main.py [task] [format] [initial range] [propagations bit-width] 
        [parameters updates bit-width] [ranges updates frequency]
        [maximum overflow rate] [number of epochs of ranges initialization]

### Task

There are 4 different tasks: the permutation invariant MNIST (PI_MNIST), 
MNIST, CIFAR10 and SVHN.
A set of hyperparameters is associated with each of those tasks 
(They are stored in model.py).
For the SVHN dataset, 
you need to set an environment variable: 

    SVHN_LOCAL_PATH=/tmp/SVHN/ 
    
You then need to pre-process it with the script 
utilities/svhn_preprocessing.py (script taken from pylearn2).

### Format

There are 4 different formats: floating point (FLP), 
half floating point (HFLP), 
fixed point (FXP) and dynamic fixed point (DFXP).

### Initial range

Initial range is only useful for FXP and DFXP. 
It is the initial position of the radix point 
for the fixed point formats.
5 works most of the time.

### Propagations and parameters updates bit-widths

Only useful for FXP and DFXP.
Those are the bit-widths of respectively the 
propagations and the parameters updates.
Note that the sign is not counted in the bit-width.

### Ranges update frequency

Range update frequency is only useful for DFXP.
It is the number of batches between two ranges updates.

### Maximum overflow rate

Only useful for DFXP.
It is the amount of overflow tolerated before modifying the range.
    
### Number of epochs of range initialization

Only useful for DFXP.
This is the number of epochs we train with high precision 
to find the initial scaling factors.
Once they are found, 
the parameters are reinitialized, and the DFXP training can begin.    
        
### Examples

    python main.py PI_MNIST FLP
    python main.py SVHN FXP 5 19 19
    python main.py CIFAR10 DFXP 5 9 11 100 0.0001 2
        
