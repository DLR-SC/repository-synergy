==============
Python Warrior
==============

This is a Python port of ryanb's `Ruby Warrior`_.

.. _Ruby Warrior: https://github.com/ryanb/ruby-warrior

This is a game designed to teach the Python language and artificial intelligence in a fun, interactive way.

You play as a warrior climbing a tall tower to reach the precious Python at the top level. On each floor you need to write a Python script to instruct the warrior to battle enemies, rescue captives, and reach the stairs. You have some idea of what each floor contains, but you never know for certain what will happen. You must give the Warrior enough artificial intelligence up-front to find his own way.

Getting Started
===============

First install the package.

::

  pip install pythonwarrior

Then run the "pythonwarrior" command to setup your profile. This will create a pythonwarrior directory in your current location where you will find a player.py file in your profile's directory containing this:

::

  class Player(object):
      def play_turn(self, warrior):
          return None  # Your code here

Your objective is to fill this "play_turn" method with commands to instruct the warrior what to do. With each level your abilities will grow along with the difficulty. See the README in your profile's directory for details on what abilities your warrior has available on the current level.

Here is a simple example which will instruct the warrior to attack if he feels an enemy, otherwise he will walk forward.
 
::

  class Player(object):
    def play_turn(self, warrior):
      if warrior.feel().is_enemy():
        warrior.attack_()
      else:
        warrior.walk_()

Once you are done editing player.py, save the file and run the "pythonwarrior" command again to start playing the level. The play happens through a series of turns. On each one, your "play_turn" method is called along with any enemy's.

You cannot change your code in the middle of a level. You must take into account everything that may happen on that level and give your warrior the proper instructions from the start.

Losing all of your health will cause you to fail the level. You are not punished by this, you simply need to go back to your player.py, improve your code, and try again.

Once you pass a level (by reaching the stairs), the profile README will be updated for the next level. Alter the player.py file and run pythonwarrior again to play the next level.


Scoring
=======

Your objective is to not only reach the stairs, but to get the highest score you can. There are many ways you can earn points on a level.

* defeat an enemy to add his max health to your score
* rescue a captive to earn 20 points
* pass the level within the bonus time to earn the amount of bonus time remaining
* defeat all enemies and rescue all captives to receive a 20% overall bonus

A total score is kept as you progress through the levels. When you pass a level, that score is added to your total.

Don't be too concerned about scoring perfectly in the beginning. After you reach the top of the tower you will be able to re-run the tower and fine-tune your warrior to get the highest score. See the Epic Mode below for details.


Perspective
===========

Even though this is a text-based game, think of it as two-dimensional where you are viewing from overhead. Each level is always rectangular in shape and is made up of a number of squares. Only one unit can be on a given square at a time, and your objective is to find the square with the stairs. Here is an example level map and key.

::

   ----
  |C s>|
  | S s|
  |C @ |
   ----
  
  > = Stairs
  @ = Warrior (20 HP)
  s = Sludge (12 HP)
  S = Thick Sludge (24 HP)
  C = Captive (1 HP)


Commanding the Warrior
======================

When you first start, your warrior will only have a few abilities, but with each level your abilities will grow. A warrior has two kinds of abilities: actions and senses.

An action is something that effects the game in some way. You can easily tell an action because it ends in an underscore. Only one action can be performed per turn, so choose wisely. Here are some examples of actions.

::

  warrior.walk_
    Move in given direction (forward by default).

  warrior.attack_
    Attack the unit in given direction (forward by default).

  warrior.rest_
    Gain 10% of max health back, but do nothing more.

  warrior.bind_
    Bind unit in given direction to keep him from moving (forward by default).

  warrior.rescue_
    Rescue a captive from his chains (earning 50 points) in given direction (forward by default).


A sense is something which gathers information about the floor. You can perform senses as often as you want per turn to gather information about your surroundings and to aid you in choosing the proper action. Senses do NOT end in an underscore.

::

  warrior.feel
    Returns a Space for the given direction (forward by default).

  warrior.health
    Returns an integer representing your health.

  warrior.distance
    Returns the number of spaces the stairs are away.

  warrior.listen
    Returns an array of all spaces which have units in them.


Since what you sense will change each turn, you should record what information you gather for use on the next turn. For example, you can determine if you are being attacked if your health has gone down since the last turn.


Spaces
======

Whenever you sense an area, often one or multiple spaces (in an array) will be returned. A space is an object representing a square in the level. You can call methods on a space to gather information about what is there. Here are the various methods you can call on a space.

::

  space.is_empty
    If true, this means that nothing (except maybe stairs) is at this location and you can walk here.
  
  space.is_stairs
    Determine if stairs are at that location
  
  space.is_enemy
    Determine if an enemy unit is at this location.
  
  space.is_captive
    Determine if a captive is at this location.
  
  space.is_wall
    Returns true if this is the edge of the level. You can't walk here.
  
  space.is_ticking
    Returns true if this space contains a bomb which will explode in time.

You will often call these methods directly after a sense. For example, the "feel" sense returns one space. You can call "captive" on this to determine if a captive is in front of you.

::

  warrior.feel().is_captive()


Epic Mode
=========
  
Once you reach the top of the tower, you will enter epic mode. When running pythonwarrior again it will run your current player.py through all levels in the tower without stopping.

Your warrior will most likely not succeed the first time around, so use the -l option on levels you are having difficulty or want to fine-tune the scoring.

::

  pythonwarrior -l 3

Once your warrior reaches the top again you will receive an average grade, along with a grade for each level. The grades from best to worst are S, A, B, C, D and F. Try to get S on each level for the ultimate score.

Note: I'm in the process of fine-tuning the grading system. If you find the "S" grade to be too easy or too difficult to achieve on a given level, please add an issue for this on GitHub.


Tips
====

If you ever get stuck on a level, review the README documentation and be sure you're trying each ability out. If you can't keep your health up, be sure to "rest" when no enemy is around (while keeping an eye on your health). Also, try to use far-ranged weapons whenever possible (such as the bow).

Remember, you're working in Python here. Don't simply fill up the "play_turn" method with a lot of code. Organize it with methods and classes. The player directory is set up as a load path so you can include other python files from your player.py file.

Senses are cheap, so use them liberally. Store the sensed information to help you better determine what actions to take in the future.

Running "pythonwarrior" while you are in your profile directory will auto-select that profile so you don't have to each time.

If you're aiming for points, remember to sweep the area. Even if you're close to the stairs, don't go in until you've gotten everything (if you have the health). Use far-ranged senses (such as look and listen) to determine if there are any enemies left.

Make sure to try the different options you can pass to the pythonwarrior command. Run "pythonwarrior --help" to see them all.

Versions
========

0.0.8
-----

* Minor documentation updates

0.0.7
-----

* Fix bug where ticking captives don't explode after being hurt by detonate
* Add command line options

0.0.6
-----

* Add epic mode
* Fix bug when a user rests at full health

0.0.5
-----

* Add intermediate towers

0.0.4
-----

* Fix bug with finding the instructions README
* Fix bug with towers path finding init files

0.0.3
-----

* Fix bug with towers folder not being packaged

0.0.2
-----

* Fix towers not being found on first play

