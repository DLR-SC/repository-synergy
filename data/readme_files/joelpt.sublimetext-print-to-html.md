Sublime Text 2 Print to HTML
============================

A Sublime Text 2 plugin to print files as HTML with color syntax highlighting and line numbers, and open them in your browser for printing.

Colorization and HTML conversion is currently performed by [Pygments][0], which supports a range of [languages and syntaxes][3].

## Installation

 * Install [Package Manager][2].
 * Use `Cmd+Shift+P` or `Ctrl+Shift+P` then `Package Control: Install Package`.
 * Look for `Print to HTML` and install it.

If you prefer to install manually, install git, then:

    git clone https://github.com/joelpt/sublimetext-print-to-html "<Sublime Text 2 Packages folder>/Print to HTML"

## Usage

 * For best results, save your file with an appropriate extension beforehand.
 * To print the current file, use one of the following methods:
   * use `Shift+Alt+P` to print current file as HTML via your browser, or
   * from File menu, use `Print as HTML to Browser` or `Print as HTML to New Buffer`.
   * press `Ctrl+Shift+P` or `Cmd+Shift+P` then type `print`.
 * Edit settings in `Preferences->Package Settings->Print in HTML` to customize output formatting and behavior. Options such as monochrome, line numbering, and browser behavior can be modified.

## Future goals

 * Use ST2's internal scope and color data from a buffer to produce an exact replica of a file from ST2 in HTML form. The current approach using Pygments has limitations regarding formats unknown by Pygments (e.g. Markdown) and documents with mixed syntaxes (e.g. PHP embedded in HTML).

## Credits

This code is available on [Github][1]. Pull requests are welcome.

Created by [Joel Thornton][4]. 

Uses the [Pygments][0] library (included) for code-to-HTML conversion.


 [0]: http://pygments.org/
 [1]: https://github.com/joelpt/sublimetext-print-to-html
 [2]: http://wbond.net/sublime_packages/package_control
 [3]: http://pygments.org/languages/
 [4]: mailto:sublime@joelpt.net