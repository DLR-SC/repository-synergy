A Python Implementation of a Random Forest
==========================================

This repository contains a few python modules that can be used to make 
a random forest classifer. 

This was implemented for my CS613 class as the final project. The point 
of the project was to evaluate the effectivness of using calculated joint
angles to classify dance gestures. An additional objective was to compare
the angle features to the more classical position features. 

The random generator that is used for bagging and making the subset of features
uses a system set seed, or random resouce, each time meaning that the results
will vary from trial to trial. The results have the same general pattern 
but you will not very likely see the same exact stats twice. 

To run through all of the experiements execute the python script:

./testing.py

inside of the src folder. 
