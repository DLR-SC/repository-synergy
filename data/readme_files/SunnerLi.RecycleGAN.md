# Re-cycle GAN
### The Re-implementation of Re-cycle GAN Idea

[![Packagist](https://img.shields.io/badge/Pytorch-0.4.1-red.svg)]()
[![Packagist](https://img.shields.io/badge/Python-3.5.0-blue.svg)]()
[![Packagist](https://img.shields.io/badge/Backend-OpenCV_only-green.svg)]()
[![Packagist](https://img.shields.io/badge/OS-Ubuntu_16.04-orange.svg)]()

![](https://github.com/SunnerLi/recyclegsn/blob/clear/img/recycle.png)

Abstract
---
This repository try to re-produce the idea of Re-cycle GAN [1] which is purposed by CMU. However, since CMU doesn't release any source code and collected dataset, we only extract the simple white and orange flower video to train the model. **You should notice that it's not the official implementation**. The idea of Re-cycle GAN is very similar to [vid2vid](https://github.com/NVIDIA/vid2vid). On the other hand, we provide the simple version whose idea can be traced much easily! For simplicity, this repository doesn't provide multi-GPU training or inference.     

Branch Explain
---
* master: This branch clearly address the code with detailed comment. You can refer to this branch if you are not realize the content of each part.
* develop: This branch will update the latest version of repo.
* clear: Since the full comment is lengthy and hard to trace, we also provide the code version with **least** comment in the `recycle_gan.py`. Also, some redundant check will be removed to add the readability. You can read with shortest length.    

Usage
---
The detail can be found in here. But you should download the dataset from the following link.
```
https://drive.google.com/drive/folders/1mmWND9ZLK9nZwa8lMQWOVjN5sU_rrWD0?usp=sharing
```
And you can simply use the following command:
```
# For training
$ python3 train.py --A <domain_A_path> --B <domain_B_path> --T 3 --resume result.pkl --record_iter 500 --n_iter 30000
# For inference
$ python3 demo.py --in <video_path> --direction a2b --resume result.pkl
```

Result
---
![](https://github.com/SunnerLi/RecycleGAN/blob/master/img/recycle_val.png)    
The above image shows the both domain. The left column is the original image in both domain. The middle column is the rendered result which adopt the linear-smoothing function in paper. The right column is the reconstruction result. In our experiment, we don't consider usual cycle-consistency loss but thinking of recycle loss.    

![](https://github.com/SunnerLi/RecycleGAN/blob/master/img/green_to_orange.gif)    
We only show the single flower-to-flower transform result. In the first domain, the flower is composed by green stem and white bundle part, and the flower is orange in the second domain. The above GIF shows that the generator can render the whole image with fire tone, and the plant can be colored into orange.    

![](https://github.com/SunnerLi/RecycleGAN/blob/master/img/orange_to_green.gif)    
The next marvelous example is shown above. For the opposite direction, the generator can realize the petal meaning in both domain, and render into white! Also, the stem can be remain as green. As the time extend, the flower will open with green tone. The most successful feature is that **there is no discontinuous artifact** between each frame in time series.    

Reference
---
[1] A. Bansal, S. Ma, D. Ramanan, and Y. Sheikh, "Recycle-gan: Unsupervised video retargeting," arXiv preprint arXiv:1808.05174, 2018.