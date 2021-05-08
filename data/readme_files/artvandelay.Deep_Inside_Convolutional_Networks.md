# Deep_Inside_Convolutional_Networks
This is a caffe implementation to visualize the learnt model.

Part of a class project at [Georgia Tech](www.cc.gatech.edu/~zk15/deep_learning_course.html)   
Problem Statement [Pdf](https://github.com/artvandelay/Deep_Inside_Convolutional_Networks/blob/master/Assignment3.pdf)   

Simonyan, K., Vedaldi, A., Zisserman, A.: Deep inside convolutional networks:
Visualising image classification models and saliency maps [Pdf](https://github.com/artvandelay/Deep_Inside_Convolutional_Networks/blob/master/1312.6034v2.pdf)

###Results: 

**Class Model visualization of Cat**  
In this exercise, we will use the method suggested in the “Deep inside convolutional
networks: Visualising image classification models and saliency maps” to visualize the class
model learnt by a convolutional network. We will use caffe for this exercise and visualize
the class model learnt by the “bvlc_reference_caffenet.caffemodel”.
Another aspect pointed out by the paper is that, the unnormalized Image score needs to be maximized instead of the
probability. For this reason, we will be drop the final softmax layer(as the output here is
the probability) and maximize the score at the inner product layer “fc8”.


![Cat](/results/ps3part1.png)

**Class Saliency extraction**  
The core idea behind this approach is to use the gradients at the image
layer for a given image and class, to find the pixels which need to be changed the least
i.e, the pixels for which the gradients have the smallest values. Also since our image is
a 3 channel image, for each pixel, there will three different gradients. The maximum of
these three will be considered the class saliency extraction.

![Cat](/results/ps3part2.png)

**Understanding backpropagation**
Here we simply visuzlize the gradients at different layers

![Cat](/results/ps3part3_conv2.png)
![Cat](/results/ps3part3_norm2.png)
![Cat](/results/ps3part3_pool5.png)
![Cat](/results/ps3part3_fc8.png)

### Instructions:
- Install [Caffe](https://github.com/BVLC/caffe)-*rc2* tag
- Copy the deploy_fc8.prototxt file to /models/bvlc_reference_caffenet/
- Copy all the py files to /examples/
- the just run `python visualize.py`



