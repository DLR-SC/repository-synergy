[![JetBrains team project](http://jb.gg/badges/team.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

This is a tool to convert color schemes from TextMate to IntelliJ Platform
based products such as IntelliJ IDEA, RubyMine and PyCharm.

Since the way highlighting works in TextMate is not an exact match for
the capabilities of IntelliJ Platform, we try to perform an intelligent
mapping between the two. In particular, color definitions not existing in
TextMate are remapped from the default IntelliJ color scheme based on the
background color used in the TextMate theme, to ensure that the resulting
text is readable.

The table of the mappings is not yet complete; additions and corrections
are very much welcome.

Note that the tool requires Python version 2.7. The default version of
Python installed on MacOS X Snow Leopard is 2.6; you'll need to use Python 
from MacPorts/Homebrew if you'd like to run the tool on 10.6.
