#+OPTIONS: html-postamble:nil toc:nil
#+INFOJS_OPT: view:t toc:t ltoc:t mouse:underline buttons:0 path:http://thomasf.github.io/solarized-css/org-info.min.js
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="http://thomasf.github.io/solarized-css/solarized-light.min.css" />
#+TITLE: Dotty, a dotfile sync tool

#+BEGIN_CENTER
[[https://github.com/vibhavp/dotty][View on Github]]

Dotty is a little python script for syncing dotfiles stored on your git repo.
#+END_CENTER

* Installation:
  Add dotty to your dotfiles git repository:
  
  ~git submodule add https://github.com/vibhavp/dotty~
  
  To Update dotty to the latest version:
  
  ~git submodule update --remote dotty~
  
* Configuration
  Dotty uses a JSON-formatted config located on the root of your dotfile repository.
  Currently, dotty can create/check ~directories~, ~link~ or ~copy~ files/directories, ~install~ packages and execute shell ~commands~. 

* Example
  #+BEGIN_SRC javascript
    {
        "directories": ["~/emacs.d"],
        
        "link": {
            "source": "dest",
            "zshrc": "~/.zshrc"
            //directories can be linked too
            "emacs/lisp/": "~/.emacs.d/lisp"
        },

        "copy": {
            "source": "dest",
            "offlineimaprc": "~/.offlineimaprc"
        },

        "install_cmd": "pacaur -Syu",
        "install": [
            "zsh",
            "emacs"
        ],
		
        "commands": [
            "emacs -batch -Q -l ~/.emacs.d/firstrun.el"
        ]
    }
  #+END_SRC
  
* Usage
  #+BEGIN_SRC sh
    usage: dotty.py [-h] [-r] config

    positional arguments:
      config         the JSON file you want to use

    optional arguments:
      -h, --help     show this help message and exit
      -r, --replace  replace files/folders if they already exist
  #+END_SRC 
