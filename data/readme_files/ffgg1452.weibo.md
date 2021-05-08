1.环境配置：
---------------------------
### (1)下载Python2.7
地址：http://www.python.org/getit/ （*注意一定是2.7）
### (2)下载用到的包
（*包的版本必须是可用于python2.7的）：<br />
a. numpy 地址：https://pypi.python.org/pypi/numpy<br />
b. scipy 地址：https://pypi.python.org/pypi/scipy<br />
c. rsa 地址：https://pypi.python.org/pypi/rsa<br />
d. scikit-learn 地址：http://sourceforge.net/projects/scikit-learn/files/<br />
### (3)其他工具：
a. libsvm 地址：http://www.csie.ntu.edu.tw/~cjlin/libsvm/index.html<br />
b. gunplot 地址：http://sourceforge.net/projects/gnuplot/

2.文件说明：
-----------------------------------------
### (1)程序文件：

> weibo_pkg.py    微博爬虫部分<br />
> sentiment_pkg.py    情感分析部分<br />
> save_to_file_raw.py    将微博内容从数据库转存为txt文本，便于情感分析<br />
> distinct.py    一个排除重复内容微博的程序，速度比较慢，不推荐用

### (2)数据文件：
> database/    数据库文件夹<br />
> > 2013_05_06_lichengpengjiuzai.sqlite3    本次实验的数据库文件

> weibodata/    已标注的微博数据文件夹<br />
> > train.txt    微博数据训练集<br />
> > test.txt    微博数据测试集

> otherdata/    已标注的对照数据文件夹<br />
> > train.txt    微博数据训练集<br />
> > test.txt    微博数据测试集<br />
> > 0603result.txt    本次实验结果

### (3)其他文件：
> ICTCLAS50.dll<br />
> ICTCLAS50.h<br />
> ICTCLAS50.lib<br />
> ICTCLAS.log<br />
> user.lic<br />
> Configure.xml<br />
> Data/    以上是分词工具ICTCLAS的文件


3.如何使用：
------------------------------------------
(1) 用weibo_pkg.py爬取微博数据，存入数据库，注意在使用前修改关键词、输入输出文件名等参数。<br />
(2) 用save_to_file_raw.py将数据库中数据转存到txt文件，要修改输入输出文件名。<br />
(3) 手动标注微博情感，正向为p，负向为n，与微博内容用\t符隔开。并分开为训练集和测试集。<br />
(4) 在sentiment_pkg.py中调用分类器对微博进行分类。注意参数修改。<br />
(5) 在用RBF SVM做分类时，可以使用libsvm中的tool工具优化参数，详情参考libsvm页面。<br />


4.界面展示：
------------------------------------------
(1) 最大影响微博<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/1.png" width="600"/><br /><br />

(2) 按地区、情感趋向<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/2.png" width="600"/><br /><br />

(3) 按地区、性别<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/3.png" width="600"/><br /><br />

(4) 按时间、影响力、情感趋向<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/4.png" width="600"/><br /><br />

(5) 按时间、影响力、性别<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/5.png" width="600"/><br /><br />

(6) 关键词热度图<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/6.png" width="600"/><br /><br />

(7) 微博基本信息统计<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/7.png" width="600"/><br /><br />

(8) 微博转发路径图<br />
<img src="https://raw.githubusercontent.com/ffgg1452/weibo/master/example_img/9.png" width="600"/><br /><br />