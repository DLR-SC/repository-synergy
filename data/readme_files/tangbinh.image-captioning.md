### Overview
This repository contains PyTorch implementations of [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf) and [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/pdf/1502.03044.pdf). These models were among the first neural approaches to image captioning and remain useful benchmarks against newer models.

<img src="images/captions.jpg" alt="drawing"/>

### Installation
The code was written for Python 3.6 or higher, and it has been tested with [PyTorch](http://pytorch.org/) 0.4.1. Training is only available with GPU. To get started, try to clone the repository

```bash
git clone https://github.com/tangbinh/image-captioning
cd image-captioning
```

### Preprocessing
First, you need to download images and captions from the [COCO website](http://cocodataset.org/#download). By default, we use `train2014`, `val2014`, `val 2017` for training, validating, and testing, respectively. The data directory should have the following structure:
```
.
├── annotations
│   ├── captions_train2014.json
│   ├── captions_val2014.json
│   └── captions_val2017.json
└── images
    ├── train2014
    │   └── COCO_train2014_000000000092.jpg
    ├── val2014
    │   └── COCO_val2014_000000000042.jpg
    └── val2017
        └── 000000000139.jpg
```
Once all the annotations and images are downloaded to, say, `DATA_DIR`, you can run the following command to map caption words into indices in a dictionary and extract image features from a pretrained VGG19 network:
```bash
python preprocess.py --data $DATA_DIR --dest-dir $DEST_DIR
```
Note that the resulting directory `DEST_DIR` will be quite large; the features for training and validation images take up 157GB and 77GB already. Experiments with HDF5 shows that there's a significant slowdown due to concurrent access with multiple data workers (see [this discussion](https://discuss.pytorch.org/t/hdf5-multi-threaded-alternative/6189) and [this note](https://cyrille.rossant.net/moving-away-hdf5/)). Hence, the preprocessing script saves CNN features of different images into separate files.

### Training
To get started with training a model on SQuAD, you might find the following commands helpful:
```bash
python train.py --arch show_attend_tell --data $DEST_DIR --save-dir checkpoints/show_attend_tell --log-file logs/show_attend_tell.log
```
The show-attend-tell model results in a validation loss of 2.761 after the first epoch. The loss decreases to 2.298 after 20 epochs and shows no lower values than 2.266 after 50 epochs. Although the implementations doesn't support fine-tuning the CNN network, the feature can be added quite easily and probably yields better performance.

### Prediction
When the training is done, you can make predictions with the test dataset and compute BLEU scores:
```bash
python generate.py --checkpoint-path checkpoints/show_attend_tell/checkpoint_best.pt > /tmp/show_attend_tell.out
grep ^H /tmp/show_attend_tell.out | cut -f2- | sed -r 's/'$(echo -e "\033")'\[[0-9]{1,2}(;([0-9]{1,2})?)?[mK]//g' > /tmp/show_attend_tell.sys
grep ^T /tmp/show_attend_tell.out | cut -f2- | sed -r 's/'$(echo -e "\033")'\[[0-9]{1,2}(;([0-9]{1,2})?)?[mK]//g' > /tmp/show_attend_tell.ref
python score.py --reference /tmp/show_attend_tell.ref --system /tmp/show_attend_tell.sys
```

### Visualization
To display generated captions alongside their corresponding images, run the following command:
```bash
python visualize.py --checkpoint-path checkpoints/show_attend_tell/checkpoint_best.pt --coco-path $DATA_DIR
```
