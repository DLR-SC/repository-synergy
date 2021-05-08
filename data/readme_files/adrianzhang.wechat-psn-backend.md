# wechat-psn-backend
一个微信公众号（服务号，Public Service Number）后台环境（Linux+python+werobot+cherrypy），使用[DaoCloud网站][1]或[灵雀云][4]来管理运行，使用者几分钟即可拥有自己的类似SAE/GAE/BAE云的应用开发平台，只要部署了自己的代码，即可在几秒钟内提供微信订阅号/服务号后台服务。这个平台使用纯Python、CherryPy和WeRoBot构建。在这个平台上开发请[阅读WeRoBot的文档][5]。或者您也可以把Dockerfile改改，安装成您自己喜欢的应用框架和web服务器。

## 起源
这个项目的起源是被逼无奈。起初，在SAE上申请个账号，申请了应用空间。结果遇到了巨大的麻烦：
- SAE主要推荐SVN管理代码，而开发Python最方便的Mac OS上并没有什么好的免费GUI工具.
- SAE也支持Git管理代码，但是使用方法没有详细介绍以至于摸索了一阵子。
- 帐户未作实名认证只能申请最多两个应用。一个应用已经可以运行了，另一个应用需要部署一个框架，这个框架必须用SVN部署到SAE应用空间去，而SAE并不支持同时SVN+Git的管理方法，只能选择其中之一，无奈只好删除应用，打算重新启用SVN管理代码，谁知道SAE上删除应用居然要两天！于是有两天时间必须寻找其他平台解决方法。

## [DaoCloud][1]
通过[七牛网][2]的友情链接发现了[DaoCloud][1]，在[DaoCloud][1]的技术人员热情地帮助下，发现了Docker是一个非常先进的工具，可以用来快速构建自己的应用环境，而[DaoCloud][1]则可以帮助我们实现快速将Docker方式实现的应用环境部署到云中。如此一来，还需要xAE们吗？自己就可以实现一个**myAE**了。

更好玩的是：在[DaoCloud][1]的管理下，我们可以将环境的不同组件部署到不同的地方去——应用主机可以放在AWS的VPS上，数据库可以放在RackSpace或阿里云、腾讯云、微软Arzur云平台上，存储放到七牛云。实现了应用环境的分布式。甚至高兴的话，把应用主机部署在自己家里的树莓派上，哪怕没有公网IP也可以！

## [灵雀云][4]
这是另一个类似DaoCloud的网站，用来作为网络Docker系统实现，可以网络式构建docker image，然后直接部署在灵雀云的容器中，上线！

## [时速云][7]
这个网站是比较早的一个Docker云服务商。在这个网站上面使用该repo和在上面两个网站的使用方法是一致的。

## Docker

若第一次看到Docker这个词，请参考[《Docker和DaoCloud纯小白入门手册》][3]来了解它。若有了一定了解，那么这个Repository里的dockerfile就是用来构建docker image的。目标是形成一个开箱即用的用于开发微信公众号后台的App Engine，当然了，这个App Engine与其他SAE/GAE等不同的地方在于它完全是属于开发者自己的。可以随便更改环境配置，比如增加个框架什么的。

## 使用方法

那么对于开发者，这个Repository到底有什么好处呢？这个Repository里有构建环境必要的Dockfile和配置文件yaml，只需要fork这个Repository，然后您本人的GitHub目录下就有了同名repository，把自己的Python代码push到这个同名repository里，使用[DaoCloud][1]，点两下鼠标就能在几分钟之内发布自己的微信服务号后台，在微信公众号配置页面开发者模式中关联这个后台，微信公众号立刻可用。相比较原先需要几个小时乃至几天的安装、配置环境、部署代码、运行，大大节省了时间。作为演示，此Repo中已经放置了index.py，在任何一个Docker云服务商那里运用这个Repo生成镜像并部署成应用，那么马上就可以把微信公众号后台开发者模式绑定这个应用，Token使用testrobot。关注自己的公众号，发个消息，看看会发生什么吧。

## 测试方法
在DaoCloud或灵雀云上运行起来之后，使用微信提供的[测试页面][6]，URL填写为在DaoCloud或灵雀云获得的应用URL，Token填写为testrobot，加密调试选“兼容模式”，其他的按照微信文档说明填写。即可向这个后台应用发消息并获得回复。

[1]: <https://account.daocloud.io/signup?invite_code=nsvv3jvpfve4ejlapnze>
[2]: <http://www.qiniu.com>
[3]: <./Docker和DaoCloud纯小白入门手册.md>
[4]: <http://www.alauda.cn>
[5]: <https://werobot.readthedocs.org/en/latest/>
[6]: <https://mp.weixin.qq.com/debug/cgi-bin/apiinfo?t=index&type=%E6%B6%88%E6%81%AF%E6%8E%A5%E5%8F%A3%E8%B0%83%E8%AF%95&form=%E6%96%87%E6%9C%AC%E6%B6%88%E6%81%AF>
[7]: <http://www.tenxcloud.com>