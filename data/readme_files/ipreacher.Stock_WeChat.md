# Stock_WeChat

微信股价预警提示.

This package supports only Python 3.x.

如果这些对你有帮助，不妨通过 [微信](http://ol5pvu2w5.bkt.clouddn.com/wechat.JPG) 或 [支付宝](http://ol5pvu2w5.bkt.clouddn.com/Alipay.JPG) 对我打赏.

## Installation

    $ pip install Stock_WeChat

## Update

    $ pip install -U Stock_WeChat

## How to Use

### 登陆个人微信

    >>> from Stock_WeChat import sw
    >>> sw.login()
    Getting uuid of QR code.
    Downloading QR code.
    Please scan the QR code to log in.
    Please press confirm on your phone.
    Login successfully as ipreacher


### 开启推送模式
* 每 3 秒推送一次
* 支持最多 30 支股票同时推送
* 关键词：['股票代码', 最低预警价格, 最高预警价格]

```
>>> sw.push(['000001', 10, 11, '000002', 20, 21])
Stock_WeChat 已开始执行！
22:46:06
000001 当前价格为 9.500
低于最低预警价格
000002 当前价格为 20.720
价格正常
***** end *****
```

### 开启提醒模式
* 每 3 秒获取一次股价
* 如果超过预警价格则发送信息至微信
* 支持最多 30 支股票同时推送
* 关键词：['股票代码', 最低预警价格, 最高预警价格]

```
>>> sw.remind(['000001', 10, 11, '000002', 20, 21])
Stock_WeChat 已开始执行！
22:48:07
000001 当前价格为 9.500
低于最低预警价格
000002 当前价格为 20.720
价格正常
***** end *****
```

## Comments

You can commit an Issue if you have any question or suggestion.


## License

MIT
