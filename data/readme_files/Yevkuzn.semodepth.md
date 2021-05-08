# Semi-Supervised Deep Learning for Monocular Depth Map Prediction

This repository contains code for the depth estimation system as described in
**[Semi-Supervised Deep Learning for Monocular Depth Map Prediction, CVPR 2017](http://openaccess.thecvf.com/content_cvpr_2017/papers/Kuznietsov_Semi-Supervised_Deep_Learning_CVPR_2017_paper.pdf)**

By Yevhen Kuznietsov, Jörg Stückler, Bastian Leibe at Computer Vision Group, RWTH Aachen University

## Presentation video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=KpJRSJx5yKs
" target="_blank"><img src="http://img.youtube.com/vi/KpJRSJx5yKs/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10" /></a>

## Prerequisite

In order to run the code, your setup has to meet the following requirements (tested versions in parentheses. Other versions might work as well):

* Python (2.7.14)
  * SciPy (1.0.0)
* TensorFlow (1.4.0)
  * CUDA (9.1.x)
  * cuDNN (7.0.x)
* GPU compatible with CUDAv9.1

### Running the system
1.  Download network model [here](https://www.vision.rwth-aachen.de/media/papers/best_model.tgz)
2.  Create a file, containing input-output file paths in each line. The format to be used for each line is `input_path/input.png,output_path/output.mat`. Example can be found at [filenames.txt](filenames.txt)
3.  Edit the [config file](/inference/config.py), set all the paths.
4.  Run the system: `python %PROJ_DIR%/inference/produce_predictions.py` 

## Remarks

* While the model may work with other datasets, this code is only supposed to be run with input resolution of [KITTI](http://www.cvlibs.net/datasets/kitti/) dataset

* The code was tested with 6GB NVIDIA GeForce GTX 980 Ti. It should also be possible to run it with less GPU RAM. Running on CPU may require code modifications.

* The metric depth map predictions, as well as the inputs and the generated depth ground truth for 'Eigen' test set are available [here](https://www.vision.rwth-aachen.de/publication/00150/)

If you have any issues or questions about the code, you can contact [me](mailto:YevKuzn@gmail.com) or [my alter ego](mailto:Yevhen.Kuznietsov@esat.kuleuven.be)

## Citing

If you find the depth estimation model useful in your research, please consider citing:

    @InProceedings{Kuznietsov_2017_CVPR,
        author = {Kuznietsov, Yevhen and Stuckler, Jorg and Leibe, Bastian},
        title = {Semi-Supervised Deep Learning for Monocular Depth Map Prediction},
        booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
        month = {July},
        year = {2017}
    } 
