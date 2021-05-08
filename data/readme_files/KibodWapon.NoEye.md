# NoEye
## update 2019-6-2 Flask，WEB服务更加稳定，不会因为高并发死锁。
Flask版dnsandwebFlask.py 需要如下命令安装Flask开发框架  ：

```shell
pip install Flask
```

https://github.com/KibodWapon/simpleeye



## update 2017-12-7：
本仓库是研究性质，新写一个简便易用的项目，单个脚本文件实现dns和web服务的oob利用平台（ a all in one script  oob exploit web  platform），无需繁琐的mysql和php环境，一键启动。地址如下：

https://github.com/KibodWapon/simpleeye

## update 2016-03-16:

修复之前的程序错误:

  - db.sql与程序逻辑对不上

  - noeye.php 66行 mysql_real_escape_string修改成addslashes函数对输入数据处理。

## How to use?
> http://localhost/noeye.php?uk=md5(userkey)

Original readme:
	
	A blind exploit tool( a dns server and a web app) that like wvs's AcuMonitor Service or burpsuite's collabrator or cloudeye!

	Send me any bug to cmdbat#126.com
