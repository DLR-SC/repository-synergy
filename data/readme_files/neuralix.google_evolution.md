Exotic structured image classifier
=====================================

This implements one of result networks from [Large-scale evolution of image classifiers](https://arxiv.org/abs/1703.01041) by Esteban Real, et. al.

## Requirements
- Install [pytorch](http://pytorch.org/) (I recommend anaconda environment.)
- Install [scikit-learn](http://scikit-learn.org/stable/)
- Download [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html)

## Training
1. Copy two files to `{torchvision_path}/models`
```bash
cp {__init__.py,evloution.py} {torchvision_path}/models
```

2. Run
```bash
python main.py -a evolution {cifar10_data_dir}
```

cf. How to know {torchvision_path}?
```
import torchvision
print(torchvision.__file__)
```

## Note
1. The numbers of channels are not in the paper and it is set by me similar with vgg.
You need to adjust these for better performance.

2. If you want to adsjust learning rate on-the-fly, create `lr.txt` having lr value in same directory with main.py. And just change the value before some epoch you want to adopt new lr value.

3. Used CIFAR10 is image file dataset. It's not CIFAR-10 {python,Matlab,binary} version.
You should convert it to conventional image files. It you don't want it, you have to use your proper dataloader.

## Implemented network
<p align="center">
<img src="https://raw.githubusercontent.com/neuralix/google_evolution/master/fig_network.png"/>
</p>
