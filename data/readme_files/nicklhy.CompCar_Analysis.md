# Some experiments evaluated on CompCar dataset
Created by nicklhy(at gmail dot com)

Dataset reference
@InProceedings{Yang_2015_CVPR,
    author = {Yang, Linjie and Luo, Ping and Change Loy, Chen and Tang, Xiaoou},
    title = {A Large-Scale Car Dataset for Fine-Grained Categorization and Verification},
    journal = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2015}
}

### Experimental Results
1. Make level recognition rate
![Alt text](https://github.com/nicklhy/CompCar_Analysis/blob/master/pics/make_result.png)
2. Model level recognition rate
![Alt text](https://github.com/nicklhy/CompCar_Analysis/blob/master/pics/model_result.png)
3. All results(table)

|Make (Top 1)   |   Front   |   Rear    |   Side    |   FS      |   RS      |   All     |
|:-------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|GoogleNet      |   0.946   |   0.885   |   0.804   |   0.906   |   0.857   |   0.844   |
|VGG16          |   0.953   |   0.949   |   0.259   |   0.777   |   0.789   |   0.767   |
|Overfeat       |   0.710   |   0.521   |   0.507   |   0.680   |   0.656   |   0.829   |

|Model (Top 1)  |   Front   |   Rear    |   Side    |   FS      |   RS      |   All     |
|:-------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|GoogleNet      |   0.814   |   0.841   |   0.840   |   0.881   |   0.871   |   0.914   |
|VGG16          |   0.845   |   0.888   |   0.232   |   0.750   |   0.756   |   0.718   |
|Overfeat       |   0.524   |   0.431   |   0.428   |   0.680   |   0.598   |   0.767   |

|Model (Top 5)  |   Front   |   Rear    |   Side    |   FS      |   RS      |   All     |
|:-------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|GoogleNet      |   0.831   |   0.851   |   0.854   |   0.893   |   0.883   |   0.926   |
|VGG16          |   0.868   |   0.899   |   0.235   |   0.766   |   0.760   |   0.746   |
|Overfeat       |   0.748   |   0.647   |   0.602   |   0.769   |   0.777   |   0.917   |

### Introduction

### Requirements
1. [Requirements: software]
2. [Requirements: hardware]

### Requirements: software
1. Requirements for `Caffe` and `pycaffe` (see: [Caffe installation instructions](http://caffe.berkeleyvision.org/installation.html))

  **Note:** Caffe *must* be built with support for Python layers!

    ```make
    # In your Makefile.config, make sure to have this line uncommented
    WITH_PYTHON_LAYER := 1
    ```
Caffe build with mkl, cudnn is strongly recommended.
2. For fast-rcnn based classification experiments, [fast-rcnn](https://github.com/rbgirshick/fast-rcnn) is needed.
3. For xgboost based experiments, [xgboost](https://github.com/dmlc/xgboost) is needed.
4. Python packages you might not have: `python-numpy`, `python-scipy`, `python-matplotlib`, `python-opencv`, `python-scikit-learn`.

### Requirements: hardware
1. For training large CNN networks (VGG16, GoogleNet), a good GPU (e.g., Titan, K20, K40, ...) is needed.
2. Other non-deep-learning methods have no specific hardware requirements.

### Instructions
1. Prepare the dataset
Download the CompCar dataset at any place in you hard disk and build a soft link to our repo’s root directory as the name `data`:

    ```
    ln -s /path/to/CompCar /path/to/CompCar_Analysis/data
    ```

2. Split and transform the original dataset into some specific forms

* To split the vehicle images for training and testing into different angles, use tools/split_viewpoints.py

    ```
    ./tools/split_viewpoints.py
    ```

* To crop all vehicles from the original images

    ```
    ./tools/generate_cropped_image.py 4
    # the argument `4` is the process num we use to accelerate the program, default is 2(multi-thread is useless in Python, thus, we choose multi-process).
    ```

* Generate label list files
    ./tools/generate_label_list.py will generate the label included list files.

    ```
    ./tools/generate_label_list.py data/train_test_split/classification/train.txt make
    # You can substitute `${phase}${_viewpoint}.txt`({phase: [train, test], _viewpoints: [``, `_front`, `_rear`, `_side`, `_front_side`, `_rear_side`]}) for `train.txt` and subsitute `${level}`({level: [make, model]}) for `make`, which will generate a new `phase_viewpoint_level.txt` list file with labels after the image name.
    ```

    <!-- ./tools/generate_lmdb.sh will generate the lmdb data of different phases, viewpoints and level. Just run it in the root directory of repo `CompCar_Analysis`. -->

    <!-- ``` -->
    <!-- ./tools/generate_lmdb.sh -->
    <!-- ``` -->

3. Train a CNN classifier:
* src/caffe/train.py: classifier training code
* src/caffe/evaluation.py: classifier evaluation code
* src/caffe/extract_deep_feature.py: CNN feature extractor

