QHangups
========

Alternative client for Google Hangouts written in PyQt

Requirements
------------

- Python >= 3.3
- PyQt >= 5
- Quamash (https://github.com/harvimt/quamash)
- hangups (https://github.com/tdryer/hangups)
- appdirs (https://github.com/ActiveState/appdirs)
- asyncio (https://pypi.python.org/pypi/asyncio) for Python < 3.4

Usage
-----

Run ``qhangups --help`` to see all available options.
Start QHangups by running ``qhangups``.

The first time you start QHangups, you will be prompted to log into your
Google account. Your credentials will only be sent to Google, and only
OAuth 2 refresh token will be stored locally.

Help
----
::

    usage: qhangups [-h] [-d] [--log LOG] [--token TOKEN]
    
    optional arguments:
      -h, --help     show this help message and exit
      -d, --debug    log detailed debugging messages (default: False)
      --log LOG      log file path (default:
                     ~/.local/share/QHangups/hangups.log)
      --token TOKEN  OAuth refresh token storage path (default:
                     ~/.local/share/QHangups/refresh_token.txt)
