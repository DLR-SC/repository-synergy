# Implementation of VoxResNet

This is a repository containing code of Deep Voxelwise Residual Networks for Volumetric Brain Segmentation (VoxResNet) [1].

Note that this is not an official implementation.


# Requirements
- python 3.6
- chainer v2
- cupy
- dipy
- nibabel
- numpy
- pandas
- SimpleITK


# Preparing dataset
1. Download [Internet Brain Segmentation Repository (IBSR)](https://www.nitrc.org/frs/download.php/5731/IBSR_V2.0_nifti_stripped.tgz) (or other dataset you want to try)
2. preprocess dataset
  - training dataset
  `$ python preprocess.py -i /path/to/IBSR/dataset -s IBSR_01 IBSR_02 IBSR_03 IBSR_04 IBSR_05 --input_image_suffix _ana_strip.nii.gz --output_image_suffix _preprocessed.nii.gz --label_suffix _segTRI_ana.nii.gz -f dataset_train.json --n_classes 4 --zooms 1. 1. 1.`
  - test dataset
  `$ python preprocess.py -i /path/to/IBSR/dataset -s IBSR_11 IBSR_12 IBSR_13 IBSR_14 IBSR_15 --input_image_suffix _ana_strip.nii.gz --output_image_suffix _preprocessed.nii.gz --label_suffix _segTRI_ana.nii.gz -f dataset_test.json --n_classes 4 --zooms 1. 1. 1.`


# Train VoxResNet
`$ python train.py -g 0 -f dataset_train.json`


# Test VoxResNet
`$ python segment.py -g 0 -i dataset_test.json -m vrn.npz -o _segTRI_predict.nii.gz`


# Reference

[1] Chen, Hao, et al. "VoxResNet: Deep Voxelwise Residual Networks for Volumetric Brain Segmentation." arXiv preprint arXiv:1608.05895 (2016).
