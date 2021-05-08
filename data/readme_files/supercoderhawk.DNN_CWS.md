# 基于深度学习的中文分词

使用TensorFlow实现基于深度学习的中文分词

本项目使用`python3`编写，没有支持`python2`的计划。

**注：本项目主要是为了进行中文分词等相关自然语言处理研究而创建，暂时不推荐在正式的生产环境使用，另外本项目目前还在开发阶段**

## 使用方法

### 准备

1. 安装tensorflow：
```python
pip install tensorflow
```

2. clone本项目至本地.

3. 运行文件`init.py`，生成训练用数据

### 开始使用

在本项目文件夹下创建一个文件，在里面添加如下代码并运行：

```python
from seg_dnn import SegDNN
import constant

cws = SegDNN(constant.VOCAB_SIZE,50,constant.DNN_SKIP_WINDOW)
print(cws.seg('我爱北京天安门')[0])
```

详细示例可见文件[`test.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/test.py)

## 相关代码文件说明

* [`seg_dnn.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_dnn.py): 使用（感知机式）神经网络进行中文分词，对应论文1
* [`seg_lstm.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_lstm.py): 使用LSTM神经网络进行中文分词，对应论文2
* [`seg_mmtnn.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_mmtnn.py): 使用MMTNN网络进行中分分词，对应论文3
* [`prepare_data.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/prepare_data.py): 预处理语料库，包括msr和pku
* [`init.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/init.py): 用于生成进行训练和测试的数据的脚本文件

## 参考论文：

* [deep learning for chinese word segmentation and pos tagging](www.aclweb.org/anthology/D13-1061) （已完全实现，文件[`seg_dnn.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_dnn.py)）
* [Long Short-Term Memory Neural Networks for Chinese Word Segmentation](http://www.emnlp2015.org/proceedings/EMNLP/pdf/EMNLP141.pdf) (基本实现，正在改进，文件[`seg_lstm.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_lstm.py))
* [Max-Margin Tensor Neural Network for Chinese Word Segmentation](www.aclweb.org/anthology/P14-1028) （正在实现，文件[`seg_mmtnn.py`](https://github.com/supercoderhawk/DNN_CWS/blob/master/seg_mmtnn.py)）
## Todo List

- [ ] 支持`pip`
- [ ] 添加更加详细的注释
- [ ] 提供词性标注功能