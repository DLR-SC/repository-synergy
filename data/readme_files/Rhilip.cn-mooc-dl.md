# cn-mooc-dl
Since most Scripts in [renever/cn_mooc_dl](https://github.com/renever/cn_mooc_dl) and it's networks are not able to work,
I wrote another repository to download those MOOC Courses (**But there still some code from it,Thanks**).

![](https://img.shields.io/badge/build-passing-brightgreen.svg)
![](https://img.shields.io/badge/coverage-86%25-red.svg)
![](https://img.shields.io/badge/Wiki-Out_Of_Date-red.svg)
![](https://img.shields.io/github/license/Rhilip/cn-mooc-dl.svg)

## How it work
### 1) Prerequisites
The following dependencies are required and must be installed separately.
* [Python3](https://www.python.org/downloads/),and install it into PATH.
* With Model :
| [Request](http://docs.python-requests.org/zh_CN/latest/user/install.html#install)
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
| [lxml](http://lxml.de/installation.html#installation)
| [progressbar2](http://pythonhosted.org/progressbar2/installation.html)

You can use this command:
```
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests beautifulsoup4 lxml progressbar2
```
* Maybe [Aria2](https://github.com/aria2/aria2) is a good Download tools,you can use it to Download Video,if set currently.([Suggest settings](https://gist.github.com/Rhilip/cd2d28fa11b7f919ea5fcdc6cf84af8d))
* Also don't forget download this packet......

### 2) Supported Sites

| File | Site | URL | Videos?  | Documents? | Subtitle?|
|:-------------:|:------------------:|:---:|:---:|:---:|:---:|
| icourse163-dl.py | 中国大学MOOC | <http://www.icourse163.org/> | ✓ | ✓ | ✓ |
| xuetangx-dl.py | 学堂在线 | <http://www.xuetangx.com/> | ✓ | ✓| ✓ |

### 3) Instruction manual
See [Wiki](https://github.com/Rhilip/cn-mooc-dl/wiki) please.

## Test Environment
* Python :`v3.6.0`
* OS : `Windows 10` and `Chrome 56`
* IDE : `IntelliJ IDEA 2016.3.4`
* Download tools :`Aria2c`

## Met Problem
* Issues Please~