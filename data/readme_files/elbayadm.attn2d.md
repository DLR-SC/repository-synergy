## Pervasive Attention: 2D Convolutional Networks for Sequence-to-Sequence Prediction

This is an open source PyTorch implementation of the pervasive attention model described in:

Maha Elbayad, Laurent Besacier, and Jakob Verbeek. 2018. **[Pervasive Attention: 2D Convolutional Networks for Sequence-to-Sequence Prediction](https://arxiv.org/abs/1808.03867)**. In Proceedings of the 22nd Conference on Computational Natural Language Learning (CoNLL 2018)


### Requirements
```
pytorch (tested with v0.4.1)
subword-nmt
h5py (2.7.0)
tensorboardX 
```

### Usage:

#### IWSLT'14 pre-processing:
```
cd scripts
./prepare-iwslt14.sh
cd ..
python preprocess.py -d iwslt
```

#### Training:

```
mkdir -p save events
python train.py -c config/iwslt_l24.yaml
```
Note: in this setup the model takes up to 15G gpu memory.
If you want to train the model on a smaller GPU try with the memeory-efficient implementation of the DenseNet or with a Log-DenseNet:

```
python train.py -c config/iwslt_l24_efficient.yaml
python train.py -c config/iwslt_l24_log.yaml

```

#### Generation & evaluation
```
python generate.py -c config/iwslt_l24.yaml

```



