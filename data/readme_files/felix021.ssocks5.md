ssocks5
=======

socks5 proxy simplified from shadowsocks and mixo.

好吧，我把自己的[mixo](https://github.com/felix021/mixo)也简化了一下，两个版本的socks5 proxy，换着玩吧……

usage
----
msocks5.py 或者 ssocks5.py 随便挑一个：

    python msocks5.py #监听7070
    
    python msocks5.py 1080 #监听1080

把shadowsocks/mixo简化只留下最基本的socks5代理功能。msocks5.py是完全public的；至于ssocks.py……如果一定需要个什么协议的话，参考[shadowsocks的协议](https://github.com/clowwindy/shadowsocks/blob/master/LICENSE)吧 :)

p.s. msocks5 依赖于 gevent，ssocks5 则可以在无gevent的情况下运行。

p.p.s. 如果你需要一个带加密、转发功能的翻墙socks5代理，你也可以用我写的 [mixo](https://github.com/felix021/mixo) :D
