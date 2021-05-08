KortURL
=======
[![Support Python Version](http://img.shields.io/badge/Python-3.5|3.6|3.7|3.8-brightgreen.svg?style=flat-square)](https://www.python.org/)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)

One-stop short url service.一站式的短网址服务,提供浏览器端及API两种方式缩短网址,以及可视化的流量追踪。


## [项目介绍](#项目介绍)
One-stop short url service.一站式的短网址服务,提供浏览器端及API两种方式缩短网址,以及可视化的流量追踪。欢迎Issue & PR!

本项目为自带分析统计的短网址服务，提供浏览器端长网址的缩短，还原，以及批量缩短网址API。
同时有账号系统，匿名用户只能访问短网址然后跳转。


目前统计的维度:
* 每日访问量
* 24小时访问趋势
* 访问设备
* 访客操作系统
* 浏览器
* 运营商
* 国内访问分布


<table>
    <tr>
        <td ><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/395e33ab103b29e8.png' /></center></td>
        <td ><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/e616f2064dbc8d99.png' /></center></td>
        <td ><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/040e2925f863b092.png' /></center></td>
    </tr>
    <tr>
        <td><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/41b20aa70ca7339e.png' /></center></td>
        <td ><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/b19827665cbd3e2c.png' /></center></td>
        <td><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/dc6534cd50bfc812.png' /></center></td>
    </tr>
    <tr>
        <td><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/2166bcdc4e50c809.png' /></center></td>
        <td><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/9fb337622707f9b5.png' /></center></td>
        <td><center><img src = 'https://ftp.bmp.ovh/imgs/2019/12/10d418bd1ea11459.png' /></center></td>  
    </tr>
</table>

## [部署(以Ubuntu16.04为例)](#)
```text
pip3 install pipenv
```
在项目根目录下:
```text
pipenv install
```
#### [redis安装](#)
```text
sudo apt-get update
sudo apt-get install redis-server
```
> 安装后配置文件在`/etc/redis/redis.conf`。

#### [数据库](#)
Django ORM支持的数据库，推荐`mysql`。

以mysql为例:
```text
sudo apt-get install python3-dev
sudo apt-get install libmysqld-dev
pipenv install mysqlclient
```


#### [参数设置](#)
配置文件位于KortURL/settings.py

API身份验证模块:
* SIMPLE_JWT.ACCESS_TOKEN_LIFETIME: 令牌过期时间。默认5分钟。
* SIMPLE_JWT.REFRESH_TOKEN_LIFETIME: 刷新令牌过期时间。默认24小时。
* SIMPLE_JWT.AUTH_HEADER_TYPES: API身份验证时请求头的认证类型。默认`KortURL`。

Redis相关设置:
* REDIS_HOST: Redis的ip地址。
* REDIS_PORT: Redis的端口。
* REDIS_PASSWORD: Redis的密码。如果没有设置密码，则赋值`None`。
* MAP_CACHE_DB: 缓存长短网址键值对的Redis数据库(如果没有修改过redis配置，可选值有0-15)。
* BROKER_DB: Celery broker 使用的Redis数据库。
* RESULT_DB: Celery 任务执行结果存储Redis数据库。
> `MAP_CACHE_DB`, `BROKER_DB`, `RESULT_DB`不要设置为相同的数据库。

Celery相关设置:

这里如果你的服务器的Redis是有密码的。则注释掉无密码的两行，使用下面的两行。

KortURL 设置:
* KORT_URL.PROTOCOL: 你的服务协议。有`HTTP`和`HTTPS`两种选择，默认`HTTPS`。
* KORT_URL.SERVER_NAME: 域名。即nginx配置里的`server_name`。必须正确填写，默认是`localhost:8000`，会导致短网址无法正确跳转。
* KORT_URL.SITE_NAME: 站名。默认`KortURL`。将会显示在页面上的导航栏。
* KORT_URL.COMPANY_NAME: 企业名称。默认`KortURL`。将会显示在页面的footer。
* KORT_URL.BACKGROUND_COLOR: 页面背景色。如果你不喜欢默认的背景色。那尽管修改它!
* KORT_URL.IP_RATE: 限制每个ip的访问频率，可选周期有`day`, `hour`, `min`, `sec`，默认`3/sec`，即每个ip每秒最多3次。

> 如果有需要，可将static/imgs中的`favicon.ico`和`logo.png`替换为自己想要的。文件名保持一致即可。

#### [迁移](#)
以上参数设置完毕后:
```text
pipenv run python manage.py makemigrations

pipenv run python manage.py migrate

```

#### [生产环境下的部署](#)
原本这里是一些自己写的生产环境部署的内容，后来想了想，文档还是官方的好，所以就只附链接了:

[使用uWSGI和nginx来设置Django和你的web服务器](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/tutorials/Django_and_nginx.html)

[部署django-django官方文档](https://docs.djangoproject.com/zh-hans/3.0/howto/deployment/)


#### [一些常用命令](#)
运行celery命令: 

    pipenv run nohup celery -A KortURL worker -l info --logfile logs/celery.log &

uwsgi(如果是虚拟环境级别的uwsgi, 在命令前加上pipenv run):
* 启动
```text
uwsgi --ini 你的uwsgi配置文件名(.ini格式)
```

* 停止
```text
uwsgi --stop uwsgi.pid
```

* 重新加载
```text
uwsgi --reload uwsgi.pid
```
