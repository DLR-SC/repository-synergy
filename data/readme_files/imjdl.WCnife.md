## ![](http://ovjdtotu0.bkt.clouddn.com/WCnifelogo.png?nocache2650=1533351196368)

## ![](https://img.shields.io/badge/WCnife-%E5%BC%80%E5%8F%91%E4%B8%AD-blue.svg?nocache2650=1533347576833) ![](https://img.shields.io/badge/author-elloit-yellow.svg?nocache2650=1533347614582) ![](https://img.shields.io/badge/progress-100%25-red.svg?nocache2650=1533347786458) ![](https://img.shields.io/badge/version-1.0.0_Alpha-black.svg?nocache2650=1533347920866)

WCnife 是对中国菜刀抓包分析后，写成的WEB应用，可以连接php一句话木马，对目标进行目录遍历、文件下载、文件上传、文件删除和重命名文件等操作。

目前处于开发状态。

### Progress

*   上传文件(100%)
*   目录遍历(100%)
*   下载文件(100%)
*   删除文件(100%)
*   新建文件(100%)
*   新建文件夹(100%)
*   重命名(100%)
*   虚拟终端(100%)

## Development log

*   7-31: 父目录遍历完成, 异常信息没有处理
*   8-1: 子目录遍历以及文件下载完成，异常信息没有处理
*   8-2: 删除操作完成，发现中文显示为None，异常信息没有处理
*   8-4 上传操作完成，重命名操作完成，重命名文件和文件夹完成
*   8-5 虚拟终端完成

## Requirements

1.  直接利用venv中的虚拟环境: source venv/bin/activate
2.  也可以自己安装python环境：pip install -r requerments.txt

## Installation

1.  git clone git@github.com:imjdl/WCnife.git
2.  pip install -r requerments.txt 
3.  python manage.py runserver 8080
4.  浏览器访问 [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

### 虚拟终端的使用

虚拟终端并没有建在WEB页面，而是放在了命令行中

执行 python manage.py 可以看到nifeshell选项

![](http://ovjdtotu0.bkt.clouddn.com/032.png?nocache2650=1533443999206)

在后面添加 -url -pwd 参数 指定木马的链接和密码，进行连接

![](http://ovjdtotu0.bkt.clouddn.com/123.png?nocache2650=1533444187302)

#### WIndows

![](http://ovjdtotu0.bkt.clouddn.com/34.png?nocache2650=1533444078833)

#### Linux

![](http://ovjdtotu0.bkt.clouddn.com/35.png?nocache2650=1533444104234)

### Screenshot

![](http://ovjdtotu0.bkt.clouddn.com/dmeo1.png?nocache2650=1533370659404)

![](http://ovjdtotu0.bkt.clouddn.com/demo2.png?nocache2650=1533370684313)
