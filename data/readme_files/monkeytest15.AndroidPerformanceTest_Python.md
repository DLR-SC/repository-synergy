AndroidPermanceTest_Python
==========================
Windows小白用户慎用，此脚本目前需要少量的修改才能够用在你的工作中
环境准备： 
> 1.本地还是需要有android sdk环境。至少adb能够使用
> 2.本地需要安装python2.x版本

使用教程：
> 1. git clone项目到本地
> 2. 电脑链接机器，adb识别出来机器
> 3. 安装listener.apk，并启动，隐藏到后台
> 4. 打开终端，并且输入python Test_File.py {package name} {time(hour)}
> 5. 然后就进行测试
> 6. 测试结束之后，可以等设置的时间到了，也可以切换到终端，然后Ctrl+C，终止程序


> 报告会在根目录下生成。注意：Android4.3以及以上机器流量无法获取暂时

AndroidPermanceTest_Python_V1.0

> 1.增加了Monkey的通用脚本
> python版本必须是2.x。然后执行的时候如下
> python Monkey_Script.py <参数1> <参数2> <参数3> <参数4>

> 参数1:要执行的类型，有三种可以选择（分别是Normal，alltouch，other）

> 参数2:要测试的应用的包名（com.xxx.xxx）

> 参数3:要执行monkey的次数

> 参数4:可以进行定时，单位是s

> 生成的报告在脚本的同一个目录下，名字是MonkeyTest_Report+当前的时间.txt

> 2.重构性能脚本

> Command.py为主要获取数据脚本，执行之后再用Log_Analysis.py来做数据总体的分析，最终可以获取到所有我们想要的数据。未完待续
