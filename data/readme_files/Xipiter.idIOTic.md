id-IOT-ic : Simple ways to pop simple devices.
=========

# Overview

idIOTic is a tool that makes attacks on some "IOT" devices "point and click"
simple. It has an interactive CLI. It is also modular so that that as new
"IOT" vulns are published they can be quickly added to this tool without
modification of the code for the tool itself (just drop the new .py into the modules
directory and a command for it is added to the CLI).

This tool accompanies the [Insecurity Of Things](http://www.xipiter.com/musings/the-insecurity-of-things-part-one)
blogpost series at Xipiter. As new vulns are disclosed their exploit "modules" will be added
to this simple little tool.

# Example

```
tachiro:idIOTic s7$ ./idIOTic.py 
Loading 'modules.sucasa' as a 'simple' idIOTic execute module...
Loading 'modules.wemo' as a 'simple' idIOTic execute module...


            ...oooOOO The Internet of Things is idIOTic OOOooo...
   

idIOTic.>> help

Documented commands (type help <topic>):
----------------------------------------
EOF  dropshell  exit  help  hist  pdb  subcmdexample  sucasa  wemo

idIOTic.>> exit
tachiro:idIOTic s7$
```
# Animated Example
![](misc/idiotic.gif)
