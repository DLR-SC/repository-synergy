NSLoger.com
-

> This is a lightweight forum, use the Django framework to develop.

### 截图
![Screenshot](https://raw.githubusercontent.com/isaced/NSLoger/master/Screenshot.jpg)

### 关于
第一个用 Python/Django 写的完整项目，在这里感谢 [@cloverstd](https://github.com/cloverstd) 的付出，本来想打造一个 Cocoa 开发者社区，历经种种，虽然社区最终还是迎来关闭，有时候结果也许不太重要，不过这个过程是有意义的。

### 一点一点

Django当时是采用的最新版1.6，强大的不能再强大，路由、模板、缓存，基本上一般 Web 应用里可能用到的都有了，后来体会过一下下 *Flask* 就能感觉这是完全不同的两个方向。

- Django
- South
- argparse
- misaka
- wsgiref
- qiniu
- gunicorn

> 采用七牛作为头像储存源，用七牛表单上传API保存头像。
>
> 用网易企业邮箱支撑邮件服务(不过很不稳定，QQ邮箱基本收不到)。
>
> Markdown 解析也是几经波折，测试过 *Markdown* 、*Markdown2* 等等解析库，最后在segmentfault([Python中的Markdown和Markdown2有何区别？](http://segmentfault.com/q/1010000000424159))，找到 *Misaka*。
>
> 部署则是 Nginx + Gunicorn + Django ,写过一篇笔记在 [这里](http://www.isaced.com/post-248.html) 。

### To be continue
生命不息，代码不止！
