threebody
=========
## What is it?

Threebody is a virtual currency trade system written by [littlkfc](https://github.com/littlekfc). It supports almost all main trade platform including [OkCoin](https://www.okcoin.cn/), [BTCChina](https://www.btcc.com/), [Huobi](https://www.huobi.com/), [BTC-e](https://btc-e.com/) and [Chbtc](https://www.chbtc.com/). 

The system's trade strategy is very simple. If 'A' trade market's buy price is higher then 'B' trade market's sell price, it sell the coin at 'A' and buy the equal amount coin at 'B'. 

## How to use it?
It runs under python environment. Firstly, git clone it & fetch the related python library through pip.
```
git clone https://github.com/littlekfc/threebody.git
cd threebody
pip install -r requirements.txt
```
###Configures
In config directory, there are two config file with `init` suffix, copy them & remove `init` suffix.
```
cp accounts.py.init accounts.py
cp constant.py.init constant.py
```
All accounts information is in `accounts.py` file, you need to config at least two trade platform.
The trade control configure in in `constant.py` file. You can use the default settings at begining.
###Run
```
python threebody.py
```
###Monitor
The log is created in current directory. You can `tail` it to monitor the status.  

