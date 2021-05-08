#  DevTools Proxy

[![Build Status](https://travis-ci.org/bayandin/devtools-proxy.svg?branch=master)](https://travis-ci.org/bayandin/devtools-proxy)
[![PyPI](https://img.shields.io/pypi/v/devtools-proxy.svg)](https://pypi.python.org/pypi/devtools-proxy)
[![GitHub release](https://img.shields.io/github/release/bayandin/devtools-proxy.svg)](https://github.com/bayandin/devtools-proxy/releases/latest)

DevTools Proxy is a tool for creating simultaneous connections via DevTools Protocol (~~[which is not possible by default](https://developer.chrome.com/devtools/docs/debugger-protocol#simultaneous)~~ and it is [possible](https://developers.google.com/web/updates/2017/10/devtools-release-notes#multi-client) since Chrome 63 even without DevTools Proxy).

## How it works

```
+---+      +---+
| C |      |   |
| L |      | D |    +-----------+
| I |      | E |    |           |
| E |<---->| V |    |  BROWSER  |
| N |      | T |    |           |
| T |      | O |    |           |
+---+      | O |    |   +---+   |
           | L |    |   | T |   |
           | S |<-----> | A |   |
+---+      |   |    |   | B |   |
| C |      | P |    |   +---+   |
| L |      | R |    |           |
| I |<---->| O |    |           |
| E |      | X |    |           |
| N |      | Y |    +-----------+
| T |      |   |
+---+      +---+
```

## Installation

* Download & unzip [standalone binary](https://github.com/bayandin/devtools-proxy/releases/latest) for your system.
* If you use Python (at least 3.6) you can install it via pip: `pip install devtools-proxy`

## Usage

### With Selenium and ChromeDriver

There are [examples](examples/) for Python and Ruby. Demos for [CPU Throttling](https://youtu.be/NU46EkrRoYo), [Network requests](https://youtu.be/JDtuXAptypY) and [Remote debugging](https://youtu.be/X-dL_eKB1VE).

#### Standalone (for any language)

* Configure [`ChromeOptions`](https://sites.google.com/a/chromium.org/chromedriver/capabilities#TOC-chromeOptions-object):
    * Set path to `chrome-wrapper.sh` as a `binary`. Optional arguments are mentioned in example for Python below
    * Add `--devtools-proxy-binary=/path/to/devtools-proxy` to `args`

#### Python

`devtools-proxy` pypi package supports at least Python 3.6. If you use lower Python version use Standalone package.

```bash
pip install -U devtools-proxy
```

```python
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from devtools.proxy import CHROME_WRAPPER_PATH

devtools_proxy_binary = 'devtools-proxy' # Or path to `devtools-proxy` from downloaded binaries

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['chromeOptions'] = {
    'binary': CHROME_WRAPPER_PATH, # Or path to `chrome-wrapper.sh` from downloaded binaries
    'args': [
        f'--devtools-proxy-binary={devtools_proxy_binary}',
        # Optional arguments:
        # '--chrome-binary=/path/to/chrome/binary', # Path to real Chrome/Chromium binary
        # '--devtools-proxy-chrome-debugging-port=some-free-port', # Port which proxy will listen. Default is 12222
        # '--devtools-proxy-args=--additional --devtools-proxy --arguments, # Additional arguments for devtools-proxy from `devtools-proxy --help`
    ],
}
```

### With multiple Devtools instances

* Run `devtools-proxy` (by default it started on 9222 port)
* Run Chrome with parameters `--remote-debugging-port=12222 --remote-debugging-address=127.0.0.1`
* Open a website which you want to inspect
* Open debugger in a new Chrome tab:  `http://localhost:9222` and choose your website to inspect
* Repeat the previous step as many times as you need it
