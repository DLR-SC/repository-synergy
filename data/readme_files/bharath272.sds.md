# SDS using hypercolumns

This repository implements the ideas from our [CVPR 2015 paper][4] and [my thesis][3]. In particular, it uses the hypercolumn representation to segment detections. It uses ideas from [SPP][5] and [Fast RCNN][2] to speed things up. The full details are in Chapter 3 of my thesis (look at Figure 3.7 for an overview).

##Preliminaries
The task we are interested in is [Simultaneous Detection and Segmentation][1], where we want to *detect* every instance of a category in an image and *segment* it out. We approach this task by first running an off-the-shelf object detector such as [Fast RCNN][2] and then segmenting out the object in each bounding box output by the detector. 

Included in the repository is an ipython notebook called *demo*. This demo should give you an idea of what the code does. The first three cells download the demo data and the trained model, and segment out a horse detection. `test_hypercolumns.get_hypercolumn_prediction` outputs the soft heatmap while `test_hypercolumns.paste_output_sp` projects the heatmap to superpixels.

Running the demo also automatically downloads the pretrained model. You can also get the model [here](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/hypercolumn/trained_model.caffemodel).

The last cell of the demo also runs the evaluation on 100 images. This requires you to have VOC2012 downloaded, and a link to that directory available in the `cache` directory.



##Overview of approach
If you want to delve into details of the network architecture etc, it is important to understand the approach. I describe it briefly here, but more details are in our [CVPR2015 paper][4] and my [thesis][3].

Our system segments out a detection by classifying each pixel in the detection window as belonging to figure or ground. It uses multiple intermediate feature maps of the CNN to do this. We can construct a feature vector for each pixel by upsampling each feature map to a fixed size,concatenating them together and convolving with a classifier. An equivalent approach is to run classifiers convolutionally over each feature map, then upsample the responses and add them together. We follow the latter approach.

To allow the classifier to vary with location, we use a coarse grid (say 5x5) of classifiers, and at each pixel use a linear combination of the nearby classifiers. In practice, we convolve with all 25 classifiers and then have a layer that does the interpolation into these 25 classifiers.

Finally, to be able to do fast segmentation, we run the classifiers convolutionally over the entire image, and then for each detection window simply crop and upsample the classifier outputs.

##Deconstructing the network
The main work is performed by a network implemented in [caffe](http://caffe.berkeleyvision.org/). I have added a few layers to caffe, and these modifications are available in the caffe-sds repository that comes bundled with this one.

The network definition is in `model_defs/hypercolumn_test.prototxt`. The network takes in four inputs:

1. The first input is the image itself. In principle the network can take in multiple images, though the rest of the code ignores this functionality and handles one image at the time, partly because of memory constraints. 

2. The second input is the bounding boxes you want to segment, written down as `[image_id categ_id xmin ymin xmax ymax]`. xmin, ymin, xmax and ymax are in normalized coordinates (i.e, the full image corresponds to `[0 0 1 1]`. `image_id` is the image number this box belongs to (since the code typically just passes in one image at a time, this is always 0) and `categ_id` is the category id of the bounding box.

3. The third input is the bounding boxes in the coordinates of the conv5 feature map, required for the spatial pyramid pooling. For VGG and Alexnet, this simply means the box coordinates divided by 16. The format of this blob is `[image_id xmin ymin xmax ymax]`.

4. The final input is again a list of category ids.

There is a lot of redundancy in these inputs, and currently `prepare_blobs.py` contains code to take in the image and detections as input and produce these blobs. This might be simplified in the future.

The network architecture reflects the architecture shown in Figure 3.7 of my [thesis][3]. 
The first part of the model definition describes your standard Fast R-CNN detection architecture. Next the 25 classifiers for each category are applied over the pool3 and pool4 feature maps of the entire image. The `BoxUpsample` layer takes the resulting response maps and a set of boxes with category labels as input. It then crops the response map around each box, takes the 25 channels that correspond to the category in question and upsamples it to a fixed size. The `channels` parameter defines how many channels it has to pick per category, and the `height` and `width` define the fixed upsampled size. Finally, the `LocallyConnected` layer takes these 25 outputs for each pixel and, depending on the location of the pixel in the window, linearly interpolates between the appropriate outputs.

We also run a classifier on the global fc7 features for each box. This gives us 25 numbers per box per category, and the `PickSlice` layer picks the appropriate set of 25 numbers. These 25 numbers are essentially just biases, one bias for each of the 25 classifiers.

##Training
Training relies on a python data layer, `hypercolumn_data_layer.py`. `run_command.sh` shows a sample training command. The initialization is a Fast-RCNN network.

The training prototxt is `model_defs/hypercolumn_train_pydata.prototxt` and is very similar to the testing model definition. The only difference is that the last layer is the `LocallyConnectedWithLoss` layer, which also takes in the target figure-ground masks and produces a loss (which is the standard sum-of-log-losses over all the pixels). It also takes in a weight for each box: this helped in preliminary experiments. In the current set up, small boxes are weighed less because they are noisier.

This README will continue to be updated.
[1]:http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/sds
[2]:http://arxiv.org/abs/1504.08083
[3]:http://www.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-193.html
[4]:http://www.cs.berkeley.edu/~bharath2/pubs/pdfs/BharathCVPR2015.pdf
[5]:http://arxiv.org/abs/1406.4729
