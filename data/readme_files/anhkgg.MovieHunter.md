# 电影下载小工具

电影资源一键下载脚本。

**鉴于不能传播盗版，已屏蔽网站地址，只留下代码**

**仅供娱乐和技术研究，如有任何人用作商业或非法用途，产生任何法律纠纷均于作者无关**

使用方法：

直接使用已经编译好的exe：

```
bin/main.exe 电影名
```

或者自行安装python环境后使用

```
python main.py 电影名
```

依赖：
1. python2.7
2. requests、simplejson

说明：

1. 仅支持电影下载，其他功能可自行增加
2. 视频资源为m3u8，并没有严格遵循其格式解析，仅仅简单解析ts列表，多线程下载ts
3. 所有ts下载完成后，自行合并

具体细节，请看代码，以及注释。


```
pip install requests
pip install simplejson
```

演示：

```
PS D:\> .\main.exe 哈哈哈
[+] Find film url:  https://xxxx.xxx1.com/2019/02/07/xxxx/playlist.m3u8
[+] Start downloading  哈哈哈
[+] Start parse ts list...
[+] Start parse ts list finish.  1332
[+] Start download ts file...
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
[+] pop task Finish.
[+} Task 49 is running.
[+} Task 45 is running.
[+} Task 34 is running.
[+} Task 28 is running.
[+} Task 21 is running.
[+} Task 14 is running.
[+} Task 7 is running.
[+} Task 5 is running.
[+} Task 2 is running.
[+} Task 1 is running.
[+] All task finish.
[+] Download ts file finish
[+] 开始合并...
[+] 完成
```

# 赞我

![img](pay.png)