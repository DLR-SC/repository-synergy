# Visual Question Generation in Tensorflow
It's simple question generator based on visual content written in Tensorflow. The model is quite similar to GRNN in ***[Generating Natural Questions About an Image](https://arxiv.org/abs/1603.06059)*** but I use LSTM instead of GRU. It's quite similar to Google's new AI assistant [***Allo***](https://play.google.com/store/apps/details?id=com.google.android.apps.fireball&hl=zh_HK) which can ask question based on image content. Since Mostafazadeh et al. does not released VQG dataset yet, we will use VQA dataset temporarily.

## Requirement
- Tensorflow, follow the [official installation](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#download-and-setup)
- python 2.7
- OpenCV
- VQA  dataset, go to the [dataset website](http://www.visualqa.org)

## Data
We will use VQA dataset which contains over 760K questions. We simply follow the steps in original [repo](https://github.com/VT-vision-lab/VQA_LSTM_CNN) to download the data and do some preprocessing. After running their code you
should acquire three files: ```data_prepro.h5```, ```data_prepro.json``` and ```data_img.h5```, put them in the root directory.

## Usage 
Train the VQG model:
```
python main.py --model_path=[where_to_save]
```
Demo VQG with single image: (you need to download pre-trained VGG19 [here](https://github.com/machrisaa/tensorflow-vgg))
```
python main.py --is_train=False --test_image_path=[path_to_image] --test_model_path=[path_to_model]
```


## Experiment Result

<img src="https://github.com/JamesChuanggg/VQG/blob/master/assets/demo.jpg?raw=true" width="400">    

**Model: How many zebras are in the picture** ?

<img src="https://github.com/JamesChuanggg/VQG/blob/master/assets/demo2.jpg?raw=true" width="400">     

**Model: Where is the chair** ?

**Problem**: Since we use VQA dataset which is designed for challenge so its question must be relevant to image content. No wonder the model train from VQA can not ask natural questions like human. We will adapt [VQG dataset](https://arxiv.org/abs/1603.06059) once it release to ask more meaningful question.

## Allo: Google AI Assistant
We also let Allo reply to these images. Here's the result.        
<img src="https://github.com/JamesChuanggg/VQG/blob/master/assets/allo.png?raw=true" width="600">

## TODO
Apply [VQG dataset](https://arxiv.org/abs/1603.06059) instead of VQA to ask more useful question. 

## Reference
- [Generating Natural Questions About an Image](https://arxiv.org/abs/1603.06059), ACL 2016.
- [show_and_tell.tensorflow](https://github.com/jazzsaxmafia/show_and_tell.tensorflow)
- [tensorflow-vgg](https://github.com/machrisaa/tensorflow-vgg)
