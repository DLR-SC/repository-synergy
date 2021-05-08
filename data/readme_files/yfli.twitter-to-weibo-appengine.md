同步twitter到新浪微博
====================

部署在Google Appengine上，自动同步twitter到新浪微博。可以同步图片，包括Twitter自身图床及instagram等主流图床。被同步的微博账号需要开通开发者账号并创建一个未审核应用。

安装部署
---

下载本项目代码。

安装步骤:

* 申请一个Twitter API https://dev.twitter.com/, Callback URL为 http://'youappid'.appspot.com/oauth/callback. 更改myid.py中的CONSUMER_KEY, CONSUMER_SECRET及CALLBACK值
* 上传代码到你的appengine
* 用浏览器访问http://yourappid.appspot.com/ ,按指示操作
* Done


示例
---

[http://twitter8weibo.appspot.com](http://twitter8weibo.appspot.com)

License
-------
[GPLv3][gplv3]

参考
----
本项目参考/使用了以下项目

* http://code.google.com/p/twitter-feed/
* https://github.com/michaelliao/sinaweibopy
* http://code.google.com/p/twitter2weiboviagtalk/

联系
----

* [yfli](https://twitter.com/yfli)@twitter
* [warehou](http://www.weibo.com/u/1410749162)@微博

Changelog
---------

- master 20140-7-11

    Remove old master branch, as Sina remove gtalk bot support in April

- app_br ver 1.0 2013-4-16

    Incorporate many changes in master branch    
    Use non-audit app to send message to sina

- ver 1.1 2013/3/24

    Upgrade to python 2.7   
    Fix bug: support multiline message

- ver 1.0 2013/3/20

    Major release. No need to deploy app for yourself, but use App setup by others.  
    No need to change twitter or weibo id in code. Directly binding gtalk on webpage.    
    Use gtalk bot to sync. Made a mistake that thought gtalk was removed from sina while it is still available.    
    Tiny.cc is blocked by sina since 3/14, change to another short url

- ver 0.4 2013/1/20

    Add Twitter OAuth for account
    Fallback to App login for weibo, as Weibo disabled gtalk bot

- ver 0.29 2012/7/31

     Enmergency update. Sina blocked Basic Auth since 7/24. Use gtalk robot instead.

- ver 0.2 2012/7/17

    Support image sync

- ver 0.1 2012/4/27

    First implement.

[gplv3]: http://www.gnu.org/licenses/gpl.html




