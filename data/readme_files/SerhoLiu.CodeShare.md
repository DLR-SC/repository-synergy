这个是一个运行在SAE（Sina App Engine）上，基于Tornado的简单的代码分享网站。见：http://tocode.sinaapp.com

## 使用方法

> 1. 在 SAE 上新建 Python 应用，在`setting.py`中设置站点名，修改后上传
> 2. 开启MySQL服务，进入数据库，导入db.sql
> 3. 打开 http://youapp.sinaapp.com/admin/start 输入你的管理员帐号（为了安全，建议初始化后删除urls.py文件中的对应网址）

## 一些特征

用户可以自由发布代码，拥有一个自己设定的密码，用于修改和删除自己的代码，管理员可以删除代码，如果要修改只能去数据库修改。

## License

See MIT-LICENSE.txt