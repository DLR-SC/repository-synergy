# Semantic Video CNNs through Representation Warping

This is the code accompanying the following **ICCV 2017** publication:

--------

**Semantic Video CNNs through Representation Warping**.

--------

This is developed and maintained by
[Raghudeep Gadde](https://ps.is.tuebingen.mpg.de/person/rgadde),
[Varun Jampani](https://varunjampani.github.io),
[Peter V. Gehler](https://ps.is.tuebingen.mpg.de/person/pgehler).

Please visit the project website [http://segmentation.is.tue.mpg.de](http://segmentation.is.tue.mpg.de) for more details about the paper and overall methodology.

## Installation

The code provided in this repository relies on the same installation procedure as the one from [Caffe](http://caffe.berkeleyvision.org/).
Before you start with the `NetWarp` code, please install all the requirements of Caffe by following the instructions from [this page](http://caffe.berkeleyvision.org/installation.html) first.
You will then be able to build Caffe with our code.
The repository also contains external code from [https://github.com/tikroeger/OF_DIS](https://github.com/tikroeger/OF_DIS) to compute the optical flow and [https://github.com/mcordts/cityscapesScripts](https://github.com/mcordts/cityscapesScripts) to evaluate results on the Cityscapes dataset.

## Integration into Caffe

There are mainly two ways for integrating the additional layers provided by our library into Caffe:

* Dowloading a fresh clone of Caffe and patching it with our source files, so that you will be able to test the code with minimal effort.
* Patching an existing copy of Caffe, so that you can integrate our code with your own development on Caffe.

### Downloading and Patching

This can be done just by the following commands:
```
cd $netwarp
mkdir build
cd build
cmake ..
```

This will configure the project, you may then run:

* for building the project
  ```
  make 
  ```
  This will clone a Caffe version from the main Caffe repository into the `build` folder and compiles together with our newly added layers.
* for running the tests, including the ones of the NetWarp:
  ```
  make runtest
  ```

  (this follows the same commands as for Caffe)

**Notes**

* Our code has been tested with revision `691febcb83d6a3147be8e9583c77aefaac9945f8` of Caffe, and this
is the version that is cloned. You may change the version by passing the option `CAFFE_VERSION` on the command line of
`cmake`:

        cmake -DCAFFE_VERSION=some_hash_or_tag ..

such as `cmake -DCAFFE_VERSION=HEAD ..`.

* If you want to use your fork instead of the original Caffe repository, you may provide the option `CAFFE_REPOSITORY` on the `cmake` command line (it works exactly as for `CAFFE_VERSION`).
* Any additional command line argument you pass to `cmake` will be forwarded to Caffe, except for those
  used directly by our code:

      cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBOOST_ROOT=../osx/boost_1_60_0/
        -DBoost_ADDITIONAL_VERSIONS="1.60\;1.60.0" ..

### Patching an existing Caffe version

#### Automatic CMAKE way
You may patch an existing version of Caffe by providing the `CAFFE_SRC` on the command line
```
cd $netwarp
mkdir build
cd build
cmake -DCAFFE_SRC=/your/caffe/local/copy ..
```

This will add the files of the NetWarp to the source files of the existing Caffe copy, but **will also
overwrite caffe.proto** (a backup is made in the same folder).
The command will also create a build folder local to the NetWarp repository (inside the `build` folder on the previous example): you may use this one
or use any previous one, Caffe should automatically use the sources of the NetWarp.

#### Manual way
The above patching that is performed by `cmake` is rather a copying of the files from the folder of the `netwarp` to the
corresponding folders of Caffe. Caffe will then add the new files into the project.

Alternatively, you can manually copy all but `caffe.proto` source files in `netwarp` folder to the corresponding locations in your Caffe repository. Then, for merging the `caffe.proto` file of `netwarp` to your version of the `caffe.proto`:

1. the copy the lines 409-412 and 1418-1451 in `caffe.proto` to the corresponding `caffe.proto` file in the destination Caffe repository.
2. Change the parameter IDs for `BNParameter`, `WarpParameter`, and `InterpParameter` based on the next available `LayerParameter` ID in your Caffe.

## Example Usage
To use the provided code and replicate the results on the Cityscapes `val` dataset, 

#### Preparing the data
Download `leftImg8bit_sequence.zip` from the Cityscapes dataset webpage [https://www.cityscapes-dataset.com/](https://www.cityscapes-dataset.com/) in the `data` folder. If you want to compute the accuracy scores on the `val` set, also download the gtFine.zip file. Extract content from both the zip files and place them in the `data` folder following the same directory structure. Also set the `CITYSCAPES_DATASET` environment variable with the path to the dataset.

```
export CITYSCAPES_DATASET='$netwarp/data/cityscapes/'
```

#### Computing optical flow

Next, compute the optical flow using the following command 
```
export NETWARP_BUILD_DIR='/path/to/build/'
cd $netwarp
python scripts/extract_opticalflow.py VAL 
```

The above command will compute the optical flow on the Cityscapes val set and save them in the Cityscapes dataset folder.

#### Get the trained PSPNet-NetWarp model

Execute the below command to download a NetWarp model for PSPNet, trained on Cityscapes `train` videos.
```
sh scripts/get_cityscapes_model.sh
```

This will download the caffemodel in the `models` folder. (We shall hopefully release more models in the coming days).

#### Doing the segmentation

You can run the segmentation using the `run_netwarp.py` python script in the `$netwarp/scripts` folder which rely on the Python extensions of Caffe.

Syntax for running the segmentation script:
```
cd $netwarp
python scripts/run_netwarp.py data_split path_to_prototxt path_to_caffemodel path_to_results_dir number_of_gpus_to_use
```

To run the segmentation on Cityscapes validation set:
```
python scripts/run_netwarp.py VAL models/pspnet101_cityscapes_conv5_4netwarp_deploy.prototxt models/pspnet101_cityscapes_conv5_4netwarp.caffemodel results/ 2
```

The above command will save color coded segmentation masks in `results/color/` and class indexed segmentation masks suitable for computing IoU using `cityscapesScripts` in `results/index/`

#### Evaluating the results
We provide a python script to compute the Trimap IoU score of the obtained segmentations.
```
cd $netwarp
python scripts/compute_scores.py VAL path_to_results trimap_width
```

An example to compute Trimap IoU on the obtained results:
```
python scripts/compute_scores.py VAL results/index/ 3
```


## Citations

Please consider citing the below paper if you make use of this work and/or the corresponding code:

```
@inproceedings{gadde2017semantic,
  author = {Gadde, Raghudeep and Jampani, Varun and Gehler, Peter V.},
  title = {Semantic Video CNNs Through Representation Warping},
  booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
  month = {Oct},
  year = {2017}
} 
```

If you use the dense inverse search based optical flow, please do not forget citing the relavant paper:

```
@inproceedings{kroeger2016fast,
  title={Fast optical flow using dense inverse search},
  author={Kroeger, Till and Timofte, Radu and Dai, Dengxin and Van Gool, Luc},
  booktitle={European Conference on Computer Vision},
  pages={471--488},
  year={2016},
  organization={Springer}
}
```
