## 妹子说，自动从其他网站采集妹子图，并上传微博图床，然后发布至wordpress脚本

**脚本较长时间没有更新，可能已经失效，请自行检查**
 


接爬虫、web开发单：
1. 比如需要爬其他美女图站
2. 有其他需求：比如：需要批量下载懒人听书的音频、批量从贴吧获取邮箱等
3. 接web开发：比如需要仿站等


----

## 脚本介绍

1. uploader.py 上传图片至图床脚本。
    - **第28行**修改微博账号和密码
    - **第191行**填写flickr的api key和secret，申请api地址：https://www.flickr.com/services/apps/create/apply/
2. wp_db.py wordpress发布脚本。需在脚本**第26行**修改自己的wordpress网址、admin账号密码
3. ocr.py 接入第三方打码平台脚本，实现**微博自动登录**。 需自行注册[云打码](http://yundama.com)，然后在脚本**第10、11行**修改云打码的用户名密码
4. mm131.py 爬虫脚本；可以参考该脚本自行写爬虫入库
5. localdb.py 数据库操作脚本
6. auto_post.py 图片上传&wordpress发布脚本
7. weibo.py 采集微博图片的脚本

----

## 用法

0. 安装依赖包：`pip install -r requirement.txt`
1. 采集数据
    - 首先需要运行爬虫脚本，从其他网站爬取数据：`python mm131.py`
    - 采集微博图片：首先编辑`wblist.txt`，一行一个微博博主名字，然后运行：`python weibo.py`
2. 图床选择：修改`auto_post.py`脚本修改**第9行**，修改**tc**参数，可选：`flickr`:**flickr图床**,`weibo`:**微博图床**
    - 如果用**微博图床**，则按照上面的脚本介绍设置了就行
    - 如果用**flickr**图床，在uploader设置了api_key和api_secret之后，第一次运行`python auto_post.py`会让你用浏览器打开一个网址，然后获取token
2. 然后直接运行`auto_post.py`脚本，开始发布：`python auto_post.py`

    - **确保你的wordpress的服务器MySQL可远程连接并开放了3306端口**

就是这么简单


----

