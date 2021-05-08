pybaidudisk
=============================

安装
-------
.. sourcecode:: 

    cd pybaidudisk
    python setup.py install

使用
----------
.. sourcecode:: python

    >>> from pybaidudisk import NetDisk
    >>> disk = NetDisk(username, password)
    >>> if disk.check_login():
    ...     disk.list()
	
	
    >>> from pybaidudisk import run_cmd
    >>> run_cmd(username, password)
    Baidu Yun cli
    ☁ > 
    ☁ > help
    ========================================
    EOF  exit  help  ls     mv   quota   rm      upload  wget
    cd   get   jobs  mkdir  pwd  rename  status  watch 	
	
	
命令行工具	
----------
.. sourcecode:: 

    bdiskcmd -u username -p passwd

