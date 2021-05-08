This kernel adds support for Elm to [Jupyter](http://jupyter.org/) notebooks.

While basic functionality is in place, this is still very much a work in
progress. I'm still figuring it all out. Any help, ideas, etc. would be great.

# Requirements
- Python 3.6+

# Installation

Either install from a repository using `pip`:

```
pip install elm_kernel
```

or install the package from source:

```
pip install -e .
```

Then install the kernel spec:
```
python -m elm_kernel.install
```

# Usage

Run `jupyter notebook` and select the Elm kernel for a new notebook.

## Multi-cell code examples

By default, when you execute a code cell with the Elm kernel the code will *not*
be compiled. Instead, the kernel simply queues up code cells. This way you can
break longer examples over multiple cells, interleaving the code cells with
supporting Markdown cells.

In order to ask the kernel to actually compile your code, you need to terminate
a code cell with the line:

```
-- compile-code
```

When the kernel sees a cell like this it contatenates, in cell-execution order,
all of the executed but uncompiled code cells (i.e. everything since the start
of the kernel or the last `-- compile-code` cell). It then compiles the
concatenated code, returning the result to the notebook.

For a concrete example of this, see
[`examples/the-elm-architecture.ipynb`](https://github.com/abingham/jupyter-elm-kernel/blob/master/examples/the-elm-architecture.ipynb).

This is a bit hacky, and we're actively searching for a better alternative.
Ideas are welcome!

# Examples

The `examples` directory contains a few examples of how to use this kernel. Just
go to that directory and run `jupyter notebook` to see them.
