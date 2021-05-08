# 什么值得买 每日签到奖励 #
此脚本用于 [什么值得买](http://www.smzdm.com/) 网站的每日签到.

# 如何使用? #
脚本语言是`Python`, 所以首先你要[安装Python](https://www.python.org/downloads/)

然后脚本依赖于`requests`库, 所以你要[安装requests](http://www.python-requests.org/en/latest/user/install/)

都安装完成之后, 还需要修改脚本中的`SMZDM_USERNAME`(你的账号名)及`SMZDM_PASSWORD`(你的密码)变量

最后, 只需要添加`cron`定时任务即可!

# 关于脚本 #
~~2015年(具体什么时候我也不知道), 值得买引入防爬虫机制, 第一次访问页面会返回`521`错误, 页面内容为`JavaScript`脚本, 此脚本会设置一个名为`__jsl_clearance`的`Cookie`, 并刷新页面.~~

~~此机制直接导致我[之前的签到脚本](https://gist.github.com/isayme/5efc1bf611da29a3121c)无效, 所以才有了今天的版本.~~

# 联系我 #
`email`: isaymeorg # gmail.com
