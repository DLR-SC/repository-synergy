![alt text](Images/facebook_cover_photo_2.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CodeFactor](https://www.codefactor.io/repository/github/misterbianco/boopsuite/badge)](https://www.codefactor.io/repository/github/misterbianco/boopsuite)

### Synopsis:

BoopSuite is a wireless testing suite with extensible and independent components.

Need to hop wireless channels?         ... ✅

Need to only work with beacon packets? ... ✅

Need to Monitor Deauth requests?       ... ✅

### Both a library and a toolset

Enumerate wireless interfaces

```
sudo python3 -m boop interface
```

Need additional information about a wireless interface?

```
sudo python3 -m boop interface {INTERFACE} -vvvv
```

Changing a cards mode

```
sudo python3 -m boop mode {INTERFACE} {monitor|managed}
```

### The suite mimics flask!

```python
#!/usr/bin/env python3

import boop
import time

app = boop.BoopSniff(boop.WIRELESS_DEVICES[0])
app.packets = 0

@app.handler(boop.MGMT_DEAUTH)
def pkt(self, p):
    self.packets += 1
    return

@app.handler(boop.MGMT_BEACON)
def pkt(self, p):
    self.packets += 1
    return

app.run()
```

Import the modules you need, add handlers for the packets you want and parse away.

List of all packet types:

* MGMT_ASSOC_REQ
* MGMT_ASSOC_RESP
* MGMT_REASSOC_REQ
* MGMT_REASSOC_RESP
* MGMT_PROBE_REQ
* MGMT_PROBE_RESP
* MGMT_BEACON
* MGMT_ATIM
* MGMT_DISASSOC
* MGMT_AUTH
* MGMT_DEAUTH
* CTRL_POLL
* CTRL_RTS
* CTRL_CTS
* CTRL_ACK
* CTRL_CFEND
* CTRL_CFECFA
* DATA_ANY

### Note:

I use this project personally for my wireless endeavours,
feel free to use, modify and extend.

# Requirements:

+ python3
+ Now uses Poetry for library management

# Installation:

#### To install open a terminal and type:

```
* work in progress adding to pypi
```

# Motivation:

I am motivated by the want to be better. To prove others wrong and to prove
to myself that I can do things that were previously impossible to me.

# In Progress:

+ Code Fixes will be happening.
+ More functional API and better imports
+ recreating the old boopsuite sniffer in the __main__ file
+ argparsing for said file

# License:

Logos are all free to use.

MIT License
(c) MisterBianco, 2017-2019
