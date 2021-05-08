# PyFeast
Python bindings to the FEAST Feature Selection Toolbox..

## Download

[Downlaod Version 1.1](https://github.com/mutantturkey/PyFeast/releases/tag/v1.1)
## About PyFeast
PyFeast is a interface for the FEAST feature selection toolbox, which was
originally written in C with a interface to Matlab.

Because Python is also commonly used in computational science, writing bindings 
to enable researchers to utilize these feature selection algorithms in Python 
was only natural.

At Drexel University's [EESI Lab](http://www.ece.drexel.edu/gailr/EESI/), we are using PyFeast to create a feature
selection tool for the Department of Energy's upcoming KBase platform. We are also integrating a tool that utilizes
PyFeast as a script for Qiime users: [Qiime Fizzy Branch](https://github.com/EESI/FizzyQIIME)

## Requirements
In order to use the feast module, you will need the following dependencies

* Python 2.7
* Numpy
* Linux or OS X 
* [MIToolbox](https://github.com/Craigacp/MIToolbox)
* [FEAST](https://github.com/Craigacp/FEAST) v1.1.1 or higher

## Installation

    python ./setup.py build
    sudo python ./setup.py install

## Demonstration
See test/test.py for an example with uniform data and an image
data set. The image data set was collected from the digits example in 
the Scikits-Learn toolbox. Make sure that if you are loading the data from a file and converting the data to a `numpy` array that you set `order="F"`. This is *very* important. 

## Documentation
We have documentation for each of the functions available [here](http://mutantturkey.github.com/PyFeast/feast-module.html)

## References
* [FEAST](http://www.cs.man.ac.uk/~gbrown/fstoolbox/) - The Feature Selection Toolbox  
* [Fizzy](http://www.kbase.us/developer-zone/api-documentation/fizzy-feature-selection-service/)  - A KBase Service for Feature Selection
* [Conditional Likelihood Maximisation: A Unifying Framework for Information Theoretic Feature Selection](http://jmlr.csail.mit.edu/papers/v13/brown12a.html) 
