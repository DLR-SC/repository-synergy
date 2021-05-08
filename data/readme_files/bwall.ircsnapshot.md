ircsnapshot
===========

Tool to gather information from IRC servers

<pre>$ python ircsnapshot.py
usage: ircsnapshot.py [-h] [options] server [port]

IRCSnapshot v0.9
Gathering information from IRC servers
By Brian Wallace (@botnet_hunter)

Options:
  -n --nick NICK                Set nick of bot
  -u --user USER                Set user of bot
  -r --real REAL                Set real name of bot
  -x --ssl                      SSL connection
  -p --password PASS            Server password
  -c --channels #chan1,#chan2   Additional channels to check
  --proxy SERVER[:PORT]         SOCKS4 proxy to connect through
  -o --output Directory         Output directory (default .)
  -t --throttle 1.0             Seconds to sleep before sending commands (default 1)

  -h --help                     Print this message

</pre>

Output
======
The UI writes the contents of the log, but the primary output is to a json file in the executing directory.
<pre>
server.log.txt - Log file
server.json - JSON encoded list of links visible to connecting user
{
    'links': [], // List of link metadata
    'linkList': {}, // Dictionary of links and users connected to them
    'channels': {}, // Dictionary of channels and their metadata
    'userList': {}, // Dictionary of channels and users in them
    'users': {}, // Dictionary of users and their whois data
    'userDetails': {} // Dictionary of parsed details from user's whois
}
</pre>

Output to.gexf.py
=================
Output from to.gexf.py can be loaded in Gephi.  If the IP information is parsable, the output will include coordinates for Geolocation plugins for Gephi to plot to create an image like the following.

![Sample 1 botnet mapped](https://raw2.github.com/bwall/ircsnapshot/master/ircsnapshot/example.png)
![Sample 2 botnet mapped](http://openbwall.com/static/images/fi/allnet.link.png)
![Sample 3 botnet graphed](http://openbwall.com/static/images/fi/irc.byroenet.com.UserToChannel.png)

Support Scripts
===============
<pre>$ python to.gexf.py
usage: to.gexf.py [-h] [options] conversion input

to.gexf v0.1
Convert IRCSnapShot output to Gephi compatible format
Gexf output is to STDOUT
By Brian Wallace (@botnet_hunter)

Conversion Types:
  UserToLink                    Show relation between users and links
  UserToChannel                 Show relation between users and channels

GPS:
  -m MaxMind Location           Location of Maxmind database files (default .)

  -h --help                     Print this message

You can get Maxmind databases from Maxmind.com.
Free database: http://geolite.maxmind.com/download/geoip/database/GeoLiteCity_CSV/GeoLiteCity-latest.zip

</pre>

Notes
=====
Please report any issues you encounter.  This tool has proven to be useful in a few cases so I decided it would be good to publish.

Proxy support currently is just for SOCKS5.  This is compatible with Tor.  I will add more proxy support in the future.  DNS queries will be sent through the proxy.

To Do
=====
 * Session management (restoring after being banned, crashes, etc)
 * Set limit of channels to resolve per connection
 * Multiple connections with jobs across sesssions
 * Add optional CTCP queries
 * More scripts to parse data post scan
 * to.gexf.py to include a UserToGPS to create bot heat maps
 * More fail over states in to.gexf.py
 * Support multiple network inputs to to.gexf.py
 * Merge Maxmind databases as included file (add licensing)
