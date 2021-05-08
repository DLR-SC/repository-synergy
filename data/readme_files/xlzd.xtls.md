xtls : 我的工具包
===============================


什么是xtls
-------

xtls是xlzd's tools的简写，在写代码的过程中会遇到很多需要重复复制粘贴的代码。为了保持代码的美观整洁，所以抽取成了这个库，以方便自己使用。如果能够方便更多朋友，那就更好了。

(注意: 部分功能不支持在Windows环境, 由于我平时的工作娱乐环境为Linux和OS X, 暂时并没有支持Windows环境的计划, 如果你有这方面需求且愿意的话, 欢迎修改后提merge request)


安装与升级
-------

xtls已经上传到了pypi(https://pypi.python.org/pypi/xtls)，所以你可以直接通过pip安装和升级：

**安装：**

.. code-block:: console

    $ pip install xtls


**升级：**

.. code-block:: console

    $ pip install xtls --upgrade



已经实现的部分功能
-------


由于这个库很大程度上是我自用，所以并没有完整的注释和文档，下面简单列举一些常见的功能。
 

**检测函数运行时长：**

.. code-block:: Python

    from xtls.codehelper import timeit
    
    # 将运行时间打印到控制台
    @timeit
    def func():
        pass
        
    # 将运行时间记录到日志
    @timeit(logger)
    def func():
        pass
        
        
        
**检测语句块运行时长：**

.. code-block:: Python

    from xtls.codehelper import timetime
    
    # 将运行时间打印到控制台
    with timetime():
        # 执行一段代码，完成之后将会打印出这段代码的运行时间
        pass
        
    # 将运行时间记录到日志
    with timetime(tag='这段代码的标签', logger=logger):
        # 执行一段代码，完成之后将会打印出这段代码的运行时间
        pass
         
        
        
        
**控制函数不抛出异常：**

.. code-block:: Python

    from xtls.codehelper import no_exception
    
    
    # 同上，支持一个可选的logger参数
    @no_exception(on_exception='当发生异常时返回这个')
    def func():
        pass
    
    # 这个装饰器主要是用在有些时候并不关心函数抛出异常，要把代码整个try-catch起来的情况。 
        
        
    
        
**控制语句块不抛出异常：**

.. code-block:: Python

    from xtls.codehelper import trytry
    
    # 同上，支持一个可选的logger参数
    with trytry():
        # 如果遇到异常，后面的代码会继续执行
        pass
        
    
        
    
**装饰单例：**

.. code-block:: Python

    from xtls.codehelper import singleton
    
    @singleton
    class Singleton(object):
        # 这个类将只能被创建一个实例
        pass
           

    
**获取当前机器IP等：**

.. code-block:: Python

    from xtls.codehelper import get_ip, get_user, get_runner
    
    print get_ip()      # 192.168.1.100
    print get_user()    # xlzd
    print get_runner()  # xlzd@192.168.1.100
    
    
    
**时间解析：**

.. code-block:: Python

    from xtls.timeparser import parse_time
    
    parse_time(u'20160325')
    parse_time(u'2016年3月25日15点13分53秒')
    parse_time(u'二零一六年三月二十五日')
    parse_time(u'1天前')
    parse_time(u'3分钟以后')
    
    
    
**在终端打印彩色字符：**

.. code-block:: Python

    from xtls.colorful import colorful_print, Color, dyeing
    
    colorful_print('what', Color.RED)      # 在终端直接打印红色的 ‘what’
    color_str = dyeing('what', Color.RED)  # 返回“染色后”的字符串，通过print打印一样会有颜色
    

    
    
**汉字转拼音：**

.. code-block:: Python

    from xtls.pinyin import parse
    parse(u'你好')  # [('NI', '3'), ('HAO', '3')]， 
    

        
**基于tornado的并发爬虫：**

.. code-block:: Python

    from xtls.basecrawler import AsyncCrawler
    
    这个自己看代码或者直接问我吧，只言片语不好描述

    
    
后续
-------

这里面大多是我常用到的东西，也有部分不常用但是挺有趣的内容，如果你也有想放进来的代码，尽管fork之后提交pull request吧。
        
