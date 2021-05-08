声明
========

本人自知精力与能力有限，欢迎志同道合之士送上您宝贵的建议与Patch!



关于
========

一个分布式定向抓取集群的简单实现。

目前实现功能
-------------

1. 多线程下载,线程数可配置。
2. 无需修改代码，按照规则添加配置就可以完成页面抽取、入库。
3. 利用Redis的list作为抓取队列，zset作为已抓取集合。
4. 支持分布式部署多个爬虫，Redis作为核心，mysql为存储,当然redis/mysql自身拥有各自的扩展方案。


TODO List
-------------

1. KISS: Keep it simple & stupid!
2. Supports cookies,and authentication.
3. Write information into files (using protobuf??).



INSTALL
========

确认安装Python2.7及依赖库: 
        
        MySQLdb: http://sourceforge.net/projects/mysql-python/
        
        redis: https://pypi.python.org/pypi/redis/
        
        lxml: http://lxml.de/
        
下载源码包:

        git clone https://github.com/agathewiky/spider-roach.git


How?
========


scheduler.py 
-------------

定义自己的爬虫,实现爬虫的调度算法，并将pipeline中负责解析的类注册到爬虫中;
继承BaseSpider基类即可实现一个自己的爬虫，然后重写 Rules函数，定义自己的爬行策略。

    class spider_name(BaseSpider):
        def Rules(self):
            #linkbase
            linkbase = getRedis()
            self.url_list = DQueue(linkbase,'url_list')
            self.url_set = Record(linkbase, 'crawled_set')
            base.url_maps = get_Maps('./maps.cfg')
            list = {
                'url':self.url_list,
                'url_set':self.url_set,
            }
            self.AddRules(list, 'Parse_url', 'url', 10)
    
        def scheduling(self):
            """重写scheduling,实现自己的调度策略"""
            start_url = 'http://venue.damai.cn/search.aspx'
            self.url_list.push(start_url)
            while 1:
                #do something
                time.sleep(5)
    

maps.cfg
-------------

配置待抓取页面相应的抽取规则
详细例子参见maps.cfg

    {
        "http://venue.damai.cn/search.aspx":{
            "info":"抓取XX网场馆列表页页",
            "pre_url":"http://venue.damai.cn",#抽取出的link添加默认前缀
            "link_xpath":[
                "//div[@class='pagination']/a[@class='next']/@href", #下一页
                "//span[@class='type']/h3/a/@href", #详情页
                ],
         },
        "http://venue.damai.cn/venue":{
            "info":"抓取XX网场馆详情页",
            "table":"pastime", #mysql表名
            "page_xpath":{
                "name":"//div[@class='site_guide']/a[3]/text()", #与mysql表字段名必须保持一致
                "image":"//div[@class='venueDetal']/p/img[@class='img']/@src",
                "detail":"//div[@class='info']/div/text()",
                }
         },
    }


settings.py
-------------

配置Redis,mysql的连接参数
配置maps.cfg路径位置


RUN
========

首先确认redis和mysql服务是否已启动并可用，然后执行：

    ./crawl spider_name
    options:
        -d ./logs 可将输出写入指定文件夹的日志中
