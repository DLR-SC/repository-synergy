# All-IT-eBooks-Spider

项目地址：https://github.com/Kulbear/All-IT-eBooks-Spider
喜欢欢迎Star！

### 简介
---
最近在公司实习，项目多数和爬虫有关，越发的感觉爬虫十分的好用，闲来无事便有了这个小程序。

首先感谢 [崔庆才的Python爬虫学习系列教程](http://cuiqingcai.com/1052.html)，当年我的第一个爬虫（其实可能比本文这个还要复杂一点）是参考他的教程完成的。

代码相当简单，大牛轻喷。只是给想用Python学习爬虫的童鞋们一点~~矮地儿~~Idea而已。

这几日和朋友搜索东西的时候无意间发现了一个国外的存有大量PDF格式电子书的网站。其实我相当奇怪在国外版权管控如此严的环境下这个网站是如何拿到这么多电子书的，而且全是正版样式的PDF，目录索引一应俱全，没有任何影印和扫描的版本。

之前多数的Python开发都是在UNIX环境下完成的，这次这个小爬虫也是为了测试一下刚在Windows上部署好的环境。

闲话少说，今天要做的事情就是爬取[All IT eBooks](http://www.allitebooks.com/)这个网站上面PDF的下载链接了。

### 准备工作
---
- 安装Python 3.5.X

      因为Windows上配置Python稍微麻烦，我个人使用的是Anaconda提供的一站式安装包，针对Windows平台Anaconda提供了很傻瓜的一键安装包
- 或者选择 Anaconda [下载页](https://www.continuum.io/downloads)
- ~~没了~~

这个项目（姑且叫项目）的结构十分简单，要爬取的网站结构设计也十分清晰，所以我们不需要用任何第三方库！

### 分析网页代码并提取
---
其实这个简单的爬虫需要做的事情仅仅是爬取目标网页的源代码（一般是HTML），提取自己需要的有效信息，再做进一步使用。

打开这个网页，可以看到这个网站的设计十分简洁和整齐，估计源代码应该也是结构简洁的
![http://www.allitebooks.com/](http://upload-images.jianshu.io/upload_images/2527939-31e1152a890c239e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将网页往下拖可以看到在页底有Pagination的按钮，提供翻页，翻页后的链接为 http://www.allitebooks.com/page/数字页码/ 这个格式。
 
点击每本书或者标题以后，会进入到每本书的详细资料页面，并且有一个十分明显的Download PDF的按钮（这里我就不截图了）。

比如某本书详细页面的链接（不在上图中，找了一本链接比较短的书）：
http://www.allitebooks.com/big-data/

首先我们要拿到每个书detail页面的链接，然后通过这个链接进入到具体的页面，再找寻下载的链接。

多检查几个链接我们可以发现首页上的每本书详细页面的链接很容易找到，每本书的内容都是一个article的node里所包含的，例如：

    <article id="post-23083" class="post-23083 post type-post status-publish format-standard has-post-thumbnail hentry category-networking-cloud-computing post-list clearfix">
        <div class="entry-thumbnail hover-thumb">
            <a href="http://www.allitebooks.com/ssl-vpn/" rel="bookmark">
                ![578ff04dd3488.jpg](http://upload-images.jianshu.io/upload_images/2527939-a975ffbeba6c3748.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) </a>
        </div>
        <!-- END .entry-thumbnail -->
        <div class="entry-body">
            <header class="entry-header">
                <h2 class="entry-title"><a href="http://www.allitebooks.com/ssl-vpn/" rel="bookmark">SSL VPN</a></h2>
                <!-- END .entry-title -->
                <div class="entry-meta">
                    <span class="author vcard">
    				<h5 class="entry-author">By: <a href="http://www.allitebooks.com/author/j-steinberg/" rel="tag">J. Steinberg</a>, <a href="http://www.allitebooks.com/author/joseph-steinberg/" rel="tag">Joseph Steinberg</a>, <a href="http://www.allitebooks.com/author/t-speed/" rel="tag">T. Speed</a>, <a href="http://www.allitebooks.com/author/tim-speed/" rel="tag">Tim Speed</a></h5>
    				</span>
                </div>
                <!-- END .entry-meta -->
            </header>
            <!-- END .entry-header -->
            <div class="entry-summary">
                <p>This book is a business and technical overview of SSL VPN technology in a highly readable style. It provides a vendor-neutral introduction to SSL VPN technology for system architects, analysts and managers engaged in evaluating and planning
                    an SSL VPN implementation. This book aimed at IT network professionals…</p>
            </div>
            <!-- END .entry-summary -->
        </div>
        <!-- END .entry-body -->
    </article>


很容易就可以找到这本书的链接在第一层div的第一个子node上

    <a href="http://www.allitebooks.com/ssl-vpn/" rel="bookmark">
 
仔细观察整个网页源码后发现，唯独这个带有书detail页链接的tag里有这条

    rel="bookmark"

那么现在就很简单了，我们有以下几个选择来提取这个链接：
1. BeautifulSoup
2. 正则表达式（Regular Expression）
3. 其他...

BeautifulSoup这里不过多做叙述，简单来说，这个库可以帮你很好的分解HTML的DOM结构，而正则表达式则是Ultimate Solution，可以匹配任何符合条件的字符串，这里我们选用正则表达式（我也只学过皮毛，不过解决这次的问题只需要5分钟入门级就可以），具体正则教程可以参见网上的资源，比如 [这里](http://deerchao.net/tutorials/regex/regex.htm)。

先推荐一个在线检测正则的网站 [Regex101](https://regex101.com/)

    'href="(.*)" rel="bookmark">'

![Regex101.png](http://upload-images.jianshu.io/upload_images/2527939-3ac7d47f856b566c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

匹配刚才那个网页链接所需要的正则表达式如上，现在我们来开始Python代码的部分：

    import urllib.request
    import re

    BASE_URL = 'http://www.allitebooks.com'
    BOOK_LINK_PATTERN = 'href="(.*)" rel="bookmark">'

    req = urllib.request.Request(BASE_URL)
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')
    # print(doc)
    url_list = list(set(re.findall(BOOK_LINK_PATTERN, doc)))

以上代码能够将网页源码解码并返回我们需要的url_list, 其中re.findall(...)这一部分的作用是，找到doc中所有符合BOOK_LINK_PATTERN的部分并return一个list出来，转换为set只是为了去重，又在之后重新转回为了list为了方便遍历。

仅仅抓取第一页显然不够，所以我们加入对页码的遍历，如下：

    ....
    i = 1    
    while True:
        req = urllib.request.Request(BASE_URL)
        html = urllib.request.urlopen(req)
        doc = html.read().decode('utf8')
        # print(doc)
        url_list = list(set(re.findall(BOOK_LINK_PATTERN, doc)))
        # Do something here
        i += 1

这里并没有对可能出现的Error做处理，我们稍后补上。

至此，我们的程序已经可以抓取这个网站所有页面里的书detail页面的链接了（理论上）

具体到每个页面以后的工作变得十分简单，通过访问每本书的detail页面，检查源代码，可以很轻松的提取出页面里Download PDF按钮对应的下载链接。

```
<span class="download-links">
<a href="http://file.allitebooks.com/20160908/Expert Android Studio.pdf" target="_blank"><i class="fa fa-download" aria-hidden="true"></i> Download PDF <span class="download-size">(48.5 MB)</span></a>
</span>
```

其中，

    <a href="http://file.allitebooks.com/20160908/Expert Android Studio.pdf" target="_blank"><i class="fa fa-download" aria-hidden="true"></i> Download PDF <span class="download-size">(48.5 MB)</span></a>

就是我们需要的部分了。

故技重施，使用如下的正则表达式匹配这一段HTML代码：

    <a href="(http:\/\/file.*)" target="_blank">

这段代码就不分解放出了，自己动手吧（源码和Github链接在最后）。

（其实是因为我是写完了整个代码以后才返回来写这个文章，现在懒得拆了......）

### 小结
---
当然，这个简单的程序只是一个最最基本的小爬虫。离~~枝繁叶茂~~真正功能的爬虫还差很多。多数网站都有多少不等的反爬虫机制，比如单位时间内单一IP的方位次数限制等等。通常网站会有一个robots.txt文件，规定了针对爬虫的要求，比如能不能使用爬虫。这个文件一般在www.hostname.com/robots.txt这个格式的网址可以直接查看，比如我们这次爬取的网站
  
    http://www.allitebooks.com/robots.txt

应对不同网站的反爬虫机制，我们可以选择增加Header，随机Header，随机IP等很多方法来绕开，当你大量或者高频爬取一些网站的同时，如果可以，别忘了给网站拥有者做一些贡献（比如之前爬取Wiki的时候，捐赠了5刀...），以缓解网站作者维持服务器的压力。

### 源码
---
Github: https://github.com/JiYangE/All-IT-eBooks-Spider
请尽情的~~鞭笞~~Star我吧！

趁着午休的一小时赶工出来的代码，也没备注重构修改过，结构略乱，单一指责根本没有，~~我不管，能打仗的兵就是好兵~~，各位凑活一下看，逻辑非常简单

文件1 crawler.py

```
# -*- coding: utf-8 -*-
import re
import time
import urllib.request

import conf as cf

BASE_URL = 'http://www.allitebooks.com'

class MyCrawler:

    def __init__(self, base_url=cf.BASE_URL, header=cf.FAKE_HEADER, start_page=1):
        self.base_url = base_url
        self.start_page = start_page
        self.headers = header

    # 链接代理
    def build_proxy(self):
        proxy = cf.PROXY
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    def fetch_book_name_list(self):
        while True:
            try:
                req = urllib.request.Request(
                    self.base_url + '/page/{}'.format(self.start_page), headers=self.headers)
                html = urllib.request.urlopen(req)
                doc = html.read().decode('utf8')
                alist = list(set(re.findall(cf.BOOK_LINK_PATTERN, doc)))
                print('Now working on page {}\n'.format(self.start_page))
                time.sleep(20)
                self.start_page += 1
                self.fetch_download_link(alist)
            except urllib.error.HTTPError as err:
                print(err.msg)
                break

    def fetch_download_link(self, alist):
        f = open('result.txt', 'a')
        for item in alist:
            req = urllib.request.Request(item)
            html = urllib.request.urlopen(req)
            doc = html.read().decode('utf8')
            url = re.findall(cf.DOWNLOAD_LINK_PATTERN, doc)[0]
            print('Storing {}'.format(url))
            f.write(url + '\n')
            time.sleep(7)
        f.close()

    def run(self):
        self.fetch_book_name_list()


if __name__ == '__main__':
    mc = MyCrawler()
    # mc.build_proxy()
    mc.run()
```

文件2 conf.py

```
# -*- coding: utf-8 -*-
import random

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

PROXY = {'http': "http://127.0.0.1:9743/"}

BOOK_LINK_PATTERN = 'href="(.*)" rel="bookmark">'
DOWNLOAD_LINK_PATTERN = '<a href="(http:\/\/file.*)" target="_blank">'

BASE_URL = 'http://www.allitebooks.com'

FAKE_HEADER = {
    'User-Agent': random.choice(USER_AGENTS),
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.allitebooks.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
}
```

运行结果文件 result.txt 内容：

    http://file.allitebooks.com/20160708/Functional Python Programming.pdf
    http://file.allitebooks.com/20160709/Mastering JavaScript.pdf
    http://file.allitebooks.com/20160708/ReSharper Essentials.pdf
    http://file.allitebooks.com/20160714/Mastering Python.pdf
    http://file.allitebooks.com/20160723/PHP in Action.pdf
    http://file.allitebooks.com/20160709/Learning Google Apps Script.pdf
    http://file.allitebooks.com/20160709/Mastering Yii.pdf
    ......

### 再废话两句
---
Python的功能日益强大起来，有很多现成的爬虫框架可以学习，在熟练网络协议和抓取等基础的网络知识以后，也可以试试学习一些较为完善的框架，比如Scrapy，详情可以看[崔庆才的总结](http://cuiqingcai.com/2433.html)

公司的项目比这个要复杂得多，日后有时间再拿出可以公开的部分写一写总结 ......
