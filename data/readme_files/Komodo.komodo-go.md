[Komodo](http://www.activestate.com/komodo) extension to add support for the [Go
language](http://golang.org).

![Example screenshot](https://github.com/Komodo/komodo-go/raw/master/example.png)

I haven't yet put up a build to the [Komodo addons
site](http://community.activestate.com/addons) so you'll have to build it
yourself for now. We'll be including this in Komodo builds by default starting
from Komodo 9.

# Features

- File-type language detection for .go files
- Syntax highlighting (including folding)
- Syntax Checking (linting)
- Codeintel via [Gocode](https://github.com/nsf/gocode)
  - Code Outline (for Code Browser and Sections List in IDE)
  - Jump to definition via [godef](http://godoc.org/code.google.com/p/rog-go/exp/cmd/godef)

# Requirements

- Install 'go' and 'gocode', ensure are on the PATH configured in your overall
  or project-specific Komodo settings
- For code completion and go to definition ensure 'gocode' and 'godef' are on
  your paths as well. To install gocode and godef:
  - $ go get github.com/nsf/gocode
  - $ go get code.google.com/p/rog-go/exp/cmd/godef

# Building

- Find the 'koext' binary that is within your Komodo install (within sdk/bin).
- Run 'koext build' from the repository root, it should produce an .xpi for you.
- Open this .xpi with Komodo to install it.
