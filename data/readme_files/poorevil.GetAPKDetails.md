【项目介绍】：
	在以前的某个安卓市场的项目中的一部分功能。主要服务于服务器端批量自动获取apk软件信息功能模块。

【主要功能】：
	获取apk软件详细信息，包括：
	1.应用名称（支持多国语言）
	2.应用icon（支持多分辨率）
	3.软件包名
	4.软件所申请的权限
	5.软件签名
	6.软件支持的语言种类
	7.适用的sdk版本号
	8.软件版本号
	9.文件大小
	
【运行平台】：
	OS：Linux
	运行环境：python2.6以上，java1.6以上

【如何使用】：
	目前支持的操作包括，单apk文件解析、多apk文件解析、文件删除。操作结果通过json格式返回。

	单apk文件解析:
	python <base-path>/GetApkDetails <apk file path>
	
	多apk文件解析:
	python <base-path>/GetApkDetails <apk filedir path>
	
	文件删除:
	python <base-path>/GetApkDetails -D <file path>
	
【需要注意的地方】：
	建立链接：
	ln -s /usr/local/<GetApkDetails path>/aapt /bin/aapt

	修改GetApkDetails.py文件的32行AXMLPrinter2.jar所在目录，如：
	xmlStr = commands.getoutput('java -jar /usr/local/GetApkDetails/AXMLPrinter2.jar '+unpackPath+'/AndroidManifest.xml')
	
	另外，有啥不明白或者想交流的同学可以直接联系我。
	
【关于我】：
	韩超
	qq：13630574
	mail：poorevil@gmail.com
