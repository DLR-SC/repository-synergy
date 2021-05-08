Microsoft Outlook WebAPP Brute
==========

Outlook.py只有一个工作线程.   Outlook_threaded.py是多线程版本.

测试发现多线程版本在SSL handshake时可能出错，比如破解email.baidu.com时。这跟服务器的稳定性有关。 目前的处理方法是出错后重试!


使用:

Outlook.py domain users passwords
domain是站点域名，users和passwords是字典文件的名称。


Outlook_threaded.py domain users passwords threads
再额外提供一个线程数，根据服务器的稳定性自行调整，程序不是自适应的