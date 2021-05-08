## wechat-admin

### Background
***
写了一堆背景，后来都删掉了，简单说就是迁移公众号后台到自己的服务器，需求你懂的。


### Usage
***


1. 创建虚拟环境

    * 如果你是用`virtualenvwrapper`管理的运行环境

    ```
    mkvirtualenv wechat
    pip install -r requirements.txt
    ```
    
    * 如果你希望把依赖包安装到global环境(三思啊)

    ```
    sudo pip install -r requirements.txt 
    ```
    
2. 配置

    可以将你的`app_id`及`secret_key`配置到`settings.py`中，为了方便区分开发环境和生产环境，建议把配置项写到`local_settings.py`中，它会覆盖`settings.py`的配置项

    ```
    cp settings.py local_settings.py
    ```

3. 创建数据库

    数据库的配置也是在settings.py或local_settings.py里的，配好以后

    ```
    make initdb
    ```
    这个初始化脚本写的比较简单，可以根据自家的习惯修改

4. 部署

    本地测试直接执行`python app.py`就够了，如果想用其他的web server，可自行考虑部署方案



### TODO

1. UI
2. see those `TODO` comments
