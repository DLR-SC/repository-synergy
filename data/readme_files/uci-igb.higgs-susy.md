higgs-susy
==========

This project contains python code to replicate the results in the following publication:

Baldi, P., P. Sadowski, and D. Whiteson. “Searching for Exotic Particles in High-energy Physics with Deep Learning.” Nature Communications 5 (July 2, 2014).

Warning: Pylearn2 is no longer being developed. For more active deep learning software frameworks, check out Keras, Tensorflow, etc. 

Note: Due to an old bug in the Pylearn2 termination_criteria module, the deep models were trained for ~1000 epochs. The models here may terminate training after only ~200 epochs, in which case the termination criteria should be changed to train for the full 1000 epochs to get the same results in the paper. 

Additional Requirements:

1) The HIGGS and SUSY datasets available from the UCI ML Repository

http://archive.ics.uci.edu/ml/datasets/HIGGS

http://archive.ics.uci.edu/ml/datasets/SUSY

2) Pylearn2 and Theano

http://deeplearning.net/software/theano/

http://deeplearning.net/software/pylearn2/
