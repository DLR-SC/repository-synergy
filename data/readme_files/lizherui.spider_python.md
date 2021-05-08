spider_python
=============
##概述

抓取北邮人论坛和水木社区校招信息的爬虫程序。

新增手机短信通知功能，需要在conf.py里配置139手机号，发件箱账号和密码。(短信通知功能也可作为邮件通知功能)。

不支持Python3。

##策略

###爬虫爬取
爬取模块默认每1小时运行1次，同时抓取web_urls和current_message_urls。每爬取10次清空所有数据。

###发送短信
发短信模块默认每10分钟扫描一次current_message_urls，不为空才会发短信。发送成功后会把current_message_urls合并到outdated_message_urls中，并清空current_message_urls。

###关键词筛选
在conf.py里根据自己的兴趣定制筛选的关键词,抓取你想要的信息：

* WEB_FILTER_XXX_KEYS是针对Web页面抓取的关键词

* MESSAGE_FILETER_XXX_KEYS是针对短信及邮件通知的关键词


包含XXX_FILETER_PRI_KEYS的链接一定会被抓取。
  
包含XXX_FILETER_KEYS且不包含XXX_FILETER_EXCLUDE_KEYS的链接也会被抓取。

###关键词筛选测试样例

设置如下：
    
    WEB_FILETER_PRI_KEYS = (u'校招', u'应届', u'毕业生')
    WEB_FILETER_KEYS = (u'百度', u'阿里', u'腾讯',u'网易')
    WEB_FILETER_EXCLUDE_KEYS = (u'社招',)

测试结果如下:
    
    "[社招/校招] 阿里巴巴招聘实习生" # True,信息包含WEB_FILETER_PRI_KEYS 

    "[社招] 阿里巴巴招聘实习生" # False,信息虽包含WEB_FILETER_KEYS但也包含WEB_FILETER_EXCLUDE_KEYS 

    "阿里巴巴招聘实习生" # True,信息虽包含WEB_FILETER_KEYS且不包含WEB_FILETER_EXCLUDE_KEYS 

###爬取目标的设置
本程序默认爬取北邮和水木两个BBS板块的信息，如果你还想爬取其他目标的信息，要在conf.py中HTTP_QUERYS元组内添加新网站设置信息的字典项。下面示例添加了爬取'天津大学就业指导中心的招聘信息板块'的设置：

    {
        'host' : 'http://job.tju.edu.cn/', #网站的域名，'host'+'href'应该能够合成为一个可访问的招聘信息的链接。
        'url'  : 'http://job.tju.edu.cn/zhaopinxinxi.php', #设置你要爬取的页面，该页面包含了招聘信息的链接，通常为招聘板块的首页。
        'headers' : {	                   #headers的设置保持不变
            "X-Requested-With" : "XMLHttpRequest",
         },
        'href' : r"^zhaopinxinxi_detail.php\?id=\d+$", #设置匹配字符串，匹配'url'网页中<a>标签的href内容。设置本项时可以在'url'网页中找一条招聘信息的超链接<a>，将其中的href内容放入字符串，href尾部数字部分用'\d+'代替，如果链接中有'?'，需要改成'\?'进行转义。
        'source' : u'天津大学就业指导中心-招聘信息',
    },
    
##安装与运行
Unix/Windows下均需要先在本机安装[redis](http://redis.io)服务程序，然后在Unix下运行redis-server，在Windows下启动redis-server.exe。

安装示例：Mac OS X下安装redis

    brew install redis

此外，程序依赖以下Python第三方包：

* [APScheduler](http://pythonhosted.org/APScheduler)

* [BeautifulSoup 3.2.1](http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html)

* [redis-py](https://github.com/andymccurdy/redis-py)

* [requests](https://github.com/kennethreitz/requests)

安装示例：Mac OS X/Linux下安装Python第三方包
    
    pip install apscheduler
    pip install BeautifulSoup
    pip install redis
    pip install requests
    
然后直接运行main.py程序，访问<http://127.0.0.1:8888> -e 与 -s 参数分别开启 邮件与短信通知功能,具体可以python main.py help 查看
    
##WEB页面效果

![1](https://lh4.googleusercontent.com/-DdobnB7RIf8/UhTs2OdrPNI/AAAAAAAAAM4/df2OmS0bhV0/w958-h599-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-08-22+%25E4%25B8%258A%25E5%258D%258812.36.50.png)

Enjoy it。

