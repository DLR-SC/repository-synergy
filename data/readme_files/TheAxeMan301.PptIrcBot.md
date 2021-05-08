PptIrcBot
=========

IRC bot for a TAS project

`theaxebot.py` is the main program.

You can use readpipe.py to print out the pipes that go to tasbot and replay.

    python readpipe.py replay_pipe
    python readpipe.py tasbot_pipe

Source for bad-words.txt is here, modified for the context of this project:
https://www.cs.cmu.edu/~biglou/resources/bad-words.txt

`pptcontrol.py` is the interface for the replay.

The replay code should import the BitStreamer class. It should then create an
object of that class, giving it the name of the pipe that the chat bot is
writing to. The BitStreamer will launch an async I/O thread to manage that
interface. The replay code should use the getNextBits() method to get the chat
input. The result will be a 16-bit integer encoded as described at the top of
that file. If there is nothing incoming from chat then the result is a no-op.

To run a test, open a terminal and run 'python writepipe.py'.
In a separate terminal run 'python pptcontrol.py'. It should print
out a stream of input with some debugging.
