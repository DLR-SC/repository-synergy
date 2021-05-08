InfoPi的定位是**个人信息收集服务器**。

用户可以灵活地定义信息的来源，比如从网页抓取感兴趣的信息、订阅博客、从温度传感器读取数据，等等。  
然后，把收集到的信息用web的方式展示出来。


可以把InfoPi部署在树莓派等卡片式电脑上，7x24不间断运行，每月仅耗一度电。

    从网页抓取信息，需要用到正则表达式，通常学习1-2天即可入门，2-4周可熟练掌握。


点击[这里](https://wjssz.tpddns.cn:5000)可以试用，用户名demo，密码不用填，需手动信任私人证书。  
教程、文档见此博客：[http://www.cnblogs.com/infopi/](http://www.cnblogs.com/infopi/)  
反馈交流帖子：[http://tieba.baidu.com/p/3315855755](http://tieba.baidu.com/p/3315855755)

特性
----
1、支持多用户，有多种权限（管理员帐号、普通帐号、公共帐号）。  
2、有多种网页版式（电脑版、PAD版、大屏手机版、手机版）。  
3、为树莓派等卡片式电脑优化。

    a, 在配置tmpfs后，一天仅读写一次存储卡，以延长存储卡寿命。  
    b, 限制同时任务数，防止突然占用大量带宽，影响到同网络上的其他人。  
4、可动态调整配置。  
5、追求品质（高安全性、高可靠性、高性能）。

截图
----
汇总查看  
![汇总查看](https://raw.githubusercontent.com/animalize/pics/master/infopi/1.PNG)

分类查看  
![汇总查看](https://raw.githubusercontent.com/animalize/pics/master/infopi/2.PNG)

