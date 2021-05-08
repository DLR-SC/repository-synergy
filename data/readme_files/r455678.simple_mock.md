# simple_mock
# sql文件为mysql中表结构文件
# mock_server.py为实际mock文件。
# mock_web.py为web管理页面所用server。
# mock文件夹中为管理页面,在indexJQ.js文件中配置mock_web.py访问地址。

## 操作步骤简述：
# 1、执行sql脚本建表
# 2、修改db.config数据库配置文件
# 3、安装需要的第三方依赖库，运行mock_server.py。
# 4、运行mock_web.py。
# 5、把web项目拷贝到web容器中正常访问，修改mock/js/config.js接口访问地址为mock_web的地址和端口。
# 6、打开index页，添加/导入自己需要的mock数据。
