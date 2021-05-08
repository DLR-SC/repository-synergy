## sqlmapapi_pi 批量注入工具
------------
**Intorduction:**

- 本程序是基于[manning23](https://github.com/manning23)的项目二次开发，参考地址 [click me](http://drops.wooyun.org/tips/6653)
- 本程序利用百度爬取特定的url链接，然后调用sqlmapapi（sqlmap自带的批量接口），进行注入的判断。
- AutoSqli.py中option的设置可参考set_option.txt；可自定义判断注入的方法，例如，基于时间/布尔等。

**Useage:**
- 在sqlmap的目录下执行`python sqlmapapi.py -s`进行监听操作。
- 运行AutoSqli.py `python AutoSqli.py` 参数可通过`-h`查看

**Tips:**
* 这里要注意的是在代码里自定义搜索关键字：`key='inurl:asp?id='`
* 以及线程数：`nloops = range(4)   #threads Num`
* 建议线程数不要太多，以免卡死。
