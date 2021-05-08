# 🏆 A Comparative Study on Handwritten Digits Recognition using Classifiers like K-NN, Multiclass Perceptron and SVM

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](#)
[![GitHub Forks](https://img.shields.io/github/forks/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM.svg?style=social&label=Fork&maxAge=2592000)](https://www.github.com/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM/fork)
[![Build Status](https://semaphoreapp.com/api/v1/projects/d4cca506-99be-44d2-b19e-176f36ec8cf1/128505/badge.svg)](#)
[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM/issues)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&label=Contributions&colorA=red&colorB=black	)](#)



For the full report, refer to the file named [Detailed Report.pdf](../master/Detailed_Report.pdf).

## Problem Statement
The task at hand is to classify handwritten digits using supervised machine learning methods. The digits belong to classes of **0 to 9**. 

*“Given a query instance (a digit) in the form of an image, our machine learning model must correctly classify its appropriate class.”*

## Dataset
MNIST Handwritten Digits dataset is used for this task. It contains images of digits taken from a variety of scanned documents, normalized in size and centered.
Each image is a 28 by 28 pixel square (784 pixels total). The dataset contains 60,000 images for model training and 10,000 images for the evaluation of the model.

## Methodology
We have used **supervised machine learning models** to predict the digits. Since this is a **comparative study** hence we will first describe the **K-Nearest Neighbors Classifier** as the baseline method which will then be compared to **Multiclass Perceptron Classifier** and **SVM Classifier**.

### 1) K-Nearest Neighbors Classifier – Our Baseline Method
k-Nearest Neighbors (k-NN) is an algorithm, which:
*	ﬁnds a group of k objects in the training set that are closest to the test object, and
*	bases the assignment of a label on the predominance of a class in this neighborhood.

When we used the K-NN method the following pros and cons were observed:

#### Pros
*	K-NN executes quickly for small training data sets.
*	No assumptions about data — useful, for example, for nonlinear data
*	Simple algorithm — to explain and understand/interpret
*	Versatile — useful for classification or regression
*	Training phase is extremely quick because it doesn’t learn any data

#### Cons
*	Computationally expensive — because the algorithm compares the test data with all examples in training data and then finalizes the label
*	The value of K is unknown and can be predicted using cross validation techniques
*	High memory requirement – because all the training data is stored
*	Prediction stage might be slow if training data is large

### 2) Multiclass Perceptron Classifier:
A multiclass perceptron classifier can be made using multiple binary class classifiers trained with 1 vs all strategy. In this strategy, while training a perceptron the training labels are such that e.g. for the classifier 2 vs all, the labels with 2 will be labeled as 1 and rest will be labeled as 0 for Sigmoid Unit while for Rosenblatt’s perceptron the labels would be 1 and -1 respectively for positive and negative examples. 

Now all we have to do is to train (learn the weights for) 10 classifiers separately and then feed the query instance to all these classifiers (as shown in figure above). The label of classifier with highest confidence will then be assigned to the query instance. 

#### How Multiclass Perceptron mitigates the limitations of K-NN:

As we already discussed, K-NN stores all the training data and when a new query instance comes it compares its similarity with all the training data which makes it expensive both computationally and memory-wise. There is no learning involved as such. On the other hand, Multiclass perceptron takes some time in learning phase but after its training is done, it learns the new weights which can be saved and then used. Now, when a query instance comes, it only has to take to dot product of that instance with the weights learned and there comes the output (after applying activation function). 

*	The prediction phase is extremely fast as compared to that of K-NN. 
*	Also, it’s a lot more efficient in terms of computation (during prediction phase) and memory (because now it only has to store the weights instead of all the training data). 

### 3) SVM Classifier using Histogram of Oriented Gradients (HOG) Features:

Just for comparison purposes, we have also used a third supervised machine learning technique named Support Vector Machine Classifier.
The model isn’t implemented. Its imported directly from scikit learn module of python and used.

In K-NN and Multiclass Perceptron Classifier we trained our models on raw images directly instead of computing some features from the input image and training the model on those computed measurements/features. 

A feature descriptor is a representation of an image that simplifies the image by extracting useful information and throwing away extraneous information. Now we are going to compute the Histogram of Oriented Gradients as features from the digit images and we will train the SVM Classifier on that. The HOG descriptor technique counts occurrences of gradient orientation in localized portions of an image - detection window.


## Analysis

Now the final phase. After running the experiment with different algorithms, the results are summarized. First comparing the techniques on basis of Accuracy:

### Accuracy (Performance):

<p align="middle">
  <img src="../master/Images/r1.png" width="600"/>
</p>

When we compare the K-NN method with Multiclass Perceptron and SVM on basis of accuracy then its accuracy is similar to that of other two classifiers which means despite its simplicity K-NN is really a good classifier.

### Prediction Time (Efficiency):

#### Our Observations:

One of the main limitations of K-NN was that it was computationally expensive. Its prediction time was large because whenever a new query instance came it had to compare its similarity with all the training data and then sort the neighbors according to their confidence and then separating the top k neighbors and choosing the label of the most occurred neighbor in top k. In all this process, it takes a comparable amount of time.

While for Multiclass Perceptron Classifier we observed it will mitigate this limitation in efficiency such that its prediction time will be short because now it will only compute the dot product in the prediction phase. The majority of time is spent only once in its learning phase. Then it’s ready to predict the test instances. 

#### Results:

<p align="middle">
  <img src="../master/Images/r2.png" width="600"/>
</p>


## Conclusion:

When the times were calculated for the prediction phases of K-NN, Multiclass Perceptron and SVM, the Multiclass Perceptron clearly stands out with the shortest prediction time while on the other side, K-NN took a large time in predicting the test instances.
Hence Multiclass Perceptron clearly leaves K-NN behind in terms of efficiency in Prediction Time and also in terms of computation and memory load. Thus, it mitigates the limitations of our baseline method K-NN.

----------------------------------------------------------------------------------------------------------------------------------------

## How to Run Code
The code files are in running condition and are directly executable.

(To install all the necessary packages at once, install [Anaconda](https://www.anaconda.com/download/#download))

----------------------------------------------------------------------------------------------------------------------------------------

## Author
You can get in touch with me on my LinkedIn Profile: [![LinkedIn Link](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/harismuneer)

You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/harismuneer)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

## Issues
[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/harismuneer/Handwritten-Digits-Classification-Using-KNN-Multiclass_Perceptron-SVM/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](../master/LICENSE)

Copyright (c) 2018-present, harismuneer                                                        

