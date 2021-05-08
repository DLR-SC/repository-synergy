# FCN_via_Keras

## FCN

FCN (Fully Convolutional Network) is deep fully convolutional neural network architecture for semantic pixel-wise segmentation. This is implementation of "https://arxiv.org/abs/1605.06211" by using Keras which is a neural networks library. FCN can train by using any size of image, but I trained this network using the images of the same size (224 * 224).

## Usage

### train

```
$ python train.py -tr <path to train dataset> -ta <path to target dataset> -tt <image file names text> -e <epoch> -b <batchsize>
```
#### Example
```
$ python train.py -tr /Volumes/DATASET2/VOCdevkit/VOC2012/JPEGImages/ -ta /Volumes/DATASET2/VOCdevkit/VOC2012/SegmentationClass/ -t train.txt
```
### predict
```
$ pyton predict.py -i <path to image>
```
#### Example
```
$ python train.py -i demo_imgs/2011_003255.jpg
```

## Caution

Please use theano as backend  because this couldn't work on tensorflow backend. I'm trying debug now. I update this code if I get factor of that.
