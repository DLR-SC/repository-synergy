


# Tensorflow-Image-Classification
Easy and updated tensorflow image classificator

# See this proyect being used in a webpage:

https://github.com/AxelAli/Tensorflow-Image-Classifier-Web-Demo
## BASED ON / Thanks To:
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/
https://github.com/llSourcell/tensorflow_image_classifier

### Requirements 
[Tensorflow](https://www.tensorflow.org/)

[Python](https://www.python.org/)

[Pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)


### Getting Started!

Clone This Project
(In Terminal or Desktop App)
```
git clone https://github.com/AxelAli/Tensorflow-Image-Classification.git
```
Start Docker! (in project folder)
```
docker run -it -v $HOME/Tensorflow-Image-Classification:/Tensorflow-Image-Classification  gcr.io/tensorflow/tensorflow:latest-devel
```

Use the following command to install latest Tensorflow package
```
sudo pip install tensorflow --upgrade
```

Now. (Just in case)
```
cd ..
cd ..
cd /tensorflow
git pull
```
Then 
```
cd ..
cd ..
cd /Tensorflow-Image-Classification
git pull
```
#### Optional (Getting a dataset)
Great!

Install Dependencies for The Image Downloader (Optional, Makes it easier to download)
(In Terminal)
```
sudo pip install BeautifulSoup bs4 requests image
```

We have 2 Python scripts to download images from google.


##### With "user interface"
```
python GetImagesfromgoogle.py
```
We get the following Question:
```
What do i search for?
```

Here you can write anything you want, (Ex. Dog,Car,Flower).

You can also add extra words to be more specific or to get a wider dataset (Ex. White Dog,Ferrari Car, Sun Flower).

The terminal will start to output each image downloaded 

```
there are total 100 images
1
2
3
4
5
[...]
```
##### With console commands
```
python GetImagesfromgoogleCommand.py
```
How do i use it?
Easy, just write after GetImagesfromgoogleCommand.py you query
```
python GetImagesfromgoogleCommand.py QUERY
```
Ex.
```
python GetImagesfromgoogleCommand.py Dog
```

You can also "Batch download" 
```
python GetImagesfromgoogleCommand.py DOG
python GetImagesfromgoogleCommand.py CAT
python GetImagesfromgoogleCommand.py PARROT
python GetImagesfromgoogleCommand.py RAT
```
**NOTE!**

If you want to search something like "Mashed Potatoes" or "Sports Car" **replace all spaces** with '+' !

Example:
```
python GetImagesfromgoogleCommand.py Cute+Dog
python GetImagesfromgoogleCommand.py Red+Car
python GetImagesfromgoogleCommand.py Coke+Bottle
```
Now you can let it download overnight


Your folder will look like this:

![](http://i.imgur.com/TuMl59M.png)

NOTE:All downloads are in the data folder, there is also a folder for each query.

#### Let's Train!
Just Run the following commands

```
python image_retraining/retrain.py --bottleneck_dir=./processed-data/bottlenecks --how_many_training_steps 1000  --model_dir=./processed-data/inception --output_graph=./processed-data/retrained_graph.pb --output_labels=./processed-data/retrained_labels.txt --image_dir ./data/
```
##### What are these arguments?
**--bottleneck_dir :** Bottleneck directory, you should not change this unless you want to change things later (/PATH/TO/FOLDER)

**--how_many_training_steps : **Training Steps, these make your accuracy better (XXXX Number)

[**NOTE:** if you have <1000 images just place **1000**]  If you arent getting enough Precision , increase images and training steps

**--model_dir:** Model directory, you should not change this unless you want to change things later (/PATH/TO/FOLDER)

**--output_graph:** Output Graph file, you should not change this unless you want to change things later (/PATH/TO/FOLDER/FILE.pb)

**--output_labels:** Output Labels files, you should not change this unless you want to change things later (/PATH/TO/FOLDER/FILE.txt)

**--img_dir:** Image Directory , you should not change this unless you want to change things later (/PATH/TO/FOLDER)

[**NOTE: DO NOT** , i repeat , **DO NOT** place folders inside folders



![](http://i.imgur.com/18T94h3.png)


You should get:
```
>> Downloading inception-XXXX-XX-XX.tgz %
```

Wait till downloaded (It's Around 200 mb)

You Might get this Warning, dont worry
```
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use XXX instructions, but these are available on your machine and could speed up CPU computations.
```

Then (This searches the folders)
```
Looking for images in 'apple+pie'
Looking for images in 'cheesecake'
```

Eventually you will get this:
```
Creating bottleneck at /data/bottlenecks/XXX/*_XX.jpg.txt
```
**YOU MIGHT GET THE FOLLOWING ERROR: (Usually 1 in every 50 images)**
```
Not a JPEG file: starts with 0x89 0x50
```

**UPDATE: April/2017**



YOU MIGHT NEED TO INSTALL ImageMagick

SEE:

http://www.imagemagick.org/script/download.php

Run the following commands (inside each folder [example: data/dog])!

```
mogrify -format jpg *.ashx
rm *.ashx
mogrify -format jpg *.png
rm *.png
mogrify -format jpg *.jpeg
rm *.jpeg
mogrify -format jpg *.jpg
```
~~~~~~~~ NO LONGER NEEDED AS OF APRIL/17 ~~~~~~~~

**SOLUTION**
```
Creating bottleneck at /data/bottlenecks/apple+pie/*_47.jpg.txt.
Not a JPEG file: starts with 0x89 0x50
```
Delete the image that it got stuck with. (in this case *_47.jpg inside data/apple+pie/)

**Why does this happen?!** [is a renamed file (png>jpg) , your web browser can show it , but the library does not]

After this, repeat 
**Let's Train!**

~~~~~~~~ NO LONGER NEEDED AS OF APRIL/17 ~~~~~~~~

After a couple minutes you should start seeing 
```
2017-02-19 08:55:55.615936: Step XXXX: Cross entropy = 0.008041
2017-02-19 08:55:55.660845: Step XXXX: Validation accuracy = 100.0%
```
And when finished:
```
Final test accuracy = XX.X%
```
Great! We Trained it successfully!

### Guessing the images!

Now we just test an image!

Just in case:
```
pip install image
```

Run the following:
```
python label_image.py  data/cheesecake/*_9.jpg
```
##### What are these arguments?
The only argument is the path to the file:
(PATH/TO/FILE.jpg)

You will get :
```
cheesecake (score = 0.90928)
carrot cake (score = 0.06337)
apple pie (score = 0.02339)
smashed potatoes (score = 0.00396)
```
(Multiply result by 10 ,[ Ex. score = 0.90928 x 10 = 90.9% ])This is the likelihood that the image is of a cheesecake

If you want to add another item just start again from **Let ' s Train!**


### Known Bugs / Errors / Improvements
~~>We should have a system that checks every image and checks if it is a renamed png~~

Fixed April/17

