# Factorized-Bilinear-Network
This repository holds the MXNet code for the paper:

>
**Factorized Bilinear Models for Image Recognition**,
Yanghao Li, Naiyan Wang, Jiaying Liu, and Xiaodi Hou,
arXiv preprint arXiv:1611.05709, 2016
>
[[Arxiv Preprint](https://arxiv.org/abs/1611.05709)]


## Introduction

Factorized-Bilinear-Network proposes a novel Factorized Bilinear (FB) layer to model the pairwise feature interactions by considering the quadratic terms in the transformations. The factorized parameterization makes our FB layer only require a linear increase of parameters and affordable computational cost. A specific remedy called DropFactor is also devised during the training process to further reduce the risk of overfitting of the FB layer.

#### CIFAR Results:

| Method | params | CIFAR-10 | CIFAR-100 |
| :------------ | :---------: | :---------: | :-------------: |
| Inception-BN | 1.7M  | 5.82 | 24.70 |
| ResNet-164 (ours) | 1.7M | 5.30 | 23.64 |
| ResNet-1001 (ours) | 10.2M | 4.04 | 20.50 |
| Inception-BN-FBN | 2.4M | 5.58 | 21.98 |
| ResNet-164-FBN | 2.2M  | 5.00 | 22.50 |
| ResNet-1001-FBN | 10.7M | 4.09  | 19.67 |

#### ImageNet Results:

| Method  | Top-1(%) | Top-5 (%) |
| :------------ | :---------: | :---------: |
| Inception-BN | 27.5 | 9.2 |
| Inception-BN-FBN | 26.4 | 8.4 |
| ResNet-34 | 27.7     | 9.1 |
| ResNet-34-FBN | 26.3 | 8.4 |
| ResNet-50     | 24.7 | 7.4 |
| ResNet-50-FBN | 24.0 | 7.1 |


## Prepare Datasets

Prepare the corresponding datasets (CIFAR-10, CIFAR-100 or ImageNet) before training FBNs. In our experiments, we use RecordIO data format to generate `.rec` files for different datasets. Please refer to [MXNet Example](https://github.com/dmlc/mxnet/tree/master/example/image-classification#prepare-datasets). 

For example, you should first prepare the `train.lst` and `test.lst`, then generate the `.rec` file using `im2rec` tool. An example for ImageNet:
```shell
$im2rec_path train.lst train/ data/imagenet/train_480_q90.rec resize=480 quality=90
```


## Usage

Download this repo recursively:
```shell
git clone --recursive https://github.com/lyttonhao/Factorized-Bilinear-Network.git
```

We implement two versions of factorized bilinear layer:
1. `mx.symbol.FMConvolution1()`: similar to Convolution layer with additional FB parameters:
    * **num_factor**: the factor number for the FB layer. We use 20 in CIFAR dataset. For ImageNet, larger value (50) may improve the performance.
    * **p**: drop rate for DropFactor

2. `mx.symbol.FMConvolution3()`: speed-up version of `FMConvolution1` using batch_dot, but cost more memory. (The GPU memory may not be enough for large model.)

### CIFAR
The original fully connected layer can be replaced by a `FMConvolution3` layer:
```python
bilinear = mx.symbol.FMConvolution3(data=in5b, num_filter=num_classes, num_factor=args.fmconv_factor,
                                    kernel=(1, 1), stride=(1, 1),
                                    pad=(0, 0), p=args.fmconv_drop, name='bilinear1')
```
The training command:
```shell
python train_cifar.py --gpus 2,3 --data-dir /mnt/hdd/lytton/mx_data/cifar-100 --lr 0.1 --wd 0.0001 --batch-size 128 --data-shape 32 --num-epoches 100 --network resnet-small-fmconv --num-classes 100 --lr-step 50,75 --model-prefix cifar100_res18_fmconv22-3  --res-module-num 18  --fmconv-slowstart 3 --fmconv-drop 0.5 --fmconv-factor 20
```
More examples can be seen in the `cifar/run.sh` and you can run `python cifar/train_cifar.py` with `-h` to see more options.

### ImageNet
Our training policy and augmentation methods follow the [MXNet ResNet](https://github.com/tornadomeet/ResNet#imagenet) which reproduced ResNet in MXNet. Please using specific settings (like lr schedulers and training epochs) in [MXNet ResNet](https://github.com/tornadomeet/ResNet#imagenet) if compares with its original MXNet ResNet results.

An example of training command:
```shell
python train_imagenet.py --gpus 0,1,2,3,4,5,6,7  --model-prefix resnet34-fmconv --network resnet-fmconv --batch-size 256 --aug-level 2  --num-epoches 120 --frequent 50  --lr 0.1 --wd 0.0001   --lr-step 60,75,90  --fmconv-drop 0.5  --fmconv-slowstart 1 --fmconv-factor 50 --depth 34
```
Usually, we will cancel the scale/color/aspect augmentation during training (set `--aug-level=1` for around additional 10 epochs) for better result.
