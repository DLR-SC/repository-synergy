# PPCL

Base PCL python library for deep learning, which DINK needs.

Already supported PointCloud_PointXYZI, PointCloud_PointXYZRGB, PointCloud_PointXYZRGBA ApproximateVoxelGrid.
[example](https://github.com/FPAI/PPCL/blob/master/examples/tests/test_filters.py)


Already supported PointCloud_PointXYZI, PointCloud_PointXYZRGB cluster.
[example](https://github.com/FPAI/PPCL/blob/master/examples/official/Segmentation/cluster_extraction_XYZI.py)



![PCL](pcl_logo.png)

# QUICK SRART

## 1 Install Depandency

```bash
sudo apt-get update 

sudo apt-get install cython

sudo apt-get install git build-essential linux-libc-dev 

sudo apt-get install cmake cmake-gui 

sudo apt-get install libusb-1.0-0-dev libusb-dev libudev-dev 

sudo apt-get install mpi-default-dev openmpi-bin openmpi-common 

sudo apt-get install libflann1.8 libflann-dev 

sudo apt-get install libeigen3-dev 

sudo apt-get install libboost-all-dev 

(sudo apt-get install libvtk5.10-qt4 libvtk5.10 libvtk5-dev) 

sudo apt-get install libqhull* libgtest-dev 

sudo apt-get install freeglut3-dev pkg-config 

sudo apt-get install libxmu-dev libxi-dev 

sudo apt-get install mono-complete 

sudo apt-get install qt-sdk openjdk-8-jdk openjdk-8-jre 
```


## (2 Install PCL)


```bash
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl

sudo apt-get update

sudo apt-get install libpcl-dev
```

```bash
wget https://github.com/PointCloudLibrary/pcl/archive/pcl-1.9.1.tar.gz

tar -xzvf pcl-1.9.1.tar.gz

cd pcl-pcl-1.9.1

mkdir build && cd build

cmake -DCMAKE_BUILD_TYPE=Release ..

make -j2

sudo make -j2 install
```

## 3 Install PPCL

```bash
git clone https://github.com/FPAI/PPCL

cd PPCL

pip3 install cython&&sudo python3 setup.py build_ext -i&&sudo python3 setup.py install

(pip install cython&&sudo python setup.py build_ext -i&&sudo python setup.py install)
```

## 4 Validation

```bash
python

import pcl

```

## 5 Test


examples/tests/test_filters.py

run unittest     TestApproximateVoxelGrid Class



***

[![第一太平洋AI](fpai.png)](http://fp-ai.com)

第一太平洋AI，TF源码贡献者顶尖人工智能团队，底层技术驱动上层应用，垂直领域规模化落地。

First Pacific AI, the top AI team of TF source contributors, the bottom technology drives the upper application, and the vertical field is landed on a large scale.


官网|Official website： http://fp-ai.com

联系电话|Contact number： 400-153-0988

商务邮箱|Business email： info@fp-ai.com
