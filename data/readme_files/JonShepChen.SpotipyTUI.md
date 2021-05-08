# Spotipy-TUI 
[![PyPI version](https://badge.fury.io/py/spotipy-tui.svg)](http://badge.fury.io/py/spotipy-tui)

### Update 7/10/2018: Spotify changed their API in 2017 such that any calls to endpoints now requires access tokens from users. This project currently has not been updated to reflect these changes, and is broken for the time being.

Spotipy-TUI is a text-based UI program to control the Spotify desktop client on OSX. <br>
Requires OSX, Python 3, and the Spotify desktop client. <br>
Run it within a terminal session. <br>

* Make sure the terminal window you are running this program in is big enough! 
* If the terminal window is not large enough, the program can't start up.
* [Quick Demo Video](https://www.youtube.com/watch?v=BYVSOE8mjWs)

## Installation

#### Pip
```bash
$ pip install spotipy-tui
```
If you have both Python 2 and 3 installed, make sure the pip command is pointing to the Python 3 version. 
(or replace 'pip' with whichever command you use to invoke pip for Python 3)

#### Clone Repo
```bash 
$ git clone https://github.com/JonShepChen/SpotipyTUI.git
$ cd SpotipyTUI
$ python setup.py install
```
If you have both Python 2 and 3 installed, make sure the python command is pointing to the Python 3 version.
(or replace 'python' with whichever command you use to invoke Python 3)

## Usage 
```python 
# Start the program
$ spotipy-tui
```
## Command List
* S: Search for music
* I: Jump to song at index within search results
* A: Go to album of current selection
* T: Get current selection's artist's top tracks
* C: Show command list
* F: Bring Up Spotify desktop client
* Y: Change Country ISO Code
* B: Go back one listing in track listing history
* N: Go forward one listing in track listing history
* [Space]: Toggle Play/Pause
* [Enter]: Play track at current cursor position
* [Up]/K: Go Up
* [Down]/J: Go Down
* [Left]/H: Play previous track (based on cursor position)
* [Right]/L: Play next track (based on cursor position)
* O: Lower volume
* P: Increase volume
* V: Set volume level
* Q: Quit

## Dependencies 
```bash
$ pip install requests
```
