# README #

The codes are with the CVPR2016 paper ["CRAFT Objects from Images"](http://byangderek.github.io/projects/craft.html).

In a word, we extend the conventional two-stage object detection framework (first locating object proposals, then classifying object categories) to a four-stage pipeline, in which the proposal localization task is solved with a cascade network of Region Proposal Network (RPN) and Fast R-CNN to improve the proposal quality, while the object classification task is handled by a cascade network of two Fast R-CNN nets with different objective functions (one-hot classification and one-vs-rest classification) to eliminate false positives.

We name our approach "CRAFT" (short for "Cascade Rpn And FasT-rcnn") and show considerable improvement over Fast R-CNN and Faster R-CNN baselines on PASCAL VOC 07/12 and ILSVRC datasets. For more details please refer to our [CVPR2016 paper](http://byangderek.github.io/projects/craft.html).

The codes are built on [RPN](https://github.com/ShaoqingRen/faster_rcnn) (Stage 1) and [Fast R-CNN](https://github.com/rbgirshick/fast-rcnn) (Stage 2,3,4). It would be easier to use the codes if you are familiar with these two projects.

The codes are tested on Ubuntu 14.04, 256GB Memory, Titan X GPU, MATLAB R2015a.

### Preparation ###
1. Follow instructions in [Faster R-CNN](https://github.com/ShaoqingRen/faster_rcnn) to make the codes in `1_RPN`, using [Caffe](https://github.com/ShaoqingRen/caffe/tree/062f2431162165c658a42d717baf8b74918aa18e) provided by Shaoqing Ren
2. Follow instructions in [Fast R-CNN](https://github.com/rbgirshick/fast-rcnn) to make the codes in `2_CasRPN`, `3_FRCN`, and `4_CasFRCN`, using our slightly modified [Caffe](https://github.com/byangderek/caffe-fast-rcnn)
3. Download the VGG16 pre-trained model and PASCAL VOC 2012 dataset and make proper links pointing to them
4. You can create a soft link of folders `caffe-fast-rcnn` and `data` for `2_CasRPN`, `3_FRCN`, and `4_CasFRCN` for convenience.

### Training and testing ###

The whole pipeline is stage-wise. Now we show how to train an object detector using CRAFT approach on PASCAL VOC 2012 train+val dataset and test it on PASCAL VOC 2012 test set. For simplicity, we do not use joint training between RPN and Fast R-CNN networks. 

**Stage 1. RPN**

```
cd 1_RPN
matlab ./experiments/script_faster_rcnn_VOC2012_VGG16.m
matlab saveProposals.m
```

**Stage 2. CasRPN**

```
cd 2_CasRPN
bash train.sh
bash test.sh
matlab saveProposals.m
```

**Stage 3. FRCN**

```
cd 3_FRCN
bash train.sh
bash test.sh
matlab saveDetections.m
```

**Stage 4. CasFRCN**

```
cd 4_CasFRCN
bash train.sh
bash test.sh
```

### Results ###
                          | training data                          | test data            | mAP   
------------------------- |:--------------------------------------:|:--------------------:|:-----:
CRAFT, VGG-16             | VOC 2007 trainval + 2012 trainval      | VOC 2007 test        | 75.7% 
CRAFT, VGG-16             | VOC 2012 trainval                      | VOC 2012 test        | 71.3% 

Note: The real mAP results may vary a little from the above results reported in the paper. We do not adopt joint training between RPN and Fast R-CNN currently.

### Reference ###

If you use our codes in your research, we are grateful if you cite the paper:

```
@inproceedings{binyang16craft,
  title={Craft Objects from Images},
  author={Yang, Bin and Yan, Junjie and Lei, Zhen and Li, Stan},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2016}
}
```

### Acknowledgement ###

We give our sincere gratitude to the following people, groups and institutions:

* Anonymous reviewers
* Ross Girshick for the Fast R-CNN project
* Shaoqing Ren for the Faster R-CNN project
* Caffe team
* VGG team
* SenseTime Group Limited
* NVIDIA Corporation
