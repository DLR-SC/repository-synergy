# HeadPoseEstimator

1. Introduction

The HeadPose Estimator predicts face landmarks (68 points) and head pose (3d pose, yaw, roll, and pitch).

2. Install 

caffe 

dlib18.17 

(cd your dlib folder 

cd python_example 

./compile_dlib_python_module.bat 

add dlib.so to the PYTHONPATH)

opencv

numpy, pandas

3. Usage

Unzip dlib-18.17.zip

Creat folder "img" to store your testing img

Creat folder "result" to store your visualized results

Creat folder "pose" to store your estimated poses (yaw angles) for each img

Pycharm run dlib-18.17/python_examples/landmarkPredict.py
(modify the caffe_root path and testList.txt if needed. testList.txt is a file containing the path of the testing images.)

4. Train 

Modify train.prototxt and train_solver.prototxt files, train the model using your own data.
