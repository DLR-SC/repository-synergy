## DecoupledNet: Decoupled Deep Neural Network for Semi-supervised Semantic Segmentation 

Created by [Seunghoon Hong](http://cvlab.postech.ac.kr/~maga33/), [Hyeonwoo Noh](http://cvlab.postech.ac.kr/~hyeonwoonoh/) and [Bohyung Han](http://cvlab.postech.ac.kr/~bhhan/) at POSTECH

Acknowledgements: Thanks to Yangqing Jia and the BVLC team for creating Caffe.

### Introduction

DecoupledNet is semantic segmentation system which using heterogeneous annotations.
Based on pre-trained classification network, DecoupledNet fine-tune the segmentation network with very small amount of segmentation annotations and obtains excellent results on semantic segmentation task.

Detailed description of the system will be provided by our technical report [arXiv tech report] http://arxiv.org/abs/1506.04924 

### Citation

If you're using this code in a publication, please cite our papers.

    @article{hong2015decoupled,
      title={Decoupled Deep Neural Network for Semi-supervised Semantic Segmentation},
      author={Hong, Seunghoon and Noh, Hyeonwoo and Han, Bohyung},
      journal={arXiv preprint arXiv:1506.04924},
      year={2015}
    }

### Pre-trained Model

If you need model definition and pre-trained model only, you can download them from following location:
  0. caffe for DecoupledNet: https://github.com/HyeonwooNoh/caffe
  0. DecoupledNet [Full annotation] : 
    0. [prototxt] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_Full_anno/DecoupledNet_Full_anno_inference_deploy.prototxt)
    0. [caffemodel] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_Full_anno/DecoupledNet_Full_anno_inference.caffemodel)
  0. DecoupledNet [25 annotations] : 
    0. [prototxt] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_25_anno/DecoupledNet_25_anno_inference_deploy.prototxt)
    0. [caffemodel] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_25_anno/DecoupledNet_25_anno_inference.caffemodel)
  0. DecoupledNet [10 annotations] : 
    0. [prototxt] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_10_anno/DecoupledNet_10_anno_inference_deploy.prototxt)
    0. [caffemodel] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_10_anno/DecoupledNet_10_anno_inference.caffemodel)
  0. DecoupledNet [5 annotations] : 
    0. [prototxt] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_5_anno/DecoupledNet_5_anno_inference_deploy.prototxt)
    0. [caffemodel] (http://cvlab.postech.ac.kr/research/decouplednet/model/DecoupledNet_5_anno/DecoupledNet_5_anno_inference.caffemodel)

### Licence

This software is being made available for research purpose only.
Check LICENSE file for details.

### System Requirements

This software is tested on Ubuntu 14.04 LTS (64bit).

**Prerequisites** 
  0. MATLAB (tested with 2014b on 64-bit Linux)
  0. prerequisites for caffe(http://caffe.berkeleyvision.org/installation.html#prequequisites)

### Installing DecoupledNet

**By running "setup.sh" you can download all the necessary file for training and inference including:**
  0. caffe: you need modified version of caffe which support DeconvNet - https://github.com/HyeonwooNoh/caffe.git
  0. data: data used for training
  0. model: caffemodel of trained DecoupledNet and caffemodel of pre-trained classification network

### Training DecoupledNet

Training scripts are included in *./training/* directory

**To train DecoupledNet with various setting, you can run following scripts**
  0. 001_convert_classification_network_to_fp_bp_network.sh: 
    * converting classification network to make forward-backward propagation possible (this converted model is prerequisite for DecoupledNet training)
  0. 002_train_seg_Full_anno.sh: 
    * training DecoupledNet with full segmentation annotations
  0. 003_train_seg_25_anno.sh: 
    * training DecoupledNet with 25 segmentation annotations per class
  0. 004_train_seg_10_anno.sh: 
    * training DecoupledNet with 10 segmentation annotations per class
  0. 005_train_seg_5_anno.sh: 
    * training DecoupledNet with 5 segmentation annotations per class

### DecoupledNet Inference

Inference scripts are included in *./inference/* directory.

Run *run_demo.m* to run DecoupledNet on VOC2012 test data.

**run_demo.m script will run DecoupledNet trained in various settings (Full, 25, 10, 5 annotations):**
  0. DecoupledNet-Full (66.6 mean I/U on PASCAL VOC 2012 Test)
  0. DecoupledNet-25   (62.5 mean I/U on PASCAL VOC 2012 Test)
  0. DecoupledNet-10   (58.7 mean I/U on PASCAL VOC 2012 Test)
  0. DecoupledNet-5    (54.7 mean I/U on PASCAL VOC 2012 Test)

