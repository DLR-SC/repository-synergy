# CaffeLMDBCreationMultiLabel
LMDB Creation in Caffe is conventionally supported for a single label setting, i.e. each given data instance has only one possible label. For a multi-label scenario (where each of N data instances can have M potential labels, M > 1), LMDB creation in Caffe is not straightforward. This code repository helps to create LMDBs for training and testing with a multi-label setting in Caffe. We will work with RGB image data here. 

-------------------------------
For a multi-label scenario, the data will be a N x H x W x 3 4D blob, and the *corresponding* labels will be a N x M x 1 x 1 4D blob. The necessary steps can now be listed as follows: 

(1) **Shuffling of data:** Shuffle all the data in sync with their corresponding labels before proceeding onto the next steps, as we will not use any shuffle operation during LMDB creation. In case you are not using a CNN which supports different image aspect ratios (like SPPNet), please also resize all the images to a common size. 

(2) **Specifying data files:** Make a data.txt file which lists the data file names (in order) and a dummy label (which will never be used) for each file. The data.txt file in the repository shows an example snippet of how to list the image file names with dummy labels. 

(3) **Creating data LMDB and the mean:** Use create_data_lmdb.sh script to create the data_lmdb database from the data.txt file. Use data_lmdb to create the mean file with create_mean.sh. Both the create_data_lmdb and create_mean scripts need [Caffe](https://github.com/BVLC/caffe). 

(4) **Specifying corresponding labels for the data:** For the order of the data files specified in data.txt, let the corresponding labels be stored in a labels.mat file as an N x M matrix. We will import this MAT file into python. Alternatively, you can have this N x M matrix directly in the numpy format. In either case, make sure that the label values are formatted to be integers in [0,255]. The labels.mat file in this repository is a 162770 x 40 matrix, and is included just as an example.

(5) **Creating label LMDB:** Use create_label_lmdb.py to form a label_lmdb database with labels.mat file (or any alternative specification of N x M matrix)

(6) **Prototxt modification:** Specify the respective data_lmdb, label_lmdb for train and validation datasets along with the mean file in your train prototxt as shown in train_vgg_11_sigmoid_cross_entropy_loss.prototxt. The idea is to essentially create two Caffe data layers, one for only the data instances and one for only the (corresponding) labels. Note the scaling of the labels in the transform_param of the DATA layers. This is to convert the label range from [0,255] to [0,1] as per the requirement of the Sigmoid Cross Entropy Loss function. Depending on your multi-label loss function, the scaling parameter can be altered. 

In all cases, please take care of the file paths as per your setup. 

-------------------------------
You should now be ready to train your prototxt (step 6) using [Caffe](https://github.com/BVLC/caffe) with a multi-label loss (like sigmoid cross-entropy) with your data and labels both in LMDB format. 
