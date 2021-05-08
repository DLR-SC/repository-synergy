# pet-chain-buyer
百度莱茨狗抢购脚本，采用多线程查询购买，支持调用API识别验证码，Google tesseract-ocr识别验证码以及手动输入验证码三种方式，代码持续优化中

# 项目介绍
最近百度上线的莱茨狗区块链宠物( [项目地址](https://pet-chain.baidu.com/) )支持买入卖出操作，使用本脚本的目的就是找到下图中的低价狗，迅速买入，然后高价卖出，通过低买高卖来积累微积分

![image](https://github.com/Acamy/Images/blob/master/2018-02-07_095853.png)


# 使用方法
- 配置好需要的依赖库
- 用自己的headers替换config目录下headers.txt文件内容
- 编辑config/config.ini文件配置不同种类狗的最高买入价格以及是否自动填写验证码

### 1. 手动输入验证码
##### a. 先在命令行执行 `python pic.py`，加载验证码，当有新的验证码时会及时刷新

![image](https://github.com/Acamy/Images/blob/master/4.png)

##### b. 然后执行`python pet-chain.py`

![image](https://github.com/Acamy/Images/blob/master/2.png)

### 2. 调用ShowApi识别验证码
( [API使用地址](https://www.showapi.com/api/view/184) )，该API识别率还是非常高的，花1毛钱即可体验，平均识别时间2-3秒，如下图：

![image](https://github.com/Acamy/Images/blob/master/2018-02-07_153002.png)

##### a. 修改config/config.ini里ShowAPI为中的appid和sign为自己的
##### b. 然后执行`python pet-chain.py`
![image](https://github.com/Acamy/Images/blob/master/2018-02-07_152735.png)

### 3. 自动输入验证码
##### a. 修改config/config.ini的isAuto为True

##### b. 执行`python pet-chain.py`
现在自动输入验证码正确率比较低，建议采用第一种方式，后续进行代码优化

参考 [pet-chain](https://github.com/yanwii/pet-chain) 项目