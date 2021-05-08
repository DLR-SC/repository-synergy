Feather
=======
## 简介
A Community Web App like [V2EX](http://www.v2ex.com).

一个模仿 [V2EX](http://www.v2ex.com) 的 Web 程序，用 [Flask](http://flask.pocoo.org) 这个微框架写成。

<http://feather.im> 的源代码。

第一个 Web App，很简陋，望各位高手指点。

## 安装插件

- flask-sqlalchemy
- flask-markdown
- flask-script
- flask-cache
- python-memcached

## 配置

### 数据库信息

修改 feather/config.py 文件：

- _DBUSER = "" # 数据库用户名
- _DBPASS = "" # 数据库密码
- _DBHOST = "localhost" # 数据库服务器 默认 localhost
- _DBNAME = "feather" # 数据库名称 默认 feather

### 数据库选择

修改 feather/__init__.py 文件：

- app.config.from_object('feather.config.DevConfig') # SQLite
- app.config.from_object('feather.config.ProConfig') # MySQL

用 # 注销其一

## 运行

### 初始化数据库

- python run.py createall

### 启动

- python run.py runserver

### 运行
- 于浏览器中打开：http://127.0.0.1:8888
