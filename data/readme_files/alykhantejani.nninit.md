# nninit

Weight initialization schemes for PyTorch nn.Modules. This is a port of the popular [nninit](https://github.com/Kaixhin/nninit) for [Torch7](https://github.com/torch/torch7) by [@kaixhin](https://github.com/Kaixhin/).

##Update

This repo has been merged into [PyTorch's nn module](https://github.com/pytorch/pytorch/blob/master/torch/nn/init.py), I recommend you use that version going forward.

###PyTorch Example
```python
import nninit
from torch import nn
import torch.nn.init as init
import numpy as np

class Net(nn.Module):
  def __init__(self):
     super(Net, self).__init__()
     self.conv1 = nn.Conv2d(5, 10, (3, 3))
     init.xavier_uniform(self.conv1.weight, gain=np.sqrt(2))
     init.constant(self.conv1.bias, 0.1)

network = Net()
```



##Installation
Clone the repo and run `python setup install`

##Usage
```python
import nninit
from torch import nn
import numpy as np

class Net(nn.Module):
  def __init__(self):
     super(Net, self).__init__()
     self.conv1 = nn.Conv2d(5, 10, (3, 3))
     nninit.xavier_uniform(self.conv1.weight, gain=np.sqrt(2))
     nninit.constant(self.conv1.bias, 0.1)

network = Net()
```

##Supported Schemes
* **`nninit.uniform(tensor, a=0, b=1)`** - Fills `tensor` with values from a uniform, U(a,b)
* **`nninit.normal(tensor, mean=0, std=1)`** - Fills `tensor` with values drawn from a normal distribution with the given mean and std
* **`nninit.constant(tensor, val)`** - Fills `tensor` with the constant `val`
* **`nninit.xavier_uniform(tensor, gain=1)`** - Fills `tensor` with values according to the method described in ["Understanding the difficulty of training deep feedforward neural networks" - Glorot, X. and Bengio, Y.](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf), using a uniform distribution.
* **`nninit.xavier_normal(tensor, gain=1)`** - Fills `tensor` with values according to the method described in ["Understanding the difficulty of training deep feedforward neural networks" - Glorot, X. and Bengio, Y.](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf), using a normal distribution.
* **`nninit.kaiming_uniform(tensor, gain=1)`** - Fills `tensor` with values according to the method described in ["Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification" - He, K. et al.](https://arxiv.org/abs/1502.01852) using a uniform distribution.
* **`nninit.kaiming_normal(tensor, gain=1)`** - Fills `tensor` with values according to the method described in ["Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification" - He, K. et al.](https://arxiv.org/abs/1502.01852) using a normal distribution.
* **`nninit.orthogonal(tensor, gain=1)`** - Fills the `tensor` with a (semi) orthogonal matrix. Reference: ["Exact solutions to the nonlinear dynamics of learning in deep linear neural networks" - Saxe, A. et al.](https://arxiv.org/abs/1312.6120)
* **`nninit.sparse(tensor, sparsity, std=0.01)`** - Fills the 2D `tensor` as a sparse matrix, where the non-zero elements will be drawn from a normal distribution with mean=0 and std=`std`.
