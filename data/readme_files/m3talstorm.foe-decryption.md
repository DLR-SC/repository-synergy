# FoE Decryption

Python tool and tutorial of how to decrypt the [Forge of Empires](https://en.forgeofempires.com/) Flash/SWF and generate request signatures

Used by [FoE Bot](https://github.com/m3talstorm/foe-bot) for request signature generation.

*Purely educational and to fuel curiosity*


:exclamation:
This project is no longer maintained by myself as I no longer player FoE, an from what i've heard they have/are switching to a 'HTML5' based solution. This approach may still work but you will need to make sure the version and secret (below) are up to date.
:exclamation:

## Summary
- Binary: https://foeen.innogamescdn.com/swf/Main.swf?1518000888
- Version: 1.119
- Timestamp: 1518000888
- Secret: 6q01Zd9YKTSEVjhtqqGEYjBGr3pUTRFojYL+m2/6GorQ892bVcY4QMoqLbc6A+DhXQEaMtZfkczMgiHt3tVJ4w==

:star: Star the repo if you use this, would be nice to know if people are :) :star:

---

## Explanation

[Forge of Empires](https://en.forgeofempires.com/) is a Flash based web and mobile game. Under the hood it uses simple HTTP requests to fetch data and perform operations whilst the game is being played, to build things, start production, collect resources, etc.

These HTTP requests contain a header called 'Signature' which in turn contains a hash of the request being sent. This is used to sign the request so that the server can verify it hasn't been tampered with and also to make it more difficult to manipulate the request.

If we want to issue our own requests then we also need to generate this signatures, for which we need to know how this hash is generated. To find this out we need to look inside the client.

The game's Flash application is called Main.swf which can be downloaded and run through a flash decompiler like [FFDec](https://www.free-decompiler.com/flash/), however, the Main.swf has been 'tampered' with so that tools like this cannot read them.

As a result of this, the standard Flash player also cannot read/load the SWF, so the 'tampering' needs to be reverted before it can be loaded. This is were Preloader.swf comes into play.

So, same kind of deal, we can open Preloader.swf inside of [FFDec](https://www.free-decompiler.com/flash/) to see how it reverts the 'tampering', however, another layer of 'lets make things difficult' is that Preloader.swf has had its code obfuscated so it is harder to read and follow. Luckily, FFDec can (somewhat) fix this for us, replacing the obfuscated class, method, variable names with things like 'class_1', 'method_5', 'var_11'.

We can then see a file called 'Preloader' with in-turn instances a class called 'class_3' inside of 'package_1' (after the name changes), this class and the methods in it essentially just bit-shift a few specific bytes back to their originals, 'decrypting' the Main.swf (decrypting in a very loose sense of the word).

Then we can search for 'Signature' inside of Main.swf, finding where each and every request is constructed, and then find how the Signature is generated.

The crux of it is, it's just a simple MD5 of the user's key, a static salt (which was 'forgeofempires', now its a random string) and then the request body as JSON, all concatenated together, converted to hex, and then only the first 10 characters are used.

This can be seen inside of 'scripts/de/innogames/shared/networking/providers/JSONConnectionProvider'

- The 'secret' is VERSION_SECRET at the top of the file
- The 'user_key' being the '?h=xxx' bit of each request made to the backend server: 'https://en1.forgeofempires.com/game/json?h=thisistheuserskey'.
- The 'request_body' is just the key-value payload encoded as JSON with spaces removed (the keys must be kept in the same order otherwise this would generate a different hash).
- New versions might change the request body order and/or secret, you can see the 'sudo' version (unix timestamp of when it was released/built?) on the end of the request for the 'Main.swf' file

For example, a request to get the player's great buildings (requestId is just an incrementing number, but doesn't seem to affect anything), in Python:

~~~
import json
import hashlib
from collections import OrderedDict

payload = [OrderedDict([
    ("requestClass", "StartupService"),
    ("requestId", 0),
    ("requestData", []),
    ("__class__", "ServerRequest"),
    ("requestMethod", "getData")]
)]

encoded = json.dumps(payload).replace(' ', '')

user_key = "thisistheuserskey"
# As of 12:00 28/08/2017 UTC (version 1.108 / timestamp 1503565657)
secret = "yOy3qr/HW9NZ9iLXjYLVADMO7wKMZcTgsUVqcqkl+h7ddVER8sHYEH6bxsSJOzerXci2kJKcMM9xQZjmdVD08Q=="

data = user_key + secret + encoded
# This should be the same value you see for the 'Signature' header in the request
signature = hashlib.md5(data).hexdigest()[0:10]
~~~


All-in-all this turned a couple of minutes exercise to craft HTTP requests into a 10-15 minute exercise, not sure it was worth Innogames going through all this trouble to hide it.

---

## HOW-TO

### Fetching FoE SWF files


- Download the two files we are interested in: [Main.swf](https://foeen.innogamescdn.com/swf/Main.swf) and [Preloader.swf](https://foeen.innogamescdn.com/swf/Preloader.swf) (These should be the latest versions)
- These can be seen in the network console of your developer tools when loading the game

### If the 'encryption' algorithm hasn't changed

- git clone https://github.com/m3talstorm/foe-decryption.git
- cd foe-decryption/
- wget "https://foeen.innogamescdn.com/swf/Main.swf" (or copy the downloaded 'Main.swf' file into the 'foe-decryption' directory)
- Run `python src/decryption.py`
- This will take the Main.swf file and decrypted it into 'Main.decrypted.swf'


### If the 'encryption' algorithm changes

- Download [FFDec](https://www.free-decompiler.com/flash/download/)
- Open the 'Preloader.swf' inside of FFDec
- Go to the 'Tools' tab at the top left
- To the far right, select 'Rename Invalid Identifiers' (it will give you a warning...click ok, select 'Type + Number')
- All the variables names should not be readable
- There should be a 'package_1' in the source tree to the bottom right, and a 'class_3' within that, open this file
- This contains the 'decryption' algorithm, we want to 'extract' this and convert it to Python
- The mostly likely things to change is the static ints in 'method_14' and/or the body in 'method_15'
- The static array of (3) ints are renamed 'magic_bytes' and put at the top of 'decryption.py'
- Make the Python class 'Decryption' in 'decryption.py' match the AS3 class inside of class_3


### Opening up Main.swf

- Download [FFDec](https://www.free-decompiler.com/flash/download/)
- Open the 'Main.decrypted.swf' inside of FFDec
- Request signature generation is inside of 'scripts/de/innogames/shared/networking/providers/JSONConnectionProvider'
