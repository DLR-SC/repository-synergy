# amazon-recommender-system
recommender system of amazon product ( for final project of CSE544 )

## An Optimized Recommender System from Integrating Multiple Algorithms
 
Team members : Sewon Min, Chaofan Han
 
### Project Abstract
This project aims to build an integrated recommender system with versatile features based on the Amazon reviews dataset. This project tries to solve problems confronting present recommender systems such as how to improve the degree of automation, how to make algorithms run faster and more robust with parallel computation.

### The main contents of this project are following:
- Implementation of various algorithms
- Different ways of ensemble learning of the algorithms
- Support of parallel tasks on distributed system, and performance/time comparison of each algorithm by the number of computation instances
- Implementation of demo program of the final recommender system

### Algorithms to be implemented:
- Content-based Recommender System
- Collaborative Filtering
- Weight Learning
- Latent Factor Model
- Bias Extension
- Ensemble Model 

### Datasets
- Amazon Review Data accessed from (http://snap.stanford.edu/data/web-Amazon-links.html)
- Number of reviews : 34,686,770
- Number of users : 6,643,669 (56,772 with more than 50 reviews)
- Number of products : 2,441,053

### Tools
- Python, Myria, AWS


### Progress

1. Download data
You need to have 'data' directory in your HOME.

```bash
chmod +x download.sh; ./download.sh 
```

This will takes several minutes.

2. Preprocess data and create DB
```bash
python prepro/preprocess.py
```

3. Run Recommender System
```bash
python -m model.main
```
It builds recommender with train data and also evaluates performance on test data. If you want to specift certain recommender system, you can use '--recom'.

Content Based : 'cb'
Collaborative Filtering : 'cf'
Weight Learned : 'l'
Latent Factor : 'lf'
Latent Factor with Bias Extension : 'blf'

For example, if you want to run Weight Learned Recommender,
```bash
python -m model.main --recom l
```
If you want to run Content Based and Collaborative Filtering,
```bash
python -m model.main --recom cb cf
```
It runs recommender in small dataset by default. If you want to run in large dataset, you can use '--small False'. Batch size is 128 by default. If you want to change it, you can use '--batch_size'. For example,
```bash
python -m model.main --small False --batch_size 256
```

### References
- M. Pazzani, D. Billsus, Content-based Recommendation System.
- G. Adomavicius and A. Tuzhilin, “Towards the next generation of recommender systems: a survey of the state-of-the-art and possible extensions,” IEEE Trans. on Data and Knowledge Engineering 17:6, pp. 734– 749, 2005.
- Y Koren, R Bell, C Volinsky.  Matrix factorization techniques for recommender systems. Computer, 2009.
- M Jahrer, A Töscher, R Legenstein. Combining predictions for accurate recommender systems. Proceedings of the 16th ACM. 
