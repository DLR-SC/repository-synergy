This is the code used to compute the results for the CVPR paper 

```
@inproceedings{wohlhart15,
  author = "Paul Wohlhart and Vincent Lepetit",
  title = {{Learning Descriptors for Object Recognition and 3D Pose Estimation}},
  booktitle = {{Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition}},
  year = 2015
}
```

or more precisely a refactored but functionally equivalent version thereof.

Thus far, there is _no_ documentation, except for the sporadic, cryptic comments in the code.
As soon as people start using this code and get back to me with questions, 
I will try to assemble a combination of tutorial and FAQ at the project website: 
https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/object-detection-and-3d-pose-estimation/


Additionally, I would like to make you aware of the efforts by Yida Wang to implement the 
above mentioned paper using a combination of opencv and caffe and contributing to both. 
At this point there is an initial pull request for the triplet loss layer: https://github.com/BVLC/caffe/pull/2603 


# Disclaimer

This code is released under LPGLv3.0 (see lgpl-3.0.txt)

Additionally, note that running this code might cause unpleasent and unexpected output ranging from killing your kitten
 to the most unprobable events like turning a nuclear missile into a sperm whale or petunia. 

Also, keep in mind this is my first project in python. 
If you find chunks making you feel "that's not how you do that in python", please go ahead and tell me about it.

#  Basic Requirements / Installation

1. You need theano up and running (http://deeplearning.net/software/theano/)
2. The project consists of two parts: TheanoNetCore and ObjRecPoseEst
    * ObjRecPoseEst is the application containing the logic to load and preprocess data,
define a network, train and test it, visualize filters and sample results and output performance curves.  
It builds on TheanoNetCore which needs to be in the PYTHON_PATH to run any of the main routines of ObjRecPoseEst.
    * TheanoNetCore is our attempt to build a CNN specification/training/running framework on top of theano.
(Had things like lasagne been around when we started, we would probably just have used that, 
but now we are stuck with our own stuff, and honestly I dont think its so bad.)  
TheanoNetCore was "designed" (ie. hacked away) with the idea to be very flexible. 
We dont impose any data-format other than the basic input to a theano function, which is essentially a numpy ndarray.
Networks can be specified in config files, but dont have to be.
There is functionality to specify, train, save, load and test networks.
There are definitions for a number of different kinds of layers.
With the recent additional of DAGNetworks (directed acyclic graph) 
the networks can even be quite complex in structure.  
There is a trainer taking care of training the network. Currently it's doing too much. 
Optimizers and Cost functions are not yet pulled into separate modular and interchangable entities.
(That's a TODO).  
Additionally, there is a MacroBatchManager taking care of swapping in and out sets of minibatches (macro batches) 
if the whole training set (in addition to the network itself) is too large to fit into GPU all at once. 

3. You need my version of the LineMOD data  
Download the data from our project page
https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/object-detection-and-3d-pose-estimation/  
Additionally you need the color images (colorXXX.jpg) of the 
test sequences from the original LineMOD dataset: 
http://campar.in.tum.de/Main/StefanHinterstoisser
(median filtered versions of the corresponding depth data are included in the tars as pngs)

# Main Workflow  - to get the results of the paper

```
> cd ObjRecPoseEst 
> mkdir data/results/linemod_realandsynth_o15_dagnet
> cd src 
```

Adjust the path to the LineMOD data (lmDataBase) in linemod_ras_o15_rgbd_dagnet_simple.ini

```
> python main_train_dagnet.py ../configs/linemod_ras_o15_rgbd_dagnet_simple.ini 
> python main_test.py ../data/results/linemod_realandsynth_o15_dagnet/
```

For a simple demo on only 3 objects, 3-dim descriptors and only a few epochs of training
(and thus to check if everything works)
try the config file linemod_ras_o3_rgbd_dagnet.ini

# TODO
Things I wanted to get done before releasing the code, but apparently wont get around to  

Overall

* Use logging instead of just printing everywhere


main_train_dagnet.py

* Use loading and saving of networks, instead of pickling them a as a whole 
  (which makes problems, for instance, when you move them between computers 
  where you dont have the exact same theano version)


TheanoNetCore

* Introduce Cost layers instead of computing the cost in the trainer
* Move the optimization scheme from the trainer to reusable and exchangeable Optimizers
