# Keras implementation of Classification, Detection and Segmentation Networks

## Introduction

This repo contains the code to train and evaluate state of the art classification, detection and segmentation methods in a unified Keras framework working with Theano and TensorFlow. Pretrained models are also supplied.



## Available models

### Classification
 - [x] Lenet network as described in [Gradient-Based Learning Applied to Document Recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf).
 - [x] AlexNet network as described in [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf).
 - [x] VGG16 and VGG19 network as described in [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556.pdf).
 - [x] ResNet50 network as described in [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385v1.pdf).
 - [x] InceptionV3 network as described in [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/pdf/1512.00567v3.pdf).
 - [x] DenseNet network as described in [Densely Connected Convolutional Networks](https://arxiv.org/pdf/1608.06993).
 
### Detection
 - [X] YOLO network as described in [You Only Look Once: Unified, Real-Time Object Detection](https://pjreddie.com/media/files/papers/yolo.pdf).
 - [ ] SSD network as described in [SSD: Single Shot MultiBox Detector](https://arxiv.org/pdf/1512.02325).
 - [ ] Overfeat network as described in []().
  
### Segmentation
 - [x] FCN8 network as described in [Fully Convolutional Neural Networks](https://arxiv.org/abs/1608.06993).
 - [x] UNET network as described in [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597).
 - [x] Segnet network as described in [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://arxiv.org/pdf/1511.00561).
 - [x] ResnetFCN network as described in [Wider or Deeper: Revisiting the ResNet Model for Visual Recognition](https://arxiv.org/pdf/1611.10080).
 - [ ] DeepLab network as described in []().

## Available dataset wrappers

### Classification
 - [x] MIT dataset described in []().
 - [x] TT100K classsification dataset described in []().
 - [x] INRIA pedestrian dataset described in []().
 - [ ] ImageNet dataset described in []().
 - [ ] Pascal dataset described in []().
 
### Detection
 - [x] TT100K detection dataset described in []().
 - [x] INRIA pedestrian dataset described in []().
  
### Segmentation
 - [x] Camvid dataset described in [Semantic Object Classes in Video: A High-Definition Ground Truth Database ](http://www.cs.ucl.ac.uk/staff/G.Brostow/papers/SemanticObjectClassesInVideo_BrostowEtAl2009.pdf).
 - [x] Cityscapes dataset described in [The Cityscapes Dataset for Semantic Urban Scene Understanding](https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes.pdf).
 - [x] Synthia dataset described in [The SYNTHIA Dataset: A Large Collection of Synthetic Images for Semantic Segmentation of Urban Scenes](http://synthia-dataset.net/wp-content/uploads/2016/06/gros_cvpr16-1.pdf).
 - [x] Polyps dataset described in []().
 - [x] Pascal2012 dataset described in []().
 - [ ] Pascal2012 extra dataset described in []().
 - [ ] MSCOCO dataset described in []().
 - [ ] KITTI dataset described in []().
 - [ ] TT100K segmentation dataset described in []().

## Installation
You need to install :
- [Theano](https://github.com/Theano/Theano) or [TensorFlow](https://github.com/Theano/Theano). Preferably the last version
- [Keras](https://github.com/fchollet/keras)

## Run experiments
All the parameters of the experiment are defined at config/dataset.py where dataset.py is the name of the dataset to use. Configure this file according to you needs.

To train/test a model in Theano, use the command: `THEANO_FLAGS='device=cuda0,floatX=float32,lib.cnmem=0.95' python train.py -c config/dataset.py -e expName` where dataset is the name of the dataset you want to use and expName the name of the experiment.

To train/test a model in TensorFlow, use the command: `CUDA_VISIBLE_DEVICES=0 python train.py -c config/dataset.py -e expName -s SharedPath -l LocalPath` where dataset is the name of the dataset you want to use and expName the name of the experiment, SharedPath points to the folder in which the shared path is (same for LocalPath).

All the logs of the experiments are stored in the result folder of the experiment.

## Authors
David Vázquez, Adriana Romero, Michal Drozdzal, Lluis Gomez

## How to cite

## TODO
- [ ] Relaunch: Remember the number of the last epoch
