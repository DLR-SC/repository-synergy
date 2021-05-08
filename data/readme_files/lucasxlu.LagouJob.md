# Data Analysis of [Lagou Job](http://www.lagou.com/)
![Lagou](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)

## Introduction
This repository holds the code for job data analysis of [Lagou](http://www.lagou.com/). 
The main functions included are listed as follows: 

1. Crawling job data from [Lagou](www.lagou.com), and get the latest information of jobs about Internet.
2. Proxies are collected from [XiCiDaiLi](https://www.xicidaili.com/nn/1).
3. Data analysis and visualization.
4. Crawling job details info and generate word cloud as __Job Impression__.
5. In order to train a [NLP](http://baike.baidu.com/item/nlp/25220#viewPageContent) task with machine learning, the data of interviewee's comments will be stored in [mongodb](https://docs.mongodb.com/) 


## Prerequisites
1. Install 3rd party libraries  

    ```sudo pip3 install -r requirements.txt```
2. Install [mongodb](https://docs.mongodb.com/) and start [mongodb](https://docs.mongodb.com/) service [optional]

    ```sudo service mongod start```


## How to Use
1. clone this project from [github](https://github.com/lucasxlu/LagouJob.git).
2. Lagou's anti-spider strategy has been upgrade frequently recently. I suggest you run [proxy_crawler.py](./spider/proxy_crawler.py) to get IP proxies and execute the code with [PhantomJS](http://phantomjs.org/). 
3. run [m_lagou_spider.py](spider/m_lagou_spider.py) to crawl job data, it will generate a collection of Excel files in ```./data``` directory.
4. run [hot_words_generator.py](analysis/hot_words_generator.py) to cut sentences, it will return __TOP-30__ hot words and wordcloud figure.


## Analysis Results
> ![Image1](https://pic2.zhimg.com/a0c42bc6bd7c8743687ba50305c85821_b.jpg)  
> ![Image2](https://pic3.zhimg.com/f89ca5a008f8ad84a1a2121888aa10c2_b.jpg)  
> ![Image3](https://pic1.zhimg.com/85b930c6aff823a3b8ee73973d20f274_b.jpg)  
> ![Image4](https://pic1.zhimg.com/v2-b5ef151109c8787a0a46efed111d3884_b.png)  
> ![Image5](https://pic3.zhimg.com/v2-aae9b487a843b00298166b6335b061aa_b.png)  
> ![Image6](https://pic3.zhimg.com/9c2e99674bcb59e0ff54ca0a3fbe4142_b.jpg)  
> ![Image7](https://pic3.zhimg.com/6ea06ad7dd376f51e629635a69b09cba_b.jpg)  


## Report
* For technical details, please refer to my answer at [Zhihu](https://www.zhihu.com/question/36132174/answer/94392659). 
* The PDF report can be downloaded from [here](https://lucasxlu.github.io/blog/projects/LagouJob.pdf).


## Change Log
- [V2.0] - 2019.04. Upgraded to [PhantomJS](http://phantomjs.org/) and IP proxies.
- [V1.2] - 2017.05. Rewrite WordCloud visualization module.
- [V1.0] - 2017.04. Upgraded to mobile Lagou.
- [V0.8] - 2016.05. Finish Lagou PC web spider.


## LICENSE
[Apache-2.0](./LICENSE)