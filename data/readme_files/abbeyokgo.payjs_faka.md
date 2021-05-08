# 基于[payjs](https://payjs.cn/ref/KZVNLZ)的个人发卡平台
----

开发环境: Python2.7

开发框架: flask

前端框架: bootstrap

数据库: MySQL

----
**预览**
1. 首页
![index.png](index.png)

2. 购买确定信息
![buy_ok.png](buy_ok.png)

3. 确定弹出支付二维码
![buy_pay.png](buy_pay.png)

4. 库存不足
![buy_no.png](buy_no.png)

5. 提取卡密
![getkm.png](getkm.png)

6. 后台首页
![admin.png](admin.png)

7. 后台订单管理
![admin4.png](admin4.png)

8. 添加卡密
![add_code.png](add_code.png)

----
**安装教程**

0. 推荐环境：centos7+python2.7

1. git clone https://github.com/tangrela/payjs_faka.git

2. cd payjs_faka/faka

3. 安装依赖:`pip install -r requirement.txt`

4. 修改配置信息: `vi config.py`
    - payjs商户号`PAYJS_ID`和密钥`PAYJS_KEY`
    - mysql配置

5. 添加管理员账号：`python run.py deploy`，按照提示输入管理员邮箱和密码

6. 运行：`gunicorn -w4 -b 0:35000 run:app`，然后访问你的`ip:35000`试试

---
**我的示例网站：[http://iofaka.com](http://iofaka.com)**

**TG交流群：[https://t.me/joinchat/EJ46bxKHAD-oXG3jWbdteQ](https://t.me/joinchat/EJ46bxKHAD-oXG3jWbdteQ)**






