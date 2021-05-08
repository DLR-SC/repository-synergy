# action-faster-rcnn
This repository is a strongly modified version for action detection originally from [py-faster-rnn](https://github.com/rbgirshick/py-faster-rcnn.git) for my ECCV16 paper. It wraps three popular action detection dataset classes: UCF-Sports, JHMDB, and UCF101. Also, it provides useful action detection evaluation scripts for both frame level and video level. 
*Note the results on UCF101 are updated at https://hal.inria.fr/hal-01349107/file/eccv16-pxj-v3.pdf dut to some annotation  parsing errors.*

### Installation
1. Clone this reporsitory
  ```Shell
  git clone --recursive https://github.com/pengxj/action-faster-rcnn.git
  ```
  
2. Build the Cython modules which mainly compiles the nms module
  ```Shell 
  cd $THIS_ROOT/lib
  make
  ```
  
3. Build Caffe and pycaffe
  ```Shell
  cd $THIS_ROOT/caffe-fast-rcnn-faster-rcnn-upstream-33f2445
  # Now follow the Caffe installation instructions here:
  #   http://caffe.berkeleyvision.org/installation.html
  ```
  
4. Dive into the code
  ```Shell
  dataset classes: lib/datasets/ucfsports.py JHMDB.py UCF101.py
  training script: action_experiments/scripts/train_action_det.sh
  evaluation scripts: action_tools/action_util.py ucfsports_eval.py jhmdb_eval.py ucf101_eval.py fusion_eval.py eval_linked_results.py
  script for merging 2 stream models: action_tools/net_surgery_rgbflow.py
  ```

### Run experiments
The entire pipeline for two-stream rcnn includes optical flow extraction, r-cnn training, frame-level detecting, linking and evaluation. All these are included in this repository.

If you just want to get the final video AP, you [download](https://drive.google.com/open?id=0B-DiRMXFmUKQVDBRTy12UVJ2enM) the UCF101 linked results and run the eval_linked_results script. The folder 'action_results' includes linked results for UCF-Sports and JHMDB datasets.

### video mAP results with different iou thresholds (without multi-region scheme):

|                | 0.2   | 0.5   | 0.75  | 0.5:0.95 |
|----------------|-------|-------|-------|----------|
| UCF-Sports     | 95.12 | 95.12 | 47.33 | 50.95    |
| JHMDB          | 72.75 | 72.11 | 48.15 | 42.23    |
| UCF101 Split 1 | 73.20 | 35.91 | 1.55  | 8.76     |

python action_tools/eval_linked_results.py --imdb UCF101_RGB_1_FLOW_5_split_0 --res path/to/ucf101_vdets_3scales_rgb1flow5.pkl

{0.05: 0.7881, 0.1: 0.7745, 0.2: 0.7320, 0.3: 0.6630, 0.4: 0.5604, 0.5: 0.3591, 0.6: 0.1469, 0.7: 0.0349}

python action_tools/eval_linked_results.py --imdb JHMDB_RGB_1_FLOW_5_split_2 --res action_results/jhmdb_s03_vdets_3scales_rgb1flow5.pkl

{0.5: 0.7124, 0.4: 0.7124, 0.2: 0.7139, 0.05: 0.7139, 0.6: 0.7028, 0.3: 0.7134, 0.1: 0.7139, 0.7: 0.6009}

python action_tools/eval_linked_results.py --imdb JHMDB_RGB_1_FLOW_5_split_1 --res action_results/jhmdb_s02_vdets_3scales_rgb1flow5.pkl

{0.5: 0.7304, 0.4: 0.7360, 0.2: 0.7412, 0.05: 0.7414, 0.6: 0.7063, 0.3: 0.7412, 0.1: 0.7414, 0.7: 0.6004}

python action_tools/eval_linked_results.py --imdb JHMDB_RGB_1_FLOW_5_split_0 --res action_results/jhmdb_s01_vdets_3scales_rgb1flow5.pkl

{0.5: 0.7207, 0.4: 0.7240, 0.2: 0.7273, 0.05: 0.7299, 0.6: 0.6909, 0.3: 0.7244, 0.1: 0.7273, 0.7: 0.5974}

python action_tools/eval_linked_results.py --imdb UCF-Sports_RGB_1_FLOW_5_split_0 --res action_results/ucfsports_vdets_3scales_rgb1flow5.pkl

{0.5: 0.9512, 0.4: 0.9512, 0.2: 0.9512, 0.05: 0.9512, 0.6: 0.9034, 0.3: 0.9512, 0.1: 0.9512, 0.7: 0.7370}

And for the 'imdb' option, you can find them in dir action_experiments/listfiles/ which are actually the names of files. 
### Citation

If you find this repository useful in your research, please consider citing:

    @inproceedings{peng2016multi,
    title={Multi-region two-stream R-CNN for action detection},
    author={Peng, Xiaojiang and Schmid, Cordelia},
    booktitle={European Conference on Computer Vision},
    pages={744--759},
    year={2016},
    organization={Springer}}
  
  
    @inproceedings{renNIPS15fasterrcnn,
        Author = {Shaoqing Ren and Kaiming He and Ross Girshick and Jian Sun},
        Title = {Faster {R-CNN}: Towards Real-Time Object Detection
                 with Region Proposal Networks},
        Booktitle = {Advances in Neural Information Processing Systems ({NIPS})},
        Year = {2015}
    }
