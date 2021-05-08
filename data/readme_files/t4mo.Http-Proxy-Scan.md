作者不是我 我从git上面搜索fork过来的。。
## Http-Proxy-Scan

利用censys.io快速更新全网的优势，爬取http代理。提取关键字为'Mikrotik','Squid','Proxy','Tinyproxy','Wingate','CCProxy','Pound'。如需添加请修改censys.io main函数的keyword字段，测试的端口号为8080、80、3128。


### 部署方法

* python 2.7.x
* mysql导入proxy.sql
* 修改dbconnect.py数据库连接信息
* 修改censys.py UID、SECRET为你自己的api
* 设置crontab:</br>
 0 * * * *  python  /root/proxy/checkproxy.py

### 效果

用10美元1年的vps抓了10来天的效果</br>
```
mysql> select count(*) from proxy where type=2;
+----------+
| count(*) |
+----------+
|     2096 |
+----------+
1 row in set (0.01 sec)</br>
mysql> select count(*) from proxy where type=2 and status=1;
+----------+
| count(*) |
+----------+
|      320 |
+----------+
1 row in set (0.00 sec)
```
加上自己用其他方式抓的公开代理，基本可以保障每天800左右的可用代理</br>
```
mysql> select count(*) from proxy where status=1;
+----------+
| count(*) |
+----------+
|      891 |
+----------+
1 row in set (0.00 sec)
```
