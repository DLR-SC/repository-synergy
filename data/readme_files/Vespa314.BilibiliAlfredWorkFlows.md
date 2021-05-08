## B站搜索
~~介绍可以参见[博客](http://www.kylen314.com/archives/6670)~~

关键字：`bl` (喂，`bl`是`b`i`l`i的简写啊！)

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bl1.png)

如按下文配置好[biligrab-danmaku2ass](https://github.com/m13253/biligrab-danmaku2ass)及[you-get](https://github.com/soimort/you-get)，选中搜索结果中的视频：
* 回车直接在默认浏览器中打开视频
* 按住`cmd`然后回车即可使用mpv本地播放视频
* 按住`ctrl`再回车可以查看高清视频；【因为macbook观看弹幕视频发热太过严重，这个方法不仅可以有效解决这个问题，并且新番可以**跳广告**！！】
* 按住`alt`再回车可以下载视频【如果可以的话】；

11/07更新：
按住`shift`可以下载弹幕文件到桌面
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bl2.gif)


~~## B站新番 Version 1 【已废弃】~~
~~介绍可以参见[博客](http://www.kylen314.com/archives/6670)~~

关键字：`bgm`

食用方法：
* 直接输入`bgm`可以查看最近更新的二次元新番
* 后面加`t`可以查看今天会更新的新番
* 输入`wn`可以查看`周n`更新的视频，比如`bgm w3`就是查看周三更新的视频
* 前面的各种命令前面加个`3`可以查看三次元新番

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm1.png)
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm2.png)
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm3.png)
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm4.png)

> 比较讨厌的有两点，一是这些更新顺序我代码中明明是按更新时间顺序输出的，但是显示出来却不全是，貌似跟你最近点击有关。。
>还有一点，获取到的新番信息里面包含封面的URL的，但是好像Alfred列表的每个选项前面的图标只能是本地icon，不然不显示。。
 
## B站新番 Version 2
由于上一个命令只能打开新番搜索页面，然后试图对选中的新番直接打开所在URL，但是无奈Alfred设计上的问题，无法直接选中新番然后像之前别的方法一般按着`cmd`就可以直接本地播放，于是暂时采用了一个迂回的方法：

**输入命令`bgm`，然后选中新番，回车！！将会把本地播放的命令(也就是`bili —hd http://www.bilibili.com/video/avxxxxx`)复制到剪贴板，然后打开终端ctrl+V运行即可。（当然的，你需要按照本文末尾方法配制播放环境！！）**

演示：
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm5.gif)

> 忘了什么时候更新的功能，选中之后`cmd`+回车，会把url(http://www.bilibili.com/video/avxxxxx )复制到剪贴板，使用[这个脚本](https://github.com/Vespa314/bilibili-api/tree/master/GetVedioUrl) 获取视频下载url，就可以直接扔迅雷下载了。。【唉，虽然现在版权越来越严。。】或者使用[弹幕下载的alfred](https://github.com/Vespa314/BilibiliAlfredWorkFlows/tree/master/GetAssFromBilibili)或者[脚本](https://github.com/Vespa314/bilibili-api/tree/master/GetDanmuAss)直接下载弹幕文件到本地【这样就可以在高铁上离线弹幕了！！】

演示：
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bgm6.gif)


## B站排行
~~介绍可以参见[博客](http://www.kylen314.com/archives/6670)~~

关键字：`bhot`

食用方法：
* 查看热门视频只要输入`bhot`即可[默认返回的是`全站`   `3天`内`除了新番区`以外`点击量`最高的`20`个视频；]
* 选择分区，后面加上：
	*  动画区:`dh`
	* 音乐舞蹈区:`yy`
	* 游戏区:`yx`
	* 娱乐区:`yl`
	* 科学与技术:`kj`
* 设置天数范围只要加个`dx`就可以返回`x天`内排名最高的；
* 排名方式默认点击量，也可以选择:
	* 按弹幕数排:`dm`
	* 收藏数:`sc`
	* 评论数:`pl`
	* 硬币数:`yb`

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bhot1.png)

> 举个例子，你想查看`60天`内`音乐区` `硬币数`最高的视频：那么输入`bhot d60ybyy`【参数顺序随便写，比如`bhot ybyyd60`也可以】

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bhot2.png)

如按下文配置好[biligrab-danmaku2ass](https://github.com/m13253/biligrab-danmaku2ass)及[you-get](https://github.com/soimort/you-get)，选中搜索结果中的视频：
* 回车直接在默认浏览器中打开视频
* 按住`cmd`然后回车即可使用mpv本地播放视频
* 按住`ctrl`再回车可以查看高清视频；【因为macbook观看弹幕视频发热太过严重，这个方法不仅可以有效解决这个问题，并且新番可以**跳广告**！！】
* 按住`alt`再回车可以下载视频【如果可以的话】；

演示：
![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/bhot3.gif)

## 获取弹幕ASS文件以供本地播放
关键字:`danmu`

使用方法：
danmu加上视频URL地址即可，比如：
* danmu http://www.bilibili.com/video/av510515/index_3.html
* danmu http://www.bilibili.com/video/av1687261/

然后转换成功的话可以获得ASS文件，请到桌面查找

> 有些时候一些新番的的弹幕需要登录才可以获取，这里没有实现。。。也不会去实现。。

## 获取视频下载url
关键字:`url`

食用方法：
url加上视频URL地址即可，比如：
* url http://www.bilibili.com/video/av1687261/

选中后会自动将将url复制到剪贴板，可以直接打开迅雷粘贴即可！！

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/url1.png)

> 注：如果出现多个下载url，最好不要使用这个方法，而采用you-get之类的会自动合并多个短视频的脚本。

## 转化xml弹幕文件为ass文件
关键字:`xml2ass`

食用方法：
直接xml2ass，会读取桌面xml文件供你选择，选中即转化为同名ass文件，拖入播放器即可。

![image](https://github.com/Vespa314/BilibiliAlfredWorkFlows/raw/master/img/xml2ass.png)

> 问题一：有了danmu这个Alfred为什么还要写这个？因为B站封appkey，danmu必须借助appkey+av号获取到视频的cid，才可以自动获取到xml文件，现在没有appkey的用户自然获取不到xml文件。
> 问题二：那么如何获取xml文件呢？请使用[bilibili-mac-client](https://github.com/typcn/bilibili-mac-client)
> 问题三：请问有了[bilibili-mac-client](https://github.com/typcn/bilibili-mac-client)，要你这个Alfred何用？额。。假设你能容忍暗牧的存在的话，或者B站有些视频低画质之类的。。。这个是没什么用。。

## 配合使用的系统设置
首先完成以下三项配置：
* [you-get](https://github.com/soimort/you-get)
* [biligrab-danmaku2ass](https://github.com/m13253/biligrab-danmaku2ass)
* [danmaku2ass](https://github.com/m13253/danmaku2ass)

目标：
* 可以使用`you-get http://www.bilibili.com/video/avXXXX`下载B站视频
* 假设cd到[biligrab-danmaku2ass](https://github.com/m13253/biligrab-danmaku2ass)所放的路径，可以使用`./bilidan.py http://www.bilibili.com/video/avXXX/`在MPV中本地播放视频

然后：
在'\usr\bin'中建立一个名为`bili`的文本文件，内容如下：
```
#!/bin/bash
xxxxxxx/bilidan.py $@
```
其中前面`xxxxxxx`表示`bilidan.py`路径，然后添加执行权限`sudo chmod +x bili`后便可以随时随地在任意路径下终端使用`bili http://www.bilibili.com/video/avXXX/`播放视频了！！
当然你也可以设置默认配置，比如弹幕透明度：
```
#!/bin/bash
~/danmaku2ass/bilidan.py --d2aflags 'text_opacity=0.5' $@
```
完成以上配置即可！！