CMDTree
-------
[![PyPI version](https://badge.fury.io/py/cmdtree.svg)](https://badge.fury.io/py/cmdtree)
[![Build Status](https://travis-ci.org/winkidney/cmdtree.svg?branch=master)](https://travis-ci.org/winkidney/cmdtree) 
[![Coverage Status](https://coveralls.io/repos/github/winkidney/cmdtree/badge.svg?branch=master)](https://coveralls.io/github/winkidney/cmdtree?branch=master)


Yet another cli library for python, click-like but sub-command friendly
and designed for cli auto-generating. 

Let's generate your command line tools from a cmd_path
or just use shortcut decorators like `click`.


## Feature
+ Designed for cli auto-generating(make your commands by program)
+ Easy to use: works like `click`
+ Friendly low-level api(Use a tree and add your command by `command path`!)
+ no extra dependencies(only `six` is needed)
+ Python3 support
+ argument-type support 
+ decorators has no side-effect on function call(call it in any other
place in python style)

## Install 
run `pip install cmdtree` or clone the repo and use it.

## Run Test
+ `pip install -r test-requirements.txt`
+ `make test` or `py.test cmdtree`

## Quick Start

**Note**: Follow the examples in folder `examples`.

### Hello world
```python
from cmdtree import INT
from cmdtree import command, argument, option


@argument("host", help="server listen address")
@option("reload", is_flag=True, help="if auto-reload on")
@option("port", help="server port", type=INT, default=8888)
@command(help="run a http server on given address")
def run_server(host, reload, port):
    print(
        "Your server running on {host}:{port}, auto-reload is {reload}".format(
            host=host,
            port=port,
            reload=reload
        )
    )

if __name__ == "__main__":
    from cmdtree import entry
    entry()
```

Get help
```bash
➜  examples git:(master) python command.py --help
usage: command.py [-h] {run_server} ...

positional arguments:
  {run_server}  sub-commands
    run_server

optional arguments:
  -h, --help    show this help message and exit
```

Run command 
```bash
➜  examples git:(master) python command.py run_server localhost
Your server running on localhost:8888, auto-reload is False
```


### SubCommand of SubCommand

Code here:
```python
from cmdtree import group, argument, entry

@group("docker")
@argument("ip")
def docker():
    pass


# nested command
@docker.command("run")
@argument("container-name")
def run(ip, container_name):
    print(
        "container [{name}] on host [{ip}]".format(
            ip=ip,
            name=container_name,
        )
    )

# nested command group
@docker.group("image")
def image():
    pass


@image.command("create")
@argument("name")
def image_create(ip, name):
    print(
        "iamge {name} on {ip} created.".format(
            ip=ip,
            name=name,
        )
    )


if __name__ == "__main__":
    entry()
```

Run command:
```bash
➜  examples git:(master) python command_group.py docker localhost image create your-docker
iamge your-docker on localhost created.
```


## Why `cmdtree`?
Alternatives:
+ [`click`](http://click.pocoo.org/5/) from `pocoo`
+ `argparse`

But when you should choose `cmdtree`?

When you need:
+ fully sub-command support(not `group` in `click`)
+ Higher-level api support(compared to `argparse`)
+ More arg-type support(compared to `argparse`)
+ decorators has no side-effect on function call(compared to `click`)

In both of them, you have to make implementation yourself.
CmdTree works on this point.

In most case , you can make your command `flat`. 
But when you need sub-command? 

I use it in my `schema-sugar` project,
the project generate cli-tool from schema that describes REST-API.

For example:
You want to generate a `CRUD` commandline for http resources,

```bash
# list the resource 
GET http://example.com/computer/disks
# show one of the disk info
GET http://example.com/computer/disks/1
# delete
DELETE http://example.com/computer/disks/1
```

I want to make a command line just like
```bash
rest-cli computer disks list
rest-cli computer disks delete <id>
rest-cli computer disks show <id>
```
The `computer` is to used to make the resource `unique`, so I can not
ensure that all of the commands could be made `flat`.

`click` lacks the support for multiple-level sub-command.

`argparse` has very low-level api(really makes me crazy).

So I wrote `cmdtree` to handle this problem. Now I just wrote:
```python
from cmdtree.tree import CmdTree

tree = CmdTree()


def index():
    print("Hi, you have 10 disks in your computer...")


def show(disk_id):
    print("This is disk %s" % disk_id)


def delete(disk_id):
    print("disk %s deleted" % disk_id)


# Add list command
tree.add_commands(["computer", "list"], index)

# get the parser in any place, any time
tree.add_commands(["computer", "show"], show)
tree_node = tree.get_cmd_by_path(["computer", "show"])
show_parser = tree_node['cmd']
show_parser.argument("disk_id")

# Add delete command
delete3 = tree.add_commands(["computer", "delete"], delete)
delete3.argument("disk_id")

# run your tree
tree.root.run()
```

## Change Log
+ 2016.09.22 Fix help-message missing in command and group
+ 2016.09.08 Global argument support


## Inspired by
+ `click`
+ `argparse`

## About

Author: [winkidney@github](https://github.com/winkidney/)

Repo: [GithubRepo](https://github.com/winkidney/cmdtree)

Blog: [Blog](http://blog.winkidney.com)