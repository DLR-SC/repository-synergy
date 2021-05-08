# recommandation
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/)<br>
[![](https://img.shields.io/badge/pandas-0.21.0-brightgreen.svg)](https://pypi.python.org/pypi/pandas/)
[![](https://img.shields.io/badge/numpy-1.13.1-brightgreen.svg)](https://pypi.python.org/pypi/numpy/)
[![](https://img.shields.io/badge/pyspark-1.6.1-brightgreen.svg)](https://pypi.python.org/pypi/pyspark/)
## 语言
Python3.5<br>
## 依赖库
pandas=0.21.0<br>
numpy=1.13.1<br>
pyspark=1.6.1<br>
## 原理说明
推荐系统的原理在于计算用户对各个物品的期望，从而将高期望的物品推荐给用户。本人写的方法有：

### 物品的相似度矩阵:similar_matrix.py
原始数据为用户-物品是否购买的一个0-1矩阵(m\*n)。通过计算物品两两间的相似度，从而得到物品的相似度矩阵(n\*n)。相似度矩阵\*用户-物品矩阵(即原始数据)，就可以得到用户已购买物品对未购买物品的一个权重求和，从而得到用户对每个物品的购买期望(m\*n)*(n\*n)=m\*n的推荐矩阵<br>
![ex1](https://github.com/renjunxiang/recommandation/blob/master/picture/similar%20matrix%20result.png)

### ALS矩阵分解:ALS.py
原始数据为用户-物品打分或者是否购买矩阵(m\*n)。通过矩阵分解，将m\*n的矩阵分解为m\*k的用户矩阵和k\*n的物品矩阵，(m\*k)*(k\*n)=m\*n的推荐矩阵，从而从而得到用户对每个物品的购买期望(填充了原来的缺失值或0值）。ALS的使用范围要大于相似度矩阵，且精确性要更高，矩阵分解可以直观的得到用户特征和物品特征。<br>
![ex2](https://github.com/renjunxiang/recommandation/blob/master/picture/ALS矩阵分解.png)

### ALS矩阵分解在pyspark上有现成模块:mllib_recommandation
![ex3](https://github.com/renjunxiang/recommandation/blob/master/picture/pyspark_1.png)
![ex4](https://github.com/renjunxiang/recommandation/blob/master/picture/pyspark_2.png)
![ex5](https://github.com/renjunxiang/recommandation/blob/master/picture/pyspark_3.png)

### SVD矩阵分解:Recommandation_SVD
原始数据为用户-物品打分或者是否购买矩阵(m\*n)。通过矩阵分解，将m\*n的矩阵分解为m\*m的用户矩阵、m\*n的特征矩阵和n\*n的物品矩阵。再降至k维，m\*k的用户矩阵、k\*k的特征矩阵和k\*n的物品矩阵，(m\*k)*(k\*n)=m\*n的推荐矩阵。通过用户购买向量\*k\*n的物品矩阵\*k\*k的特征矩阵的逆得到空间位置，求得余弦相似度、欧氏距离等来查询相似用户和相近产品<br>
![ex6](https://github.com/renjunxiang/recommandation/blob/master/picture/SVD分解.png)