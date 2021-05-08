
* Demo

* Features
+ 消息通过WebSocket发送和接收
+ 浏览器多个Tab页共享Session
+ 使用AngularJS渲染数据

* TODOs
+ 学习 ws4py + gevent, 并使用它改写webapp.py
+ 添加用户注册/登录, OpenID登录: [Google, GitHub, 豆瓣, 微博]
+ 检测WebSocket是否断线并尝试重连
+ 时间的国际化问题

  

* 如何运行本项目?
#+BEGIN_SRC
git clone git@github.com:TheWaWaR/python-websocket-demos.git
cd python-websocket-demos
pip install -r deps.txt
python webapp.py 8888
#+END_SRC
