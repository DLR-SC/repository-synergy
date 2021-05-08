# BetBoy - DEPRECATED/NOT WORKING 
Artificial neural networks for predicting results of football(soccer) matches.

Features:

* predicting results of football matches
* predicting odds if not available in update
* automatic updates
* simulations
* statistics (tables, form, series, schedle with odds)
* rating system

program license: Apache License v2

e-mail: jacek87markowski@gmail.com

author: Jacek Markowski

## Requirements:

* Windows:
	* Pyside for Python 2.6 32 bit
	* Python 2.6 32 bit

* Linux:
	* Python 2.6 or 2.7
	* Pyside
	* Pyfann (FANN bindings for Python)

## Installation
Download latest BetBoy release:
[BetBoy download page](https://sourceforge.net/projects/betboy/files/)

Before you can run BetBoy you have to install Python,Pyside and Pyfann(only on linux, included in windows version) on your system.

BetBoy repository is available on [github](https://github.com/jacekm-git/BetBoy).

### Windows
Download and install [Python 2.6 32 bit](http://www.python.org/ftp/python/2.6/python-2.6.msi)

Download and install [Pyside for Python 2.6 32 bit](http://download.qt-project.org/official_releases/pyside/PySide-1.2.1.win32-py2.6.exe)

To run BetBoy just double click on bet_boy.py
### Linux - Ubuntu 12.04
Go to Ubuntu software center install :

*  pyside-tools
*  pyfann
	
To run BetBoy open betboy directory in terminal and type 'python bet_boy.py'
## How to use
BetBoy has 8 modules for different tasks:

* Stats central
* Match selector
* Simulator
* Update manager
* Links creator
* Leagues creator
* Export manager
* Learning manager
### [Stats central](https://www.youtube.com/watch?v=XXzGUsWyFT8)
In this module you can check statistics for selected league:

* standings
	* points (overall, home, away)
	* under 2.5
	* over 2.5
	* BTS - both team scored
	* MOW - margin of wins
		* formula: goal diffrence in won matches/played matches
	* MOL - margin of loses
		* formula: goal diffrence in lost matches/played matches
	* BB rating - BetBoy rating:
		* win: 3 points + (opponent points(scaled to [0,1]) + opponent form(scaled to [0,1]))/2
		* draw: 1 point + (opponent points(scaled to [0,1]) + opponent form(scaled to [0,1]))/2
* form
* schedle
* matches of selected teams
* series of selected teams
* predictions and odds:
	* 1 - home team to win
	* x - draw
	* 2 - away team to win
	* 1x - draw or home team to win
	* x2 - draw or away team to win

*(predictions are made only for upcoming match day not whole round, if you take predictions from day after upcoming match day it will be inaccurate and won't be included in simulation for accuracy check)

### [Match selector](https://www.youtube.com/watch?v=sSwNXzk1V90):
This module allows to generate list of upcoming matches for selected leagues based on criteria defined in filters (series, odds).

### [Simulator](https://www.youtube.com/watch?v=9--Cf9QBotU) - perform simulation to select bets
Here you can perform batch simulations for selected leagues,nets and filters. Slecet league filters, net andd click button 'add' to add selected items to list.
To run simulation click button 'run'. After all simulations
you will be taken to selected bets tab and checks if any bets matching filters criteria where selected.

r_min - minimal round to start simulation

r_max - maximum round where stop simulation

* ##### [Match filters](https://www.youtube.com/watch?v=W8cE2HYc-6Y) 
Here you can define filters for matches: points diffrences, form diffrences (between home team and away team) and series(wins, loses, draws etc.)
For example:when you select series wins home => 1 for home team in simulation will be included only matches where home team has 1 or more home wins streak.
When you select points > 30 for home team in simulation will be included only matches where home team points are 30% or more (home team points and away team points = 100%)
[You can also filter matches by odds](https://www.youtube.com/watch?v=qsLCX8uT6hU)

* ##### [Net ranges](https://www.youtube.com/watch?v=9--Cf9QBotU)
Here you can define how program will transform ann output(from -1 to 1) for bet (1,1x,x,x2,2)
For example:
net ranges are:
1 min=-1 max=-0,3
x min=-0,3 max=0,3
2 min=0,3 max=1
neural networks gives number -0,79382
so program gives us bet 1 – home to win, beacuse -0,79382 is in range [-1,-0,3]

* ##### Bet filters
Here you can define filters for selecting bets.
In simulation process net accuracy is checked, for example:
net accuracy for 1 bets is: 50% and bet filter for 1 is 60%, so program will ignore bets (1 - home to win) from this net becausse of low accuracy.
Net frequency - sometimes when ranges don't give bets from specifin ann output simulation will give none prediction, for example: there were 100 matches in simulation and 50 matches had no prediction- it means that net frequency is 50%, let's say user defined min net frequency at 60% in this case program will ignore bets from this net.

### [Update manager](https://www.youtube.com/watch?v=UahVBOUsOGY)
* Scrape website - 
This module is for automatic database updates. It uses list of urls to download data from sites.
Before you can update database, you have to prepare file with urls in **links creator**.
	 Select urls base from saved and click load → urls list is dispalyed → select url to update click button add → click button update.

	* [errors](https://www.youtube.com/watch?v=5E4s_C_Tn04):
Sometimes after update some leagues won't work properly. It's caused by to long lines in league file:
for example:
 		* normal line is : 2012.10.10,Real,Arsenal,0,1
 		* broken line is : 2012.10.10,Real,Arsenal,(postponed for blah balah blah.....) - in this case delete this line from file
 		*broken line is : 2012.10.10,Real,Arsenal,(by decision blah blah result; 3:0) - in this case change this line to:
2012.10.10,Real,Arsenal,3,0

	If any errors,there will be created directory data/tmp/leagues (there are stored copies of broken files) and log.txt - shows wchich lines are bad and need manual fixing (for manual fixing i recommend to use notepad++).
After fixing you can copy files from data/tmp/leagues to data/leagues.

### [Link creator](https://www.youtube.com/watch?v=Cs3DwGa6ETw)
* Scrape website

	Here you can create file with list of urls used for updates. On the left of displayed website choose football and select league, go to fixtures **select all matches and week by week**. On the left next to address bar there is text line where you can enter your name for this league, after you give name to league click button '+' to add to list. When you complete picking urls you can save entire list to file. This saved file can be opened in update manager.


### [Leagues creator](https://www.youtube.com/watch?v=j_Ag30E6FVY)
In this module you can manually update leagues or create own leagues.

### [Export manager](https://www.youtube.com/watch?v=mskxkTn8F5c)
Before you can learn artificial neural network(ann) you have to prepare data for learning:

* r_min - minimum round to start export
* r_max - maximum round to stop export

Select leagues on which ann will be trained, give name fof exported file (above export button) and click export button (wait it takes some time dependly on numbers of selected leagues)
During this process data is scaled round by round and saved to file.

There are 145 inputs[in range -1,1] scaled every round for every team and 1 output(-1 - home team won, 0- draw, 1- away team won)

In inputs included are:

* points (overall,home,away)
	* scaled for max and min value available to get in whole season
	* scaled for max and min value actual in table
* form (overall,home,away)
	* scaled for max and min value available to get in whole season
	* scaled for max and min value actual in table
* series (overall,home,away)
* odds
	
### [Learning manager](https://www.youtube.com/watch?v=mskxkTn8F5c)
Select earlier prepared file from exports, set setting for neural network (training algorithm, activation functions, epochs, reports frequency, hidden layer) and click learn, after succesful learning there will be new file in neaural networks. This created net can be used for predicting of matches(you can check in simulation for which leagues it has the best accuracy)
