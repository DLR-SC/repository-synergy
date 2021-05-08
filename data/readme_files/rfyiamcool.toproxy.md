# toproxy

> 用tornado实现的高性能代理服务器，涵盖了基本的method

*性能方面测试，toproxy在单进程模式下，新连接请求在3500 QPS*


### New Future

* 加入了白名单功能
* 当访问的地址连接失败的时候，会做重试机制
* support 301 redirect
* 加入了基本认证


更多的httpclient文档，[httpclient 更多文档](http://tornado.readthedocs.org/en/latest/httpclient.html  "tornado httpclient") 

### 安装

方法1:

```
pip install toproxy
```

方法2:

```
python setup.py install
```

### 直接使用

```
python toproxy/proxy.py -h

usage: proxy.py [-h] [-p PORT] [-w WHITE] [-u USER]

python -m toproxy/proxy -p 8888 -w 127.0.0.1,8.8.8.8 -u xiaorui:fengyun

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  tonado proxy listen port
  -w WHITE, --white WHITE
						white ip list ---> 127.0.0.1,215.8.1.3
  -u USER, --user USER  Base Auth , xiaoming:123123
```

**快速启动**

```
python  -m toproxy/proxy -p 8888 -w 127.0.0.1 -u xiaorui:123
python  -m toproxy/proxy
::::Starting HTTP proxy on port 8888
...
```

### 模块的调用

```
from toproxy import run_proxy
run_proxy(port, start_ioloop=False)
...
tornado.ioloop.IOLoop.instance().start()
```

### TODO

1.  提高toproxy的性能
2.  加入异步回调通知模式
3.  批量传送
