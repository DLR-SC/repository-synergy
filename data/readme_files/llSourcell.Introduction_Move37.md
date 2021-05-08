# Overview

This is the code for [this](https://youtu.be/fRmZck1Dakc) video on Youtube by Siraj Raval as part of the move 37 course at School of AI. GridWorld is a test-bed frame for learning about Markov Decision Processes. This project is meant to be a tool for anyone to get started learning about Markov Decision Processes.

## Prerequisites
* Python 3
* `tkinder` for the UI

## Getting Started
The main program to run is `main.py`. This must be supplied with a JSON configuration file to build your GridWorld. See `example.json` for a rudimentary configuration.

Example Usage:
```bash
python3 main.py example.json
```

Click the buttons to step through value iteration or progress in increments of 100. The policy current is shown as arrows at each cell.

## Building Your Own GridWorld
The map descriptor for GridWorld is in the JSON configuration file given to `main.py` on startup. The JSON configuration defines the following parameters:

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `width` | `int` > 0 | width of GridWorld in cells |
| `height` | `int` > 0| height of GridWorld in cells |
| `initial_value` | `float` | initial value to populate all values with |
| `discount` | 0 ≤ `float` ≤ 1 | discounting factor for compute future expected rewards |
| `living_cost` | `float` ≤ 0 | cost subtracted from each value at each iteration |
| `obstacles` | `list` of indices (`list`) | cells that we consider to be non-traversable obstacles |
| `transition_distribution` | `dict` with `float`s for `"forward"`, `"left"`,`"right"`,`"backward"` | transition function; adjacent tiles only; must sum to 1! |
| `terminals` | `list` of objects with `"state"` (index `list`) and `"reward"` (`float`) | terminal states and their associated rewards |

__There is no input validation so unexpected behavior will occur for unreasonable values, e.g., a negative width or height. YOU HAVE BEEN WARNED!__

## License
This project is licensed under the MIT License. In other words, do whatever you want with it! Just remember to give appropriate credit :-)

## Credits
Credits for this code go to [mohitd](https://github.com/mohitd/gridworld). I've merely created a wrapper to get people started. 
