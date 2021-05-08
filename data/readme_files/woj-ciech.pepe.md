# PEPE - Post Exploitation Pastebin Emails
Collect information about leaked email addresses from Pastebin

![](https://github.com/woj-ciech/pepe/blob/master/imgs/pepe.png?raw=true)

## About
Script parses Pastebin email:password dumps and gather information about each email address. It supports Google, Trumail, Pipl, FullContact and HaveIBeenPwned. Moreover, it allows you to send an informational mail to person about his leaked password, at the end every information lands in Elasticsearch for further exploration.

**It supports only one format - email:password.**

**Everything else will not work!**

For now, notification works when it finds match on FullContact and next sends you email address and associated social media accounts.

## Requirements:
- Python 3
- FullContact API https://www.fullcontact.com/developer/
- Google
- Pipl API https://pipl.com/api/
- HaveIBeenPwned
- SafePush (for notification - optional - In progress) https://www.pushsafer.com/
- Trumail https://trumail.io/
- Gmail account (sending emails)
- Elasticsearch (optional) 

```python
pip install -r requirements
```

## Config
```
{"domains": 
	{ #domains to whitelist or blacklist
	"whitelist": [""],
	"blacklist": ["yahoo.com"]
},
"keys": 
	{ #API KEYS
	"pushsafer": "API_KEY",
	"fullcontact": "API_KEY",
	"pipl": "API_KEY"
},
"gmail": 
	{ #GMAIL credentials and informational message that will be send
	"username": "your_username@gmail.com",
	"password": "password",
	"message": "Hey,\n\nI am a security researcher and I want to inform you that your password !PASSWORD! has been leaked and you should change it immediately.\nThis email is part of the research, you can find more about it on https://medium.com/@wojciech\n\nStay safe!"},
"elasticsearch":
	{ #ElasticSearch connection info
	"host": "127.0.0.1",
	"port": 9200}
}
```

## Usage
```python
root@kali:~/PycharmProjects/pepe# python pepe.py -h
usage: pepe.py [-h] [--file FILE] [--stream] [--interactive]
                 [--modules MODULES [MODULES ...]] [--elasticsearch]
                 [--whitelist] [--blacklist]

                            ,=.
              ,=''''==.__.="  o".___
        ,=.=="                  ___/
  ,==.,"    ,          , \,===""
 <     ,==)  "'"=._.==)    `==''    `"           `

  clover/snark^
  http://ascii.co.uk/art/platypus
  
  Post Exploitation Pastebin Emails
  github.com/woj-ciech
  medium.com/@woj_ciech
  
  Example:
  python pepe.py --file <dump.txt> --interactive --whitelist
  python pepe.py --file <dump.txt> --modules hibp google trumail --elasticsearch --blacklist

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           Load file
  --stream              Stream Pastebin
  --interactive         Interactive mode
  --modules MODULES [MODULES ...]
                        Modules to check in non-interactive mode
  --elasticsearch       Output to ElasticSearch
  --whitelist           Whitelist
  --blacklist           Blacklist
```

## Example
Interactive mode, each email is checked individually and specific module is executed.
```
root@kali:~/PycharmProjects/pepe# python pepe.py --file paste.txt --interactive --blacklist

-----------------------Found email [REDACTED]@hotmail.com with password [REDACTED]-----------------------
[A] Add domain hotmail.com to blacklist
[T] Test
[G] Google search
[H] HaveIBeenPwned
[P] Pipl
[F] FullContact
[I] Inform
[N] Next
> G
---Google Search---
http://[REDACTED]
http://[REDACTED]
http://[REDACTED]

[A] Add domain gmail.com to blacklist
[T] Test
[G] Google search
[H] HaveIBeenPwned
[P] Pipl
[F] FullContact
[I] Inform
[N] Next
> N
-----------------------Found email [REDACTED].[REDACTED]@gmail.com with password [REDACTED]-----------------------
[A] Add domain gmail.com to blacklist
[T] Test
[G] Google search
[H] HaveIBeenPwned
[P] Pipl
[F] FullContact
[I] Inform
[N] Next
> F
---FullContact---
[REDACTED] [REDACTED]
https://twitter.com/[REDACTED]
https://facebook.com/[REDACTED]
https:/linkedin.com/[REDACTED]
[A] Add domain gmail.com to blacklist
[T] Test
[G] Google search
[H] HaveIBeenPwned
[P] Pipl
[F] FullContact
[I] Inform
[N] Next
> P
---Pipl---
Name: [REDACTED]
[REDACTED] years old
Jobs:
Quality Control [REDACTED] (since 2018)
[REDACTED] Review [REDACTED] (2017-2018)
[REDACTED] Attorney [REDACTED] (2017-2018)
[REDACTED] Attorney at [REDACTED] (2017-2017)
...
[REDACTED] (2012-2012)
[REDACTED] Assistant at [REDACTED] (2012-2012)
Author/Founder at [REDACTED] (2009-2011)
https://www.linkedin.com/in/[REDACTED]
http://www.facebook.com/people/[REDACTED]
http://twitter.com/[REDACTED]
http://pinterest.com/[REDACTED]
https://plus.google.com/[REDACTED]

...
[REDACTED]
```
Non-interactive mode, when only choosen modules are executed against email addressess.
```
root@kali:~/PycharmProjects/# python pepe.py --file pastetest.txt --blacklist --modules hibp google fullcontact trumail --elasticsearch
-----------------------Found email [REDACTED]@hotmail.com with password [REDACTED]-----------------------
---Google Search---
https://pastebin.com/[REDACTED]
---Have I Been Pwned---
LinkedIn
---FullContact---
No results
---Trumail---
Email test passed
-----------------------Found email charlie.[REDACTED]@live.com with password [REDACTED]-----------------------
---Google Search---
https://justpaste.it/[REDACTED]
https://pastebin.com/[REDACTED]
---Have I Been Pwned---
MyHeritage
RiverCityMedia
Tumblr
YouveBeenScraped
---FullContact---
Charlie [REDACTED]
https://twitter.com/[REDACTED]
[REDACTED]
---Trumail---
Email test passed
-----------------------Found email [REDACTED].[REDACTED]@gmail.com with password [REDACTED]-----------------------
---Google Search---
http://[REDACTED]
http://[REDACTED]
http://[REDACTED]
https://pastebin.com/[REDACTED]
---Have I Been Pwned---
BTSec
Exactis
HauteLook
Houzz
LinkedIn
---FullContact---
[REDACTED] [REDACTED]
https://www.facebook.com/[REDACTED]
[REDACTED]
---Trumail---
Email test passed
-----------------------Found email [REDACTED].[REDACTED]@gmail.com with password [REDACTED]-----------------------
---Google Search---
https://[REDACTED]
https://[REDACTED]
https://[REDACTED]
https://pastebin.com/[REDACTED]
---Have I Been Pwned---
Lastfm
LinkedIn
MySpace
Trillian
Tumblr
---FullContact---
[REDACTED] [REDACTED] [REDACTED].
https://www.facebook.com/[REDACTED]
https://plus.google.com/[REDACTED]
https://www.linkedin.com/in/[REDACTED]
http://www.pinterest.com/[REDACTED]
https://twitter.com/[REDACTED]
https://youtube.com/user/[REDACTED]
[REDACTED]
```
## Screens
![](https://github.com/woj-ciech/pepe/blob/master/imgs/pipl.jpg?raw=true)

![](https://github.com/woj-ciech/pepe/blob/master/imgs/kibana.jpg?raw=true)

![](https://github.com/woj-ciech/pepe/blob/master/imgs/email.jpg?raw=true)
## Other
I'm not responsible for any damage caused.
You know, it was made for educational purposes.
