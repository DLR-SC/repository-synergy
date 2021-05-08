# Evolving_Boxes
Python implementation of [Evolving Boxes for Fast Vehicle Detection](http://zyb.im/research/EB/), a paper on ICME 2017.

## License & Citation
This project is released under the BSD 3-clause "New" or "Revised" License (details in LICENSE file). If you think our work is useful in your research, please consider citing:<br />
```
@inproceedings{wang2017evolving,
  title={Evolving Boxes for Fast Vehicle Detection},
  author={Wang, Li and Lu, Yao and Wang, Hong and Zheng, Yingbin and Ye, Hao and Xue, Xiangyang},
  booktitle={IEEE International Conference on Multimedia and Expo (ICME)},
  year={2017}
}
```

## Configuration
Our implementation is based on the [Faster R-CNN](https://github.com/rbgirshick/py-faster-rcnn), please see the [Requirements](https://github.com/rbgirshick/py-faster-rcnn#requirements-software) for helping configure your Caffe environment.

## Demo for Vehicle Detection
To run the demo<br />
```
python tools/demo.py
```
Models can be seen at `data/vgg16_eb_5(1-3-5)_final.caffemodel` which indicate the use of features of final convolutional layer( the 1st, 3rd and the 5th convolutional layers). <br />

## Training & Testing
### Datasets<br/>
We trained and tested our model on the recent [DETRAC](http://detrac-db.rit.albany.edu) vehicle detection dataset, you can download datasets at their website.<br />

Training and validation datasets preparation operations can be seen at `data/data_prepare/*`:<br />

>Considering the continuous frames in each directory (25 frames per seconds), we trained our model every three frames for saving traing time.<br />
>In order to prevent mistaking foreground with background, ignored regions in every picture are replaced by black occlusions. <br />
>My datasets directory structure like this:
```
*DATA_PATH
	*Insight-MVT_Annotation_Train
		*Cloudy_MVI_39931
		*...
	*Insight-MVT_Annotation_Test
		*MVI_39031
		*...
	*anno
		*Cloudy_MVI_39931
		*...
```

### Training:
We have four options of multi-layer feature concatenation:1-3-5(1st, 3rd and 5th convolutional layers), 3-5, 3-4-5 and only final convolutional layer.<br />
You need replace the `DATA_PATH` in `experiments/scripts/train.sh` with your own dataset path
```
./experiments/scripts/train.sh GPU([0-9]) NET(VGG16) DATASET(detrac) HYPERNET(1-3-5/3-5/3-4-5/5)
```
The training models are saved under `output/default/`<br />

### Testing:
Like Training process, you need to replace the`DATA_PATH` in `experiments/scripts/test.sh` :
```
./experiments/scripts/test.sh GPU([0-9]) NET(VGG16) DATASET(detrac) HYPERNET(1-3-5/3-5/3-4-5/5)
```
The testing results are saved as files in `data/test_results` according to the detection submission format.

## Thanks
Thank you for appreciating our works.<br />
If you have any question, please contact wangli16@fudan.edu.cn
