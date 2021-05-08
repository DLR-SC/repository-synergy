ZJUWLAN_AUTO_LOGIN
==================
A ZJUWLAN login script, implemented in Python.

It implements some basic functions such as wifi scanning, wifi connecting, login, connection lost recovering and error recovering.

Implemented in Python 2.7.6.

Support OS: Windows 7

##BUGS
- Key expires so quickly. It only last about 1 day. Checking it...SOLVED
- Sometimes it refreshes the connection though we are still online, which causes a connection lost.

##TODO 
- Support Ethernet login **via vpn**. 10.5.1.7 or vpn2.zju.edu.cn
- Check the connection states via some more efficient methods. (currently it tries to connect to a testwebsite using HTTP protocol.)
- It can't ... 算了还是用中文说吧。目前此脚本无法真正做到自动开启电脑wifi。以Windows 7为例，用户需要在控制面板-网络和共享中心-更改适配器设置-相应的无线网络连接 * 上打开属性面板，共享ZJUWLAN的网络连接，才能实现wifi共享。实现程序自动开启wifi，需要用Python调用Win32 API。算作一个待完成的项目，欢迎有同学愿意贡献此处的代码。

##Author
Bo Song

songbo.sunny@gmail.com
