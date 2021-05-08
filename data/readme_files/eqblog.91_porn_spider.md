
# 91主站目前开启了cloudflare，采用了recaptcha验证

目前已增加绕过recaptcha功能，需要anti-captcha.com账户。

增加相应余额后，至此网站的settings->api setup处获取API。

注意：此站非免费，并且不支持国内主流支付方式


# 91_porn_spider使用注意事项：
`本脚本仅支持python3`
# python所需库：
```bash
pip3 install requests
pip3 install python3_anticaptcha
#js解析需要js2py
pip3 install js2py
```
# 使用方法：
```bash
python3 91_spider.py
```
# 视频地址加密解决办法：
暂时使用的是html5分享的视频无加密，可以直接获取视频地址。
目前爬虫已可以正常使用。


# 关于新增cookie的使用
在同目录下创建一个cookie.txt文件
里面内容为cookie，例如：
```
__cfduid=xxx; __dtsu=xxx; AJSTAT_ok_times=xxx; __uid=xxx; __utmz=|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); evercookie_cache=undefined; evercookie_etag=undefined; l91lb91a=1; __utmc=xxx; CLIPSHARE=xxx; __51cke__=; 91username=xxx; whatch_times=xxx; whtch_times=xxx; __utma=xxx; __utmb=50351329.0.10.1528090648; DUID=xxx; USERNAME=xxx; EMAILVERIFIED=xxx;
```

# 关于作者
网站：https://eqblog.com
邮箱：i@t667.com 
