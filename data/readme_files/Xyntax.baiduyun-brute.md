# baiduyun-brute  
多线程百度云(私密分享)密码爆破工具  
问题请反馈至 i@cdxy.me  
  
**2016/6/7 由于漏洞修复，该工具现已失效，多线程定向爆破可参考[https://github.com/Xyntax/POC-T/blob/master/script/brute-example.py](https://github.com/Xyntax/POC-T/blob/master/script/brute-example.py)**  

## info  
爆破百度云私密分享的四位密码(共168万条)  
可自定义线程数(默认为30)  
自己本子测试30线程一个小时能把字典全跑完  
## usage  
 1. 复制私密分享页面url  
    ![baiduyun.png](http://www.cdxy.me/wp-content/uploads/2015/12/baiduyun.png)   
 2. `python baiduyunBrute.py -t [thread_num] ["url"]`  
      
    示例(注意url外引号):  
    `python sub.py -t 50 "http://pan.baidu.com/share/init?shareid=385857944&uk=1544574381"`  
 3. 结果在命令行显示，同时存储到`./pass.txt`查看  
    ![pass-found.png](http://www.cdxy.me/wp-content/uploads/2015/12/pass-found.png)  
  
## reference  
 - 多线程框架参考[lijiejie](https://github.com/lijiejie)大师的项目[subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)
