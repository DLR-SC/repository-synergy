==========
	
##本项目为日常工作中的使用的python脚本


###1.  ssh_thread.py  是一个批量执行命令的脚本，支持直接执行ssh命令及文件传输，支持多线程

		使用说明如下：
	
		-h,-H,--help         帮助页面 
        -C, --cmd            执行命令模式 
        -M, --command        执行命令模式 
        -S, --sendfile       传输文件模式 
        -L, --localpath      本地文件路径 
        -R, --remotepath     远程服务器路径 

	    IP列表格式:

   	    IP地址		用户名     密码     端口
	    192.168.1.1        root	  123456    22

      	e.g.
              批量执行命令格式： -C "IP列表" -M '执行的命令'
              批量传送文件：     -S "IP列表" -L "本地文件路径" -R "远程文件路径"
	    错误日志文件：$PWD/ssh_errors.log

###2. check_ping.py  多进程检测ping，并取值
	
		默认开启4个进程，需要将hosts.txt IP列表文件放入同一目录下，IP列表每行一个，支持域名、IP


###3. check_ip138.py 通过ip138检测IP（域名）归属地

		使用方法: python check_ip138.py  192.168.1.1
	
	
	
	
###4. vps_baidu.py  使用baidupan备份VPS

		pip install baidupan
	
参考：http://solos.github.io/baidupan/