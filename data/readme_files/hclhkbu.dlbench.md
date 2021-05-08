# Deep learning software tools benchmark
A benchmark framework for measuring different deep learning tools. Please refer to http://dlbench.comp.hkbu.edu.hk/ for our testing results and more details. Benchmarking with newer versions of frameworks is on the way:

| Tool        | Version                                      									|
|-------------|-----------------------------------------------------------------------|
| Caffe       | [1.0rc5(39f28e4)](https://github.com/BVLC/caffe/tree/39f28e4)         |
| CNTK	      | [2.0Beta10(1ae666d)](https://github.com/Microsoft/CNTK/tree/1ae666d)  |
| MXNet       | [0.93(32dc3a2)](https://github.com/dmlc/mxnet/tree/32dc3a2)           |
| TensorFlow  | [1.0(4ac9c09)](https://github.com/tensorflow/tensorflow/tree/4ac9c09) |
| Torch       | [7(748f5e3))](https://github.com/torch/torch7/tree/ac3751c) 	        |

This project is licensed under MIT License.
## Introduction
### Overview of **dlbench**    

| Dirctory         	| Description                                      									|
|------------------	|--------------------------------------------------------------------------------	|
| configs/         	| Configuration files for running benchmark                                      	|
| network-configs/ 	| Description of our tested models                                               	|
| synthetic/       	| Our benchmark tests with fake data                                             	|
| tools/           	| Contains running scripts and network configurations of each deep learning tool 	|
| logs/           	| Will be generated by running benchmark.py. Running logs should be put in here 	|

### Run benchmark  
#### Prepare Data  
Prepare data for the tools you want to run and put them under $HOME/data. Note that the name of each data directory should be the same as the name of the tool for convenience.   
You can download data we used for our benchmark through following links:
- Caffe: [http://dlbench.comp.hkbu.edu.hk/s/data/caffe.zip](http://dlbench.comp.hkbu.edu.hk/s/data/caffe.zip)
- CNTK: [http://dlbench.comp.hkbu.edu.hk/s/data/cntk.zip](http://dlbench.comp.hkbu.edu.hk/s/data/cntk.zip)
- MXNet: [http://dlbench.comp.hkbu.edu.hk/s/data/mxnet.zip](http://dlbench.comp.hkbu.edu.hk/s/data/mxnet.zip)
- TensorFlow: [http://dlbench.comp.hkbu.edu.hk/s/data/tensorflow.zip](http://dlbench.comp.hkbu.edu.hk/s/data/tensorflow.zip)
- Torch: [http://dlbench.comp.hkbu.edu.hk/s/data/torch.zip](http://dlbench.comp.hkbu.edu.hk/s/data/torch.zip)

For the synthetic data generation, please refer to scripts in the link: [http://dlbench.comp.hkbu.edu.hk/s/html/v5/index.html](http://dlbench.comp.hkbu.edu.hk/s/html/v5/index.html).

#### Prepare .config file
There are some sample configuration files in configs/, you can choose one of them as example and change values of each item according to your needs and environment.
#### Run
To run benchmark test just execute   
> **python benchmark.py -config configs/\<your config file>.config**

### Add new tools
Follow the instructions in *tools/Readsme.md* preparing the running scripts and netowrk configurations. Note that training data should be put in **$HOME/data/** so that we can test new tools in our machines and update benchmarking results to our website.

### Update log    
May 24, 2017:   
- Updated the scripts for mxnet0.9.5, previous scripts are still preserved in tools/mxnet/mxnet0.7    
- Updated benchmark.py and the format of config files. Now you only need to specify the device id (-1 for CPU; 0,1,2,3 for GPU) and device count (number of cores to use)  in the config file. An example called test.config can be found in configs/   
- yaroslavvb helped improve the performance of CNTK CIFAR by keeping variables on CPU. Thank you!
- tfboyd optimized the scripts for tensorflow by changing the image processing place to CPU and some other tweaks making tensorflow run faster then before. Thank you!   
- testbm.sh in tools/common updated. Scripts for testing on CPU added. 