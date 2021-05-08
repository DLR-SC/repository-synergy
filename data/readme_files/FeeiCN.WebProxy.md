# WebProxy
> Create an HTTP / HTTPS proxy server based on MITMProxy and log all requests to the log file and parse the log for rewriting into the database.

> 基于MITMProxy创建HTTP/HTTPS代理服务器，并记录所有请求到日志文件，解析日志去重写入数据库。

## Installation（安装）

#### MITMProxy
http://docs.mitmproxy.org/en/stable/install.html

#### Python module
```
cd t1.proxy/
pip install -r requirements.txt
```

## Start Proxy Server (启动代理服务器)

| | |
| --- | --- |
|代理服务器IP | 本机IP（内网外网IP均可）|
| 代理服务器端口 | 8088 |

```
mitmdump -p 8088 -s traffic.py
```

## Config devices proxy (配置各端代理)
> 在各端配置好代理后，访问`http://mitm.it`下载CA证书，并按照以下方式进行验证。

#### iOS
- 打开设置-无线局域网-所连接的Wifi-配置代理-手动
- 填上代理服务器IP和端口
- 打开设置-通用-关于本机-证书信任设置
- 开启mitmproxy选项。

#### Android
- 打开设置-WLAN-长按所连接的网络-修改网络-高级选项-手动
- 填入代理服务器IP和端口
- 打开设置-安全-信任的凭据
- 查看安装的证书是否存在

#### macOS
- 打开系统配置（System Preferences.app）- 网络（Network）- 高级（Advanced）- 代理（Proxies）- Web Proxy(HTTP)和Secure Web Proxy(HTTPS)
- 填上代理服务器IP和端口
- 打开Keychain Access.app
- 选择login(Keychains)和Certificates(Category)中找到mitmproxy
- 点击mitmproxy，在Trust中选择Always Trust


## Start Traffic Stash (去重并入库)
```
# 创建好数据库(编码使用utf8mb4)，并配置MySQL数据库信息
export host="127.0.0.1"
export user="your_username"
export password="your_password"
export database="t1.proxy"

# 启动脚本
python stash.py proxy.mitm
```
