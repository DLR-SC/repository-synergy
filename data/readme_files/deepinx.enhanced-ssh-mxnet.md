
## The MXNet Enhanced SSH (ESSH) for Face Detection and Alignment

The Single Stage Headless (SSH) face detector was introduced in [ICCV 2017 paper](https://arxiv.org/abs/1708.03979). This repository includes code for training and evaluating the Enhance SSH (ESSH) face detector, which adds localization of five semantic facial landmarks to the original SSH method and also improves accuracy. You can use this ESSH method for face detection and 2D-5P face alignment.

Pre-trained models can be downloaded on [BaiduCloud](https://pan.baidu.com/s/1sghM7w1nN3j8-UHfBHo6rA) or [GoogleDrive](https://drive.google.com/open?id=1eX_i0iZxZTMyJ4QccYd2F4x60GbZqQQJ).

Evaluation on WIDER FACE:

|   Model   | Easy-Set | Medium-Set | Hard-Set |
| ------------------ | -------- | ---------- | -------- |
| *Original Caffe SSH* | 0.93123  | 0.92106    | 0.84582  |
| *Insightface SSH Model* | 0.93489  | 0.92281    | 0.84525  |
| *ESSH-VGG16 Model* | 0.94228  | 0.93207  | 0.87105  |
| *ESSH-Resnet50 Model* | **0.96100**  | **0.95122**  | **0.89610**  |

Note: More accurate pre-trained models will be released soon.

## Environment

This repository has been tested under the following environment:

-   Python 2.7 
-   Ubuntu 18.04
-   Mxnet-cu90 (==1.3.0)
-   Cython 0.29.6
-   MATLAB R2016b

## Installation

1.  Prepare the environment.

2.  Clone the repository.
    
3.  Type  `make`  to build necessary cxx libs.

## Testing

  -  Download the pre-trained model and place it in *`./model/`*.

  -  You can use `python test.py` to test the pre-trained models.

## Training
1. First, you should train an original SSH model on the [*WIDER* dataset](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace).
  -  Download the WIDER face training images from [BaiduCloud](https://pan.baidu.com/s/1NI4Pu4kyjH-j_miTqVKZlw) or [GoogleDrive](https://drive.google.com/file/d/0B6eKvaijfFUDQUUwd21EckhUbWs/view?usp=sharing) and the face annotations from the [dataset website](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/bbx_annotation/wider_face_split.zip). These files should be decompressed into `data/widerface` directory. 
  -  Download MXNet VGG16 ImageNet pretrained model from [here](http://data.dmlc.ml/models/imagenet/vgg/vgg16-0000.params) and put it under `model` directory. 
  -  Edit `config.py` and type `python train.py` or using the following command to train your SSH model.
```
python train.py --network ssh --prefix model/sshb --dataset widerface --gpu 0 --pretrained model/vgg16 --lr 0.004 --lr_step 30,40,50
```
2. Then, use the above SSH model as the pre-training model to train the final ESSH model on [CelebA Dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html). 
  - Download the CelebA dataset from [BaiduCloud](http://pan.baidu.com/s/1eSNpdRG) or [GoogleDrive](https://drive.google.com/open?id=0B7EVK8r0v71pWEZsZE9oNnFzTm8) and decompressed it into `data/celeba` directory.
  - Download our re-annotated bounding box labels from [BaiduCloud](https://pan.baidu.com/s/1wiOo__wWjjiauI7li_naDg) or [GoogleDrive](https://drive.google.com/open?id=1bIq7Eu108HySN5y5WLKbIks5isDxAYnh) and replace `Anno/list_bbox_celeba.txt` with this file. Note that our bounding box annotations  are more accurate than the original labels, so be sure to download and replace it.
  -  Edit `config.py` and type `python train.py` or using the following command to train the ESSH model.
```
python train.py --network essh --prefix model/e2e --dataset celeba --gpu 0 --pretrained model/sshb --lr 0.004 --lr_step 10,15
```

## Evaluation
  
  The evaluation is based on the official *WIDER* evaluation tool which requires *MATLAB*. You need to download the [validation images](https://drive.google.com/file/d/0B6eKvaijfFUDd3dIRmpvSk8tLUk/view?usp=sharing) and the [annotations](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/support/bbx_annotation/wider_face_split.zip) (if not downloaded for training) from the *WIDER* [dataset website](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/). To evaluate pre-trained models on validation set of the WIDER dataset, you can use `python test_on_wider.py` to obtain the performance in “easy”, “medium”, and “hard” subsets respectively. We give some examples below. 

1. Evaluate SSH model on validation set of the WIDER dataset without an image pyramid.
```
python test_on_wider.py --dataset widerface --method_name SSH --prefix model/sshb --gpu 0 --output ./output --thresh 0.05
```

2. Evaluate ESSH model on validation set of the WIDER dataset with an image pyramid.
```
python test_on_wider.py --dataset widerface --method_name ESSH-Pyramid --prefix model/essh --gpu 0 --output ./output --pyramid --thresh 0.05
```

## Results

Results of face detection and 2D-5P face alignment (inferenced from *ESSH-Resnet50* model) are shown below.

<div align=center><img src="https://raw.githubusercontent.com/deepinx/SSH_alignment/master/sample-images/detection_result.png" width="700"/></div>

## License

MIT LICENSE


## Reference

```
@inproceedings{Najibi2017SSH,
  title={SSH: Single Stage Headless Face Detector},
  author={Najibi, Mahyar and Samangouei, Pouya and Chellappa, Rama and Davis, Larry S.},
  booktitle={IEEE International Conference on Computer Vision},
  year={2017},
}

@inproceedings{yang2016wider,
  author = {Yang, Shuo and Luo, Ping and Loy, Chen Change and Tang, Xiaoou},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  title = {WIDER FACE: A Face Detection Benchmark},
  year = {2016}}
  
  @inproceedings{liu2015faceattributes,
  author = {Ziwei Liu and Ping Luo and Xiaogang Wang and Xiaoou Tang},
  title = {Deep Learning Face Attributes in the Wild},
  booktitle = {Proceedings of International Conference on Computer Vision (ICCV)},
  month = December,
  year = {2015} 
}
```

## Acknowledgment

The code is adapted based on an intial fork from the [SSH](https://github.com/mahyarnajibi/SSH) and the [mxnet-SSH](https://github.com/deepinsight/mxnet-SSH) repository.


