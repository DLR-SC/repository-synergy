# **Python-script-converter**

[![PyPI](https://img.shields.io/pypi/v/yagmail.svg?style=flat-square)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)]()

[中文介绍请戳这里](https://github.com/ZYunH/Python-script-converter/blob/master/Readme-cn.md)

## Introduction:

​	This is a tiny tool used to convert a python script(e.g. demo.py -> demo.command) to a executable file(For mac and Linux),so that you are able to use it anywhere.

## Installation

Tip: Add #!/usr/bin/env python or #!/usr/bin/env python3 in  first line of your script to specify interpreter.So you do not need add python version when you use psc.

### Option 1:Install via pip（Better）

```
$ pip3 install python-script-converter
```

you can also use pip.

### Option 2:Download from Github

You may either download the stable (identical with the latest release on PyPI) or the master branch of python-script-converter. Unzip it, and do 

```
$ [sudo] python3 setup.py install
```

you can also use python.

## Usage:

Before use it, you should ensure:

- You're using Mac OS or Linux.

Here's' how you use `psc`  to create a new executable file base on you original script :

#### If your script based on python3.x

```
$ psc test.py
```

Or use abspath.

```
$ psc /Users/zyh/test.py
```

#### If your script based on python2.x

```
$ psc test.py 2
```

or

```
$ psc /Users/zyh/test.py 2
```

then,you can get a executable file,its name is the same as your script,but its extension is **.command**. and what's more,**it will not change your original script**.
