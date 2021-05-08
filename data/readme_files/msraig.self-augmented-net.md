# Modeling Surface Appearance from a Single Photograph using Self-augmented Convolutional Neural Networks

The main contributors of this repository include [Xiao Li](http://home.ustc.edu.cn/~pableeto), [Yue Dong](http://yuedong.shading.me), [Pieter Peers](http://www.cs.wm.edu/~ppeers/) and [Xin Tong](https://www.microsoft.com/en-us/research/people/xtong/).

## Introduction

This repository provides a reference implementation for the SIGGRAPH 2017 paper "Modeling Surface Appearance from a Single Photograph using Self-augmented Convolutional Neural Networks".

More information (including a copy of the paper) can be found at http://msraig.info/~sanet/sanet.htm.

## Update
10/23/2018: If you are looking for a (improved) Tensorflow version of Self-Augmentation training, you may have a look at our latest Pacific Graphics 2018 project page: https://github.com/msraig/InexactSA.

## Citation
If you use our code or models, please cite:

```
@article{Li:2017:MSA, 
 author = {Li, Xiao and Dong, Yue and Peers, Pieter and Tong, Xin},
 title = {Modeling Surface Appearance from a Single Photograph using Self-Augmented Convolutional Neural Networks},
 month = {July},
 year = {2017},
 journal = {ACM Transactions on Graphics},
 volume = {36},
 number = {4},
 article = {45},
 }
```

----------------------------------------------------------------
## Usage:

### System Requirements
   - Windows or Linux system (validated on Windows 10 and Ubuntu 12.04. Mac OSX is currently not supported)
   - A NVidia GPU (tested on Titan X and GTX 1080)
   - Python 2.7 (Python 3.x is not supported)
   - Caffe with Python support (tested with both CUDA 7.5 + cuDNN 5.0 and CUDA 8.0 + cuDNN 5.1)
   - We strongly recommend to install Anaconda2 which includes many of the necessary external packages. The following packages are required:
     * NumPy (tested with version 1.10.4, however newer versions should work too)
     * OpenCV (tested with version 3.1.0)
     * PyCUDA (tested with version 2016-1-2)
     * Matplotlib (tested with version 1.5.1)
     * skimage
     * jinja2


### Installation
After installing all the prerequisites listed above, download (or git clone) the code repository. Furthermore, to retrain the network, you may also need to download the datasets which includes training/test patches and collected lighting maps (see below).

### Preparing data
We also provide both training and test datasets to quickly test or reproduce SA-BRDF-Net or SA-SVBRDF-Net. The dataset can be downloaded from the project website: http://msraig.info/~sanet/sanet.htm. Because the complete rendered training and test image patches are too large, the dataset needs to be generated from the original SVBRDFs and lighting maps using the provided python scripts.

To generate from the downloaded data, first edit ./BRDFNet/folderPath.txt (for BRDF-Net) and/or ./SVBRDFNet/folderPath_SVBRDF.txt (for SVBRDF-Net). Next, to generate the training and test data for BRDF-Net, execute:

    python ./BRDFNet/RenderBRDFNetData.py $GPUID$ $BRDF_NET_DATA_FOLDER$

and/or to generate training and test data for SVBRDF-Net, execute:

    python ./SVBRDFNet/RenderSVBRDFDataset.py $SVBRDF_NET_DATA_FOLDER$ $CATEGORY_TAG$ $GPUID$ $RENDERTYPE$ -1 -1 $RENDERTEST$

with:

**$BRDF_NET_DATA_FOLDER$:** output folder for the BRDF-Net dataset.

**$SVBRDF_NET_DATA_FOLDER$**: folder containing the provided SVBRDFs (downloaded from the project website). This is also the output folder for the SVBRDF-Net dataset.

**$CATEGORY_TAG$**: set to "wood" "metal" or "plastic".

**$RENDERTYPE$**: 0 - only render PFM images; 1 - only render JPG images; 2 - render both. (0 or 2 are preferred)

**$RENDERTEST$**: set to "train" - only render training images; "test" - only render testing images; "all" - render both training and testing data.

### Testing the trained model
We also provide the trained CNN model for SA-SVBRDF-Net on Wood, Metal and Plastic dataset, as well as the model for SA-BRDF-Net, on the project website: http://msraig.info/~sanet/sanet.htm. 

To test the models on the provided SVBRDF datasets, execute: 

    python ./SVBRDFNet/TestSVBRDF.py $MODELFILE$ $TESTSET$ $GPUID$
    
with:

**$MODELFILE$**: Caffe model to test.

**$TESTSET$**: test dataset. Typically: **$SVBRDF_NET_DATA_FOLDER$\Test_Suppmental\$DATA_TAG$\list.txt**

For BRDF-Net, by default, the training script will automatically generate test reports after finishing the training. To manually test the model on the BRDF dataset, run:

    python ./BRDFNet/TestBRDF.py $MODELFILE$ $TESTCONFIG$ $GPUID$

with:

**$MODELFILE$**: Caffe model to test.

**$TESTCONFIG$**: a config ini file for testing. This should be generated during training.

The test results and a report (a HTML file) will be generated at the folder containing the trained model. 

**Note**: For to run this test you will need to download and generate the test data first (see section 2 above)

Advice for testing on your own images:

 - All our models are provided in the Caffe format.
 - The input to SVBRDF-Net model is an image (in [0, 1] range) with size 256*256. The output of our model is an albedo map and a normal map with the same size as input, a 3-channel vector represents RGB specular albedo and a float value representing the roughness. 


### Training from scratch
#### Training SA-BRDF-Net:
Edit the text file **./BRDFNet/BRDF_Net_Config.ini**, which contains all the relevant settings w.r.t. training. Change the following rows:

    dataset = $BRDF_NET_DATA_FOLDER$/train_envlight/train_full.txt
    unlabelDataset = $BRDF_NET_DATA_FOLDER$/train_envlight/train_full.txt
    testDataset = $BRDF_NET_DATA_FOLDER$/test_envlight/test_full.txt

These rows setup the paths for the training/test data; **$BRDF_NET_DATA_FOLDER$** is the folder of the BRDF-Net data.

By default, the training of SA-BRDF-Net is configured to only use the corners of the training space as labeled data, leaving rest as unlabeled data. This behavior is defined via **albedoRange**, **specRange** and **roughnessRange** parameters in the BRDF_Net_Config.ini. Changing these parameters change the distribution of labeled/unlabeled data. Please note that albedoRange and specRange are in the [0, 9] range, while roughnessRange is in the [0, 14] range.

To train the SA-BRDF-Model, run:

    python ./BRDFNet/BRDFNetTraining.py BRDF_Net_Config.ini $OUT_TAG$ $RESTORE_TAG$ $GPUID$ $RENDERGPUID$ $AUTOTEST$
    
with:

**$OUT_TAG$**: name of the training.

**$RESTORE_TAG$**: 0 - training from scratch

**$RENDERGPUID$**: must be the same as **$GPUID$**

**$AUTOTEST$**: 1 - running a full test and generate reports after training.

By default, the training snapshot and results are saved in **./TrainedResult/$OUT_TAG$** (relative to root of code folder).
You can change this by editing the first line in **./BRDFNet/folderPath.txt**.

#### Training SA-SVBRDF-Net
Open **./SVBRDFNet/SVBRDF_Net_Config.ini**, which contains all the settings w.r.t. the training, and change the following rows:

    dataset = $SVBRDF_NET_DATA_FOLDER$/$CATAGORY_TAG$/Labeled/trainingdata.txt
    unlabelDataset = $SVBRDF_NET_DATA_FOLDER$/$CATAGORY_TAG$/unlabeled.txt
    testDataset = $SVBRDF_NET_DATA_FOLDER$/$CATAGORY_TAG$/Test/test.txt
    
These rows setup the path for the training/test data; **$SVBRDF_NET_DATA_FOLDER$** is the folder of the SVBRDF-Net data. 
**$CATAGORY_TAG$** should be either of "wood", "metal" or "plastic".

    lightPoolFile = lightPool_$CATAGORY_TAG$.dat
    autoExposureLUTFile = lightNormPool_$CATAGORY_TAG$.dat
    
These rows setup the path for pre-defined lighting rotations and pre-computed auto-exposure factors.

To train the SA-SVBRDF-Model, run:
    
    python ./SVBRDFNet/SVBRDFNetTraining.py SVBRDF_Net_Config.ini $OUT_TAG$ $RESTORE_TAG$ $GPUID$ $RENDERGPUID$
    
with:    
**$OUT_TAG$**: name of the training.

**$RESTORE_TAG$**: 0 - training from scratch

**$RENDERGPUID$**: must be the same as **$GPUID$**

By default, the training snapshot and results are saved in **./TrainedResult/$OUT_TAG$** (relative to root of code folder). This can be changed by editing the first line in **./SVBRDFNet/folderPath_SVBRDF.txt**.
.
