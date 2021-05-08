# green

## 说明

本仓库是微信公众号 **Ms_haoqi** 的源代码，基于[wechat-python-sdk](https://github.com/wechat-python-sdk/wechat-python-sdk)和[Tornado](https://github.com/tornadoweb/tornado)，使用图灵机器人API回复用户的消息，可以与用户进行中文对话。

扫码查看公众号：

![二维码](http://img.blog.csdn.net/20160419140351193)

更多介绍可以参考博客 [Python快速搭建自动回复微信公众号](http://blog.csdn.net/tobacco5648/article/details/51190039)。

## 依赖

```shell
pip install -r  requirements.txt
```

## 使用配置

需要在根目录下添加```conf.json```文件，内容为：

```json
{
	"token": "your_weixin_token",
	"appid": "your_weixin_appid",
	"secret": "your_weixin_appsecret",
	"mode": "normal",

	"mongo_db": "green",

	"max_host_count": 5,

	"auto_reply": "yes",
	"tuling_key": "1d2679920f734bc0a23734ace8aec5b1",
    "tuling_url": "http://www.tuling123.com/openapi/api",

    "type": "subscribe"
}
```

其中需要修改的参数有：

- ```token``` : 修改为微信公众号的Token(令牌)
- ```appid``` : 修改为微信公众号的AppID(应用ID)
- ```secret``` : 修改为微信公众号的AppSecret(应用密钥)
- ```tuling_key``` : 修改为申请的图灵API KEY

另外需要本地安装有MongoDB

## 注意事项

### 端口

微信公众号只能设置在80端口，因此 **green** 默认运行在80端口，如果自己配置端口转发，希望 **green** 运行在其他端口，可以修改 ```config.py``` 文件中 ```settings``` 中的 ```port``` 字段。

### 服务器url

**green** 的默认配置会将所有请求路由到 ```http://ip:port/wx``` ，如果希望修改此路由，可以在 ```config.py``` 文件中 修改路由表 ```web_handlers``` 。

### 图灵key

默认的图灵key不能使用，需要自己去 [图灵机器人官网](http://www.tuling123.com/) 申请自己的图灵key， 再填写到 ```conf.json``` 对应字段下。
