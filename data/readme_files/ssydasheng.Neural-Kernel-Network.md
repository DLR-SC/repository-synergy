# Neural Kernel Network
This code is jointly contributed by [Shengyang Sun](https://github.com/ssydasheng), [Guodong Zhang](https://github.com/gd-zhang), [Chaoqi Wang](https://github.com/alecwangcq) and [Wenyuan Zeng](https://github.com/joy820)
## Introduction
Code for "Differentiable Compositional Kernel Learning for Gaussian Processes" (https://arxiv.org/abs/1806.04326)

## Dependencies
This project runs with Python 3.6. Before running the code, you have to install
* [Tensorflow](https:www.tensorflow.org)
* [GPflow-Slim](https://github.com/ssydasheng/GPflow-Slim)

## Experiments
Below we shows some examples to run the experiments.
We also provide experiment figures and logging files in [results](./results) folder, as a reference.
### Time Series
```
python exp/time-series.py --name airline --kern nkn
```
### Regression
```
python exp/regression.py --data energy --split uci_woval --kern nkn
python exp/regression.py --data energy --split uci_woval_pca --kern nkn
```
### Bayesian Optimization
```
python exp/bayes-opt.py --name sty --kern nkn --run 0
```
### Texture Extrapolation
```
python exp/texture.py --data pave --kern nkn
```
## Citation
To cite this work, please use
```
@article{sun2018differentiable,
  title={Differentiable Compositional Kernel Learning for Gaussian Processes},
  author={Sun, Shengyang and Zhang, Guodong and Wang, Chaoqi and Zeng, Wenyuan and Li, Jiaman and Grosse, Roger},
  journal={arXiv preprint arXiv:1806.04326},
  year={2018}
}
```
