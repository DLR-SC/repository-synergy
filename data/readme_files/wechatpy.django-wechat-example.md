# django-wechat-example

本项目使用django、celery、wechatpy开发微信公众号第三方平台的demo。


操作说明
-----------
1. 假设第三方平台有如下配置

    - 登录授权的发起页域名    somewebsite.cn
    - 授权事件接收URL  http://www.somewebsite.cn/wechat/callback
    - 公众号消息与事件接收URL    http://www.somewebsite.cn/wechat/server/$APPID$
    - 网页开发域名    www.somewebsite.cn

2. 修改 demo/settings.py
    - COMPONENT_APP_ID = 'app_id'
    - COMPONENT_APP_SECRET = '0c79eferferfeferf0cc0be99b20a18faeb'
    - COMPONENT_APP_TOKEN = 'srgewgegerferf'
    - COMPONENT_ENCODINGAESKEY = 'bz5LSXhcaIBIBKJWZpk2tRl4fiBVbfPN5VlYgwXKTwp'
    - AUTH_REDIRECT_URI = 'http://www.somewebsite.cn/wechat'

3. 初始化Django项目
    - python manage.py makemigrations
    - python manage.py migrate
    - \# 在 www.somewebsite.com主机上运行开发服务器
    - sudo python manage.py runserver 0.0.0.0:80

4. 打开浏览器测试一下
    - 打开http://www.somewebsite.cn/wechat/auth，获得预授权链接
    - 点击预授权链接，页面跳转到微信授权页面
    - 用微信扫描页面上的二维码
    - 在手机上选择要授权的公众号
    - 授权成功，浏览器跳转到http://www.somewebsite.cn/wechat
    - 授权过程完成

5. 开始写自己的逻辑


开发说明
--------

1. component和所有公众号的token信息会自动放入`caches['wechat']`中。要获取`component`对象，使用`wechat.utils.get_component`即可。
2. 授权成功后，微信服务器会调用`AUTH_REDIRECT_URI`,将授权码带过来，`AUTH_REDIRECT_URI`会获得公众号的信息，并保存到Wechat模型中。
3. 需要启动celery定时任务，以保证已授权的公众号的token不会失效。
