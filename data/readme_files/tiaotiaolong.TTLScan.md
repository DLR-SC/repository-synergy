# TTLScan

[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)




**一款插件化的漏洞扫描器框架**


- 目前支持ip iplist zoomeye搜索引擎 url urllist
- 目前支持RedisUn RedisGetShell Struts2系列漏洞 
- POC的准确性的已被复测
- 已经支持ZoomEYE搜索引擎自动获取ip系列POC的目标集合
- 希望大家一起来提交Poc 一起来修改框架
- To be Continued...

    
**截图**

![](http://okzjjcktf.bkt.clouddn.com/logo.png)

**使用说明**

程序的整体设计是支持3种输入源，目前支持两种输入源分别为：

- ip方式
- url方式

其中这两种都支持list形式 也就是文件列表格式。

**eg**: Redis未授权访问，输入源就是ip方式 你可以使用--ip或者--ip_list两种参数
其中--ip和--ip_list两者中--ip的优先级较高，如果同时使用了2种参数，则视为--ip_list无效

**eg**: 查询目前的所有Poc脚本

![](http://okzjjcktf.bkt.clouddn.com/logo4.png)

**POC的格式**
poc的格式非常简单，主要是2个函数被动态调用 POC()和POC_INFO()两个函数被动态调用，当检测到有漏洞的时候可以使用logger进行日志输出。

**eg：** **redis_un** script

```
#coding=utf-8
import redis
import socket
from lib import ttlscanlogger

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Redis Access Without Limit"
	dict_poc["Chinese_name"]="Redis未授权访问"
	dict_poc["author"]="qi.tao"
	dict_poc["port"]=6379
	return dict_poc
	
def POC(ip,port=6379):
	try:
		socket.setdefaulttimeout(2)
		poc="\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a"
		s=socket.socket()
		s.connect((ip,port))
		s.send(poc)
		rec=s.recv(1024)
		s.close()
		if "redis" in rec:
			ttlscanlogger.logger.error("[+]Vuln: {0} has found Redis access without limit".format(ip))
			return True
		else:
			return False
	except:
		return False

if __name__ == '__main__':
	print(POC())
```

**搜索引擎的使用方法 --search**

--search支持zoomeye搜索引擎，可以对ip系列的POC进行目标集合获取
--search_page 为获取的页数 默认为20页

**eg：** 
下图命令为利用zoomeye搜索引擎对redis未授权访问进行探测 默认只对有漏洞的ip进行日志输出，图中为了显示zoomeye搜索引擎目标集合，对整个集合进行了输出。

![](http://okzjjcktf.bkt.clouddn.com/logo5.png)

**zoomeye的设置和使用**

**zoomeye官方提供了api允许我们使用，这里我已经做了集成。但仍需相关配置项 access_token
获取zoomeye access_token的方法如下：**

平台主要使用的是 Json Web Token 的登录验证方式，用户只需使用用户名和密码，登录一次，获取 access_token。

并在接下来的其他 API 请求 HTTP 头中带上 access_token (格式如 Authorization: JWT <access_token>) 即可，无需再次登录验证。

获取access_token示例

```
curl -X POST https://api.zoomeye.org/user/login -d
'{
    "username": "foo@bar.com",
    "password": "foobar"
}'
{"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDU1NzE4NDcwLCJuYmYiOjE0N... ..."}

```

**将获取的access_token添加到config.config.py中的access_token**

```
#coding=utf-8
#Zoomeye Token
access_token=""

#Zoomeye Search API
zoomeye_search_api="https://api.zoomeye.org/host/search?query={0}&page={1}"

#Zoomeye Headers
headers={
	"Authorization":"JWT "+access_token
}
```
更多相关Zoomeye的使用方法和文档情操考zoomeye官方 
[ZoomEye API 参考手册](https://www.zoomeye.org/api#parameters)

**Will Do**

- 添加其他的搜索引擎
- 当数量比较庞大的时候引入多线程以及协程相关技术
- 对扫描的数据进行存储
- Celery分布式任务处理

**说明**

如果对您有帮助，您可以点右上角 Star 支持一下 谢谢！
或者您可以follow一下

**免责声明**

本项目只做技术研究，切勿对其他网站和系统进行攻击，违法必究。




