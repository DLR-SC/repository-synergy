# 长城交易下单脚本使用说明
## 简介
本脚本提供了以下功能:

1. 长城证券下单相关的功能。包括：自动登录、查询持仓、查询订单、查询余额、下单、撤单，通过http请求实现。
2. 条件单功能。条件单采用mysql存储触发下单的相关指令，服务进程读取命令后，定期检查价格，判断是否触发，满足触发条件则通过下单接口下单。
3. 新股一键申购。可设置系统定时任务，调用python main.py -tN进行新股自动申购。 

## 安装
1. 安装python3.5，并且把python的安装路径加入系统的环境变量PATH
2. 安装Anaconda3
3. 安装mysql，创建用户，执行代码目录里的create_table.txt里的语句。
4. 进入gw_trade目录，添加配置文件，config.ini。内容如下：
    
	[common]
	
	\#长城证券的资金账号
	
	account = 
	
	\#加密过的密码，可以用chrome的F12监控长城证券登录页面post的字段，其中有一个是password字段
	
	passwd_encrypted = 
	
	\#上海的股东代码
	
	secuids_sh = 
	
	\#深圳的股东代码
	secuids_sz =  

	[mysql]
	user = root
	password = root123


## 使用说明
### 下单功能
usage: main.py [-h] [-t {B,S,Q,A,G,C,N}] [cmd_args [cmd_args ...]]

1. [Buy Stock. Usage: -B stock_code price amount. e.g. -tB 159915 2 100] 
2. [Sell Stock. Usage: -S stock_code  price amount. e.g. -tS 159915 2 100]
3. [Query Account Info. Usage: -tA] 
4. [Query Holding Stock. Usage: -tQ]
5. [Query OnGoing Order. Usage: -tG] 
6. [Cancel OnGoing Order. Usage: -tC order_id. order_id can be acquired from the result of -tG cmd] 
7. [Buy New Stock. Usage: -tN]

### 条件单功能
1. 修改数据库，添加条件单（求人做页面）
2. 启动process_cond_order.py。该脚本用于检查是否提交条件单到长城证券。

### 新股一键申购
1. 修改run.bat里面的目录路径
2. 加入windows的系统定时任务


