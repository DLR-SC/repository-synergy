# tf_rfcn

This is an experimental tensorflow implementation of R-FCN by: Dai, Jifeng, et al. "R-FCN: Object Detection via Region-based Fully Convolutional Networks." arXiv preprint arXiv:1605.06409 (2016).

Base trunk is a ResNet (can be 50-101-152 layers). Training is done end-to-end. 

Anchor, proposal, and proposal target layers are based on Ross Girshick's py-faster-rcnn (https://github.com/rbgirshick/py-faster-rcnn), with some modifications by Orpine in (https://github.com/Orpine/py-R-FCN) for the proposal target layer.

Training only for the moment, no testing phase yet.

created by A. Labao under Pros Naval of CVMIG Lab, University of the Philippines

# Specs
tf_rfcn_fixed : accepts any image (as specified in source folder) and resacles to 600 x 1000, input is JPEG image <br />
tf_rfcn_dynamic : accepts any image size and tensors are adjusted to a size of 600 for the shorter side, input is roidb pkl file. A sample code for making the imdb is [here](https://github.com/alfonsolink/roidb_maker), adopted from the original MNC [code](https://github.com/daijifeng001/MNC) - code has to be modified to your local PASCAL VOC datasets folders.

# Performance
In terms of end cls accuracy, tf_rfcn_dynamic has an accuracy of 93% after ~70k iterations, with an anchor accuracy of 99% given the PASCAL VOC 2012 SDS dataset, and a 101-layer ResNet trunk. Results are obtained with ImageNet pretrained [weights](https://1drv.ms/f/s!AtPFjf_hfC81kUrPD2Kazg1Gtkz6), which can be called using saver_all_trunkrcnn.restore() -- which sets the base trunk and "rcnn" layers to ImageNet weights ("fc" layers are not included in ImageNet initialization)

# Requirements
GTX 1070 <br />
OpenCV 3.1 <br />
Cuda 7.5+ <br />
Cudnn 5.0+ <br />
tensorflow v10+ <br />
and psroi_pooling_op.so installed - check my other git repository [here] (https://github.com/alfonsolink/tensorflow_user_ops) for the psroi_pooling tensorflow wrap)

