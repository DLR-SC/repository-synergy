
# MobileNetV3_PyTorch_pretrained_model

<div align=center><img src="https://github.com/PengBoXiangShang/net_pytorch/blob/master/figures/MobileNet_V3_block.png"/></div>

This is an unofficial PyTorch implementation for [MobileNetV3](https://arxiv.org/abs/1905.02244). Multi-GPUs training is supported. We trained it on ImageNet-1K and released the model parameters. 

This project is designed with these goals:
- [x] Train MobileNetV3-Small 1.0 on ImageNet-1K dataset.
- [ ] Train MobileNetV3-Small 0.75 on ImageNet-1K dataset.
- [ ] Train MobileNetV3-Large 1.0 on ImageNet-1K dataset.
- [ ] Train MobileNetV3-Large 0.75 on ImageNet-1K dataset.

-----
## Requirements

Ubuntu 14.04

Python 2.7

PyTorch 0.4.0

## Our Hardware Environment

Our server details:
**2** Intel(R) Xeon(R) CPUs (E5-2620 v3 @ 2.40GHz), 128 GB RAM,
**4** GTX 1080 Ti GPUs.

For fast IO, ImageNet-1K dataset is stored in our SSD.

## Experimental Results
We report the performance (Top-1 accuracy) on ImageNet-1K validation set.

| Network | Top-1 Accuracy | Pretrained Model|
| ------ | ------ | ------ |
|MobileNetV3-Small 1.0 (Official Implementation)|67.4%||
|MobileNetV3-Small 1.0 (Our Implementation)|~~63.37%~~ 64.27%|[Google Drive](https://drive.google.com/file/d/1lGyMHhD_m7qBb-DHlFVJXhnQ6NIhjkHW/view?usp=sharing); [BaiduYun Disk](https://pan.baidu.com/s/1Dv5KAxpipzxchUNamLIi5Q) (password:j2nh); 12MB，MD5：82c676590a9ad63674b49e897937547c |

## Detailed Processings of Our Training

Data Preprocessings:
```
transform_train = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

transform_val = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

```

Optimizer：
SGD
```
optimizer = torch.optim.SGD(net.parameters(
), lr=basic_configs['learning_rate'], momentum=0.9, weight_decay=1e-5)
```

Learning rate：
1e-1 (105 epoches) ==> 1e-2 (20 epoches) ==> 1e-3 (10 epoches) ==> 1e-4 (10 epoches) ==> 1e-5 (10 epoches)

Batch Size = 1700

Please see more details in our training file train.py.

Running costs are summarized in following table.

|GPU RAM|RAM|Running Time|
| ------ | ------ | ------ |
| 30 GB| 100 GB|approximatively 48 hours|

Please see more details in our training file train.py.

Loss curve:

<div align=center><img src="https://github.com/PengBoXiangShang/MobileNetV3_PyTorch/blob/master/figures/training_loss.png"/></div>

## How to Use
```
from MobileNetV3 import *

net = MobileNetV3()
state_dict = torch.load('MobileNetV3_Small_1.0.pth')
net.load_state_dict(state_dict)

```

## Discussion about "dropout 0.8"
In the original paper, the authors said "We use dropout of 0.8". This statement is ambiguous. Therefore, our current pretrained model has no dropout operations during training. We guess the dropout should be inserted before the final 1000-way logits layer. Please see details in our MobileNetV3_dropout.py. Our "MobileNetV3_dropout.py" is implemented based on the "mobilenetv3.py" of  [kuan Wang](https://github.com/kuan-wang). Thanks to Wang Kuan.


-----------------
This work was   implemented by **[Peng Xu](http://www.pengxu.net)**, and **[Jin Feng](https://github.com/JinDouer)**.
