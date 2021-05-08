基于容器化的CI/CD及自动化运维管理平台,由于定制化开发的原因，使用sso方式登录验证、平台配置文件及依赖底层数据源众多,适合具有python二次开发能力的运维爱好者.

项目demo地址(因数据源不全，部分页面无法展示):http://122.51.190.191  登陆账号:guest 密码:guest

别忘了给个star^_^

# 开发语言与环境依赖 #
  - 编程语言：Python3.6 + HTML + JQuery
  - 前端Web框架：Bootstrap4
  - 前端图表框架：Pycharts + Datatables
  - 后端Web框架：Flask1.0+
  - 后端Task框架：apscheduler
  - 后端数据库：Mysql + Influxdb + Redis
  - 后端日志源：ElasticSearch
  - 监控数据源：zabbix
  - 后端代码库：gitlab
  - 容器化平台：Kubernetes + Docker + Harbor
  - 后端编译：jenkins
  - 登录鉴权：cas
  - 操作系统：CentOS 7+
  - Ansible版本：2.6+
  - web运行：Nginx + Gunicron
# 组织框架 #
    sparrow
    ├── api     #api接口
    │   ├── ajax_api.py
    │   ├── assets_query.py
    │   ├── __init__.py
    │   ├── k8s_project_update.py
    ├── conf    #配置文件夹
    ├── conf.py       #全局配置
    ├── index.py      #主页面
    ├── login.py      #登录页面
    ├── logout.py     #注销接口
    ├── main.py       #网站入口
    ├── module        #功能模块
    │   ├── db_idc.py
    │   ├── db_op.py
    │   ├── __init__.py
    │   ├── ip_adress.py
    │   ├── k8s_resource.py
    │   ├── loging.py
    │   ├── Md5.py
    │   ├── MyForm.py
    │   ├── Mysql.py
    │   ├── produce.py
    │   ├── SSH.py
    │   ├── Task2.py
    │   ├── task_publish.py
    │   ├── Task.py
    │   ├── tools.py
    │   └── user_auth.py
    ├── operation    #管理模块
    │   ├── assets_manage.py
    │   ├── examine.py
    │   ├── __init__.py
    │   └── resource_pool.py
    ├── sso_cas      #sso单点登录模块
    ├── static       #静态目录
    │   ├── css
    │   ├── doc
    │   ├── font
    │   ├── images
    │   ├── js
    │   └── webfonts
    ├── templates   #页面模版
    └── views       #页面视图
        ├── approval.py
        ├── app_service.py
        ├── Assets.py
        ├── business_m.py
        ├── business.py
        ├── chart_center.py
        ├── deploy.py
        ├── influxdb_m.py
        ├── __init__.py
        ├── k8s_deploy.py
        ├── k8s_manage.py
        ├── k8s.py
        ├── publish.py
        ├── report.py
        ├── sch_list.py
        └── work_order.py
# 主要功能： #
    - 全新架构优化调整
    - 由sso单点登录系统进行统一鉴权
    - 标准CMDB资产管理
    - 代码上线，包含上线、灰度、回滚等功能并实时显示执行过程 
    - 基于git、jenkins、harbor、k8s容器化实现的CI\CD流水作业 
    - k8s多集群统一UI管理及容器环境部署、代码更新
    - 自动服务器资产、应用服务的信息及关联关系抓取及资产、资源的生命周期管理
    - 生产服务资源例如mysql、redis、kafka等信息汇总查询
    - WEBSSH登录
    - 实时大数据分析包含线上业务的并发量、流量、响应时间、业务访问占比、用户地区分布等
    - 安全审查包括登录鉴权记录、用户操作记录、访问记录
    - 业务运行关键指标报警、监控报警故障自动处理
    - 访问限速、访问黑名单、用户单点登录限制等安全措施
    - 页面级别用户权限控制
    - 通过分布式全局锁,进程锁,实现多机多进程部署后台单任务运行
    — 新增工单系统、工单统计报表功能    
# 界面展示
![show](https://github.com/wylok/opsweb/blob/master/static/images/01.jpg)
# 资产管理
![show](https://github.com/wylok/opsweb/blob/master/static/images/02.jpg)
# K8s管理
![show](https://github.com/wylok/opsweb/blob/master/static/images/6.jpg)
![show](https://github.com/wylok/opsweb/blob/master/static/images/7.jpg)
![show](https://github.com/wylok/opsweb/blob/master/static/images/03.jpg)
# 工单系统
![show](https://github.com/wylok/opsweb/blob/master/static/images/4.jpg)
![show](https://github.com/wylok/opsweb/blob/master/static/images/5.jpg)
# 日志分析及监控报警
![show](https://github.com/wylok/opsweb/blob/master/static/images/8.jpg)
![show](https://github.com/wylok/opsweb/blob/master/static/images/9.jpg)
# 问题解答： #
    - 关于sql配置文件格式问题，请参考下面示例：
      SQLALCHEMY_BINDS = {'库名': 'mysql://用户名:密码@IP地址:端口/库名?charset=utf8'}
      SQLALCHEMY_ECHO = False
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      MYSQL_USER = ''
      MYSQL_PASSWORD = ''
      MYSQL_HOST = ''
      MYSQL_PORT = 
      INFLUXDB_HOST = ''
      INFLUXDB_PORT = 
      INFLUXDB_USER = ''
      INFLUXDB_PASSWORD = ''
      INFLUXDB_DB = ''
    - 关于启动报Failed to find Flask application or factory in module ‘opweb.conf’报错问题,在最新的版本中已经修复。
author:wylok@126.com
