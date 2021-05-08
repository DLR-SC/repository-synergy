# python learn

## sublime插件
* [SublimeREPL](https://github.com/wuub/SublimeREPL) 允许你在编辑界面直接运行 Python 解释器；以及执行python文件。

## 一些概念
### 缩进
不要混合使用制表符和空格来缩进，因为这在跨越不同的平台的时候，无法正常工作。我 强烈建议 你在每个缩进层次使用 单个制表符 或 两个或四个空格 。
选择这三种缩进风格之一。更加重要的是，选择一种风格，然后一贯地使用它，即 只 使用这一种风格。

## 代码规范
* http://ssv.sebug.net/Python_Coding_Rule

## 学习资源
### 中文资源
* [简明 Python 教程](http://sebug.net/paper/python/index.html)
* [Python 手册](http://sebug.net/paper/books/python_hb/)
* [ 深入 Python :Dive Into Python 中文版](http://sebug.net/paper/books/dive-into-python/)
* [crossin的编程教室](http://crossin.me/forum.php?mod=forumdisplay&fid=2)
* [深入 Python 3](http://sebug.net/paper/books/dive-into-python3/)
* [Python安全](http://sebug.net/paper/books/vulncat/python/)
* [廖雪峰的python教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)
* https://github.com/Yixiaohan/codeparkshare
* [老齐的教程](https://github.com/qiwsir/ITArticles/blob/master/BasicPython/index.md)
* [Python的神奇方法指南](http://article.yeeyan.org/view/311527/287706)

### 英文资源
* [dive into python](http://www.diveintopython.net/toc/index.html)
* [learn python the hardway](http://learnpythonthehardway.org/book/)
* [Python官网教程](https://docs.python.org/2/tutorial/)

### 邮件订阅
* [python weekly](http://www.pythonweekly.com/)

## 在sublime中运行python
“Preference(首选项)”-----》“Browse Packages(浏览程序包)”----------》“python”，在打开的目录中修改Python.sublime-build文件类似如下
```
{
    "cmd": ["python", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```
然后，Python文件就可以`ctrl／Command ＋ b`来运行

## 包管理
可以使用 [pip](https://pip.pypa.io/en/latest/user_guide.html)进行包管理。

1. 项目根路径下创建`requirements.txt`
1. 内容类似例如
```
MyApp
Framework==0.9.4
Library>=0.2
```
1. 然后执行 `pip install -r requirements.txt`

具体产看 https://pip.readthedocs.org/en/1.1/requirements.html

### python版本管理
virtualenv

### 自动化远程部署项目
* [fabric](http://www.fabfile.org/en/latest/)
