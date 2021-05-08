# PyYapf

Sublime Text 2-3 plugin to run the [YAPF](https://github.com/google/yapf) Python formatter

## Usage

By default, press `Ctrl-Alt-F` to format the current selection (or the entire document if nothing is selected).
You can also `Ctrl-Shift-P` (Mac: `Cmd-Shift-P`) and select "PyYapf: Format Selection" or "PyYapf: Format Document".
To automatically run YAPF on the current document before saving, use the `on_save` setting.

## Installation

1.  Install YAPF (if you haven't already):
   ```
   pip install yapf
   ```

2.  Install Sublime Package Control by following the instructions [here](https://packagecontrol.io/installation) (if you haven't already).

3.  `Ctrl-Shift-P` (Mac: `Cmd-Shift-P`) and choose "Package Control: Install Package".

4.  Find "PyYapf Python Formatter" in the list (type in a few characters and you should see it).

Alternatively, install manually by navigating to Sublime's `Packages` folder and cloning this repository:

      git clone https://github.com/jason-kane/PyYapf.git "PyYapf Python Formatter"

## Problems?

This makes it pretty easy to find valid python code that makes Yapf choke or give bad formatting.
Please try to reduce any problems to a minimal example and [let the YAPF folks know](https://github.com/google/yapf/issues).
If there is something wrong with this plugin, [add an issue](https://github.com/jason-kane/PyYapf/issues) on GitHub and I'll try to address it.

## Distribution

[Package Control](https://packagecontrol.io/packages/PyYapf%20Python%20Formatter)

## Mentions

* [Must-Have Packages and Settings in Sublime Text for a Python Developer](https://fosstack.com/setup-sublime-python/)
* [Teach yapf and python-fire to Python beginners](https://chibicode.com/posts/yapf-python-fire/)
* [Yapf - we brush the code of Python with autocorrector](https://weekly-geekly.github.io/articles/324336/index.html)
* [Yapf — причесываем код Python автокорректором](https://habr.com/ru/post/324336/)

I love stumbling across things like these, it's a small world sometimes.
* http://blog.leanote.com/post/kaixiang/sublime%E4%B8%AD%E4%BD%BF%E7%94%A8yafp%E6%A0%BC%E5%BC%8F%E5%8C%96python%E4%BB%A3%E7%A0%81
* https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/119839/

## LICENSE

Apache v2 per LICENSE.  Do what you want; if you fix something please share it.
