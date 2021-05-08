## Towards Principled Design of Deep Convolutional Networks: Introducing SimpNet

![SimpNet](/SimpNetV2/images/Arch2_01.jpg)

This repository contains the architectures, pretrained models, logs, etc pertaining to the SimpNet Paper (Towards Principled Design of Deep Convolutional Networks: Introducing SimpNet) : https://arxiv.org/abs/1802.06205 

#### Abstract : 

> Major winning Convolutional Neural Networks (CNNs), such as VGGNet, ResNet, DenseNet, etc, include tens to hundreds of  millions of parameters, which impose considerable computation and memory overheads. This limits their practical usage in  training and optimizing for real-world applications. On the contrary, light-weight architectures, such as SqueezeNet, are being  proposed to address this issue. However, they mainly suffer from low accuracy, as they have compromised between the processing  power and efficiency. These inefficiencies mostly stem from following an ad-hoc designing procedure. In this work, we discuss  and propose several crucial design principles for an efficient architecture design and elaborate intuitions concerning  different aspects of the design procedure. Furthermore, we introduce a new layer called *SAF-pooling* to improve the  generalization power of the network while keeping it simple by choosing best features. Based on such principles, we propose a  simple architecture called *SimpNet*. We empirically show that *SimpNet* provides a good trade-off between the  computation/memory efficiency and the accuracy solely based on these primitive but crucial principles. SimpNet outperforms the  deeper and more complex architectures such as VGGNet, ResNet, WideResidualNet \etc, on several well-known benchmarks, while  having 2 to 25 times fewer number of parameters and operations. We obtain state-of-the-art results (in terms of a balance  between the accuracy and the number of involved parameters) on standard datasets, such as CIFAR10, CIFAR100, MNIST and SVHN.

The main contributions of this work are as follows:

1.   Introducing several crucial principles for designing deep convolutional architectures, which are backed up by extensive experiments and discussions in comparison with the literature.

2.   Based on such principles, It puts under the test the validity of some of the previously considered best practices. such as Strided Convolutions vs MaxPooling, Overlapped Pooling vs Nonoverlapped Pooling, etc. Furthermore, it tries to provide intuitive understanding of each point as to why one should be used instead of the other.

3.   A new architecture called SimpNet is proposed to verify the mentioned principles. Based on such design principles, the architecture is allowed to become superior to its predecessor ([*SimpleNet*](https://github.com/Coderx7/SimpleNet)), while still retaining the same number of parameters and maintaining simplicity in design, while outperforming deeper and more complex architectures (from 2 to 25X), such as Wide Residual Networks, ResNet, FMax, etc., on a series of highly compatative benchmark datasets (e.g., CIFAR10/100, SVHN and MNIST).




## Citation
If you find SimpleNet useful in your research, please consider citing:

    @article{hasanpour2018towards,
      title={Towards Principled Design of Deep Convolutional Networks: Introducing SimpNet},
      author={Hasanpour, Seyyed Hossein and Rouhani, Mohammad and Fayyaz, Mohsen and Sabokrou, Mohammad and Adeli, Ehsan},
      journal={arXiv preprint arXiv:1802.06205},
      year={2018}
    }



## Contents : 
#### 1- Results Overview  
#### 2- Data-Augmentation /Preprocessing  
#### 3- Principle Experiments Overview   



## Results Overview :

#### Top CIFAR10/100 results:

| **Method**              | **\#Params** |  **CIFAR10**  | **CIFAR100** |
| :---------------------- | :----------: | :-----------: | :----------: |
| VGGNet(16L) /Enhanced   |     138m     | 91.4 / 92.45  |      \-      |
| ResNet-110L / 1202L  \* |  1.7/10.2m   | 93.57 / 92.07 | 74.84/72.18  |
| SD-110L / 1202L         |  1.7/10.2m   | 94.77 / 95.09 |  75.42 / -   |
| WRN-(16/8)/(28/10)      |    11/36m    | 95.19 / 95.83 |  77.11/79.5  |
| DenseNet                |    27.2m     |     96.26     |    80.75     |
| Highway Network         |     N/A      |     92.40     |    67.76     |
| FitNet                  |      1M      |     91.61     |    64.96     |
| FMP\* (1 tests)         |     12M      |     95.50     |    73.61     |
| Max-out(k=2)            |      6M      |     90.62     |    65.46     |
| Network in Network      |      1M      |     91.19     |    64.32     |
| DSN                     |      1M      |     92.03     |    65.43     |
| Max-out NIN             |      \-      |     93.25     |    71.14     |
| LSUV                    |     N/A      |     94.16     |     N/A      |
| **SimpNet**                 |    **5.4M**     |  **95.69**  |    **78.16**     |
| **SimpNet**                 |    **8.9M**    |     **96.12**     |    **79.53**     |
| **SimpNet**(†)                 |    **15M**    |     **96.20**     |    **80.29**     |
| **SimpNet**(†)                 |    **25M**    |     **96.29**     |    N/A     |

(†): Unfinished tests. the results are not finalized and training continues. These models are simply tested without any hyperparameter tuning, only to show how they perform compare to the DeseNet and WRNs. As the prelimnery results show, they outperform both architectures. The full details will be provided after the tests are finished.

#### Top SVHN results:

| **Method**                   | **Error rate** |
| :--------------------------- | :------------: |
| Network in Network           |      2.35      |
| Deeply Supervised Net        |      1.92      |
| ResNet (reported by  (2016)) |      2.01      |
| ResNet with Stochastic Depth |      1.75      |
| DenseNet                     |   1.79-1.59    |
| Wide ResNet                  |   2.08-1.64    |
| **SimpNet**                  |    **1.648**  |

* The slim version achieves 1.95% error rate.

#### Top MNIST results:

| **Method**                   | **Error rate** |
| :--------------------------- | :------------: |
| Batch-normalized Max-out NIN |     0.24%      |
| Max-out network (k=2)        |     0.45%      |
| Network In Network           |     0.45%      |
| Deeply Supervised Network    |     0.39%      |
| RCNN-96                      |     0.31%      |
| **SimpNet**                      |     **0.25%**      |

* The slim version achives 99.73% accuracy.

#### Slim Version Results on CIFAR10/100 : 

| Model                                        |    Param    |    CIFAR10    |   CIFAR100    |
| :------------------------------------------- | :---------: | :-----------: | :-----------: |
| **SimpNet**                                  |**300K - 600K**| **93.25 - 94.03** | **68.47 - 71.74** |
| Maxout                                       |     6M      |     90.62     |     65.46     |
| DSN                                          |     1M      |     92.03     |     65.43     |
| ALLCNN                                       |    1.3M     |     92.75     |     66.29     |
| dasNet                                       |     6M      |     90.78     |     66.22     |
| ResNet  <span>(Depth32, tested by us)</span> |    475K     |     93.22     |  67.37-68.95  |
| WRN                                          |    600K     |     93.15     |     69.11     |
| NIN                                          |     1M      |     91.19     |       —       |


## Data-Augmentation and Preprocessing :

As indicated in the paper, CIFAR10/100 use zero-padding and horizontal filipping.
The script used for preprocessing CIFAR10/100 can be accessed from [here](https://github.com/Pastromhaug/caffe-stochastic-depth/blob/master/examples/cifar10/preprocessing.py)

## Principle Experiments : A Quick Overview :
Here is a quick overview of the tests conducted for every principle.  
For the complete dicussion and further explanations concerning these experiments
please read the paper. 

#### Gradual Expansion with Minimum Allocation:

| **Network Properties** | **Parameters** | **Accuracy (%)** |
| :--------------------- | :------------: | :--------------: |
| Arch1, 8 Layers        |      300K      |      90.21       |
| Arch1, 9 Layers        |      300K      |      90.55       |
| Arch1, 10 Layers       |      300K      |      90.61       |
| Arch1, 13 Layers       |      300K      |      89.78       |

> Demonstrating how gradually expanding the network helps obtaining better performance. Increasing the depth up to a certain point improves the accuracy (up to 10 layers) and then after that it starts to degrade, indicating PLD issue taking place.

| **Network Properties** | **Parameters** | **Accuracy (%)** |
| :--------------------- | :------------: | :--------------: |
| Arch1, 6 Layers        |      1.1M      |      92.18       |
| Arch1, 10 Layers       |      570K      |      92.23       |

> Shallow vs Deep: showing how a gradual increase can yield better performance with fewer number of parameters.

#### Correlation Preservation:

| **Network Properties** | **Parameters** | **Accuracy (%)** |
| :--------------------- | :------------- | :--------------- |
| Arch4, (3× 3)   | 300K           | 90.21            |
| Arch4, (3 × 3)   | 1.6M           | 92.14            |
| Arch4, (5 × 5)   | 1.6M           | 90.99            |
| Arch4, (7 × 7)   | 300K.v1        | 86.09            |
| Arch4, (7 × 7)   | 300K.v2        | 88.57            |
| Arch4, (7 × 7)   | 1.6M           | 89.22            |

> Accuracy for different combinations of kernel sizes and number of network parameters, which demonstrates how correlation preservation can directly affect the overall accuracy.

| **Network Properties**                                                                                 | **Params** | **Accuracy (%)** |
| :----------------------------------------------------------------------------------------------------- | :--------- | :--------------- |
| <span>Arch5,</span> <span>13 Layers, (1 × 1)  (2 × 2) (early layers)</span>                | 128K       | 87.71  88.50     |
| <span>Arch5,</span> <span>13 Layers, (1 × 1)  (2 × 2) (middle layers)</span>               | 128K       | 88.16  88.51     |
| <span>Arch5,</span> <span>13 Layers, (1 × 1)  (3 × 3) (smaller  bigger end-avg)</span>     | 128K       | 89.45  89.60     |
| <span>Arch5,</span> <span>11 Layers, (2 × 2)  (3 × 3) (bigger learned feature-maps)</span> | 128K       | 89.30  89.44     |

> Different kernel sizes applied on different parts of a network affect the overall performance, the kernel sizes that preserve the correlation the most yield the best accuracy. Also, the correlation is more important in early layers than it is for the later ones.

> SqueezeNet test on CIFAR10 vs SimpNet (slim version).

| **Network**              | **Params** | **Accuracy (%)** |
| :----------------------- | :--------: | :--------------: |
| SqueezeNet1.1_default   |    768K    |      88.60       |
| SqueezeNet1.1_optimized |    768K    |      92.20       |
| SimpNet_Slim            |    300K    |      93.25       |
| SimpNet_Slim            |    600K    |      94.03       |

> Correlation Preservation: SqueezeNet vs SimpNet on CIFAR10. By *optimized*
we mean, we added Batch-Normalization to all layers and used the same
optimization policy we used to train SimpNet.

#### Maximum Information Utilization:

| **Network Properties**                 | **Parameters** | **Accuracy (%)** |
| :------------------------------------- | :------------- | :--------------- |
| Arch3, <span>L5</span> default         | 53K            | 79.09            |
| Arch3, <span>L3</span> early pooling   | 53K            | 77.34            |
| Arch3, <span>L7</span> delayed pooling | 53K            | 79.44            |

> The effect of using pooling at different layers. Applying pooling early
in the network adversely affects the performance.

| **Network Properties** | **Depth** | **Parameters** | **Accuracy (%)** |
| :--------------------- | :-------- | :------------- | :--------------- |
| SimpNet(*)           | 13        | 360K           | 69.28            |
| SimpNet(*)           | 15        | 360K           | 68.89            |
| SimpNet(†)     | 15        | 360K           | 68.10            |
| ResNet(*)            | 32        | 460K           | 93.75            |
| ResNet(†)      | 32        | 460K           | 93.46            |

> Effect of using strided convolution ((†))  Max-pooling ((*)).
Max-pooling outperforms the strided convolution regardless of specific
architecture. First three rows are tested on CIFAR100 and two last on
CIFAR10.

#### Maximum Performance Utilization:

> Table [\[tab:max\_perf\]](#tab:max_perf) demonstrates the performance
and elapsed time when different kernels are used. (3 × 3) has the
best performance among the
others.

| **Network Properties**             | **(3 × 3)** | **(5 × 5)** | **(7 × 7)** |
| :--------------------------------- | :--------------- | :--------------- | :--------------- |
| Accuracy (higher is better)        | 92.14            | 90.99            | 89.22            |
| Elapsed time(min)(lower is better) | 41.32            | 45.29            | 64.52            |

> Maximum performance utilization using Caffe, cuDNNv6, networks have 1.6M
parameters and the same depth.

#### Balanced Distribution Scheme:

| **Network Properties**            | **Parameters** | **Accuracy (%)** |
| :-------------------------------- | :------------- | :--------------- |
| Arch2, 10 Layers (wide end)       | 8M             | 95.19            |
| Arch2, 10 Layers (balanced width) | 8M             | 95.51            |
| Arch2, 13 Layers (wide end)       | 128K           | 87.20            |
| Arch2, 13 Layers (balanced width) | 128K           | 89.70            |

> Balanced distribution scheme is demonstrated by using two variants of
SimpNet architecture with 10 and 13 layers, each showing how the
difference in allocation results in varying performance and ultimately
improvements for the one with balanced distribution of
units.

#### Rapid Prototyping In Isolation:

| **Network Properties**                      | **Accuracy (%)** |
| :------------------------------------------ | :--------------: |
| Use of (3 × 3) filters                 |      90.21       |
| Use of (5 × 5) instead of (3 × 3) |      90.99       |

> The importance of experiment isolation using the same architecture once
using (3 ×  3) and then using (5 × 5)
kernels.

| **Network Properties**                        | **Accuracy (%)** |
| :-------------------------------------------- | :--------------: |
| Use of (5 × 5) filters at the beginning |      89.53       |
| Use of (5 × 5) filters at the end       |      90.15       |

> Wrong interpretation of results when experiments are not compared in
equal conditions (Experimental
isolation).


## Simple Adaptive Feature Composition Pooling (SAFC Pooling) :

![SAFC Pooling](https://github.com/Coderx7/SimpNet/blob/master/SimpNetV2/images/pooling_concept2%20_v5_larged_2.jpg?)

| **Network Properties** | **With SAF**  | **Without SAF** |
| :--------------------- | :--------------------------------------------- | :- |
| SqueezeNetv1.1         | 88.05(avg)                       | 87.74(avg)    |
| SimpNet-Slim                | 94.76                                  | 94.68   |

Using *SAF-pooling* operation improves architecture performance. Tests
are run on CIFAR10.

#### Dropout Utilization:

## Generalization Examples: 


