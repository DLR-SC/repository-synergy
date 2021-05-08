用于在qqwry.dat里查找IP地址归属地。  
另提供一个从纯真网络更新qqwry.dat的小工具。

本工具已上传到pypi：https://pypi.python.org/pypi/qqwry-py3  
Python 3.4及以上版本自带了pip工具，执行此命令既可安装：

    pip install qqwry-py3

特点：

﻿1. for Python 3.0+。  
﻿2. 提供两套实现供选择。有一个查找速度更快，但加载慢、占用内存多。  
﻿3. 在i3 3.6GHz，Python 3.6上查询速度达18.0万次/秒。  
4. 经过较严格测试。  
﻿5. 提供一个从纯真网络(cz88.net)更新qqwry.dat的小工具，用法见本文最后一部分。  

用法
============
    from qqwry import QQwry
    
    q = QQwry()
    q.load_file('qqwry.dat')
    result = q.lookup('8.8.8.8')


解释q.load_file(filename, loadindex=False)函数
--------------
加载qqwry.dat文件。成功返回True，失败返回False。

参数filename可以是qqwry.dat的文件名（str类型），也可以是bytes类型的文件内容。

当参数loadindex=False时（默认参数）：  
程序行为：把整个文件读入内存，从中搜索  
加载速度：很快，0.004 秒  
进程内存：较少，16.9 MB  
查询速度：较慢，5.3 万次/秒  
使用建议：适合桌面程序、大中小型网站

当参数loadindex=True时：  
程序行为：把整个文件读入内存。额外加载索引，把索引读入更快的数据结构  
加载速度：__★★★非常慢，因为要额外加载索引，0.78 秒★★★__  
进程内存：较多，22.0 MB  
查询速度：较快，18.0 万次/秒  
使用建议：仅适合高负载服务器

（以上是在i3 3.6GHz, Win10, Python 3.6.2 64bit，qqwry.dat 8.86MB时的数据）


解释q.lookup('8.8.8.8')函数
--------------
﻿找到则返回一个含有两个字符串的元组，如：('国家', '省份')  
﻿没有找到结果，则返回一个None


解释q.clear()函数
--------------
﻿清空已加载的qqwry.dat  
﻿再次调用load_file时不必执行q.clear()


解释q.is_loaded()函数
--------------
q对象是否已加载数据，返回True或False


解释q.get_lastone()函数
--------------
﻿返回最后一条数据，最后一条通常为数据的版本号  
﻿没有数据则返回一个None


从纯真网络(cz88.net)更新qqwry.dat的小工具
============
    from qqwry import updateQQwry
    
    result = updateQQwry(filename)

﻿当参数filename是str类型时，表示要保存的文件名。  
成功后返回一个正整数，是文件的字节数；失败则返回一个负整数。

﻿当参数filename是None时，函数直接返回qqwry.dat的文件内容（一个bytes对象）。  
成功后返回一个bytes对象；失败则返回一个负整数。这里要判断一下返回值的类型是bytes还是int。

负整数表示的错误：  
﻿-1：下载copywrite.rar时出错  
﻿-2：解析copywrite.rar时出错  
﻿-3：下载qqwry.rar时出错  
﻿-4：qqwry.rar文件大小不符合copywrite.rar的数据  
﻿-5：解压缩qqwry.rar时出错  
﻿-6：保存到最终文件时出错  