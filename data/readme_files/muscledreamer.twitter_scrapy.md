# 使用Scrapy获取Twitter推文及个人信息


* 下载项目并打开twitter_scrapy目录
* 输入命令即可启动
```
python Begin.py
```
* twitter_info_start为信息爬取，twitter_content_start为内容爬取
```
# cmdline.execute("scrapy crawl twitter_info_start".split())
cmdline.execute("scrapy crawl twitter_content_start".split())
```
* 内置[Redis布隆去重(安装Reids)](http://blog.csdn.net/u010286751/article/details/48924635)及数据库插入,可在setting中自定义配置

## 前期翻墙准备及IP代理池问题

* 推荐：[shadowsocksR(点击查看相关配置)](https://github.com/muscledreamer/shadowsocksR)
* 由于shadowsocksR(以下简称ssR)兼容shadowsocks(以下简称ss)配置文件,所以建议升级ss客户端至ssR,这样可以同时使用ssR和ss配置文件
* SSR默认端口为1080,由于没有找到修改默认端口的方法.所以需要建立IP代理池的同学建议使用多个ss配置文件
* 下面是ss配置文件的demo，local_port为本地端口，可以在本机的不同端口配置多个ss,以满足代理池的需要


---
第一个ss配置(将第一台服务器代理1080端口):
```

{
  "server":...
  "server_port":...
  "local_port":1080,
  "password":...
  "timeout":...
  "method":...
}
```
第二个ss配置(将第二台服务器代理1081端口):
```

{
  "server":...
  "server_port":...
  "local_port":1081,
  "password":...
  "timeout":...
  "method":...
}
```
以此类推

在setting中设置IP代理池,并使用中间件调用
```
#代理设置(最好使用墙外代理IP池,可减少重定向次数)
PROXIES = [
    {'ip_port': '127.0.0.1:1080','user_pass':None},
    {'ip_port': '127.0.0.1:1081','user_pass':None},
    ]
```
或使用国外服务器直接代理访问,[详情请点击](http://www.cnblogs.com/rwxwsblog/p/4575894.html)
```
#代理设置(最好使用墙外代理IP池,可减少重定向次数)
PROXIES = [
    # {'ip_port': '111.11.228.75:80', 'user_pass': ''},
    # {'ip_port': '120.198.243.22:80', 'user_pass': ''},
    # {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
    # {'ip_port': '101.71.27.120:80', 'user_pass': ''},
    # {'ip_port': '122.96.59.104:80', 'user_pass': ''},
    # {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
    ]
```
本项目虽内置解决Twitter反爬重定向的中间件,但不建议在不使用IP代理池的情况下长时间不间断进行多账户爬取,算是"盗亦有道"吧

如果有什么问题或者建议都可以在这个Issue和我讨论，非常愿意与大家一起分享并解决问题

如果您对这个项目感兴趣或者使用项目过程中有什么新的发现，希望可以联系我，一起优化，一起进步。
