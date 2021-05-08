# pyautotrade
股票自动化交易

## 简介
用于华泰证券通达信版, 软件可以一次监控5只股票，根据条件下单。每次下单耗时小于2s。如果有疑问，或是建议,QQ群讨论：486224275

## 使用说明
* 开发环境是win10 64bit, python3 64bit、pywin32、tushare。当然32bit python3也可以的
* 软件共有3个文件，`pyautotrade.pyw`主程序，`stockInfo.dat`存盘文件，`winguiauto.py`是封装的winapi函数
* 交易软件启动后，依次点击按钮`买入-卖出-撤单-成交-持仓-刷新`，及左边的`对买对卖`，然后启动本程序，不要再切换到其它界面，始终在`对买对卖`界面上
* 不写时间条件单，默认时间为凌晨1点。时间条件满足后才检查价格条件，如果只想要时间条件单而忽略价格条件单，可以写个始终满足条件的价格。
* 股票数量为100的倍数, 如果输入150股将作为100股。默认为0股，也就说，股票数量由交易软件自动填写，当然需提前在交易软件里设定好，在`系统设置-仓位策略`里选择固定数量, 见图5
* 时间为24小时制，形式为 `时：分：秒`， 每项都必须写， 后面的写法是错误的： `13：30`
* 交易软件的委托价格由交易软件自动填写，在`系统设置-自动策略`， 启用`启用自动跟盘`， 自己决定选哪个价格

## 版本
* v 0.01 修正了股票价格实时显示问题
* v 0.02 重构了交易软件接口，目前在最小化状态下也可以下单，下单速度加快，增加委托日志
* v 0.03 重新布局了控件，修改委托日志控件。修复了少许Bug
* v 0.04 重新布局了控件，重构了monitor函数。现在一次可以下4个条件单
* v 0.05 加入时间条件单
* v 0.06 交易软件接口函数单独放winguiauto文件
* v 0.07 时间条件单和价格条件单相结合，添加保存和载入功能,存档和主文件在同一目录下，名为stockInfo.dat，是个二进制文件
* v 0.08 代码清理，添加了注释。现在可以同时监控5只股票
* v 0.09 加入自动刷新功能，每隔10分钟刷新一次，防止软件进入待机状态
* v 0.10 修改了几个bug
* v 0.11 交易函数改用Operation类重写。现在可以获取持仓，成交，资金等信息, 下单时的价格改由交易软件填写


-----------------------------------
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting1.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting2.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting3.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting4.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting5.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting6.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/setting7.png)
![image](https://github.com/drongh/pyautotrade_tdx/raw/master/Logo/trading.png)