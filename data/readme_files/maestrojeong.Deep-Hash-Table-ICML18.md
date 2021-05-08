 # Efficient end-to-end learning for quantizable representations
This repository has the source code for the paper "Efficient end-to-end learning for quantizable representations"(ICML18).

## Citing this work
```
@inproceedings{jeongICML18,
    title={Efficient end-to-end learning for quantizable representations},
    author={Jeong, Yeonwoo and Song, Hyun Oh},
    booktitle={International Conference on Machine Learning (ICML)},
    year={2018}
    }
```

## Installation
* Python3.5
* Deep learning frame work : Tensorflow1.4 gpu
Check [https://github.com/tensorflow/tensorflow/tree/r1.4](https://github.com/tensorflow/tensorflow/tree/r1.4)
* Ortools(6.6.4656)
Check [https://developers.google.com/optimization/introduction/download](https://developers.google.com/optimization/introduction/download)

## Prerequisites
1. Make Directory for data and experiment
```
cd RROOT
mkdir dataset deep_hash_table_processed deep_hash_table_exp_results
mkdir dataset/Imagenet32
``` 
2. Change path in config/path.py
```
RROOT = '(user enter path)'
EXP_PATH = RROOT+'deep_hash_table_exp_results/'
#=============CIFAR100============================#
CIFAR100PATH = RROOT+'dataset/cifar-100-python/'
CIFARPROCESSED = RROOT+'deep_hash_table_processed/cifar_processed/'
#==========================Imagenet32===============================#
IMAGENET32PATH = RROOT+'dataset/Imagenet32/'
IMAGENET32PROCESSED = RROOT+'deep_hash_table_processed/Imagenet32_processed/'
```
3. Download and unzip dataset Cifar-100 and Downsampled imagenet(32x32)
```
cd RROOT/dataset
wget https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz
tar zxvf cifar-100-python.tar.gz

cd RROOT/dataset/Imagenet32
wget http://www.image-net.org/image/downsample/Imagenet32_train.zip
wget http://www.image-net.org/image/downsample/Imagenet32_val.zip
unzip Imagenet32_train.zip
unzip Imagenet32_val.zip
```
## Processing Data
```
cd process
python cifar_process.py
python imagenet32_process.py 
```

## Training Procedure
* Cifar-100 experiment(*cifar_exps/*) and ImageNet experiment(*imagenet_exps/*).
1. Training metric(*metric/*)
    - **train_metric.py** is to train embedding with metric learning losses.
    - **test_metric.py** is to test the embedding with the hash codes built with vector quantization method(VQ) and thresholding method(Th).
2. Training hash codes(*exp1/*)
    - **train_hash.py** is to replace the last layer and fine tune the embedding with the proposed method in paper.
    - **test_hash.py** is to test the hash codes built with the embedding trained from *train_hash.py*.
## Evaluation
* Evaluation code is in **utils/evaluation.py**.
* The hash table built with hash code is evaluated with 3 different metric(*NMI, precision@k, SUF*).

## Ortools
* The code to solve the dicrete optimization problem in polynomial time is in **utils/ortools_op.py**
* The time to solve the discrete optimization problem is calculated with the code **ortools_exp/**

## License
MIT License 
