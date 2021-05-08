Name:                   PoE ScamBot
Author:                 Tony Lau
System Requirements:    Windows, Python 3.6.0
Dependencies:           requests

PoE ScamBot is a search engine (not an indexer) that maintains a live
search of the Path of Exile stash tab API. Unlike indexers, such as
poe.trade or poeapp.com, ScamBot does not track historical data and
is instead a lightweight parser. Thus, an item may show up multiple
times if the player modified other items in their stash.

Set Up:
1. Install Python 3.6.0 from https://www.python.org/. During
   installation, make sure the "Add Python to PATH" box is checked.
2. Open command prompt as an administrator
3. Run the command "pip install requests"

Usage:
1.  Run scambot.pyw
2.  Under the default settings, simply input the desired parameters
    then press "Start". The app will automatically start searching
    for items with the input parameters.
3.  Start playing Path of Exile.
4.  When the app finds a result, it will play a tone and copy a
    whisper message to your clipboard.
5.  Paste the message into chat and profit!

Fields:
League          - the league that the item should be found in
Maximum Price   - the maximum price that the item should have
Minimum Price   - the minimum price that the item should have
Sockets         - the number of sockets that the item should have
Links           - the number of links that the item should have
Rarity          - the rarity type that the item should have
Allow Corrupted - whether the item can be corrupted
Allow Crafted   - whether the item can be crafted
Search Regex    - the regular expression that should match the item's
                  text. (The item's text is made by concatenating the
                  item's name, implicit mods, and explicit mods.)