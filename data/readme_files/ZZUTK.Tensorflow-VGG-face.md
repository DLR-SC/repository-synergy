# Tensorflow-VGG-face
Implement VGG-face by Tensorflow using the pre-trained model from [MatConvNet](http://www.vlfeat.org/matconvnet/).

## Pre-requisites
* Python 2.7
* Scipy
* Tensorflow
* Pre-trained model [vgg-face.mat](http://www.vlfeat.org/matconvnet/models/vgg-face.mat) (MD5: 3d6cd504bf9c98af4a561aad059565d1)

## Test on the pre-trained model

```
$ python test_vgg_face.py
```

## Result

```
Classification Result:
        Category Name: Aamir_Khan
        Propbability: 51.60%
        
        Category Name: Adam_Driver
        Propbability: 6.78%
        
        Category Name: Manish_Dayal
        Propbability: 1.95%
```
