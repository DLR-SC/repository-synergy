# Face identification using CNN + TPE demo
Face identification demo which implements the [Triplet Probabilistic Embedding for Face Verification and Clustering](https://arxiv.org/abs/1604.05417) work.

![demo app screenshot](https://habrastorage.org/files/f83/9d3/057/f839d305744d45e69660baf2c0986ce6.png)

### Requirements
 - python3
 - keras
 - dlib
 - scikit-image

### Usage
Get all the files from [here](https://yadi.sk/d/zIWpWyX73ACTAg) and put them to the `model` dir. Then start `demo_app1.py`.

### Training
Download the `face_template.npy` and `shape_predictor_68_face_landmarks.dat` from [here](https://yadi.sk/d/zIWpWyX73ACTAg) and put them to the `model` dir.

Place training data in following order:
```
data\
    dev_protocol.npy
    dev\
        1.jpg
        2.jpg
        3.jpg
        ...
    test\
        subject_0\
            1.jpg
            2.jpg
            ...
        subject_1\
            1.jpg
            2.jpg
            ...
        ...
    train\
        subject_0\
            1.jpg
            2.jpg
            ...
        subject_1\
            1.jpg
            2.jpg
            ...
        ...
```
Then run as follows:

1. utils/load_data.py
2. train_cnn.py
3. train_tpe.py

Use the test scripts to test your model.
