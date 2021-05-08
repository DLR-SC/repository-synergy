== OpenTrader ==

https://github.com/OpenTrading/OpenTrader/

OpenTrader is an Open Source platform to communicate with on-line trading platforms,
and includes the ability to:
* write trading Recipes for multiple back-end testers (1 at the moment :-),
* import data from CSV files or from the web for Backtesting,
* analyze the Backtesting with multiple back-end reviewers (1 at the moment :-),
* save the backtests, along with their parameters in an HDF5 file,
* send and receive data from multiple on-line trading platforms (1 at the moment :-).

This ia a work in progress but it has quite a lot in there already:
* send most Mql4 commands and gets the return values as Python, using the
  Python bridge enabled MetaTrader (https://github.com/OpenTrading/OTMql4AMQP) , or
  ZeroMQ enabled MetaTrader (https://github.com/OpenTrading/OTMql4Zmq) .
* receive bar, tick and timer notifications,  
* send and query orders to Mt4, using a
  better MQL4 trading library (https://github.com/OpenTrading/OTMql4Lib) ,
* there's a backtester for trading recipes based on 
  pybacktest (https://github.com/ematvey/pybacktest/) ,
  using pandas with TaLib (https://github.com/OpenTrading/OpenTrader/wiki/TaLib) ,
  so it's quite fast.
* reads CSV history files and treats everything internally in
  pandas DataFrames or Series,
* there's simple plotting of the CSV files and results using
  matplotlib (http://matplotlib.org) ,
* you can save recipes and backtest results as an HDF5 file,
  viewable by  ViTables (https://github.com/OpenTrading/OpenTrader/wiki/ViTables)
* if you have pyrabbit (http://pypi.python.org/packages/source/p/pyrabbit)
  installed, you can query the AMQP server.

Coming **Real Soon Now(TM)** is:
* wiring up the backtester so that it should soon support Recipes for
  live-trading on Metatrader from Recipes and Chefs.
* there's an optimizer in the backtester, but it's not yet wired up.
For our future directions, see the RoadMap (https://github.com/OpenTrading/OpenTrader/wiki/RoadMap) .

=== Messaging Protocols ===

This project now works with ZeroMQ or RabbitMQ Messaging Protocols.
The ZeroMQ protocol is preferred and all development is currently on it.

**ZeroMQ**: To use ZeroMQ, this project builds on
OTMql4Zmq (https://github.com/OpenTrading/OTMql4Zmq/) ,
and requires that to be installed in your Metatrader as a pre-requisite.
You also must have installed Python and the 
OTMql4Py Python bridge (https://github.com/OpenTrading/OTMql4Py/) and
OTMql4Lib Metatrader library (https://github.com/OpenTrading/OTMql4Lib/) .
OpenTrader runs fine with either the C coded implementation
of ZeroMQ for Metatrader:
OTZmqCmdEA.mq4 (https://github.com/OpenTrading/OTMql4Zmq/raw/master/MQL4/Experts/OTMql4/OTZmqCmdEA.mq4)
or the  or Python implementation
OTPyTestZmqEA.mq4 (https://github.com/OpenTrading/OTMql4Zmq/raw/master/MQL4/Experts/OTMql4/OTPyTestZmqEA.mq4)
.

**RabbitMQ**: To use RabbitMQ, this project builds on
OTMql4AMQP (https://github.com/OpenTrading/OTMql4AMQP/) ,
and requires that to be installed in your Metatrader Python as a pre-requisite.
You also must have installed Python and the 
OTMql4Py Python bridge (https://github.com/OpenTrading/OTMql4Py/) and
OTMql4Lib Metatrader library (https://github.com/OpenTrading/OTMql4Lib/) .
You also must have installed and started a
RabbitMQ server (http://rabbitmq.org) , which is not so easy under Windows.

One day we will make installers for a shrink-wrapped distribution, but
for now, you must clone from github.com and manually install.

{{{OTCmd2}}} is a command line script to run send commands
to a OTMql4Zmq or OTMql4AMPQ enabled Metatrader. It will start
a command loop to listen, send commands, based on the Cmd2 read-eval-print,
or take commands from the standard input, a file, or as command-line arguments.
You will have to call OTCmd2 with the{{{-P}}} option with the
path of your installed Metatrader (e.g. {{{c:\Program Files\Metatrader}}}),
or set the {{{default}}} {{{sMt4Dir}}} setting of the {{{OTCmd2.ini}}} file,
or add your installed OTMql4Py Python directory to the {{{PYTHONPATH}}}
environment variable (e.g. {{{c:\Program Files\Metatrader\MQL4\Python}}}).

=== Work in Progress ===

**This is a work in progress - a developers' pre-release version.**
It has been fully checked in, and there is a test-suite based on the
examples that provides good coverage, but the internal APIs may change.

The project wiki should be open for editing by anyone logged into GitHub:
Please report any system it works or doesn't work on in the wiki:
include the Metatrader build number, the origin of the metatrader exe,
the Windows version, and the AMQP server version and version of the Pika.
This code is known to run under Linux Wine (1.7.x), so this project
bridges Metatrader to RabbitMQ under Linux.

* Wiki (https://github.com/OpenTrading/OpenTrader/wiki/Home)
* Installation (https://github.com/OpenTrading/OpenTrader/wiki/Installation)
* Architecture (https://github.com/OpenTrading/OpenTrader/wiki/Architecture)
* Testing (https://github.com/OpenTrading/OpenTrader/wiki/Testing)

* Index (https://github.com/OpenTrading/OpenTrader/wiki/TitleIndex)

----
Parent: Home (https://github.com/OpenTrading/OpenTrader/wiki/Home)
