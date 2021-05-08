# DUpsampling
This repo is an unofficial pytorch implementation of CVPR19 paper: Decoders Matter for Semantic Segmentation: Data-Dependent Decoding Enables Flexible Feature Aggregation: https://arxiv.org/abs/1903.02120

Most recurrent update:

2019.03.14 - Add Synchronous BN operation and gradient accumulate to save gpu memory.

2019.03.13 - Add Weight pre-compute process.

2019.03.12 - Add softmax with temperature.

### Installation

* pytorch==0.4.1
* python==3.5
* numpy
* torchvision
* matplotlib
* opencv-python
* dominate
* random
* collections
* shutil

### Dataset and pretrained model

Plesae download VOC12_aug dataset and unzip the dataset into `data` folder.

Please download imagenet pretrained [resnet50-imagenet.pth](https://download.pytorch.org/models/resnet50-19c8e357.pth), and put it into `checkpoints` folder.

Please modify your configuration in `options/base options.py`.

### Usage

if you want to use the model with normal batch norm operation:

```bash
python train.py \
--name dunet \
--gpu_ids 0,1 \
--model DUNet \
--pretrained_model ./checkpoints/resnet50-imagenet.pth \
--batchSize 16 \
--dataroot ./data/voc_12aug \
--train_list_path ./data/train_aug.txt \
--val_list_path ./data/val.txt \
--accum_steps 1 \
--nepochs 100 \
--tf_log --verbose
```

if you want to use Synchronous BN operation with CUDA implementation, which must be compiled with the following commands:

```bash
cd libs
sh build.sh
python build.py
```

The `build.sh` script assumes that the `nvcc` compiler is available in the current system search path.
The CUDA kernels are compiled for `sm_50`, `sm_52` and `sm_61` by default.
To change this (_e.g._ if you are using a Kepler GPU), please edit the `CUDA_GENCODE` variable in `build.sh`.

Run the following command to run:

```bash
python train.py \
--name dunet_sybn \
--gpu_ids 0,1 \
--model DUNet_sybn \
--pretrained_model ./checkpoints/resnet50-imagenet.pth \
--batchSize 16 \
--dataroot ./data/voc_12aug \
--train_list_path ./data/train_aug.txt \
--val_list_path ./data/val.txt \
--accum_steps 1 \
--nepochs 100 \
--tf_log --verbose
```



### Segmentation results on val set

![](/image/image.png)

### To do

- [x] Add softmax function with temperature

- [ ] Modify the network and improve the accuracy.

- [x] Add Synchronous BN.

- [ ] Debug and report the performance.

- [ ] Improve code style and show more details.

under construction...

If you have any question, feel free to contact me or submit issue.

### Thanks to the Third Party Libs
[inplace_abn](https://github.com/mapillary/inplace_abn) - 
[Pytorch-Deeplab](https://github.com/speedinghzl/Pytorch-Deeplab) - 
[PyTorch-Encoding](https://github.com/zhanghang1989/PyTorch-Encoding)-
[pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)-
[Pytorch-segmentation-toolbox](https://github.com/speedinghzl/pytorch-segmentation-toolbox)

