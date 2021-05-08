# TcpRoute

TcpRoute, TCP 层的路由器。对于 TCP 连接自动从多个线路(允许任意嵌套)、多个域名解析结果中选择最优线路。

通过 socks5 代理服务器提供服务。目前支持直连及 socks5 代理线路。

已经使用 go 重写，地址：https://github.com/GameXG/TcpRoute2/


## windows 安装

有二进制文件发布，直接下载 dist/tcpRoute.exe 、dist/config 修改配置并执行即可。

## linux 安装

```bash
$ sudo pip install greenlet gevent dnspython
$ vi config.json  # 修改配置
$ python tcpRoute.py
```

## 配置

config.json 为配置文件，json格式。

```json
{
  "log_level":"INDO",
  "port":7070,
  "nameservers":"system",
  "nameservers_backup":["8.8.8.8","8.8.4.4","208.67.222.222","208.67.220.220"],
  "upstream":
  {
    "type":"multipath",
    "list":
    [
      {
        "type":"direct",
        "source_ip":"0.0.0.0",
        "source_port":0
      },
      {
        "type":"socks5",
        "host":"127.0.0.1",
        "port":5555,
        "upstream":
        {
          "type":"direct",
          "source_ip":"0.0.0.0",
          "source_port":0
        }
      }
    ]
  },
  "IpBlacklist":[]
}
```
"logLevel":"INDO", 为日志级别。一般 INFO 即可，调试时可以使用 DEBUG 。

port 为对外提供代理服务的端口。目前只支持 socks5 无密码 协议。浏览器等代理服务器填写 127.0.0.1 ，端口填写这个端口号，协议选择 socks5 即可。

nameservers 、nameservers_backup 为DNS解析服务器地址，在 nameservers 解析出错时会启用 nameserversBackup 解析。
支持过滤域名纠错，支持过滤部分DNS欺骗，在 nameservers 解析错误后会尝试 TCP DNS协议。

可选的格式：
* "system"   使用系统DNS解析
* "8.8.8.8"  使用 "8.8.8.8" 解析
* ["8.8.8.8","208.67.222.222"]   使用两个服务器进行解析

upstream 为使用上级代理。支持代理服务器嵌套，多代理自动选择等功能。

"type":"multipath", 类型表示本上层代理为多代理聚合，负载均衡策略为对每个连接自动选择最快的线路连接目标网站。"list" 是上层代理服务器列表。

"type":"direct", 表示直连，可以指定源地址。在多线路(电信+联通)时可以通过指定多个源地址配合路由器实现自动选路。

"type":"socks5", 表示 socks5 代理，"host" 、 "port" 为上级代理的地址及端口。

TcpRoute multipath 聚合代理会同时尝试使用直连及所有的代理服务器建立连接，最终使用最快建立连接的线路。TcpRoute 会缓存检测结果方便下次使用。

IpBlacklist 为静态 ip 黑名单，黑名单上的ip不会用来建立连接(目前直连线路使用)。一般不需要配置，系统会自动检测异常ip并屏蔽。
格式为["123.123.123.123","456.456.456.456"]



## 具体细节
* 对 DNS 解析获得的多个IP同时尝试连接，最终使用最快建立的连接。
* 同时使用直连及代理建立连接，最终使用最快建立的连接。
* 缓存10分钟上次检测到的最快线路方便以后使用。
* 解析不存在域名获得域名纠错IP，并添加到 IP黑名单
* 使用不存在DNS服务器解析域名，获得异常IP，并添加到 IP黑名单
* 不使用异常的dns解析结果。

## 感谢

* https://github.com/felix021/ssocks5/blob/master/msocks5.py
* http://blog.csdn.net/testcs_dn/article/details/7915505
