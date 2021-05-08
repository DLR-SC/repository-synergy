TDM1001系列电压电流表上位机
=======================

使用 Python 快速编写的串口上位机软件
![](https://github.com/harry159821/TDM1001UpMachine/raw/master/shot.png)

# 关于电表串口协议
TDM1001系列数显表头UART-RS232接口协议V2.1

| 功能           | 发送的串口数据    | 返回值            |
| -------------- |:-----------------:| -----------------:|
| 控制连接请求   | AA 55 02 F1 00 F3 | AA 55 02 F3 00 F5 |
| 控制断开请求   | AA 55 02 F2 00 F4 | AA 55 02 F3 00 F5 |
| 读取设备信息   | AA 55 02 F3 00 F5 | AA 55 08 F5 XX XX A0 A1 A2 A3 XX XX |
| 采样速率设置   | AA 55 03 F8 SPSx XX XX | AA 55 02 F3 00 F5 | 
| 波特率设置     | AA 55 03 F9 BRx XX XX  | AA 55 02 F3 00 F5 |

状态数据 14 03 02 00 XX crcL crcH


| XX | 功能 | 
|----|------|
| 00 | 充电 |
| 01 | 放电 |
| 02 | 闲置 |
| 03 | 待机 |
| 04 | 错误 |

# Requirement
* Python 2.7.10
* PyQt4

# 源码文件说明
* 核心程序

    UpMachine.py SerialUi.py SerialDev.py

* Py2exe 打包配置文件

    Makefile.py MakeFile.bat

# 联系我
* https://github.com/harry159821/
* Mail:harry159821@gmail.com
* QQ:984405219
