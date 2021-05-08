#Zhihu_voters
##介绍
Zhihu_voters使用python2.7编写，用来获取知乎某个答案下面所有点赞用户的信息，并自动输出到一个excel文档中。获取的用户信息包括用户名、用户个人主页地址、赞同、感谢、提问、回答。

写这个的初衷是因为有些时候会遇到一些莫名其妙的高票回答，让我们忍不住怀疑是否是水军刷赞。通过最后输出的excel文档可以很容易地筛选统计出三零用户的个数，以此来初步判断是否有刷赞行为。

##依赖
* 使用requests实现http请求
* 使用Beautiful Soup 4解析返回的html文档
* 使用xlwt实现对excel的写入操作

如果缺少依赖的库可以使用pip命令进行安装。
##其他信息待补充
##联系我
* 知乎： [@段晓晨](http://www.zhihu.com/people/loveQt)
* email： [shmilydxc@vip.qq.com](mailto:shmilydxc@vip.qq.com)
