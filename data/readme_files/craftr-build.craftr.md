[Ninja]: https://ninja-build.org/
[Node.py]: https://github.com/nodepy/nodepy

# The Craftr build system (v4.x)

<img align="right" src="logo.png">

Craftr is a Python based meta build system with a focus on compilation of
C and C++ projects, but also supports Cython, C# and Java out of the box.
It uses [Ninja] under the hood for parallel builds.

Build scripts are written in Python and we call them "Modules". The files
are called `build.craftr` and have some language extensions and additional
built-ins provided via [Node.py] and the Craftr API.

A build script usually imports the Craftr API first, then declares its
name and version and from that point targets can be declared. Code of
`.craftr` files is preprocessed to allow for syntactic sugar, but all
functionality can also be replicated with the functional API.

```python
import * from 'craftr'            # 1)
project('myproject', '1.0-0')     # 2)

target('main', 'cxx:build',       # 3)
{
  'cxx.srcs': glob('src/*.cpp'),  # 4)
  'cxx.type': 'executable'        # 5)
})
```

To build and run the executable, use (6)

    $ craftr -cb --variant=release main:cxx.run@="World"
    Hello, World!

__Explanation__

1) Import all members of the Craftr API. We only use `project()` and
   `target()` in this example.
2) Call the `project()` function to specify the module's name and version.
   This is used for constructing unique target identifiers and folders
   in the build output directory.
3) Declare a new target called "main" that is converted into build
   instructions using the `cxx:build` finalizer. Following are the
   properties of the target.
4) Specify the `cxx.srcs` property with all `.cpp` files in the `src/`
   directory relative to the build script's parent directory.
5) Set the `cxx.type` property to "executable" in order to create an
   executable from the source files.
6) The `-c` flag, or `--configure`, is used to run the build script and
   generate a Ninja build manifest.  
   The `-b` flag, or `--build`, indicates that the build should be executed right
   afterwards.  
   With `--variant=release`, you specify a release build (as opposed to the
   default `--variant=debug`).  
   The `main:cxx.run` argument specifies the target and operator to build --
   and this is the name of the target that is automatically generated for
   invoking the executable that is built for the target `main`.  
   The `@="World"` part that is appended directly to the operator is passed
   to the executable that is executed with the `main:cxx.run` operator. In the
   example above, the executable takes the first argument and prints it as
   `Hello, %s!`.

__Important Built-ins and API Members__

- `BUILD` <sup>api</sup>
- `OS` <sup>api</sup>
- `project()` <sup>api</sup>
- `target()` <sup>api</sup>
- `properties()` <sup>api</sup>
- `module` <sup>builtin</sup>
- `module.options` <sup>builtin</sup>
- `require()` <sup>builtin</sup>

## Installation

Craftr requires Python 3.6 or newer (preferrably CPython) and can be installed
like any other Python modules.

    $ pip install craftr-build

To install the latest version from the Craftr GitHub repository use:

    $ pip install git+https://github.com/craftr-build/craftr.git -b develop

## Tips & Tricks

### How to show Python warnings?

The Craftr API makes some usage of the Python `warnings` module. If you want
warnings to be displayed, you can add `PYTHONWARNINGS=once` to the environment,
or use the `--pywarn [once]` command-line flag which is usually preferred
because you won't see the warnings caused by your Python standard library.

---

<p align="center">Copyright &copy; 2018 Niklas Rosenstein</p>
