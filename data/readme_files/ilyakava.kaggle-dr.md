This repository contains code written for the [Kaggle Diabetic Retinopathy](https://www.kaggle.com/c/diabetic-retinopathy-detection/leaderboard) challenge, and achieved 20th place out of 661 competitors. Read more about the challenge and the creation of this repository [here](http://ilyakava.tumblr.com/post/125230881527/my-1st-kaggle-convnet-getting-to-3rd-percentile).

While I competed in the challenge, this project evolved into my personal general purpose framework for training Deep Convolutional Neural Networks. It is built on top of [theano](http://deeplearning.net/software/theano/), [Lasagne](http://lasagne.readthedocs.org/en/latest/#), [pylearn2](http://deeplearning.net/software/pylearn2/) and many other general purpose python libraries.

**Features in this framework:**

- network architecture via json
    - nonlinearities, initialization, CONV filters, FC size, CONV+FC dropout+(pooling size+stride+overlap), and padding
- data augmentation (`cmd` line options)
    - color casting
    - flipping
    - jittering
- data handling
    - image normalize/standardization (`cmd` line option)
    - automated creation of image conversion batch files
    - streaming and caching multiple minibatches in GPU (i.e. macrobatches) (`cmd` line option)
    - easy restoring of network parameters: easy to pause then continue training at a later time (`cmd` line option)
    - control over class balance per minibatch (`cmd` line option)
        - classes automatically evenly distributed throughout minibatches
        - custom class (im)balance specifiable
    - consistent training/validation sets by default (`cmd` line option)
    - minibatch shuffling (`cmd` line option)
- evaluation
    - automatic autosave of best results during training
    - plotting CONV layer weights
    - occlusion heatmap studies
    - plotting network results
    - prediction from 1 or more models (`cmd` line option)
- misc `cmd` line options
    - multiple error functions
        - cross+relative entropy
        - nnrank
        - mse
        - error function code is easy to swap
    - learning rate, flipping noise decay controllable
    - color/grayscale switching
    - number output classes configurable
    - label/image source
    - CPU or GPU
    - c01b or bc01
    - detects if fundus image was taken with indirect or direct ophthalmoscope with 90% accuracy (using identification tab from indirect ophthalmoscopes)

# Getting Started

## Code (tested on Ubuntu 14.10)

### Install for a new Machine

`sudo apt-get install -y git python-pip python-yaml python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose libfreetype6-dev libpng-dev`

### Install General Python deps:

`sudo pip install theano scikit-learn scikit-image nyanbar natsort`

- If `skimage.io` has issues, try: `sudo pip install -U scikit-image`.
- I used theano version '0.7.0'

### Install Lasagne

```
git clone https://github.com/Lasagne/Lasagne.git && cd Lasagne/ && git checkout 4e4f2f4fdefdab6c2634c7ba080dc3e036782378 && pip install -r requirements.txt && sudo python setup.py install && cd ..
```

### Install pylearn2

```
git clone git://github.com/lisa-lab/pylearn2.git && cd pylearn2/ && git checkout 04c77eb9998c9dad1f2efa020736989005cd9c98 && python setup.py develop && sudo python setup.py develop && cd ..
```

#### Create a [~/.theanorc](http://deeplearning.net/software/theano/library/config.html) file

Ex Contents:

```
[global]
floatX = float32
device = gpu0

```

[Override with another device via](http://deeplearning.net/software/theano/library/config.html): `THEANO_FLAGS='device=gpu0'` prefix. Get a list of gpus via: `nvidia-smi -L`.

Also ensure that something like the following lines are in your `~/.bashrc`:

```
export PATH=/usr/local/cuda-7.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-7.0/lib64:$LD_LIBRARY_PATH
```

## Competition Data

### Install

`sudo apt-get install -y p7zip-full graphicsmagick`

### Download & Unpack Data (~45 mins for test)

Download from [kaggle](https://www.kaggle.com/c/diabetic-retinopathy-detection/data?trainLabels.csv.zip) (maybe with w3m) and place in `data/train`, to unpack run:

`7z e -oorig/ train.zip.001`

This will place the images into `data/train/orig`

After placing the test zip files into `data/test` you can run a similar command `7z e -oorig/ test.zip.001` to place the images into `data/test/orig`

Place `trainLabels.csv` into `data/train`

### Preparing Data for the Network

#### Full Size Originals -> Smaller Originals (~2.5 images per second on single CPU)

(Ex) This will create 3 batchfiles for graphicsmagick to output 128x128 pngs:

```
mkdir data/train/centered_crop
python my_code/create_resize_batchfiles.py data/train/orig/ data/train/centered_crop/ 2 128 3
```

Then follow the on screen directions, which will list what commands to run to process the images cataloged in the generated batchfiles.

Depending on how your CPU schedules, more than 1 batchfile may not result in any speedup (3 is the best size for me however).

## The Competition Network

### Training the network

#### Running on CPU

It is possible to run the network on a cpu, though keep in mind it is 15 times slower to train a single batch of size 128!<sup>*</sup> There are two things to keep in mind:

1. prefix your python command with: `THEANO_FLAGS='device=cpu'`
2. you must use the command line options `-cc 0 -fs bc01` when you run the network.

<sup>*</sup>On an Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz with the default network on 128px images, it takes 54.8 mins per epoch on the CPU versus 3.7 mins/epoch on the GPU.

#### Easiest to train

`python -m my_code.VGGNet -x 160`

#### My 2nd best Network (Kappa ~0.72)

`python -m my_code.VGGNet -d data/train/cent_crop_192/ -n vgg_mini7b_leak_sig_ecp -x 200`

#### My best Network (Kappa ~0.74)

`python -m my_code.VGGNet -d data/train/cent_crop_256/ -n vgg_mini7b_leak_sig_ecp -x 200`

#### Seeing Validation Kappa/Error over time

`python -m my_code.plot_results -f results/best_results.pkl`

### Testing a single network

`python -m my_code.predict -M models/modelfile.pkl -D data/test/cent_crop_192/`

*This command will print out where it saves a *.csv file submittable to Kaggle, as well as a *.pkl file containing the network's raw outputs, ready to be ensembled with other raw outputs.*

### Combining/Ensembling test output

`python -m my_code.avg_raw_ouputs results/my_2nd_best.pkl,results/my_1st_best.pkl`

*Combine "My 2nd best Network" with "My best Network" to get a Kappa ~0.76*

### Comparing csvs for overlap

`python -m my_code.compare_csv data/train/trainLabels.csv results/result1.csv`

### Occlusion heatmap study

`python -m my_code.plot_occluded_activations -M models/mymodel.pkl -D data/train/centered_crop/41188_right.png`

# Misc

## Running tests

`make test`

## Getting Help

- [SO](http://stackoverflow.com/questions/tagged/neural-network)
- [DataScience Beta](http://datascience.stackexchange.com/questions/tagged/deep-learning)
- [CrossValidated](http://stats.stackexchange.com/questions/tagged/deep-learning)

## Image Alignment (~3 seconds per image)

To reduce noise in the training dataset, detect which images are inverted (taken with an indirect ophthalmoscope) and which are left/right, and invert the images until optic nerve is on the right side of the image.

`python my_code/batch_align.py data/train/orig/ n i`

This will run the ith of n partitions that creates a csv of which inversions to perform on the images in that partition. For example, you could run:

`python my_code/batch_align.py data/train/orig/ 3 1`
`python my_code/batch_align.py data/train/orig/ 3 2`
`python my_code/batch_align.py data/train/orig/ 3 3`

In three different `screen` sessions for parallel processing. Each will report having created a csv file. You can join these multiple csvs into one with: `awk 'FNR==1 && NR!=1{next;}{print}' *.csv > my.csv`

A 90% accurate alignment of the training set is made available [here](https://www.dropbox.com/s/it1e3rjh25020mq/kaggle-dr-alignment-training.csv?dl=0). `horizontal_flip == 1` means the image should be flipped on its horizontal axis (upside-down). `vertical_flip == 1` means the image should be flipped on its vertical axis (left-right). Doing both of the flips as specified in the csv file will lead to 90% of the training images having the optic nerve on the right, slightly above the horizontal.
