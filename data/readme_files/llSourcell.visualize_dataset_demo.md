#How to Best Visualize a Dataset Easily

#Overview

This is the code for [this](https://youtu.be/yQsOFWqpjkE) video by Siraj Raval on Youtube. The human activities dataset contains 5 classes (sitting-down, standing-up, standing, walking, and sitting) collected on 8 hours of activities of 4 healthy subjects. The data set is downloaded from [here](http://groupware.les.inf.puc-rio.br/har#ixzz4Mt0Teae2). This code downloads the dataset, cleans it, creates feature vectors, then uses [T-SNE](https://lvdmaaten.github.io/tsne/) to reduce the dimensionality of the feature vectors to just 2. Then, we use matplotlib to visualize the data. 

##Dependencies

* pandas(http://pandas.pydata.org/) 
* numpy (http://www.numpy.org/) 
* scikit-learn (http://scikit-learn.org/) 
* matplotlib (http://matplotlib.org/) 

Install dependencies via '[pip](https://pypi.python.org/pypi/pip) install'. (i.e pip install pandas). 

Note** updated dataset is here if the other link is broken
http://rstudio-pubs-static.s3.amazonaws.com/19668_2a08e88c36ab4b47876a589bb1d61c37.html﻿

##Usage

To run this code, just run the following in terminal: 

`python data_visualization.py`

##Challenge

The challenge for this video is to visualize [this](https://www.kaggle.com/mylesoneill/game-of-thrones) Game of Thrones dataset. Use T-SNE to lower the dimensionality of the data and plot it using matplotlib. In your README, write our 2-3 sentences of something you discovered about the data after visualizing it. This will be great practice in understanding why dimensionality reduction is so important and analyzing data visually.

##Due Date is December 29th 2016

##Credits

The credits for this code go to [Yifeng-He](https://github.com/Yifeng-He). I've merely created a wrapper around the code to make it easy for people to get started.
