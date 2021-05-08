# Neuraltalk2-tensorflow
This is a toy project for myself to start to learn tensorflow.

I started to learn torch by learning from neuraltalk2, so I started my tensorflow with this too.

I think this project is good for those who were familiar with neuraltalk2 in torch, because the main pipeline is almost the same. I don't know if it's a good tutorial to learn tensorflow, because the comments are still limited so far.

Without finetuning on VGG, my code gives CIDEr score ~0.65 on validation set (in 50000 iterations).

Currently if you want to use my code, you need to train the model from scratch (except VGG-16).

# TODO:
- ~~Finetuning VGG seems doesn't work. Need to be fixed.~~
- ~~No need to initialize from npy when having saved weight.~~
- Tensorflow stype file loading. (Multi-thread image loading)
- ~~Test of stacked LSTM. and also GRUs~~
- Pretrained model
- ~~Test code on single image~~
- Schedule sampling
- ~~sample_max~~
- ~~eval on unseen images~~
- eval on test
- visualize attention map

# Requirements
Python 2.7

[Tensorflow 1.0](https://github.com/tensorflow/tensorflow), please follow the tensorflow website to install the tensorflow.

# Train your own network on COCO
**(Copy from neuraltalk2)**

Great, first we need to some preprocessing. Head over to the `coco/` folder and run the IPython notebook to download the dataset and do some very simple preprocessing. The notebook will combine the train/val data together and create a very simple and small json file that contains a large list of image paths, and raw captions for each image, of the form:

```
[{ "file_path": "path/img.jpg", "captions": ["a caption", "a second caption of i"tgit ...] }, ...]
```

Once we have this, we're ready to invoke the `prepro.py` script, which will read all of this in and create a dataset (an hdf5 file and a json file) ready for consumption in the Lua code. For example, for MS COCO we can run the prepro file as follows:

```bash
$ python prepro.py --input_json coco/coco_raw.json --num_val 5000 --num_test 5000 --images_root coco/images --word_count_threshold 5 --output_json coco/cocotalk.json --output_h5 coco/cocotalk.h5
```

This is telling the script to read in all the data (the images and the captions), allocate 5000 images for val/test splits respectively, and map all words that occur <= 5 times to a special `UNK` token. The resulting `json` and `h5` files are about 30GB and contain everything we want to know about the dataset.

**Warning**: the prepro script will fail with the default MSCOCO data because one of their images is corrupted. See [this issue](https://github.com/karpathy/neuraltalk2/issues/4) for the fix, it involves manually replacing one image in the dataset.

**(Copy end.)**

Note that: the split used here can not be used for research. You can email me to ask for preprocessing code for COCO "standard" split, or you can modify the code by yourself if you are familiar.

~~Download or generate a tensorflow version pretrained vgg-16 [tensorflow-vgg16](https://github.com/ry/tensorflow-vgg16). ~~

I borrow the [machrisaa/tensorflow-vgg](https://github.com/machrisaa/tensorflow-vgg). I made some modification.
- Add a variable `training` to control the evaluation and training mode of model (in principle it's controling the dropout probability).
- Define all the weights and biases as Variable (previously constant).

You need to download the npy file of vgg, [vgg16](https://dl.dropboxusercontent.com/u/50333326/vgg16.npy), [vgg19](https://dl.dropboxusercontent.com/u/50333326/vgg19.npy). Put the file somewhere (e.g. a `models` directory), and we're ready to train!

```bash
$ python train.py --input_json coco/cocotalk.json --input_h5 coco/cocotalk.h5 --checkpoint_path ./log --save_checkpoint_every 2000 --val_images_use 3200
```

The train script will take over, and start dumping checkpoints into the folder specified by `checkpoint_path` (default = current folder). For more options, see `opts.py`.

If you'd like to evaluate BLEU/METEOR/CIDEr scores during training in addition to validation cross entropy loss, use `--language_eval 1` option, but don't forget to download the [coco-caption code](https://github.com/tylin/coco-caption) into `coco-caption` directory.

**A few notes on training.** To give you an idea, with the default settings one epoch of MS COCO images is about 7500 iterations. 1 epoch of training (with no finetuning - notice this is the default) takes about 45 minutes and results in validation loss ~2.7 and CIDEr score of ~0.5. By iteration 50,000 CIDEr climbs up to about 0.65 (validation loss at about 2.4). 

### Caption images after training

Now place all your images of interest into a folder, e.g. `blah`, and run
the eval script:

```bash
$ python eval.py --model model.ckpt-**** --infos_path infos_<id>.pkl --image_folder <image_folder> --num_images 10
```

This tells the `eval` script to run up to 10 images from the given folder. If you have a big GPU you can speed up the evaluation by increasing `batch_size` (default = 1). Use `-num_images -1` to process all images. The eval script will create an `vis.json` file inside the `vis` folder, which can then be visualized with the provided HTML interface:

```bash
$ cd vis
$ python -m SimpleHTTPServer
```

Now visit `localhost:8000` in your browser and you should see your predicted captions.

**Beam Search**. Beam search is enabled by default because it increases the performance of the search for argmax decoding sequence. However, this is a little more expensive, so if you'd like to evaluate images faster, but at a cost of performance, use `--beam_size 1`. ~~For example, in one of my experiments beam size 2 gives CIDEr 0.922, and beam size 1 gives CIDEr 0.886.~~

**Running on MSCOCO images**. If you train on MSCOCO (see how below), you will have generated preprocessed MSCOCO images, which you can use directly in the eval script. In this case simply leave out the `image_folder` option and the eval script and instead pass in the `input_h5`, `input_json` to your preprocessed files.

# Acknowledgements
I learned a lot from these following repositories.

- [neuraltalk2](https://github.com/karpathy/neuraltalk2)(of course)
- [colornet](https://github.com/pavelgonchar/colornet)(for using pretrained vgg-16)
- [tensorflow-vgg16](https://github.com/ry/tensorflow-vgg16.git)(tensorflow version of vgg-16)
- [machrisaa/tensorflow-vgg](https://github.com/machrisaa/tensorflow-vgg)(For better loading vgg-16, but still not perfect)
- [huyng/tensorflow-vgg](https://github.com/huyng/tensorflow-vgg)(This may be my next attempt.)
- [char-rnn-tensorflow](https://github.com/sherjilozair/char-rnn-tensorflow)(for using the RNN wrapper provided by tensorflow)
- [show_and_tell.tensorflow](https://github.com/jazzsaxmafia/show_and_tell.tensorflow)(Gave me idea how to dump option information. Furthermore, this has the same algorithm as mine but with different code structure)
- [TF-mrnn](https://github.com/mjhucla/TF-mRNN) I borrow the beam search code. And this is also a very good caption genration model.
