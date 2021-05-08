
# Angler

![anglerfish](https://raw.githubusercontent.com/juancarlospaco/anglerfish/master/temp.jpg "Ugly but Enlightening")

*Ugly but Enlightening* | https://pypi.python.org/pypi/anglerfish

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/anglerfish.svg)](https://pypi.python.org/pypi/anglerfish)
[![Build Status](https://img.shields.io/travis/juancarlospaco/anglerfish/master.svg)](https://travis-ci.org/juancarlospaco/anglerfish)


# Description of functions

##### make_logger
<details>

`anglerfish.make_logger(name, when='midnight', filename=None, interval=1,
                backupCount=100, slog=True, stder=True, crashandler=None,
                emoji=False, color=True, maxMegaBytes=1)`

**Description:** Returns a Logger, that has Colored output, logs to STDOUT, logs to Rotating File,
it will try to Log to Unix SysLog Server if any, log file is based on App name,
if the App ends correctly it will automatically ZIP compress the old unused rotated logs,
Colored output may not be available on MS Windows OS,
this should be the first one to use, since others may need a way to log out important info, you should always have a logger.
Do not worry too much about the Arguments for `make_logger()`, the only required is `name`.
Please use a unique and distinctive name for your app, and use the same name every time Angler needs an app name.

**Arguments:**
- `name` is a unique name of your App, like a unique identifier, string type.
- `when` is one of 'midnight', 'S', 'M', 'H', 'D', 'W0'-'W6', optional will use 'midnight' if not provided, string type.
- `single_zip` Unused Old Rotated Logs will be ZIP Compressed automagically, `True` equals 1 ZIP per Log, `False` equals 1 ZIP for *All* Logs, lets the user choose if you want a single ZIP or one per log file.
- `filename` log filename path or None, optional, defaults to `None`, `os.path.join(gettempdir(), name.lower().strip() + ".log")` will be used if left as `None`, log filename path on use will be printed to stdout automatically, string type.
- `backup_count` number of log backups to keep, optional, defaults to `100`, meaning 100 backups, integer type.
- `emoji` Kitten Emoji on logger *(ala [Yarn](https://yarnpkg.com) )*, Optional, defaults to `False`, boolean type.
- `backupCount` Maximum number of backup copy old rotated unused logs to keep.
- `slog` `True` to try to use systems SysLog server, if any, works Ok if no SysLog is found working on the system, optional, boolean type, defaults to `True`.
- `stder` `True` to try to use systems Standard Output to log, optional, boolean type, defaults to `True`.
- `crashandler` `True` to try to use a crashandler for Core Dumps and Critical errors, optional, defaults to `None`, advanced use, [see this Doc](https://devdocs.io/python~3.6/library/faulthandler#faulthandler.enable).
- `color` `True` to use Pretty Colored Logs, optional, boolean type, defaults to `True`.
- `maxMegaBytes` Maximum Megabytes of the Log files, when the log is bigger than this file size on Megabytes it gets automatically Rotated, 1 Megabyte of plain text is a lot of text, optional, boolean type, defaults to `1`.


**Keyword Arguments:** None.

**Returns:** logging.logger object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/__init__.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import make_logger
>>> log = make_logger("MyAppName")
Logger created with Log file at: /tmp/myappname.log.
>>> log.debug("This is a Test.")
This is a Test.
>>> log.info("This is a Test.")
This is a Test.
>>> log.warning("This is a Test.")
This is a Test.
>>> log.critical("This is a Test.")
This is a Test.
>>> log.exception("This is a Test.")
This is a Test.
```
</details>



##### get_free_port
<details>

`anglerfish.get_free_port(port_range: tuple=None)`

**Description:** Returns a free unused port number integer.
If Argument is `None`, then it ask for an OS-Provided Random port number,
since this is *the best practice* from OS and inter-operability point of view.
If Argument is provided, it takes a tuple of 2 positive integers as argument,
being the range of port numbers to scan.
When you ask for a free unused port number on your code try to use it ASAP,
since it can get taken at any moment by any other App running on the system.

**Arguments:**
- `port_range` is the range of port numbers to scan, starting port and ending port numbers. 2 items only are allowed, optional, Tuple type, eg. `(8000, 9000)`, defaults to `None`.

**Keyword Arguments:** None.

**Returns:** Integer, a free unused port number.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_free_port.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_free_port
>>> get_free_port()
Found free unused port number: 8000
8000
```
</details>



##### make_notification
<details>

`anglerfish.make_notification(title: str, message: str="", name: str="", icon: str="", timeout: int=3000))`

**Description:** Makes a Passive Notification Bubble (Passive Popup), it works cross-desktop, using one of DBus, PyNotify, notify-send, kdialog, or zenity.
Should degrade nicely on operating systems that dont have any of those.
Best results are with D-Bus.

**Arguments:**
- `title` is the short title of your message, mandatory, string type.
- `message` is body of your message, defaults to empty string, optional, string type.
- `name` is the name of your App, defaults to empty string, optional, string type.
- `icon` is the icon name of your App, defaults to empty string, optional, string type.
- `timeout` is the timeout for your notification bubble, defaults to `3000`, optional, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_notification.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import make_notification
>>> make_notification("test")
Sending Notification message via D-Bus API.
```
</details>



##### bytes2human
<details>

`anglerfish.bytes2human(integer_bytes: int)`

**Description:** Returns a Human Friendly string containing the argument integer bytes expressed as KiloBytes, MegaBytes, GigaBytes (...).
This function does *Not* use `for` loops so its super fast, even for Yottabytes.
Its basically a Bytes to 'Kilo', 'Mega', 'Giga', 'Tera', 'Peta', 'Exa', 'Zetta' and 'Yotta'.

**Arguments:**
- `bites` is the number of bytes, integer type, required.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/bytes2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import bytes2human
>>> bytes2human(3284902384)
"3 Gigabytes"
```
</details>



##### check_encoding
<details>

`anglerfish.check_encoding(check_root: bool=True)`

**Description:** Checks the all the Encodings of the System and Logs the results, to name a few like `STDIN`, `STDERR`, `STDOUT`, FileSystem, `PYTHONIOENCODING`,
`PYTHONLEGACYWINDOWSFSENCODING`, `PYTHONLEGACYWINDOWSSTDIO`  and Default Encoding,
takes no arguments, requires a working Logger, all "UTF-8" should be ideal on Linux/Mac/Windows.

**Arguments:**
- `check_root` Check for root/Administrator privileges, optional, boolean type.

**Keyword Arguments:** None.

**Returns:** Bool, `True` if everything is Ok.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_encoding.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import check_encoding
>>> check_encoding()
Default Encoding: utf-8.
STDIN   Encoding: UTF-8.
STDERR  Encoding: UTF-8.
STDOUT  Encoding: UTF-8.
I/O File Systems Encoding: utf-8.
PYTHONIOENCODING Encoding: ???.
PYTHONLEGACYWINDOWSFSENCODING Encoding: ???.
PYTHONLEGACYWINDOWSSTDIO      Encoding: ???.
Default File Systems Encode Errors:     surrogateescape.
True
```
</details>



##### check_folder
<details>

`anglerfish.check_folder(folder_to_check: str=Path.home().as_posix(),
                 check_space: int=1)`

**Description:** Checks a working folder from `folder_to_check` argument for everything that can go wrong,
like no Read Permissions, that the folder does not exists, and no space left on it, etc etc. Returns Boolean.

**Arguments:**
- `folder_to_check` path of the folder to check, string type.
- `check_space` Check for a minimum of disk space, Units are GigaBytes, Defaults to at least 1Gb, optional, integer type.

**Keyword Arguments:** None.

**Returns:** `True` if everything is Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_folder.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import check_folder
>>> check_folder("/path/to/my/folder/")
Checking the Working Folder: "/path/to/my/folder/"
Folder Total Free Space: ~88 GigaBytes.
True
```
</details>



##### get_clipboard
<details>

`anglerfish.osx_clipboard`

**Description:** Cross-platform cross-desktop Clipboard functionality, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** A `typing.NamedTuple` object, with type hinting, `clipboard_copy()` and `clipboard_paste()`.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_clipboard.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_clipboard
>>> clipboard_copy, clipboard_paste = get_clipboard()
Querying Copy/Paste Clipboard functionality.
>>> clipboard_copy("This is a Test.")
>>> print(clipboard_paste())
"This is a Test."
>>> # Or this way:
>>> get_clipboard().copy("This is a Test.")
>>> print(get_clipboard().paste())
"This is a Test."
```
</details>



##### beep
<details>

`anglerfish.beep(waveform: tuple=(79, 45, 32, 50, 99, 113, 126, 127))`

**Description:** A "Beep" sound, a Cross-platform sound playing with Standard Lib only, No Sound file is required,
like old days Pc Speaker Buzzer Beep sound, meant for very long running operations and/or headless command line apps,
it works on Linux, Windows and Mac and requires nothing to run.

**Arguments:** `waveform` tuple containing integers, as the sinewave for the beep sound,
defaults to `(79, 45, 32, 50, 99, 113, 126, 127)`, optional.

**Keyword Arguments:** None.

**Returns:** `True` is sound playing went Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_beep.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :question:         | **Windows** | Untested    |

**Usage Example:**

```python
>>> from anglerfish import beep
>>> beep()
Generating and Playing Sound...
Playing raw data '/tmp/beep.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
True
```
</details>



##### json_pretty
<details>

`anglerfish.json_pretty(json_dict: dict)`

**Description:** Pretty-Printing JSON data from dictionary to string, very human friendly representation,
similar to YML but still valid JSON, works perfectly with JavaScript too.

**Arguments:** `json_dict` a dict with data that will be converted to JSON and pretty-printed as string.

**Keyword Arguments:** None.

**Returns:** string, the JSON data.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_json_pretty.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import json_pretty
>>> json_pretty({"foo": True, "bar": 42, "baz": []})
Pretty-Printing JSON data string...
'\n\n{\n    "bar":  42,\n\n    "baz":  [],\n\n    "foo":  true\n}\n'
```
</details>



##### log_exception
<details>

`anglerfish.log_exception()`

**Description:** Log Exceptions but pretty printing with a lot more information of whats going on under the hood,
returns a string printing it via a working logger at the same time,
works for Exceptions like on `try...except...finally` constructions, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** string, the info about the exception.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_log_exception.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import log_exception
>>> try:
>>>     0 / 0
>>> except Exception:
>>>     log_exception()

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero

################################ D E B U G ###############################
Listing all Local objects by context frame, ordered by innermost last:

The Unnamed Anonymous Module Function from file <stdin> at line 4 failed!.
Unnamed Anonymous Module Function
|
|___ __name__ = '__main__'  # Type: <class 'str'>, Size: 57Bytes, ID: 139686962655984
|___ __annotations__ = {}  # Type: <class 'dict'>, Size: 64Bytes, ID: 139686962997360
|___ __builtins__ = <module 'builtins' (built-in)>  # Type: <class 'module'>, Size: 61Bytes, ID: 139686982977000
|___ make_logger = <function make_logger at 0x7f0b613650d0>  # Type: <class 'function'>, Size: 60Bytes, ID: 139686852317392
|___ log = <RootLogger root (Level -1)>  # Type: <class 'logging.RootLogge, Size: 52Bytes, ID: 139686951311120
|___ log_exception = <function log_exception at 0x7f0b657dba60>  # Type: <class 'function'>, Size: 62Bytes, ID: 139686924106336

Thats all we know about the error, check the LOG file and StdOut.
############################### D E B U G #############################
```
</details>



##### ipdb_on_exception
<details>

`anglerfish.ipdb_on_exception(debugger: str="ipdb", limit: int=100)`

**Description:** Automatic iPDB Debugger when an Exception happens,
it install a handler to attach a post-mortem ipdb console on an exception on the fly at runtime,
PDB, iPDB can be used as Debugger console.
`ipdb` Python package must be installed for `ipdb` option to work.

**Arguments:**
- `debugger` one of `"ipdb"`, `"pdb"`.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_pdb_on_exception.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import ipdb_on_exception
>>> ipdb_on_exception()
Installing an automatic Debugger upon Exceptions...
```
</details>



##### seconds2human
<details>

`anglerfish.seconds2human(ttimestamp_on_seconds: int, iso_sep: str=" ")`

**Description:** From Time on seconds to very human friendly string representation,
calculates time with precision from seconds to days, returns the string with representation.

**Arguments:**
- `time_on_seconds` time on seconds, integer type.
- `do_year` `True` to calculate Years, optional, defaults to `True`, bool type.
- `unit_words` dictionary with words representing human Time units,
useful for internationalization of the output string, defaults to English, optional, dict type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import seconds2human
>>> seconds2human(490890)
'05 Days 16 Hours 21 Minutes 30 Seconds'
```
</details>



##### timedelta2human
<details>

`anglerfish.timedelta2human(timestamp_on_seconds: int, iso_sep: str=" ")`

**Description:** Convert a TimeDelta object to human string representation.
From `timedelta` object to very human friendly string representation,
calculates time with precision from seconds to years, returns the string with representawation.
Internally is just a shortcut to `anglerfish.seconds2human()`.

**Arguments:**
- `time_delta` timedelta object, `datetime.timedelta` type.
- `do_year` `True` to calculate Years, optional, defaults to `True`, bool type.
- `unit_words` dictionary with words representing human Time units,
useful for internationalization of the output string, defaults to English, optional, dict type.

**Keyword Arguments:** None.

**Returns:** string, human friendly representation.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> import datetime
>>> from anglerfish import timedelta2human
>>> deltatime_object = datetime.timedelta(seconds=123.456789)
>>> timedelta2human(deltatime_object)
'02 Minutes 03 Seconds'
```
</details>



##### set_process_name
<details>

`anglerfish.set_process_name(name: str)`

**Description:** Set the current process name to the argument `name`,
so instead of all your apps listing as `python` on the system monitor they will have proper names,
this helps debug, troubleshooting and system administration in general.
Its very recommended you use the same string passed to `anglerfish.make_logger()`

**Arguments:**
- `name` the name of your app, string type.

**Keyword Arguments:** None.

**Returns:** `True` if it can change the process name, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_process_name.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import set_process_name
>>> set_process_name("MyApp")
True
```
</details>



##### walk2list
<details>

`anglerfish.walk2list(folder: str, target: tuple, omit: tuple=(),
              showhidden: bool=False, topdown: bool=True,
              onerror: object=None, followlinks: bool=False)`

**Description:** Perform full recursive walk of `where` folder path,
search for `target` like files, ignoring `omit` like files, follow symbolic links if `links` is `True`,
convert the output to `tuple` if `tuply` is `True`, else return the `list` containing the path of all the files.
Using a named tuple the maximum limit of items on that tuple is `255` because of the under low level Python implementation,
on CPython < 3.7 it will cause `SyntaxError: more than 255 arguments` if more than `255` items on the tuple,
[on CPython >= 3.7 this has been fixed allowing more than `255` items on that tuple](https://bugs.python.org/issue18896),
this is not an Angler Bug but a limitation of Python itself.

**Arguments:**
- `where` path to a folder to scan, string type.
- `target` type of files to search for, for example `.py`, string type.
- `omit` type of files to ignote, for example `.pyc`, string type.
- `links` a Boolean, `True` to follow simbolic links, optional, defaults to `False`, boolean type.
- `tuply` a Boolean, `True` to convert the output `list` into a `tuple`, optional, defaults to `True`, boolean type.
- `namedtuple` String or None, string to use as the name of the `NamedTuple`, convert the output `tuple` into a `NamedTuple`, optional, defaults to `None`, string type.

**Keyword Arguments:** None.

**Returns:** `list` or `tuple` or `NamedTuple`

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2list.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import walk2list
>>> walk2list(".")
("file.py", "readme.md")
```
</details>



##### walk2dict
<details>

`anglerfish.walk2dict(folder: Path, topdown: bool=True,onerror: object=None, followlinks: bool=False,
 showhidden: bool=False, strip: bool=False)`

**Description:** Return Nested Dictionary that represents the folders and files structure of the folder,


**Arguments:**
- `folder` path to folder to scan, string type.
- `links` a Boolean, `True` to follow simbolic links.
- `showhidden` a Boolean, `True` to show hidden files and folders.
- `strip` a Boolean, `True` to strip the relative folder path.
- `jsony` a Boolean, `True` to convert the `dict` to JSON.
- `ordereddict` a Boolean, `True` to convert the `dict` to `OrderedDict`.

**Keyword Arguments:** None.

**Returns:** `dict` or `str` with JSON.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/walk2dict.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import walk2dict
>>> walk2dict(".")
```
</details>



##### multiprocessed
<details>

`anglerfish.multiprocessed(function: Callable, arguments: object, cpu_num: int=1, thread_num: int=1, timeout: int=None)`

**Description:** Execute code on multiple CPU Cores and multiple Threads per CPU Core,
with optional Timeout, on a quick and easy way.

**Arguments:**
- `function` a function of Callable type to execute code,
- `arguments` is an object that represent the arguments for the function,
- `cpu_num` how many CPU Cores to use, integer type,
- `thread_num` how many Threads per CPU Core to use, integer type,
- `timeout` a Timeout on Seconds, integer type or None.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multiprocess.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import multiprocessed
>>> import time
>>>
>>> def process_job(job):  # a simple function for testing only
>>>     time.sleep(1)
>>>     count = 100
>>>     while count > 0:
>>>         count -= 1
>>>     return job
>>> jobs = [str(i) for i in range(30)]  # a simple list
>>> print(multiprocessed(process_job, jobs, cpu_num=1, thread_num=4))
>>> print(multiprocessed(process_job, jobs, cpu_num=4, thread_num=1))
```
</details>



##### threads
<details>

`@threads(n: int, timeout=None)`

**Description:** Execute code on multiple Threads, with optional Timeout, on a quick and easy way.

**Arguments:**
- `n` number of Threads to use for the function execution, integer type, required.
- `timeout` a Timeout on seconds, optional, integer type, `None` for no timeout, defaults to `None`.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_multithread.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import threads
>>> import time
>>> @threads(4)
>>> def process_job():  # a simple function for testing only
>>>     return time.sleep(1)
>>> process_job()
```
</details>



##### ChainableFuture
<details>

`anglerfish.ChainableFuture.then(on_success: Callable=None, on_fail: Callable=None)`

**Description:** Make a Chainable `concurrent.futures.Future` that has a `.then()` api.
This copies the JavaScript-like promises `.then()` api on Python 3.
For deep technical theory please see https://github.com/promises-aplus/promises-spec
For Python 3 Futures (JS-like promises) please see https://www.python.org/dev/peps/pep-3148
For simple human explanation this chains one Future with another Future.
`ChainableFuture` is subclass of `Future`.

**Arguments:**
- `on_success` a function to run when this Future success Ok,Callable type,Optional.
- `on_fail` a function to run when this Future fails,Callable type,Optional.

**Keyword Arguments:** None.

**Returns:** concurrent.futures object. A Future chained to current Future.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_chainable_future.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import ChainableFuture
>>> future1 = ChainableFuture()
>>> future2 = future1.then(lambda arg: arg + ' using ChainableFuture.then() !!!.')
>>> future1.set_result('This is an anglerfish.ChainableFuture demo')
>>> print(future1.result())  # Future 1 is Chained to Future 2.
This is an anglerfish.ChainableFuture demo
>>> print(future2.result())
This is an anglerfish.ChainableFuture demo using ChainableFuture.then() !!!.
```
</details>



##### retry
<details>

`@retry(tries: int=5, delay: int=3, backoff: int=2, timeout: int=None, silent: Bool=False, logger=None, exceptions=(Exception, ))`

**Description:** Retry calling the decorated function using an exponential backoff and timeout.

**Arguments:**
- `tries` how many times retry the operation, defaults to 5, integer type.
- `delay` delay between executions, defaults to 3, integer type.
- `backoff` an exponential backoff offset to apply to the `delay`, defaults to 2, integer type.
- `timeout` a timeout for the whole execution or None, defaults to None.
- `silent` a boolean `True` to be Silent when running the reties, defaults to False.
- `logger` a working logger to log into or None to use `print()`.
- `exceptions` A Tuple of exceptions to fail to, defaults to `(Exception, )`, optional, tuple type.

**Keyword Arguments:** None.

**Returns:** Its a Decorator.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_retry.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import retry
>>> @retry(4)
>>> def retry_job():  # a simple function for testing only
>>>     return open("").read()  # Will Fail as expected
>>> retry_job()
```
</details>



##### set_single_instance
<details>

`anglerfish.set_single_instance(name: str, port: int=8888)`

**Description:** Set a single instance Lock based on Sockets and return socket.socket object or None.

**Arguments:**
- `name` the name of your app to be used as Lock name,
- `port` port number to be used when Unix Socket is not available, mostly on MS Windows, defaults to 8888, optional, integer type.

**Keyword Arguments:** None.

**Returns:** socket.socket object or None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_single_instance.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :question:         | **Windows** | Untested    |

**Usage Example:**

```python
>>> from anglerfish import set_single_instance
>>> set_single_instance("MyApp")
<socket.socket fd=3, family=AddressFamily.AF_UNIX, type=SocketKind.SOCK_STREAM, proto=0, laddr=b'\x00_myapp__lock'>
```
</details>



##### html2ebook
<details>

`anglerfish.html2ebook(files_list: tuple, epub_file: Path=Path(uuid4().hex + ".epub"),
               extensions: tuple=(".html", ".htm", ".xhtml", ".txt"),
               compression: int=8, checksum: bool=False,
               zip_comment: str=None, metadata_dict: dict={})`

**Description:** Convert a folder with HTML5/CSS3 to eBook ePub. JavaScript does not Work on ePub.
If you want a "Print Quality" or "Print-Ready" eBook just use a Print-friendly CSS.

**Arguments:**
- `files` a tuple with the list of HTML/CSS files to add to the eBook.
- `fyle` an output file path string, defaults to an uuid4 hexadecimal if not provided.

**Keyword Arguments:** `meta` contains a dict with:
- `title` is the eBook Title (Fallbacks to Filename if not provided).
- `author`  is the eBook Author (Fallbacks to Username if not provided).
- `lang` is the eBook Language (Fallbacks to English if not provided).
- `des` is a friendly eBook Description (Fallbacks to Filename if not provided).
- `copi` eBook CopyRights (Fallbacks to Creative Commons 'CC-BY-NC-SA v.4.0' if not provided).
- `pub` the eBook Publisher (Fallbacks to 'Python' if not provided).
- `date` Date and Time ISO format of eBook creation (Fallbacks to Current Date and Time if not provided).

**Returns:** a string with the file path of the new eBook file.
**Source Code file:**https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/html2ebook.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import html2ebook
>>> html2ebook(("/mybook/html/index.html", "/mybook/html/chapter1.html"))
```
</details>



##### TemplatePython
<details>

`anglerfish.TemplatePython(template: str)`

**Description:** TemplatePython is a tiny generic Template Engine that Render and Runs native Python code. Template syntax is similar to Django Templates and Mustache. Fastest way to run Python on HTML and Render the results. No Markup enforced, it can work with HTML/CSS/JS or any kind of Markup. Has built-in optional Minification for HTML. Notice this is a Class, not a Function.
`TemplatePython` is subclass of `str`.

**Arguments:**
- `template` a template string with native Python 3 code between tags, or a file-like object that supports `.read()`.

**Keyword Arguments:** None.

**Returns:** a string with the Rendered HTML.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_template_python.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import TemplatePython
>>> demo = """<html><body>
     {%
     def say_hello(arg):
         {{"<tr> hello ", arg, " </tr>"}}
     %}
     <table>
         {% [say_hello(i) for i in range(9) if i % 2] %}
     </table>
     {% {{ testo }} {{ __doc__.title() }} %}
     {% # this is a python comment %}  </body></html>"""
>>> templar_template = TemplatePython(demo)
>>> print(templar_template(testo=9, mini=True))
```
</details>



##### path2import
<details>

`anglerfish.path2import(pat: str, name: str=None, ignore_exceptions: bool=False, check_namespace: bool=True)`

**Description:** Imports a Python module from a file path string.
This is *as best as it can be* way to load a module from a file path string that
I can find from the official Python Docs, for Python 3.5+ or higher.
This has been created after having `ImportError` trying to use a 1 line module,
that only contains `__version__ = "1.0.0"`,
not meant to replace the standard way of importing modules.

**Arguments:**
- `pat` is the file path on disk from where to load a Python module from, mandatory. String type.
- `name` is the Python module name, optional,
will try to get it from the filename on the `pat` argument if omitted. String type.
- `ignore_exceptions` optional, default to `False`, boolean type. Set to `True` will not raise
any exceptions and return `None` if loading failed.
- `check_namespace` optional, default to `True`, boolean type,  will check if the `name` is already
in `globals()` namespace, if it does, raises a `NamespaceConflictError` exception.

**Keyword Arguments:** None.

**Returns:** object, a *"live"* Python module object ready for use at runtime.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/path2import.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import path2import
>>> my_module = path2import("/path/to/module.py")
```
</details>



##### make_post_exec_msg
<details>

`anglerfish.make_post_exec_msg(start_time: object=None, comment: str=None)`

**Description:** Simple Post-Execution Message with information about RAM used by your app and execution Time. Can also display an arbitrary string ideal for Donation links, Social, etc.
It will register itself to be executed at exit via `atexit.register()`.
Its basically a *Goodbye* message.

**Arguments:**
- `start_time` a `datetime` object, ideally should be `datetime.now()`.
- `comment` an arbitrary string ideal for Donation links, Social links, Bitcoin, etc. String type.

**Keyword Arguments:** None.

**Returns:** The formatted message, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_postexec_message.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import make_post_exec_msg
>>> make_post_exec_msg()
'Total Maximum RAM Memory used: 203 of 32080MegaBytes.\n'
```
</details>



##### watch
<details>

`anglerfish.watch(file_path: str, callback: Callable=None, interval: int=60, backoff: int=1, timeout: int=None, repetitions: int=-1, silent: bool=False, logger: object=None)`

**Description:** Watch a file path for changes run callback if modified.
A WatchDog.

**Arguments:**
- `file_path` an existent readable file path to watch for changes. String type.
- `callback` a `Callable` callback function to execute when changes are detected. Callable type.
- `interval` an integer number seconds of interval between chacks for changes. Integer type.
- `backoff` an exponential backoff offset to apply to the `interval`, defaults to 1, integer type.
- `timeout` a timeout for the whole execution or None, defaults to None.
- `repetitions` how many times to check or run, -1 or 0 is infinite, defaults to -1, integer type.
- `silent` a boolean `True` to be Silent while running, defaults to False.
- `logger` a working logger to log into or None to use `print()`.

**Keyword Arguments:** None.

**Returns:** `Callable` output if theres a callable, else the file path that changed.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_watch.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import watch
>>> watch("/tmp/file.txt")
```
</details>



##### set_desktop_launcher
<details>

`anglerfish.set_desktop_launcher(app: str, desktop_file_content: str, autostart: bool=False)`

**Description:** Adds your app to autostart and/or launcher icon on the Desktop.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.
Windows and Os X dont have a desktop launcher standard file.
Windows only have `*.lnk` but thats meant to be an Internet-only shortcut.

**Arguments:**
- `app` the name of your app. String type.
- `desktop_file_content` the content of the launcher file. String type.
- `autostart` `True` to add your app to auto-start on the desktop.

**Keyword Arguments:** None.

**Returns:** the path of the newly created launcher. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_desktop_launcher.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import set_desktop_launcher
>>> set_desktop_launcher("mysuperapp", "")
```
</details>



##### set_terminal_title
<details>

`anglerfish.set_terminal_title(titlez: str="")`

**Description:** Set or Reset Bash CLI Window Titlebar Title.
According to XDG standard. Runs on Linux. Other platforms simply does nothing.
For Windows, use `title` command to approach that.
This uses a standard documented way to set title on each operating system,
so if your Terminal app wont work fill a bug for them, not an Angler problem.

**Arguments:**
- `titlez` the title for the terminal emulator window. Optional. String type.

**Keyword Arguments:** None.

**Returns:** `titlez` if the title has been set on the terminal emulator window or None. string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_terminal_title.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Untested    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import set_terminal_title
>>> set_terminal_title("mysuperapp")
'mysuperapp'
```
</details>



##### json2xml
<details>

`anglerfish.json2xml(json_obj: dict, line_padding: str="", at_end: str="")`

**Description:** Takes a JSON and returns an XML, optional custom line paddings.

**Arguments:**
- `json_obj` the json data, dict type.
- `line_padding` optional custom line paddings, string type.

**Keyword Arguments:** None.

**Returns:** XML, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/json2xml.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import json2xml
>>> json2xml({"foo": 42, "bar": 666})
'<foo>\n    42\n</foo>\n<bar>\n    666\n</bar>'
```
</details>



##### make_json_flat
<details>

`anglerfish.make_json_flat(jsony: dict, delimiter: str="__")`

**Description:** Takes a JSON and returns a JSON, but with Flatten out structure, from Nested to Flat, optional custom delimiter.

**Arguments:**
- `jsony` the json data, dict type.
- `delimiter` optional custom delimiter, string type.

**Keyword Arguments:** None.

**Returns:** JSON, a Flat JSON, dict type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_json_flat.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

</details>



##### set_zip_comment
<details>

`anglerfish.set_zip_comment(zip_path: str, comment: str="")`

**Description:** Set a comment on a ZIP file, return a Boolean. ZIP file must be Valid.

**Arguments:**
- `zip_path` ZIP file path string, str type.
- `comment` Comment for the ZIP file, optional, defaults to empty string, string type.

**Keyword Arguments:** None.

**Returns:** `True` if Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_zip_comment.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import set_zip_comment
>>> set_zip_comment("test.zip", "This is a comment.")
True
```
</details>



##### get_zip_comment
<details>

`anglerfish.get_zip_comment(zip_path: str, comment: str="")`

**Description:** Get a comment metadata from a ZIP file, UTF-8 string type.
ZIP file must be Valid.

**Arguments:**
- `zip_path` ZIP file path string, str type.

**Keyword Arguments:** None.

**Returns:** UTF-8 Comment, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_zip_comment.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_zip_comment
>>> get_zip_comment("test.zip")
"This is a comment."
```
</details>



##### has_battery
<details>

`anglerfish.has_battery()`

**Description:** Check if computer has a Battery, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** `True` if has Battery, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_hardware.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import has_battery
>>> has_battery()
False
```
</details>



##### on_battery
<details>

`anglerfish.on_battery()`

**Description:** Check if computer is running on Battery, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** `True` if computer is running Battery, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/check_hardware.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | No API      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import on_battery
>>> on_battery()
False
```
</details>



##### set_display_off
<details>

`anglerfish.set_display_off()`

**Description:** Set Display monitor OFF, will Automatically turn ON when any Key or Mouse movement detected, return Boolean.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** `True` if Ok, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_display_off.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :x:                | **Os X**    | Works Ok      |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import set_display_off
>>> set_display_off()
True
```
</details>



##### get_public_ip
<details>

`anglerfish.get_public_ip()`

**Description:** Get current public IP address as `ipaddress.ip_address()`.
Can be IPv4 or IPv6. See Python standard lib official Docs for more info.
`ipaddress.ip_address()` converted to string with `str(ipaddress.ip_address())`.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Current public IP address, `ipaddress.ip_address()` type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_public_ip.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_public_ip
>>> get_public_ip()
'181.95.185.82'
```
</details>



##### is_online
<details>

`anglerfish.is_online()`

**Description:** Check if we got internet connectivity.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** `True` if Internet is working, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_public_ip.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import is_online
>>> is_online()
True
```
</details>



##### set_process_priority
<details>

`anglerfish.set_process_priority(nice=True, ionice=False, cpulimit=0)`

**Description:** Set process I/O and CPU priority. Requires `ionice` and `cpulimit` installed on the system.
If `ionice` or `cpulimit` are Not installed on the system its usage is ignored.
- Nice is very safe to use, and its Enabled by default, no performance hit.
- IONice is NOT safe to use, and its Disabled by default, big performance hit.
- CPULimit is safe to use, its Disabled by default, almost no performance hit depending on the value passed.
- If your App has a GUI updating on real-time then `ionice` and `cpulimit` are probably not recommended.
- If your App is a background, headless, CLI, slow-running process then `ionice` and `cpulimit` are recommended.
The purpose of this is to make your App very lightweight, dont eat battery, cpu, etc. freeing up more resources on the system.

**Arguments:**
- `nice` Use a smooth cpu priority, if your app dont need real-time using this will be good, defaults to `True`, optional, bool type.
- `ionice` Use a smooth I/O priority, I/O Nice may delay I/O Operations, not recommended on user-facing GUI!, recommended leaving it as `False`!, unless you know what you are doing, defaults to `False`, optional, bool type.
- `cpulimit` Use a cpu max limit, if your app dont need real-time using this will be good,
its a percentage from the minimum `5` to maximum of your CPU cores multiplied by 100%,
meaning if you have 8 Cores, the maximum is 800%, 800% means 8 Cores at 100%,
100% means 1 Core at 100%, `0` means is Disabled and not used, defaults to `0`,
`cpulimit` may delay Processing Operations, not recommended on user-facing GUI!,
recommended use for background or non-critical apps, optional, integer type.

**Keyword Arguments:** None.

**Returns:** `True` if its working, bool type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/set_process_priority.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :x:                | **Windows** | No API      |

**Usage Example:**

```python
>>> from anglerfish import set_process_priority
>>> set_process_priority()
True
```
</details>



##### string2stealth
<details>

`anglerfish.string2stealth(stringy: str, rot13: bool=False)`

**Description:** Stealth Strings, hidden and dangerous.
No information is lost, both ways, supports everything that UTF-8 supports.
Makes invisible strings, a *"stealth"* string, you can pack lots of source code
and they remain invisible hidden, or make screenshot-proof encryptions.
String Unicode :fast_forward: ZLib Compress :fast_forward: Base64 :fast_forward: Binary :fast_forward: Stealth String

**Arguments:**
- `stringy` A string to convert to Stealth, string type.

**Keyword Arguments:** None.

**Returns:** Stealth string, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/string2stealth.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import string2stealth
>>> string2stealth("test")
""
```
</details>



##### stealth2string
<details>

`anglerfish.stealth2string((stringy: str, rot13: bool=False)`

**Description:** Stealth Strings, hidden and dangerous.
No information is lost, both ways, supports everything that UTF-8 supports.
Makes invisible strings back to visible normal strings, a *"normal"* string, you can unpack back lots of source code to visible normal string, or undo screenshot-proof encryptions.
Stealth String :fast_forward: Binary :fast_forward: Base64 :fast_forward: ZLib DeCompress :fast_forward: String Unicode

**Arguments:**
- `stringy` A string to convert to Stealth, string type.

**Keyword Arguments:** None.

**Returns:** Stealth string, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/stealth2string.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import stealth2string
>>> stealth2string("")
"test"
```
</details>



##### get_random_pastel_color
<details>

`anglerfish.get_random_pastel_color()`

**Description:** Return a random [pastel color](https://en.wikipedia.org/wiki/Pastel_%28color%29), can be Dark or Light, as string, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random pastel color, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_pastel_color.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_pastel_color
>>> get_random_pastel_color()
'seagreen'
```
</details>



##### get_random_pasteldark_color
<details>

`anglerfish.get_random_pasteldark_color()`

**Description:** Return a random [pastel color](https://en.wikipedia.org/wiki/Pastel_%28color%29), only Dark colors, as string, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random pastel color, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_pastel_color.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_pasteldark_color
>>> get_random_pasteldark_color()
'darkolivegreen'
```
</details>



##### get_random_pastelight_color
<details>

`anglerfish.get_random_pastelight_color()`

**Description:** Return a random [pastel color](https://en.wikipedia.org/wiki/Pastel_%28color%29), only Light colors, as string, takes no arguments.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random pastel color, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_pastel_color.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_pastelight_color
>>> get_random_pastelight_color()
'aquamarine'
```
</details>



##### get_random_handwriting_font
<details>

`anglerfish.get_random_handwriting_font()`

**Description:** Return a random open source free [handwriting font](https://fonts.google.com/?category=Handwriting) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
from Design point of view this fonts are good for Titles/SubTitles/big text,
as string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_handwriting_font
>>> get_random_handwriting_font()
'Calligraffitti'
```
</details>



##### get_random_mono_font
<details>

`anglerfish.get_random_mono_font()`

**Description:** Return a random open source free [Monospaced font](https://fonts.google.com/?category=Monospace) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
the names of this fonts contain spaces ` `,
from Design point of view this fonts are good for source code text,
as string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_mono_font
>>> get_random_mono_font()
'Oxygen Mono'
```
</details>


##### get_random_display_font
<details>

`anglerfish.get_random_display_font()`

**Description:** Return a random open source free [decorative display cosmetic font](https://fonts.google.com/?category=Display) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
from Design point of view this fonts are good "for Fun",
as string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_display_font
>>> get_random_display_font()
'Comfortaa'
```
</details>



##### get_random_sans_font
<details>

`anglerfish.get_random_sans_font()`

**Description:** Return a random open source free [Sans-Serif font](https://fonts.google.com/?category=Sans+Serif) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
from Design point of view this fonts are good for serious stuff and formal text,
as string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_sans_font
>>> get_random_sans_font()
'Roboto'
```
</details>



##### get_random_serif_font
<details>

`anglerfish.get_random_serif_font()`

**Description:** Return a random open source free [Serif font](https://fonts.google.com/?category=Serif) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
from Design point of view this fonts are good for serious stuff and formal text,
as string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_serif_font
>>> get_random_serif_font()
'Amethysta'
```
</details>



##### get_random_font
<details>

`anglerfish.get_random_font()`

**Description:** Return a random open source free [font](https://fonts.google.com) family name,
all fonts are available from online CDN, font names are keep Case-Sensitive,
font families have been tested on HTML/CSS with one each other,
they look pretty good on all combinations, we are Not Designers,
but this is useful for quick templating and boilerplate styling,
too extreme weird font designs are not included, is a one-by-one curated list,
from Design point of view this fonts are good for generic multipurpose text,
internally this function calls all other font functions and then choose 1 at random,
this function calls `anglerfish.get_random_sans_font()` and
`anglerfish.get_random_serif_font()` and
`anglerfish.get_random_mono_font()` and
`anglerfish.get_random_handwriting_font()` and
`anglerfish.get_random_display_font()`.
return a string, takes no arguments.
Theres several third party Python packages to get full path of TTF files from Font Names.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** Random open source free font family name, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/get_random_font.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_random_font
>>> get_random_font()
'Roboto'
```
</details>



##### DataURI
<details>

- `anglerfish.DataURI`
- `anglerfish.DataURI.make(cls, mimetype: str, base64: bool, data: str)`
- `anglerfish.DataURI.from_file(filename: str, base64: bool=True, webp: bool=True)`
- `anglerfish.DataURI.from_url(url: str, base64: bool=True, webp: bool=True)`
- `anglerfish.DataURI.wrap(width: int=80, newline: str="\n")`

**Description:** Return a Data URI Base64 URL-Safe UTF-8 string,
from URL, or file, or string, with WebP Support, designed for HTML/CSS/JS and Images.
WebP `cwebp` needs to be installed for WebP capability.
If WebP `cwebp` is not installed images will be JPG.
`anglerfish.DataURI.wrap()` uses `textwrap.wrap()` to wrap.
`anglerfish.DataURI.make()` makes a Data URI from args.
`anglerfish.DataURI.from_file()` pass args to `anglerfish.DataURI.make()`.
`anglerfish.DataURI.from_url()` pass args to `anglerfish.DataURI.from_file()`.
`DataURI` is subclass of `str`.

**Arguments:** None. Uses methods to build the Data URI.

**Keyword Arguments:** None. Uses methods to build the Data URI.

**Returns:** Data URI Base64 URL-Safe UTF-8, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_datauri.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import DataURI
>>> uri = DataURI('data:text/plain;charset=utf-8;base64,VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu')
>>> uri.mimetype
'text/plain'
>>> uri.charset
'utf-8'
>>> uri.is_base64
True
>>> uri.data
'The quick brown fox jumped over the lazy dog.'
>>> uri = DataURI.make('text/plain', base64=True, data='This is a message.')
>>> uri
DataURI('data:text/plain;charset=utf-8;base64,VGhpcyBpcyBhIG1lc3NhZ2Uu')
>>> uri.data
'This is a message.'
>>> uri = DataURI.from_file('image.png', webp=False)
>>> uri.mimetype
'image/png'
>>> uri.data
b'\x89PNG...'
>>> uri = DataURI.from_url('example.com/image.jpg')  # webp=False to Disable WebP
>>> uri
DataURI('data:image/webp;charset=utf-8;base64,...')
>>> print(uri)
'data:image/webp;charset=utf-8;base64,...'
>>> isinstance(uri, str)
True
```
</details>



##### img2webp
<details>

`anglerfish.img2webp(image_path: str, webp_path: str=None, preset: str="text",
             cwebp: str=which("cwebp"), timeout: int=60)`

**Description:** Convert `*.png, *.jpeg, *.jpg, *.tiff` Images to WebP `*.webp`.
`anglerfish.DataURI()` internally uses `anglerfish.img2webp()` for conversions.

We also checked latest Google Guetzli,
but it can freeze a system with 99% CPU usage for several minutes, crazy slow,
and in the end it outputs equal or bigger files, it does not support JPG for Web,
since Progressive RGB its not supported by design.
We also checked latest Mozillas MozJPEG,
but in the end it outputs equal files most of the time,
the only one that really makes a difference is WebP.

**Arguments:**
- `image_path`: Full path string to input `*.png, *.jpeg, *.jpg, *.tiff` image,
if image is not `*.png, *.jpeg, *.jpg, *.tiff` then the same image format and filename is returned,
if not WebP `cwebp` installed then the same image format and filename is returned,
WebP `cwebp` is autodetected using `shutil.which("cwebp")`, required, string type.
- `webp_path`: Full path string to output `*.webp` image or `None`,
if `None` then `image_path + ".webp"` will be used,
path to output image should end with extension `*.webp`, optional, string type.
- `preset`: Preset name string for conversion,
which is 1 of `default photo picture drawing icon text`,
if not in `default photo picture drawing icon text` then `text` will be used,
optional, string type.

**Keyword Arguments:** None.

**Returns:** Full path string to output `*.webp` image, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_datauri.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import img2webp
>>> img2webp("test.jpg")
"test.webp"
```
</details>



##### now2human
<details>

anglerfish.now2human(utc: bool=False)`

**Description:**
Get a Human string ISO-8601 representation of datetime.datetime with UTC info.
Other solutions I found on the internet needs importing 'time' this one dont.
ISO-8601 standard: Its permitted to omit the 'T' character by mutual agreement.
Internally is a shortcut to:
`datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).astimezone().isoformat(" ")`

**Arguments:**
- 

**Keyword Arguments:** None.

**Returns:** Human friendly ISO-8601 date, time and UTC info string, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/seconds2human.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import get_human_datetime
>>> get_human_datetime()
"2017-03-10 18:08:03-03:00"
```
</details>



##### Sync2Async
<details>

`anglerfish.Sync2Async.run_async(sync_code)`
`anglerfish.Sync2Async.run_async_on_process(sync_code)`
`anglerfish.Sync2Async.run_async_on_thread(sync_code)`
`anglerfish.Sync2Async.get_event_loop()`

**Description:** Run synchronous code as asynchronous.
Forces any module NOT compatible with `asyncio` to run Ok with `asyncio`.
Use synchronous blocking modules seamlessly on asynchronous code.
This is NOT to run async code as synchronous.
You can use this to skip re-writing your modules for asynchronous programming.
This can also be used on Angler modules itself to run them as async.
Please read Pythons `asyncio` official Documentation for more info.
`run_async_on_process()` runs the code as async on a separate Process.
`run_async_on_thread()` runs the code as async on a separate Thread.
`get_event_loop()` returns the current actual event loop in use, takes no arguments.
`get_event_loop()` is similar to `asyncio.get_event_loop()`
[For more info see this minimum possible example demo.](https://github.com/juancarlospaco/anglerfish/blob/master/examples/async.py)

**Arguments:**
- `sync_code`: A `Callable` object, a function or method or whatever callable,
anything that you want to run on an async code context,
it acts as an auto-wrapper to run your sync code as async.

**Keyword Arguments:** None.

**Returns:** Returns whatever the passed argument callable should return,
but it `await` a `Future` result.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_async.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> import asyncio, time
>>> from anglerfish import Sync2Async
>>>
>>> def blocking_function():  # This is any common normal blocking function.
>>>     print("Executing Synchronous Blocking code 'time.sleep(1)' as Async!.")
>>>     return time.sleep(1)  # Can be any for, open, with, slow operation, etc.
>>>
>>> async def async_function(sync_code):
>>>     return await Sync2Async.run_async(sync_code)
>>>
>>> async def async_on_process(sync_code):
>>>     return await Sync2Async.run_async_on_process(sync_code)
>>>
>>> async def async_on_thread(sync_code):
>>>     return await Sync2Async.run_async_on_thread(sync_code)
>>>
>>> async_tasks = (asyncio.ensure_future(async_function(blocking_function)),
>>>                asyncio.ensure_future(async_on_process(blocking_function)),
>>>                asyncio.ensure_future(async_on_thread(blocking_function)))
>>> asyncio.get_event_loop().run_until_complete(asyncio.wait(async_tasks))
"Executing Synchronous Blocking code 'time.sleep(1)' as Async!."
"Executing Synchronous Blocking code 'time.sleep(1)' as Async!."
"Executing Synchronous Blocking code 'time.sleep(1)' as Async!."
```
</details>



##### autochecksum
<details>

`anglerfish.autochecksum(filename: str, update: bool=False)`

**Description:**
Make a automagic-checksuming file using Adler32 Hash and Hexadecimal.
Resulting on a short ~8 character checksum added to the filename,
easy to parse with standard pattern,not crypto secure but useful for checksum,
is more human friendly than SHA512 checksum and its builtin on the filename,
Adler32 is standard on all ZIP files and its builtin on Python std lib.
The Checksum operation is `hex( zlib.adler32(data) )`.
A standard pattern of a **Check** `.✔` is appended to easy parse checksums from filenames.
I do this tired of people not using SHA512 on 1 separate txt file for checksum,
this not require user command line skills to check the checksum, its automagic.

**Arguments:**
- `filename`: Filename path, string type, required.
- `update`: Force update Checksum if its wrong,
set to `True` to update existing checksums, defaults to `False`, bool type, optional.

**Keyword Arguments:** None.

**Returns:**
- `True` if checksum is Ok and file integrity is Ok.
- `False` if checksum is **NOT** Ok and file integrity is **NOT** Ok.
- New filename path string is the checksum has been just created.
- New filename path string is the checksum has been just updated.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_autochecksum.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import autochecksum
>>> open("example.txt", "w").close()  # Write a new empty blank txt file.
>>> open("example.txt").read()
""
>>> autochecksum("example.txt")  # If no checksum it adds a checksum
"example.✔+1.txt"
>>> autochecksum("example.✔+1.txt")  # Check the integrity of the empty blank txt file.
True
>>> with open("example.✔+1.txt", "w") as txt_file:
        txt_file.write("Test.")  # Write something new to the file.
>>> autochecksum("example.✔+1.txt")  # Check of integrity fails, file is not empty anymore.
False
>>> autochecksum("example.✔+1.txt", update=True)  # Update the checksum.
"example.✔+5ac01cf.txt"
>>> autochecksum("example.✔+5ac01cf.txt")  # Check the integrity of the txt file.
True
>>> open("example.✔+5ac01cf.txt").read()
"Test."
```
</details>



##### url2path
<details>

`anglerfish.url2path(url: str, data: dict=None, timeout: int=None, filename: str=None,
             suffix: str=None, name_from_url: bool=False,
             concurrent_downloads: int=5, force_concurrent: bool=False,
             checksum: bool=False, use_tqdm: bool=True)`

**Description:** Take an URL or Path filename, return path if its not an URL,
download to a temporary file and return filename path if its an URL,
use multiple async concurrent multi-threaded multi-segment binary downloads for the same file,
as many other **Download Accelerators** (eg. Aria, Aria2C, Axel, Flareget, etc),
it can try to determine the filename from the URL, use a temporary file, or accept an argument one,
it can automatically determine to use multiple downloads based on file sizes,
it will use a single normal download if its faster that way, you can force to be concurrent too,
it can automagically generate a checksum for the file using `anglerfish.autochecksum()`,
will Not fail if the Certificate is self-signed, etc, making it ideal for dev/test envs,
does Not depend on `requests`, is faster than `requests` download, not meant as `requests` replacement,
if you pass as argument a file path instead of an HTTP url it will pass thru and return the same file path,
if the file is small and the download very quick it will be almost silent,
if the file is big and the download takes awhile it will have very detailed log,
this is also designed to be able to use an URL as a path filename on command line arguments.


**Arguments:**
- `url`: URL or Path, will download to file or pass thru if its already a path, will always return a path, string type, required.
- `data`: data for `urlopen()`, pass thru to `urlopen()`, optional, see `urlopen()` documentation.
- `timeout`: Timeout on integer for the download, defaults to `None`, integer type, optional.
- `filename`: Path, will download remote URL to this file path, will always return this path, defaults to `None`, uses a temporary file if set to `None`, string type, optional.
- `suffix`: File suffix, a file extension, defaults to `None`, string type, optional.
- `name_from_url`: Try to determine the file name from the URL, uses `url.split('/')[-1]`, defaults to `False`, bool type, optional.
- `concurrent_downloads`: How many concurrent downloads to use to speed up, defaults to `5`, minimum is `2`, maximum is `10`, some servers tend to cut the connection for more than 10 connections per file, integer type, optional.
- `force_concurrent`: Force to be concurrent even if its not needed, it can make downloads slower if the file is small, if set to `False` it will try to automatically determine the best based on file size, defaults to `False`, bool type, optional.
- `checksum`: Automatically generate a checksum for the file, uses `anglerfish.autochecksum()`, this checksum is super fast to calculate, see `anglerfish.autochecksum()` documentation, defaults to `False`, bool type, optional.
- `use_tqdm`: Use `tqdm` for multiple progress bars for downloads for each Thread,
if its installed on the system it displays multiple download progress bars,
if its not installed on the system it displays multiple `print()` with info,
defaults to `True`, bool type, optional.

**Keyword Arguments:** None.

**Returns:** Filename path, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/url2path.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import url2path
>>> url2path("example.txt")
"example.txt"
>>> url2path("http://example.com/example.txt", suffix="txt")
"angler_dkj3423.txt"
>>> url2path("http://example.com/example.iso", force_concurrent=True, name_from_url=True)
Angler download accelerator start.
From: http://example.com/example.iso
To: example.iso
Time: 2017-05-15 14:38:26-03:00 (2017-05-15 14:38:26.150302).
27 Megabytes(28551168Bytes) download
Using 5 async concurrent downloads for 1 file
Thread 0 is downloading bytes=0-5710234
Thread 1 is downloading bytes=5710235-11420467
Thread 2 is downloading bytes=11420468-17130701
Thread 3 is downloading bytes=17130702-22840934
Thread 4 is downloading bytes=22840935-28551168
Downloaded 5 binary data chunks total.
Finished writing downloaded output file: example.iso
Size:27 Megabytes (28551168 Bytes)
Time: 44 Seconds (0:00:44.837995).
Finished:2017-05-15 14:39:10-03:00 (2017-05-15 14:39:10.989296)
"example.iso"
```
</details>



##### tinyslation
<details>

`anglerfish.tinyslation(strin: str, to: str=getdefaultlocale()[0][:2], frm: str="en", fallback_dict: dict={}, , fallback_value=None, timeout: int=5)`

**Description:**
Tinyslation is smallest possible translation engine from Internet with fallback,
it takes 1 string containing a word or a phrase of words of any length,
`to` (eg. `"es"`) and `frm` (eg. `"en"`) standard languages ISO Codes,
and returns a translation from origin language to target language,
an optional integer `timeout` on seconds can be provided,
an optional dictionary `fallback_dict` with `key:value` strings to use if translation fails,
if translation and `falbck` dictionary both fail then the same string is returned.
this conversion is fully free and legal to use for whatever you want.
The request uses an empty string `""` for `"User-Agent"`, and Do Not Track.
API has a Limit of 1.000 Words per Day, but in practice it works Ok even beyond that limit,
I think is safe to work with it up to 1.000 Words per Day, and beyond that limit provide a fallback dictionary,
or even on the worse case that everything fails strings will pass thru untouched.
The service is based on user contributions, if you find a missing word feel free to add it yourself for free.
This is not meant to replace manual translation.
This is 100% Anonymous without Login, always uses SSL and does not require API Keys.
This service does NOT connect to Google.

**Arguments:**
- `strin`: A string containing a word or a phrase of words, string type, required.
- `to`: Target language as 2 letter standard languages ISO Codes, eg. `"es"`, defaults to current default locale language uses `locale.getdefaultlocale()[0][:2]`, string type, required.
- `frm`: Origin language as 2 letter standard languages ISO Codes, eg. `"es"`, defaults to English `"en"`, string type, required.
- `timeout`: Timeout integer on seconds, defaults to `5`, integer type, optional.
- `fallback_value`: A Fallback value string, if online translation fails and fallback dictionary fails you can optionally force this string to be the return value for all failing translations, so instead of the non-translated word you can set something like `"???"` or `" "` or `"ERROR"`, if not provided the words will pass thru, this is like a third layer of fallback, defaults to `None`, string type, optional.

**Keyword Arguments:**
- `fallback_dict`: A Fallback dictionary containing words as `key:value` a word or a phrase of words, uses this is online translation fails if any, defaults to `{}`, dict type, optional.

**Returns:** Translated string, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/make_tinyslation.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from anglerfish import tinyslation
>>> tinyslation("cute cat", "es")
'lindo gato'
>>> tinyslation("lindo gato", "en", "es")
'cute cat'
>>> tinyslation("cute cat", "it")
'gatto carino'
>>> tinyslation("cat beer wine eye hair skin computer", "es")
'gato cervezas vino ojo pelo piel ordenador'
>>>
>>> # Fake a Gettext-like auto-translation:
>>> _ = lambda s:  tinyslation(s, "es")
>>> _("cute cat")
'lindo gato'
```
</details>



# Install permanently on the system:

```
pip install anglerfish
```
- Use `sudo pip install anglerfish` for installing System-wide.
- Use `python3 examples/basic.py` to run an example of all the functionalities.
- This project is oriented to Developers, NOT end-users.
- Angler can be used with Fades and/or FireJails and/or Docker and/or RKT.
- Feel free to contact us if you need help integrating Angler on your project.


# Why?:

- Too much repeated code across my projects, almost all of them doing tha same.
- Lots of functionalities on Angler are a *"Must Have"* for modern Apps, like a Logger, etc.
- No Dependencies at all, just Python 3 standard library, cross-platform, Easy to use, KISS philosophy.
- KISS, every second a Developer spends writing and debugging code is wasted money.


# Requisites:

- [Python 3.6+](https://www.python.org "Official CPython 3.6 or higher supported")


**Optional Suggested Extras:**

- [uJSON, speeds up JSON logic.](https://github.com/esnme/ultrajson#ultrajson)
- [tqdm, pretty progress bars on terminal.](https://github.com/tqdm/tqdm#tqdm)


**Optional Suggested Linux-only Extras:**

These are fully optional but enable extra features (most Linux distros already have them).

- `cpulimit` Control CPU usage on your App, if not installed ignores CPU limits.
- `libwebp` WebP support for images on Base64 Data-URIs, if not installed uses JPG.
- `python-dbus` Freedesktop native notifications and hardware status support, if not installed no hardware status.
- `xsel` Clipboard selection support, if not installed ignores clipboard selection.
- `xclip` Clipboard copy and paste support, if not installed no clipboard support.
- `xorg-xset` Display support to turn OFF the display, if not installed ignores display off call.


# More must have helpers

*All these tiny generic awesome helpers, utilities, etc only require Python standard lib.*

- https://github.com/Stewori/pytypes#quick-manual
- https://github.com/shazow/unstdlib.py#unstandard-library-for-python
- https://github.com/hynek/attrs#attrs-attributes-without-boilerplate
- https://github.com/ssato/python-anyconfig#python-anyconfig
- https://github.com/theskumar/python-dotenv
- https://github.com/dbader/schedule#usage
- https://github.com/msiemens/tinydb#example-code
- https://github.com/jsonpickle/jsonpickle#jsonpickle
- https://github.com/theodox/spelchek#spelchek
- https://github.com/amoffat/sh
- https://github.com/jek/blinker#blinker
- https://github.com/jpaugh/agithub (ignore the name, check the project, bad name)
- https://github.com/spulec/freezegun#freezegun-let-your-python-tests-travel-through-time
- https://github.com/pybuilder/pybuilder#pybuilder
- https://github.com/czheo/syntax_sugar_python#syntax_sugar--
- https://github.com/cdgriffith/Box/#overview
- https://docs.python.org/3/library/zipapp.html#zipapp.create_archive
- For Inmmutable Objects see: [`frozenset({1, 2, 3})`](https://devdocs.io/python~3.6/library/stdtypes#frozenset "Angler will Not add Inmmutable Objects, since they are Built-in"), [`namedtuple("_", "foo bar")(42 True)`](https://devdocs.io/python~3.6/library/collections#collections.namedtuple "Angler will Not add Inmmutable Objects, since they are Built-in"), [`MappingProxyType({"a": 1, "b": True})`](https://devdocs.io/python~3.6/library/types#types.MappingProxyType "Angler will Not add Inmmutable Objects, since they are Built-in").


# Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort), [Pre-Commit](http://pre-commit.com/hooks.html) must Pass Ok. `pip install --upgrade pylama isort pre-commit pre-commit-hooks`
- If there are any kind of tests, they must pass. No tests is also acceptable, but having tests is better.


# Name convention: Obvius Names

- For names we use: `get_*`, `set_*`, `check_*`, `make_*`, `is_*`, `has_*` and `*2*`.
- Packages can have nice and cool names, but its classes, functions and methods must have obvious names.
- `MappingProxyType` is imported and used as `frozendict` on Docs and Code, since no one seems to know whats a `MappingProxyType` but a `frozendict` you already infer is a `dict`, just like `set` and `frozenset`, its imported as `from types import MappingProxyType as frozendict`.


# Tests

- Pull requests to improve tests are welcome!!!.

```bash
python -m unittest discover --verbose --locals --start-directory "tests/"
# OR
python -m unittest
# OR
pytest tests/
```

- [Test Templates.](https://gist.github.com/juancarlospaco/040fbe326631e638f2a540fe8c1f2092)


# Presentation

- [Angler Intro Presentation](http://htmlpreview.github.io/?https://raw.githubusercontent.com/juancarlospaco/anglerfish/master/angler-presentation.html "Angler Intro Presentation")


# Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).
- English is the primary default spoken language, unless explicitly stated otherwise *(eg. Dont send Translation Pull Request)*
- Pull Requests for working passing unittests welcomed.


# Licence:

- GNU GPL Latest Version *AND* GNU LGPL Latest Version *AND* any Licence [YOU Request via Bug Report](https://github.com/juancarlospaco/anglerfish/issues/new).


# Ethics and Humanism Policy:

- Politics and Religions is not allowed.
- [Contributing means you agree with the COC.](https://github.com/juancarlospaco/anglerfish/blob/master/code_of_conduct.md)
