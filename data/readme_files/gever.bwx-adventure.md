bwx-adventure
=============

A simple module for writing text adventure games in Python.

This module posits a text adventure World made up of Locations. Locations are
linked by Connections and sometimes contain Things. The player is represented
by a Hero object that has a current location. The command parser is simple but
is easily extended with new commands.

This was initially written in support of the Orange Band at <a href="http://sfbrightworks.org">SF Brightworks</a>.

Contributions are welcome! Open an issue or a pull request.

```python
from advent import *

# setup the game you are going to build on...
game = Game()

# create some locations
sidewalk = game.new_location(
"Sidewalk", """
There is a large glass door to the east.
The sign says 'Come In!'
""")

vestibule = game.new_location(
"Vestibule", """
A small area at the bottom of a flight of stairs.
Up the stars you see the reception desk.
""")

# make connections between those locations
big_door = game.new_connection("Big Door", sidewalk, vestibule, [IN, EAST], [WEST, OUT])

# create some things to put in your world. You need a name and
pebble = sidewalk.new_object("pebble", "round pebble")
elev_key = sidewalk.new_object("key", "small tarnished brass key")

# simple verb applicable at this location
sidewalk.add_verb(Say('The door makes a hollow sound.', 'knock'))

# Add an animal to roam around.  Animals act autonomously
cat = sidewalk.add_actor(Animal("cat"))
cat.add_verb(Say("The cat purrs.", "pet"))

# make the player starting on the sidewalk
hero = game.new_player(sidewalk)

# add a new hero verb (allows player to say "throw pebble")
def throw(self, actor, noun, words):
  if noun and self.get_verb('drop').act(actor, noun, words):
     print 'The %s bounces and falls to the floor' % noun
     return True
  else:
     print 'You hurt your arm.'
     return False

hero.add_verb(Verb(throw, "throw"))

# start playing (hey, there's a key here!)
game.run()
```
