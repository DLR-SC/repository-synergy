# The BFuzzer Document

---

BFuzzer是一个使用```Python```开发的简单的```浏览器内存破坏漏洞挖掘框架```，当前版本为```BFuzzer-2.0```。

## 运行平台

>* 32位Windows系统，IE8/9/10/11
>* Python 2，额外安装pydbg库

## 基本组成

BFuzzer 由主要两部分组成：***server***和***moniter***。

### *server*

*server*作为一个简单的WEB服务器：
>* 为浏览器提供当前或下一个**样本**
>* *server*的**样本**由用户根据fuzz策略/算法生成

### *moniter*

moniter负责控制浏览器行为：
>* 启动/重启/关闭浏览器
>* 调用*crasher*模块hook浏览器的异常处理，记录重要信息
>* 初始化浏览器请求

## 运行原理

*moniter*启动浏览器，hook浏览器的异常处理，强制浏览器访问http://host:port/init，**init**代表初始化页面，该页面内容较为简单，即通过包含
```HTML
<meta http-equiv="refresh" content="3;url=http://host:port/next" />
```
的方式使浏览器在3秒后请求真正的**样本**：http://host:port/next。

**样本**由根据fuzz策略编写的生成算法生成，生成的样本提供给*server*，*server*会在收到类似http://host:port/next时获取下一个待测试的**样本**，返回给浏览器。

不考虑具体内容，**样本**内容为：
``` HTML
<html>
<head>
<meta http-equiv="refresh" content="30; url=http://hostLpoer/next/long" />
<script>
// ...
// 随机生成的JS操作
// ...
window.location.href = 'http://host:port/next';
</script>
<head>
<body>
<!--
   随机生成的HTML标签内容
-->
</body>
</html>
```
**样本**控制浏览器在运行完本样本后获取并运行下一个**样本**。

如果浏览器幸运地发生了崩溃，进入异常处理，*crasher*有机会向*server*请求http://host:port/cur获取当前的样本并默认保存在```logs/```目录中，同时在同一目录下保存崩溃信息，即```poc-*.html```和```crash-*.html```，**poc样本**和**crash信息**相互对应；同时，*moniter*也会请求http://host:port/cur获取当前样本并在同一目录下保存为```dos-*.html```，这个设计是为了防止偶然发生的*crasher*没有将相关信息成功保存而设计的，不喜欢的话注释几行代码即可。

## 安装使用

### 安装
1. 下载安装```python 2``` （本人使用```Python 2.7.8```）；
2. 下载安装```pydbg```库；
3. 下载```BFuzzer```压缩包并解压缩。

### 使用
1. 了解```BFuzzer```基本原理;
2. 运行**server.py** : ```python server.py```
3. 运行**moniter.py** : ```python moniter.py```

### 建议
1. 关闭浏览器```崩溃自动恢复```功能，允许```本地执行脚本```；
2. 运行前关闭```即时调试```功能：
32位Windows设置注册表项[HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug]的Auto值为0
64位Windows设置注册表项[HKEY_LOCAL_MACHINE/SOFTWARE/Wow6432Node/Microsoft/Windows NT/CurrentVersion/AreDebug/Debugger]的Auto值为0
3. 禁用MS14-037增加的```对象延迟释放机制```：
设置注册表项[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MEMPROTECT_MODE]的iexplore.exe值为0

## 下一步？
写自己的fuzz策略，可以参考一系列会议论文。

-------------
## 版本更新
2014.11.24
>* BFuzzer-2.1发布，修复server模块在IE9下的不正常行为

## 版本历史

2014.11.3
>* BFuzzer-2.0发布，重写大部分源码
>* 易配置，易扩展，以备将来支持chrome/firefox
>* 将配置信息从代码中分离，删除不必要的测试用例和代码
>* 更新fuzz策略
>* 更新文档

2014.10.24
>* BFuzzer-1.0发布，支持win32/IE8+平台
>* 简单的fuzz策略

