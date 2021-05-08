# SelectUntil

Fill a void in your Sublime Text multiple selection capabilities! This plugin allows you to extend each selection until the next instance of a search term, making it super easy to edit multiple pieces of text that are similar but not quite the same enough.

## Usage

- <kbd>ctrl/alt</kbd> + <kbd>shift</kbd> + <kbd>s</kbd>: pulls up an input field, where you can type:

	- `search term` or `[search term]`: for each selection, select up to and including the first occurrence of the search term.
	- `/regex search/`: select through the first occurrence of the regex.
	- `{character count}`: select forward the given number of characters.
	- `-[search term]`: select backwards up to and including the search term.
	- `-/regex/`: backwards regex.
	- `-{character count}`: select backwards a certain number of characters (`{-count}` works too).

- <kbd>ctrl/alt</kbd> + <kbd>shift</kbd> + <kbd>s</kbd> a second time: reverses the search direction.

- <kbd>ctrl/alt</kbd> + <kbd>shift</kbd> + <kbd>r</kbd>: reverse all selections (so if the insertion point is at the end of the selection, it is moved to the beginning, and vice versa).

On Windows and Linux the default shortcuts use <kbd>alt</kbd>.  On OSX <kbd>ctrl</kbd> is used.

## Getting SelectUntil

The easiest way to get SelectUntil is with [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation).  Search for "SelectUntil".

Alternatively you can clone this git repository into your [Packages Directory](http://sublimetext.info/docs/en/basic_concepts.html):

	git://github.com/xavi-/sublime-selectuntil.git

## Developed by

* Xavi Ramirez
* [Nikolaus Wittenstein](https://github.com/adzenith)

## License

This project is released under [The MIT License](http://www.opensource.org/licenses/mit-license.php).
