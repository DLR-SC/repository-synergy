QRobot
======

全新优化的微博机器人，Python语言编写，可用于树莓派。

功能：

	每小时发一条密友微博，用于监控运行状态
	每天发几条普通微博
	当有新`@我的微博`的微博的时候，给他一个评论，也可回复评论


运行本项目需要： 
   
* 安装weibo的 [Python SDK](http://github.liaoxuefeng.com/sinaweibopy/)
* 在config文件夹下新建一个myConfig.py文件


myConfig.py文件内容如下

	APP_KEY = '225488****'
	APP_SECRET = '3bd49f5d***********'  
	CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
	CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
	USERID = '****登陆邮箱'
	PASSWD = '****密码'
	
[微博演示帐号](http://weibo.com/u/3798238610) （服务器不常开）
