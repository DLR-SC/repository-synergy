# tensorflow-vgg
Re-implementation of VGG Network in tensorflow

# setup

```
pip install pyyaml skimage skdata tensorflow-gpu
```

# training

```
python train_model_simple.py experiment.yaml
```

# training on multiple gpus

```
python train_model_parallel.py experiment.yaml
```

# prediction

```
python predict.py dog.jpg
```
