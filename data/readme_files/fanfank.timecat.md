# timecat
<b>强大的日志搜索辅助工具 - A powerful tool for search in log files.</b>    
环境要求/requirements：Python2.7.x    
Origin：<a href="http://blog.reetsee.com/archives/502" target="_blank">http://blog.reetsee.com/archives/502</a>    
Online Demo：<a href="http://aap.reetsee.com/page/timecat" target="_blank">http://aap.reetsee.com/page/timecat</a>      

## 安装 - Installation    
两种方式 - There are two ways to get timecat.    
1. `pip install timecat`    
2. 或下载`timecat`文件后放在你的默认程序执行路径下 - Or directly download the `timecat` file, then add it to your default execution PATH    

## 使用 - Usage    
1. `timecat -d '2016-01-02' -s '20:13:14' -e '20:14:13' LOGFILE1.log LOGFILE2.log ...`    
2. `timecat -s '2016-01-02 20:13:14' -e '2016-01-02 20:14:13' LOGFILE1.log LOGFILE2.log ...`    
3. For more: `timecat -h`    

## 简介 - Description
### 中文简介    
假如给你一个日志文件`A.log`，它的大小达到了<b>28G</b><br />    
日志的起始时间为`Jan  1 20:13:14`，日志的结束时间为`Dec 31 20:14:13`<br />    
现在要求你从中找出4月3号早上10点9分08秒到4月4好早上6点5分04秒的所有日志并输出<br />    
你会怎么做？用awk？用grep？还是用sed？<br />    
使用了`timecat`，你可以这样做：    
<pre>    timecat -s 'Apr  3 10:09:08' -e 'Apr  4 06:05:04' A.log > timecat.out</pre>      
这样，`timecat.out`保存的就是你想要的数据，定位速度之快超乎你想象。    
如果你在生产环境中需要搜索海量的日志，这个工具一定是你的得力助手。   
    
指定`-s`与`-e`时日期时间格式不需要与目标文件中的日期时间格式保持一致，`timecat`会尝试自动转换并与文件中的格式匹配。    
但是你需要使`-s`与`-e`的日期时间格式是一致的。    
例如下面两个命令的效果是一样的：      
1. `timecat -s '2016/Jan/01 06:07:08' -e '2016/Jan/01 09:10:11' XXX.log`     
2. `timecat -s '20160101060708' -e '20160101091011' XXX.log`      

### English Description    
Imagine that given a log file `A.log` with its size up to <b>28G</b><br />    
The log starts from `Jan  1 20:13:14`, ends with `Dec 31 20:14:13`<br />    
Now you are required to output all the lines between April 3rd 10:09:08 and April 4th 06:05:04<br />    
What will you do? Use awk? Use grep? Or sed?<br />    
With `timecat`, you can do it this way:
<pre>    timecat -s 'Apr  3 10:09:08' -e 'Apr  4 06:05:04' A.log > timecat.out</pre>    
After this, `timecat.out` stores what you want, at an amazing searching speed.      
When you have to search huge amounts of log files in production environment, this helps alot, saving huge amounts of disk I/Os, more importantly, time.    

The datetime format of `-s` and `-e` options need not to be consisdent with the datetime format of the target file, because `timecat` will detect and convert datetime format automatically.      
But you should at least guarantee that the datetime formats of `-s` and `-e` are the same.    
The following two commands are essentially the same:      
1. `timecat -s '2016/Jan/01 06:07:08' -e '2016/Jan/01 09:10:11' XXX.log`     
2. `timecat -s '20160101060708' -e '20160101091011' XXX.log`      
