storm-indicator
===============

A unity indicator for connecting to your SSH hosts easily.

<img src="http://i.imgur.com/0TG2kTi.png">

**storm-indicator** uses <a href="http://linux.die.net/man/5/ssh_config">~/.ssh/config</a> files to list SSH connections. If you don't use your SSH config file yet,  you can optionally use <a href="http://www.github.com/emre/storm">storm</a>
to easily add your servers. 


### installation ###


```
$ sudo pip install storm_indicator
```
or if you like 90s:

```
$ sudo easy_install storm_indicator
```

### running ###

just type:

```
$ ssh_list_indicator
```

**Note**: You might want to add ssh_list_indicator to your <a href="https://help.ubuntu.com/community/AddingProgramToSessionStartup">startup applications</a>.




