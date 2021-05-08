Roboraj
==========

This is a simple Twitch chat/irc bot written in python.


Installation
============
* Open up your terminal/shell of choice.
* Install the [http://docs.python-requests.org/en/latest/](Requests library) if you haven't already using `pip install requests`. I tested this application on Python 2.7.5.
* 
* Clone the Git repository.
* Move config/config_example.py to config/config.py. Replace all of the placeholders there with your own username/oauth token/channels to join etc (tips are given in the file).
* Type `chmod +x /serve.py`. To run, you simply need to execute the file by typing `./serve.py`.


Adding your own commands
========================

You're going to need to know basic Python if you want to add your own commands. Open up `lib/command_headers.py`. There are examples of pre-made commands in there as examples. The limit parameter is the amount of times a command can be used in seconds, if you don't want a limit to be enforced put in 0.

If your command is only going to return a string, ex - `!hello` returns `Welcome!`, don't include the `argc` parameter. Place the string you wish to be returned to the user in the `return` parameter. For example, if you wanted to create a command such as this and limit it to being used ever 30 seconds, you would add in:

```python
'!hello': {
		'limit': 30,
		'return': 'Welcome!'
}
```

However, if your command has to have some logic implemented and if the command is just going to return whatever a function returns, set the `return` parameter on the command to `command`, and set `argc` to `0`. If your command is going to take arguments, ex `!hello <name>`, set argc to `1` or however many arguments the command is going to take in.

Make a new file in `lib/commands/` and give the filename `command.py` where command is the command name. If your `argc` was set to `0`, don't include `args` in the functions parameters, else set the only parameter to `args`. Args will contain a list of whatever arguments were passed to the command.

This command will contain whatever logic needs to be carried out. You should validate the arguments in there. After you have the response that you want a user to see, just `return` it.

Let's say we want to add a command which will take two arguments, we will call it `!random` and it will take a `minimum` and `maximum` argument. We will limit this command to be allowed to be called every 20 seconds.

Add the following to the `commands` dictionary:

```python
'!random': {
		'limit': 20,
		'argc': 2,
		'return': 'command'
}
```

And then in `lib/commands/random.py` , write the following: 

```python
import random

def random(args):
  min = args[0]
  max = args[1]
    
  usage = '!random <min> <max>'
  
  # carry out validation
  try:
    return ranrange(min, max)
  except ValueError:
    return '!random <min> <max> (use full integers)'
  except:
    return usage
```

And now if somebody types `!random 5 10` into the chat, the bot will respond with a pseudo-random number between 5 and 10.
