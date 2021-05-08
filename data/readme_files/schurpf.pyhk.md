This project is not maintained anymore. There is a Python 3 version here: [https://github.com/FunkMastaZ/pyhk3](https://github.com/FunkMastaZ/pyhk3)


# PYHK

PYHK is python module that allows for simple hotkey registration in any program.
It extends pyhook to have normal hotkey functionality like autohotkey (AHK) scripts.

Main features:
* Simple hotkey registration
* Hotkey removal by hotkey or id
* Option to run trigger function in thread
* Option to run trigger function on a key up event

Tested with Python 2.6, 2.7

Total downloads before moving to github: 2562

PYHK is as simple as this:

```python
import pyhk
 
def fun():
    print "Do something"
 
#create pyhk class instance
hot = pyhk.pyhk()
 
#add hotkey
hot.addHotkey(['Ctrl', 'Alt','7'],fun)
 
#start looking for hotkey.
hot.start()
```

## Documentation
http://www.schurpf.com/python/python-hotkey-module/pyhk-end-user-documentation/

## Old version
http://www.schurpf.com/python/python-hotkey-module/#download

## Dependencies
[Pyhook](http://sourceforge.net/apps/mediawiki/pyhook/index.php?title=Main_Page)

## Links

http://www.schurpf.com/python/python-hotkey-module/                        		- Project home page
http://www.schurpf.com/python/python-hotkey-module/pyhk-end-user-documentation/     - End user documentation

## Contact Author

michael at schurpf dot com
Please write in English or German only.

##K nown Issues

Python IDLE freezes at times. Best use is to call your script directly from the command line with python YOURSCRIPT.py.

After logout or sleep on some machines the hotkeys get triggered by only pressing the modifiers.

## Alternatives

[https://github.com/IronManMark20/hooked](https://github.com/IronManMark20/hooked)

## License

Distributed under GNU General Public License version 2.
