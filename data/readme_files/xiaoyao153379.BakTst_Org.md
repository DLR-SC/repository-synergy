# BakTst_Org
中文reademe：[传送门](https://github.com/xiaoyao153379/BakTst_Org/blob/master/readme_chinese.md)
>Introduction: BakTst_Org is a prototype of the backtesting system used for BTC quantitative trading.
----
![mind Mapping](https://github.com/xiaoyao153379/BakTst_Org/blob/master/picture/mind_Mapping.png?raw=true "result")
This readme is mainly divided into the following parts:
* What kind of person is suitable for studying BakTst_Org?
* import library
* BakTst_Org's framework and various modules of the framework
* How to use BakTst_Org?
* Extension
* Question
* Results map
* Some ideas for the future
* Thanks list
---
### What kind of person is suitable for studying BakTst_Org?
BakTst_Org is just a prototype, so the rows of code is not large. It's about four hundred lines. But it also has all the features you need, such as: multi-process, simulation, a crawler that obtain trading data.

So it is suitable for these people:
* Python enthusiast
* Script developer
* Financial enthusiasts
* Quantify traders
### Library to be imported
Talib, multiprocessing, pandas, json, numpy, time, requests
### BakTst framework and introduction to each module of the framework
BakTst_Org mainly divides six modules:
* craw (crawler module)
* Feed (data acquisition module)
* Strategy (strategy module)
* Portfollio (position management module)
* Execution (order execution module)
* main function
#### craw
This module is a separate module, and the API called is the bittrex api, which is mainly used to obtain transaction data and then write to the txt file.

Api: https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=usdt-btc
If you want to obtain a transaction data of a currency, you only need to modify the last *usdt-btc* transaction pair. For example: 'usdt to ltc', you can modify it to *usdt-ltc*.

The time limit for getting is 60 requests per minute, so a `time.sleep(1)` is added.

The data that I obtained is divided into two files, one is the complete transaction data that includes details of each transaction, and the other is consisted of a time period information that includes the highest price, the lowest price, the opening price, the closing price, the transaction volume and the time.

For the format of the data, please checking the value of the two txt files in the ‘craw/’ path.

#### Feed

This module is used to transfer the transaction data and the initialized data into BakTst. 

The initialized data includes these parameters:
* data: The highest price, lowest price, opening price, closing price, time, and the transaction volume in a period of time. And the format is dataframe.
* coin_number: The number of coins already owned by us. 
* principal:  The principal already owned by us.
#### Strategy
This module is used to analyze the transaction data to predict the trend of price. Firstly it receives the transaction data from the Feed module. Secondly, it will analyze the transaction data through some function in Strategy module. Thirdly, it will sets buy_index (buy index) and sell_index (sell index). Lastly, it will transport the buy_index and the sell_index to Portfollio module.

The total structure of the Strategy module includes two parts. The one is 'Strategy.py' that is writed Strategic judgment, and the other one is 'Strategy_fun.py' file that writed two strategic functions, and a format conversion function.

#### Portfollio
This module is used to manage position. Although we have judged the buying and selling trend, we need to limit the position. For example, we can set a limiting that the proportion of the position must less than 0.5. So, this module plays a limiting role. Then, the opening and selling signals will be sent to the next one--Execution module. 

There are the meaning of some parameters:
* buy_amount and sell_amount: It is a fixed rate to trade. The fixed rate may not be same in the real situation, but we just use a software to trade.
* trade_sigle: It is a trading signal. The ‘sell’ is for sale. The ‘buy’ is for purchase. The ‘None’ is for inaction. In the subsequent code, that is a judgment basis.
* judge_position: It is standard to judge position, and the value is less than 1.

#### Execution
This module is used to execute an order to simulate the real situation about trading. And it will eventually return a total profit and loss. 
There are the meaning of some parameters:
* tip: Handling fee.
* buy_flap: The slippage of buying.
* sell_flap: The slippage of selling.
* buy_last_price and sell_last_price: the last price of trading.

#### Main function
This module is used to convert the data of the txt document into the data of the dataframe format and send it to the whole system. Finally, the system will return a final number of the coin and the number of the principal. Then, it will compares the initial price and final price to calculate profit and loss. 
There are the meaning of some parameters:
* earn: earn.
* lose: loss.
* balance: no loss, no profit.

### How to use BakTst_Org
* Firstly, you need to collect data by using the craw.py file in the craw module.
* Secondly, you need to run the BakTst_Org.py file to see the output.
### Extension
* Dynamic variable: Some values is fixed, such as  principal, position and handling fee. But there are some values ​​that can be dynamically changed, such as slippage, single billing amount.
* Function of the 'Strategy_fun.py' in Strategy module: I just wrote two functions, but you can add more.
### Question
There are two questions that I met:
* I have met a problem about naming coverage. The **open** is a function in python, and I use `with open (addr , 'w') as w:` already, so there was a mistake when I use 'open' to representative the 'open price'.
* It is a problem acout Multi-process. I used the Multi-process pool. But when I add the method in class to the Multi-process pool, I found out that I can't call them. Finally, I can call these methods, but I need to run multiple processes on the outside of class.
### Results map
![result1](https://github.com/xiaoyao153379/BakTst_Org/blob/master/picture/1.png?raw=true "result")
![result2](https://github.com/xiaoyao153379/BakTst_Org/blob/master/picture/2.png?raw=true "result")
### Some ideas for the future
I published BakTst_Org, and everyone can reference from it. But if it is used to trade in the real quantitative transaction, it can't. I will develop a quantitative trading system that can be used to trade in the real quantitative transaction based on BakTst_Org.
### Thanks list
* Thanks to everyone in 慢雾区远不止狗币技术群, helped me solve some programming problems.
* Thanks to greatshi. Greatshi,a master in the field of quantitative trading. He patiently answered some questions that I met. Thank you.