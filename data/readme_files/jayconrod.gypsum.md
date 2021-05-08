[![Build Status](https://travis-ci.org/jayconrod/gypsum.svg?branch=master)](https://travis-ci.org/jayconrod/gypsum)

# Introduction

Gypsum is an experimental new programming language. In the future, it
will be useful for developing high-performance desktop and web
applications and games.

Gypsum is a compiled, statically-typed, object-oriented language. Once
the compiler is more fully implemented, it will be functional as
well. The compiler generates bytecode for a virtual machine,
CodeSwitch. CodeSwitch currently provides basic interpretation and
memory management. Eventually, it will have an optimizing JIT compiler
and will be able to execute bytecode for other languages.

The syntax of Gypsum is inspired by Python and Scala. It is designed
to be simple, requiring less extraneous punctuation than most
languages. Here's how "hello world" is written:

```
def main =
  print("Hello, world!\n")
```

You can find several simple programs in the `examples` directory. You
can find instructions for running them in
[examples/README.md](examples/README.md).

# Projects

## Gypsum compiler

The Gypsum compiler can be found in the `gypsum` directory. It is
written in Python (2.7). Once the language is mostly complete, the
compiler will be rewritten in Gypsum.

You can build an installable Python package with
[Bazel](https://bazel.build/versions/master/docs/install.html) and
install it with pip.

```
bazel build :gypsum
sudo pip install --upgrade bazel-bin/gypsum-0.tar.gz

gypsumc file1.gy file2.gy... -o program.csp
```

To test the compiler:

```
bazel test gypsum:all
```

## CodeSwitch virtual machine

The CodeSwitch virtual machine can be found in the `codeswitch`
directory. It is intended to be minimal. Currently, it can load
packages (.csp files), manage memory (including a basic copying
garbage collector), and interpret bytecode (with a simple switch
loop).

To build and test the VM:

```
bazel test codeswitch:all
```

To build a standalone command line tool which can run Gypsum code:

```
bazel build codeswitch:codeswitch_cmd
```

See the `examples` directory for some programs to try out.

## Standard library

The standard library can be found in the `std` directory. It includes
some basic data structures (`Option`, `Tuple`, `Dict`, `Set`, ...) and
some useful traits (`Eq`, `Hash`, `Iter`, ...). All gypsum packages
depend on the standard library by default. There is also a `std/io`
library that provides access to files.

To build the standard library:

```
bazel build std std/io
```

## Other goodies

An experimental Emacs major mode for Gypsum is in
`tools/gypsum-mode.el`. It provides basic syntax highlighting.

To install, use `M-x package-install-file`, then add this to your `.emacs`:

```
(require 'gypsum-mode)
```

## Requirements

Gypsum and CodeSwitch are developed and tested on Ubuntu 14.04. They
have also been tested in MacOS Sierra and Ubuntu 16.04. They may work
on other platforms with some light modification.

CodeSwitch currently only supports 64-bit x86 platforms. Support for
other architectures will be added in the future.

## Dependencies

* [Bazel](https://bazel.build/versions/master/docs/install.html) is
  needed to build and test everything. It's also needed to run the
  examples.
* You will need Java 1.8 to run Bazel. It includes installation
  instructions on how to set that up if you don't have it installed
  already.
* Python 2.7 is needed to run the compiler and to generate some files
  needed for CodeSwitch.
* PyYAML is needed to parse some data files needed for the Gypsum
  compiler and for CodeSwitch. Bazel will fetch it automatically when
  you build Gypsum.
* Doxygen is needed to generate documentation.

Gypsum and CodeSwitch were developed and tested on Ubuntu 16.04 and
MacOS X 10.11. They may work on other platforms with some
modification, but nothing else is officially supported right now.
