# 关于
本项目主体是一个用Python写的面向web微信的小程序，该程序能指定微信联系人在电脑端的命令行窗口发送消息，有以下几个功能：
 
* 支持定时发送，再也不用担心错过xxx的零点祝福；
* 群发无上限，再也不用因为群发助手限制200人而点到手酸；
* 群发可以在消息前面加名字（或者你想要的联系人信息作为前缀），让人看不出是群发，对方再也没有理由说“群发短信我不回”；
* 你也可以修改程序，定制自己想要的发送功能（例如自动回复之类的），我也能参与到开源项目中.

参考程序：https://github.com/0x5e/wechat-deleted-friends
，在源程序基础上进行了改动及添加了功能，感谢作者的无私分享。
对原程序进行了改动，用的是Python3.5的库，额外定义了sendMsg和sendInterface函数，并去除了建群、加好友、删除好友等与发送无关函数。程序是在那个大神的基础上实现的，登陆、认证、获取联系人等他都完成了，因此我少做了很多工作。

定时发送功能是给每个sendMsg加time.sleep()实现的，同时利用了多线程，因此可以设置发送延时让程序在后台自己执行发送线程，而且多个发送线程彼此不冲突。至于接收消息，主要是接收机制对于我这个渣渣太难了，要有同步信息synckey，特别麻烦，就不弄了，如果有哪个大神能弄懂欢迎交流。想想如果能在cmd上愉快滴聊微信，也是很逗的事情哈哈。

# 程序怎么运行
如果你电脑上有Python3.0或以上以上的库，那么下载wxsendmsg.py文件后，在wxsendmsg.py的当前目录下运行命令行窗口（cmd）并执行命令Python wxsendmsg.py即可；
 
如果你的Windows系统没有安装Python3.0或以上的环境，想要直接运行，请通过网盘链接下载exe版本http://pan.baidu.com/s/1jHq0E82 由于压缩包里面含有exe程序，下载时浏览器会报有安全隐患，无视就好。

# 隐私&免责声明
本程序所需要的扫描二维码登录微信操作，是登录web微信的必须步骤。相信我，这个程序就是在你电脑上登录微信而已，对微信的控制权完全在你手上。如果这样我就能盗你微信，那腾讯可以大概可以倒闭了。
 
由于本程序是开源的，真的不放心的话可以查看源码，很短，就几百行。
 
特别说明：本程序仅供娱乐，对于任何因滥用程序造成的后果，使用者自行承担责任。

# 联系方式
你可以通过邮箱跟我联系luorunwen@qq.com