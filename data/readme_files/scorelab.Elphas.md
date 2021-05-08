# Elphas
An Elephant Identification and Counting System.

## About
Elphas is currently used to count the number of elephants in an image or to classify an image based on the appearence of an elephant. Project was designed to facilitate the census of elephants in Sri Lanka. 

## Main Functionalities Available
1. An interface to upload a single image or a compressed file of several images (a task) to the server to process(count or classify).
2. An option to save a task(processing of an uploaded files) for later processing.
3. Callification of images
+ Two neural networks are available (Google's InceptionV3 and Microsoft's ResNet50)
* Retraining is available for Inception with a custom dataset and ResNet is used as an api from Keras.
4. Counting of elephants
* By Tensorflow's object detection api where the NN model can be again trained with a custom dataset.
5. Getting the count based on locations. (Images should be geo tagged)
6. Interface to see the results.
7. Reporting for misclassified or miscounted images.
8. User authentication based on google account or email account and updation of passwords if using an email account. 

## High Level Architecture
![](https://lh3.googleusercontent.com/-63RMjBi6F8wc-7DEH7Xe67JDYeV39k6wU-2DHYgk-5U1A5eXgbpYRNpUkUaV5mYQyc3r8Yklf-iOipGQ3vLy4Vy7bw5cDTJ8Rr52WQI3rcH_x7TAL4y2Q0r7935-IfoWHOUXdRAwXYoRCSocSZr2sCgI41YJ7ma2h8G9SNSv8lYH_svdIQ2qBjAXcLfOH20z-RgPNoDEauREkXoP3ZpKSe0Wyd_Oon6Bm6UYAk9LZK49LDYqJZMXogRmVH2FXTW2gGFBgdFw0DmSkhB6bTT4NUFVcJAQNPqyDHERhwCvZfgeDptcBBpl4CVNba9UzZAnLGKhtXRVHBPc_te3Gz5Cm8ZJpn0TWAu7c0f_vj2tt81M1MyxLI6H-01DQdY-4Ad1gkBumFrFuqvUqj3D5SZI0Z2qdjC27aOER464-FES2SLvH0X4c7kF9zS8XWePKw12gmGtStcLEYwPgUOqrozmAnfg9I6zxfSc7khyfvmbd2gSo9PGUsbZtx-1AZx6ColIugY-OHz0As2aNad9xTOgB3wnRW50l6OaPZ_tZc1s_j9dm6ud6ue0UoegIh9GjbYV6WEXKuaI0NDiebVwCSzlZvFx98xDRJU6dFCiLVS2eFnJEGQVn9agZNo3UBw-uw=w2650-h1596-no) 

## Installation
To activate front-end, inside front-end execute
```
npm install
```
after the node modules are downloaded, execute
```
npm start
```

In the back-end you would find requirements.txt which includes all the required modules. To install those, in the back-end run
```
pip install -r requirements.txt
```
An Anaconda environment is preferred.

For Windows, as the server is written in app.py, run
```
set FLASK_APP=app.py
flask run
```
to start the server.

For linux or mac run
```
export FLASK_APP=app.py
flask run
```
to start the server. 

## Repo Status
At the moment, classsification of the images won't work as the weight files of the model are not present beacuse of their file size, and also the the dataset used to train the inception model is not available, you would find an empty directory inside retraining dir in back-end, if not make a directory 'dataset' inside retrain directory. 

To get the classification working you'd need to run retrain.py script to retrain the model.
To retrain the model, add two sub directories 'elephant' and 'non-elephant' inside dataset directory and your images which falls under the respective class, then run retrain.py script. 


