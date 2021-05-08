# Rent Crawler 租房爬虫
This is a house rental information crawler project for people living in Beijing.
Currently no other language documents are available, Chinese documents only.

------

##介绍
适用人群：北京,有一定程序基础人群  

最近为了抓取个人房东的出租信息，写了一个爬虫，用来整合水木清华租房版，以及豆瓣北京租房小组里面相关的租房信息，方便自己查看信息，不用每次都去搜索相关内容

> * 可以配置租房区域
> * 可以配置黑名单
> * 可以配置帖子开始时间

抓取结果示意图：
![Rent Crawelr Result](https://github.com/waylife/RentCrawer/blob/master/Images/result_1.2.png?raw=true)

##使用说明
Python 2.7+,暂时不支持Python 3    
需要先安装pip依赖管理工具  
需要先安装Requests以及BeautifulSoup库，如果已经安装可以忽略，没有安装，使用以下命令安装：

``` bash
pip install requests
pip install beautifulsoup4
```
运行步骤：


1. 【必须】配置config.ini中key_search_word_list字段为需要搜索的地名，可参考实例进行配置，逗号[半角逗号,不是全角逗号，]分隔   
2. 【必须】配置config.ini中custom_black_list字段为你不想搜到的内容,不配置则为空  
3. 【必须】配置config.ini中start_time字段为帖子开始时间
4. 【可选】其他配置可可选择进行配置，删除rentdata.db3以及rentdata_result.html文件，如果不希望本次结果与上次混合在一起，可以删除相关文件
5. 【必须】运行RentCrawler.py文件
6. 【必须】等待程序结束后打开rentdata_result.html查看结果

##注意
由于豆瓣有反刷机制，每天运行次数不要过多，有可能导致当天无法获取数据，也就是引发403错误   
豆瓣数据请求目前为每获得一次结果暂停1s

##反馈与建议
可通过以下地址提交
https://github.com/waylife/RentCrawer/issues/new

##改进
欢迎各路大神提供改进意见

## License
The MIT license.