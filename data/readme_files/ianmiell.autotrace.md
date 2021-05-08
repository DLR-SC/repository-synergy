# autotrace

Runs a process, and gives you the output along with other telemetry on the
process, all in one terminal window.

Here's me seeing what `ping google.com` (after 'forgetting' to run it under `autotrace`) does by looking at strace and tcpdump, with the command:

```
autotrace
```

You can also run:

```
autotrace 'ping google.com' 'strace -p PID' 'any other commands' ...
```

![Demo](https://raw.githubusercontent.com/ianmiell/autotrace/master/demo.gif)

See [here](https://zwischenzugs.com/2018/05/21/autotrace-debug-on-steroids/) for more.

## Features:

- Pause program in-flight to see what's going on

- Supply PID to pane's command and it gets the main pid sub'd in (see strace in the example above)

- Colorised, multi-pane output

- Output of all commands captured to files (in `/tmp/tmpautotrace/PID/*`)

- Raise PR if you want other features


## Install

```
# Requires:
# python (2 or 3)
# pip
pip install autotrace
```


## Examples

Mac example:

```
$ sudo autotrace \
    'find /' \
    'dtruss -f -p PID' \
    'iostat 1'
```

PID is replaced with the PID of the main (-c) command


Linux example with strace and vmstat:

```
$ sudo autotrace \
    'find /' \
    'strace -p PID' \
    'vmstat 1'
```

Linux example with strace and tcpdump:

```
$ sudo autotrace \
     'nmap localhost' \
     'strace -p PID' \
     'tcpdump -XXs 20000'
```

Example with `while true` script to iterate output:

```
$ sudo autotrace \
    'nmap localhost' \
    'strace -p PID' \
    'tcpdump -XXs 20000' \
    'bash -c "while true; do free; sleep 5; done"'
```

Linux example with more than four panes that can be cycled through by hitting
'm':

```
$ sudo autotrace \
    'nmap localhost' \
    'strace -p PID' \
    'tcpdump -XXs 20000' \
    'bash -c "while true; do free; sleep 5; done"' \
    'bash -c "while true; do lsof -p PID | tail -5; sleep 5; done"' \
```

A (Linux) monster:

```
$ sudo autotrace \
    'nmap localhost' \
    'strace -p PID' \
    'tcpdump -XXs 20000' \
    'bash -c "while true; do free; sleep 5; done"' \
    'bash -c "while true; do lsof -p PID | tail -5; sleep 5; done"' \
    'bash -c "while true; do pstree -p PID | tail -5; sleep 5; done"' \
    'bash -c "while true; do cat /proc/interrupts; sleep 1; done"'
```

