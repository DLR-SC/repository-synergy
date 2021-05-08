# pyfs


Mount python — it's fun, not a typo, and next to pointless!

*pyfs* is a [FUSE](http://fuse.sourceforge.net/) implementation that gives a filesystem view on [Python](http://www.python.org/) modules.

Why is that cool? You can do stuff like this:

    lib$ os/path/join /this is a path
    /this/is/a/path

Yes, that's `os.path.join` doing the work. Or look at this:

    lib$ string/capwords "let's do some python … not."
    Let's Do Some Python … Not.
	lib$ string/capwords once-more-unto-the-breach -
	Once-More-Unto-The-Breach

You can have a look at the docstring, if need be:

    lib$ os/path/join -h
    usage: join [-h] [funcargs [funcargs ...]]
    
    Join two or more pathname components, inserting '/' as needed. If any
    component is an absolute path, all previous path components will be discarded.
    An empty last part will result in a path that ends with a separator.
    
    positional arguments:
      funcargs
    
    optional arguments:
      -h, --help  show this help message and exit
    ~/test-pyfs$ 
    

Come on, that is cool, yes? Sure, it's a whee bit superfluous, a solution to no problem, but, hey, it'll get much better soon! Promise!

The whole thing started, when I had [a look at Python's FUSE modules](http://mknecht.github.io/fuse-and-python/). If you want an overview about those, go over there.


## The structure of the filesystem

How does the root of the mountpoint look like? For example, like so:

    $ tree -L 2
    .
    ├── bin
    ├── dot
    ├── lib
    │   ├── __builtin__
    │   ├── json
    │   ├── os
    │   ├── re
    │   ├── string
    │   └── sys
    └── run
        └── modules
    
(Slightly cut.)

## Runtime modifications

Wonder what `run/modules` does? It's a file. You can `cat` it:

    $ cat run/modules 
    sys
    json
    os
    string
    __builtin__

But, you can also *add* modules:

    $ echo re >> run/modules 
	$ ls lib
	__builtin__  json  os  re  string  sys

And then you can use it:

	$ lib/re/match "\d+a" 33434a
	<_sre.SRE_Match object at 0x10641d0>

Or, you can get rid of the imported modules:

    $ echo > run/modules 
    $ ls lib/
    $ cat run/modules 
    $ 

## Piping

Use pipes to concatenate Python commands. The dash character, “-”, marks the place where each element should go.

	lib$ echo Hello World | string/index - Wor | string/zfill - 10
	0000000006

## bin

Add bin/ to your PATH and get everything from __builtin__ readily available:

    $ pow 2 10
	1024

## Object attributes

You can access attributes of an object using the directory `dot`. The attribute names cannot be resolved automatically, but if you know what you want, you'll get it.

    echo Hallo | dot/__doc__
    str(object='') -> string
    
    Return a nice string representation of the object.
    If the argument is a string, the return value is the same object.

If the attribute is callable, it will be called with the given arguments.

    $ echo Hello world | dot/split | lib/string/join ' -> '
    Hello -> world

    $ echo Hello=world | dot/split = | lib/string/join ' -> '
    Hello -> world

## How to use it

Get fusepy.

    pip install fusepy

Clone the repo and run:

	mkdir mountpoint
    python  -m pyfs.filesystem mountpoint

(No pip package / setup.py just yet, sorry!)

In the dir `mountpoint` you'll find the filesystem to play with.

Unmount using:

    fusermount -u mountpoint


## More weird ideas for the future

* Transform arguments by introspection:
  * positional parameters are made explicit by adding them to the argparse Parser
  * keyword parameters are turned into optional argparse arguments
* `$ lib/SimpleHttpServer/.self 8080   # python -m SimpleHttpServer 8080`
* provide a meta function to install packages in some virtualenv, so they can be loaded. (can I create a virtualenv at startup in memory and use that? /temp would be another option)

To be continued …
