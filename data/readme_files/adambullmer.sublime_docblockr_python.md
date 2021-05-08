DocBlockr for Python
====================

[![codecov](https://codecov.io/gh/adambullmer/sublime_docblockr_python/branch/master/graph/badge.svg)](https://codecov.io/gh/adambullmer/sublime_docblockr_python)

Based off the [DocBlockr](https://github.com/spadgos/sublime-jsdocs) project, This extension provides the similar funtionality but for python docstrings.
The default formatter for this plugin is designed around [PEP-257](https://www.python.org/dev/peps/pep-0257/) compliance but with more verbosity: Added variable types, listing class extensions, and listing decorators.
The main goal of this project is to help developer provide better documentation by giving easy and consistent formatting.


Installation
------------
**Package Control**
Now you can install it with package control!

1. Open your command pallete and type `Package Control: Install Package`.
1. Find this project `DocBlockr Python` and press `Enter`.

**Manually**
Download the release and put it in your installed packages directory yourself

1. Go to the [Latest Release](https://github.com/adambullmer/sublime-docblockr-python/releases/latest) and download the `docblockr_python.sublime-package` file.
1. Move this file to your `Installed Packages` directory. (`Preferences > Browse Packages...` and go up one directory to see `Installed Packages`)
1. If you are updating your existing install, a restart of Sublime Text will be in order.


Usage
-----
There isn't a command pallete command to start this plugin, it is triggerg by hitting **enter** or **tab** after opening a docstring (`"""`) at the `module`, `class`, or `function` level.
If you wanted to simply put a new line after opening a docstring and not trigger the formatter, just hold `ctrl` and press enter.


Default and User Settings
-------------------------
You can configure which docstring format to use by updating your user settings for this package. (`Preferences > Package Settings > DocBlockr Python > Settings (User)`)
For a full list of settings with documentation on what they affect, look at the `Settings (Default)` file.


Project Settings
----------------
You can also override your user settings on a per project basis by editing your project file. Any setting will be available for overriding here.

```json
{
	"DocblockrPython": {
		"formatter": "sphinx"
	},
	"folders": [
	  // ...
	]
}
```


Supported Docstring Styles
--------------------------
- Docblockr (PEP0257 with types)
- [PEP0257](https://www.python.org/dev/peps/pep-0257/)
- [Google](https://google.github.io/styleguide/pyguide.html#Comments)
- [Numpy](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
- [Sphinx (reST)](https://pythonhosted.org/an_example_pypi_project/sphinx.html)


Extendability
-------------
If you don't like the formatting styles above, or want to make your own style to fit your use case, you can write your own formatter.
All you will need to do is extend the [Base formatter](https://github.com/adambullmer/sublime-docblockr-python/blob/master/formatters/base.py#L32) class and write your formatter functions.
If you're not sure about it, you can take a look at any of the other formatters in the `formatters` source dir and see how they did it.

```py
from DocBlockr_Python.formatters.base import Base


class MyFormatter(Base):
    # This will be used as your settings file value,
    # and how the formatter is registered in the registry
    name = 'my'
```

**Note:** The console should yell at you if you didn't write all the abstract methods. Be sure to read the docs on the `Base` formatter
to make sure you understand all the caveats of each formatter function.

Local Development
-----------------

Below are the instructions to work on this repo locally.

1. Clone the repo.
1. Uninstall the plugin from sublime text.
1. Symlink the github repo into your sublime text packages directory.
    - Debian example:
```bash
ln -s <absolute/path/to/github/repo/sublime_docblockr_python> $HOME/.config/sublime-text-3/Packages/Docblockr_Python
```
1. There are no runtime dependencies
1. Pay attention to the sublime console ```ctrl + ` ```


Testing Changes
---------------

In addition to the setup instructions above, testing will require additinoal setup.

**System Requirements:**
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)

**Setup:**
1. Install depedencies through pipenv `pipenv install --dev`
1. Run unit tests `pipenv run tox`
    - [py.test](https://docs.pytest.org/en/latest/) unit tests
    - [flake8](http://flake8.pycqa.org/en/latest/) linting
    - [pydocstyle](http://www.pydocstyle.org/en/2.1.1/) (formerly PEP257) docstring checker


Known Issues
------------
- Only detects closed docstring if it is on a line of the same indentation, and has no text in front of it. Single Line docstrings are converted to block
- The tests run in python `3.4.3`, however sublime's python version is `3.3.6`. This is due to the difficulty of getting a working version of 3.3.6 in a dev environment, and the differences should be minimal.


Roadmap
-------
Things I want to do wtih this project. Not necessarily an exhaustive or prioritized list.

- Unit Tests!
    - Needs a test harness of some sort for sublime internals.
- CI, probably circleci
- Coverage reporting
- More completions!
- Javadoc style formatter
- Keyboard Shortcuts
- Reparsing Docstring (switch templating style)
- Command Pallete Commands for changing syntax
- Dynamic completions based on chosen syntax
- Integration back with the original DocBlockr
- Better Syntax Highlighting within docstrings (in particular for other styles)
- Examples of each style to completion
- Documentation (isn't it ironic?)
