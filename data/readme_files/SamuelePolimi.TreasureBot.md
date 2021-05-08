# TreasureBot

## Overview

Probably everybody who studied machine learning thought how to use it to solve financial problem (buy and sell stocks perhaps). A very interesting article shows how to do it with direct reinforcement Learning [1]. We try to impement the idea presented in the article with some slight modification (LSTM instead of recurrent neural network, for example) and some innovative techniques.


## Installation Dependencies:
* Python 2.7 or 3
* TensorFlow 0.8.0
* Numpy 1.11.0
* Requests 2.18.4

## How to Run?

    python -m examples.lstm_example
(An example on how lstm network works in combination with Direct Reinforcement Learning)

    python utils/csvToNpy.py
(How to generate a proper dataset)

## Where to retreive Csv to use with csvToNpy.py?

[https://www.dukascopy.com/swiss/english/marketwatch/historical/](https://www.dukascopy.com/swiss/english/marketwatch/historical/)

From this website you can download different dataset with different precision (hourly, daily, evenevery minute or second).
With csvToNpy you can "merge" different datasets (the program will sincronize the dataset, so will be good to choose the same date-time period for the datasets).

## TODO LIST

TODO List:

* Plot different plots to discover some trends:
 * how perform lstm with different number of LSMTCells? 
 * how perform lstm with different network size?
 * how perform lstm with different series length?
 * how perform lstm with different dropout?

* Collect stasistics about the input data:
 * how much decrease or decrease the given stock price over the time unit? (For example, if stock is alwais "flat", there is noway to gain money)
 * how much seems to have a time dependency?
 * how much seems different stocks to depend each others?
 * ...

* Collect statistics about the agent
	We cannot afford only on performance but:
 * how many times the agent loose money? Is it risky?
 * how much does the agent gain over time? (0.0001% in one month will be not that much ;-) )
 * let's plot its behaviour
 * ...

* New optimizers:
 * Genetic algorithms (maybe to find good parameters for lstm)
 * FQI and DirectRl iterations
 * FQI with exponential averages over time?

* Future problems:
	our agent will just give us a suggestion on what to buy and when, but of course we cannot only afford to it:
	if we don't have enough money for example, we can't buy something just because the agent say it
	we will need a program that given the actual amount of money, knows when to use the suggestion gave by the agent, or not.
	Actually this is again an optimization problem (how to use money if different stocks are suggested to buy, given the fact that there is a commission to pay?) - This seems to be a linear programming problem :)

## References

[1] **Deep Direct Reinforcement Learning for Financial Signal Representation and Trading** [IEEE 2016]
