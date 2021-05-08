# RasWxMusicbox
# 树莓派-微信音乐播放器
----

## ！！重要：2017.3.5日更新

[请点击这里使用最新版本的 RasWxNeteaseMusic](https://github.com/yaphone/RasWxNeteaseMusic)。

该版本功能较简单，年假期间对RasWxMusicbox进行了一些新功能的扩展，比如支持登陆个人的网易云音乐账号，支持播放自己收藏的歌单等等，具体功能包括：

- H: 帮助信息
- L: 登陆网易云音乐
- U: 用户歌单
- M: 播放列表
- N: 下一曲
- R: 正在播放
- S: 歌曲搜索
- T: 热门单曲
- E: 退出

[请点击这里使用最新版本的 RasWxNeteaseMusic](https://github.com/yaphone/RasWxNeteaseMusic)。

----

树莓派微信音乐播放器，使用网易云音乐API，基于[itchat微信框架](https://github.com/littlecodersh/ItChat)。

##演示视频：

[猛戳这里。](http://v.youku.com/v_show/id_XMTYwMDkzOTk4MA==.html#paction)

##使用方法

1.安装依赖包： 

	sudo apt-get install python-imaging
	sudo apt-get install pillow
	sudo apt-get install mpg123

2.切换到文件目录，执行`python run.py`

3.扫码登陆。

4.发送 `歌曲名` 进行查询，将返回音乐列表，如 `南山南`。

5.发送 `歌曲名 序号` 进行播放，如 `南山南 29`，这里注意歌曲名与数字之间有空格 。


##BUG

1.部分音乐失效，系网易云音乐问题，所以有可能播放失败。

2.有些微信号可能收不到自己向自己发送的信息，就需要通过别的微信号向扫码登陆的微信号发送消息。itchat是网页版登陆微信的，所以手机退出微信后itchat也会LOG OUT，可以先断开网络再退出账号，就可以避免itchat同时LOG OUT的问题，具体方式可百度。


