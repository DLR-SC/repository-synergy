lcurse
======

Python script to have a "curse" compatible client for linux


lcurse nowadays supports git repositories too.
As git repos aren't structured the same, you will most probably need to create an link via "ln -s source destination" inside the wow/Interface/Addons folder.
But at least the update is then done via the usuall lcurse way.

### Requirements
* python 3.6
* pipenv
* PyQt5
* bs4
* cfscrape
* lxml

All requirements can be installed with:
```bash
pipenv install
```

## Running

Simply:
```bash
pipenv run ./lcurse
```

### Unattended mode

You may also run `lcurse` in "unattended mode" once you have set it up. This
will update all your addons and then exit. Use
```bash
pipenv run ./lcurse --auto-update
```
