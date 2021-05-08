###项目简介


本项目主要用于介绍使用 requests 和 BeautifulSoup 进行爬虫开发，最后采集到的条目格式如下:


```
{
    "外观颜色": "晨露白,布里奇沃特青铜,马达加斯加橙,鲜绿,塞勒涅青铜,深蓝色,栗子黑", 
    "name": "Vanquish", 
    "url": "http://car.autohome.com.cn/price/brand-35.html", 
    "brand": "阿斯顿·马丁", 
    "车身结构": "硬顶跑车", 
    "变速箱": "自动", 
    "发动机": "6.0L", 
    "级别": "跑车", 
    "price": "526.88-628.00万"
}
```


* requests 文档: [http://docs.python-requests.org/en/latest/](http://docs.python-requests.org/en/latest/)
* BeautifulSoup 文档: [http://www.crummy.com/software/BeautifulSoup/bs4/doc/](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* Chrome DevTools 文档: [https://developer.chrome.com/devtools](https://developer.chrome.com/devtools)

### 使用须知

1. clone 本项目

```
# git clone https://github.com/William-Sang/autohome_crawler.git
```
2. 配置依赖

    ```
	# cd autohome_crawler
	# pip install -r requirements
	```
	
3. 修改配置(如果有需要)


    ```
	# vim setting.py
	```
	
4. 执行爬取任务，默认结果会下载到 requests 目录下


    ```
	# python app.py
	```

### 需要加强功能

1.  下载重试功能 http://www.coglib.com/~icordasc/blog/2014/12/retries-in-requests.html

### 可能出现的问题

1. 抓取具体车型信息的时候，会出现颜色无法抓取成功的情况。（有时）
