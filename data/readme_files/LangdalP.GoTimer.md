# GoTimer
A simple external bomb-timer for CS:GO, written in Python. You will not get vacced using this, because it uses [Valve's public gamestate integration](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration). Now has an easy-to-use installer for Windows users.

## NOTE:
On December 17 2015, Valve released a patch that makes the "bomb planted" event randomly delayed. This signals that they don't want players to use this type of aid. Because of it, this program will not be developed further, but feel free to use it in it's current state. I will still work with the game state integration API to see what other cool stuff can be done with it.

## Demonstration
[![A simple video demo](http://img.youtube.com/vi/tEdAwi1Hqbk/0.jpg)](http://www.youtube.com/watch?v=tEdAwi1Hqbk)

Click image to see a small clip of GoTimer in action.

## How to get started:

**For Windows users:**

1. Download the latest installer here: https://github.com/LangdalP/GoTimer/releases (installer with cfg)
2. Unzip the file 
3. Install the program. Don't uncheck "Install Python" unless you already have Python 3.
4. Put the file called **gamestate_integration_go_timer.cfg** in X:\PATH_TO_STEAM\steamapps\common\Counter-Strike Global Offensive\csgo\cfg , where PATH_TO_STEAM is where your steam folder is.
5. Start the program from your start-menu. If CS:GO was launched before you copied the cfg-file, you have to restart it.

**For Ubuntu users:** 

Credits to [testiclopz](https://www.reddit.com/user/testiclopz) for parts of this how-to. It is assumed that python3 is already installed.

1. In the terminal: sudo apt-get install python3-tk
2. Unzip the folder from github anywhere you want
3. Place the gamestate_integration_go_timer.cfg from the listener folder into your cfg folder. The path is typically ~/.steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg
4. Use the terminal, and make sure that your current directory is in the unzipped folder
5. Type *python3 go_timer.py* to launch the program

## Credits
The GameState-listener is inspired by [csgo-c4-hue](https://github.com/doobix/csgo-c4-hue).

I also got some valuable tips from the [Quick Start guide to CS:GO Game State Integration](https://github.com/tsuriga/csgo-gsi-qsguide).

Lastly, a shout-out to [Double0negative for being the first (?) to do this](https://github.com/Double0negative/CSGO-HUD).
