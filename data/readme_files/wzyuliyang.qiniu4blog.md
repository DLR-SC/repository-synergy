[![](https://img.shields.io/badge/python-2.7.9-blue.svg)](https://pypi.python.org/pypi/qiniu4blog)

#打造自己的图床(qiniu)
#软件介绍
![](http://voyager91.qiniudn.com/2.gif)



#UPDATE
##2015-07-07:
* 支持`qiniu4blog d:/image1.jpg d:/image2.jpg d:/image3.jpg`上传图片
![](http://7qnct6.com1.z0.glb.clouddn.com/2015-07-07_07.jpg)

##2015-07-03:
* 保持目录结构,比如 根目录`/day01/image1.jpg` 上传后为 `http://voyager91.qiniudn.com/day01/image1.jpg`
* 支持子目录文件同步
* 支持中文
* 支持自定义 URL

###流程

> python 监控文件夹 --> 文件新增(FS capture 截图自动保存该目录)
--> 使用 qiniu sdk 上传到 qiniu 云存储 --> 生成外链到粘贴板 --> 复制图片外链到博客

##安装步骤
pip install qiniu4blog

> windows ,Mac os 下 python2.7.9 下验证通过,其它版本还未测试


##配置

登录[https://portal.qiniu.com/](https://portal.qiniu.com/)
新建一个**bucket**,获取以下相关信息`bucket` , `accessKey` ,`secretKey`, 

![](http://voyager91.qiniudn.com/2015-04-16_00001.jpg)

*增加自定义url  在`custom_url`里设置*
![](http://voyager91.qiniudn.com/2015-04-22_%E4%B8%AD%E6%96%8700008.jpg)


在home目录下新建配置文件`qiniu.cfg` 例如`C:\Users\leeyoung\qiniu.cfg`
`path_to_watch` 为截图自动保存的目录
`qiniu.cfg`内容如下
```
[config]
bucket = your-bucket-name
accessKey = qzA***********************sa
secretKey = P5G***********************wq
path_to_watch = D:\install\qiniu\uploadimage2qiniu

[custom_url]
enable = false 或者 true
addr = http://7qnct6.com1.z0.glb.clouddn.com/

```

> mac 系统设置截图自动保存文件夹

```
defaults write com.apple.screencapture location /Users/leeyoung/Desktop/up2qiniu
killall SystemUIServer
```

##运行

###监听模式
打开终端或cmd
```
qiniu4blog  #将会监听path_to_watch内的文件变动，上传图片
```
###命令行模式
```
qiniu4blog d:/image1.jpg d:/image2.jpg d:/image3.jpg  #指定上传多个文件
```

##相关下载
* [FastStone Capture.rar](http://pan.baidu.com/s/1o6mjrmi)

> 设置自动保存路径 settings -> Auto Save -> Output folder
