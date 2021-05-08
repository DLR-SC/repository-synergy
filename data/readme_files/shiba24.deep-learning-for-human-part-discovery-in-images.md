# Deep Learning for Human Part Discovery in Images - Chainer implementation

NOTE: This is not official implementation. Original paper is [Deep Learning for Human Part Discovery in Images](http://lmb.informatik.uni-freiburg.de/Publications/2016/OB16a/oliveira16icra.pdf).

We are now reproducing the experiments in the original paper. Any contribution will be welcomed!

# Requirements

- Python 2.7.11+

  - [Chainer 1.10+](https://github.com/pfnet/chainer)
  - numpy 1.9+
  - scipy 0.16+
  - six
  - matplotlib
  - tqdm
  - cv2 (opencv)


# Preparation

## Data

```
bash prepare.sh
```

This script downloads VOC 2010 dataset (<http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar>) and the authors' original dataset (<http://www2.informatik.uni-freiburg.de/~oliveira/datasets/Sitting.tar.gz>).

## Model

You can download pre-trained FCN model from [here](https://drive.google.com/open?id=0BxSyYt1jT6LhUlhITjdicDFyNHM).

We will use weights of this model and train new model on VOC dataset.

# Start training

```
python train.py -g 0 -b 3 -e 3000 -l on -s on
```

## Possible options

```
python train.py --help
```

## GPU memory requirement

Citation from the original paper:

> Each minibatch consists of just one image. The learning rate and momentum are fixed to 1e 10 and 0.99, respectively. We train the   refinement layer by layer, which takes two days per refinement layer. Thus, the overall training starting from the pre-trained VGG network took 10 days on a single GPU.

Current maximum batchsize is ```3``` for 12 GB memory GPU.

Also it was confirmed that MBP (Late 2016, memory 16 GiB) can run with batchsize ```1```.

## Result

Now in prep.

# Visualize Prediction

```
python visualize.py -f PATH_TO_IMAGE_FILE
```

# LICENSE

MIT LICENSE.

# Author

[shiba24](https://github.com/shiba24/), August 2016.

## Contributors

- [bobye](https://github.com/bobye)
