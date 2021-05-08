# Gluish

Note: v0.2.X cleans up some cruft from v0.1.X. v0.2.X still passes the same
tests as v0.1.X, but removes a lot of functionality unrelated to luigi. Please
check, before you upgrade.

Luigi 2.0 compatibility: gluish 0.2.3 or higher.

----

[![Build Status](https://img.shields.io/travis/miku/gluish.svg?style=flat)](https://travis-ci.org/miku/gluish)
[![pypi version](https://badge.fury.io/py/gluish.png)](https://pypi.python.org/pypi/gluish)
[![DOI](https://zenodo.org/badge/17902915.svg)](https://zenodo.org/badge/latestdoi/17902915)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

Some glue around [luigi](https://github.com/spotify/luigi).

Provides a base class, that autogenerates its output filenames based on
* some base path,
* a tag,
* the task id (the classname and the significant parameters)

Additionally, this package provides a few smaller utilities, like a TSV format,
a benchmarking decorator and some task templates.

This project has been developed for [Project finc](https://finc.info) at [Leipzig University Library](https://ub.uni-leipzig.de).

## A basic task that knows its place

`gluish.task.BaseTask` is intended to be used as a supertask.

```python
from gluish.task import BaseTask
import datetime
import luigi
import tempfile

class DefaultTask(BaseTask):
    """ Some default abstract task for your tasks. BASE and TAG determine
    the paths, where the artefacts will be stored. """
    BASE = tempfile.gettempdir()
    TAG = 'just-a-test'

class RealTask(DefaultTask):
    """ Note that this task has a `self.path()`, that figures out the full
    path for this class' output. """
    date = luigi.DateParameter(default=datetime.date(1970, 1, 1))
    def run(self):
        with self.output().open('w') as output:
            output.write('Hello World!')

    def output(self):
        return luigi.LocalTarget(path=self.path())
```

When instantiating a `RealTask` instance, it will automatically be assigned a
structured output path, consisting of `BASE`, `TAG`, task name and a slugified
version of the significant parameters.

```python

task = RealTask()
task.output().path
# would be something like this on OS X:
# /var/folders/jy/g_b2kpwx0850/T/just-a-test/RealTask/date-1970-01-01.tsv

```

## A TSV format

Was started on the
[mailing list](https://groups.google.com/forum/#!searchin/luigi-user/TSV/luigi-user/F813st16xqw/xErC6pXR8zEJ).
Continuing  the example from above, lets create a task, that generates TSV
files, named `TabularSource`.

```python

from gluish.format import TSV

class TabularSource(DefaultTask):
    date = luigi.DateParameter(default=datetime.date(1970, 1, 1))
    def run(self):
        with self.output().open('w') as output:
            for i in range(10):
                output.write_tsv(i, 'Hello', 'World')

    def output(self):
        return luigi.LocalTarget(path=self.path(), format=TSV)
```

Another class, `TabularConsumer` can use `iter_tsv` on the handle obtained
by opening the file. The `row` will be a tuple, or - if `cols` is specified -
a `collections.namedtuple`.

```python
class TabularConsumer(DefaultTask):
    date = luigi.DateParameter(default=datetime.date(1970, 1, 1))
    def requires(self):
        return TabularSource()

    def run(self):
        with self.input().open() as handle:
            for row in handle.iter_tsv(cols=('id', 'greeting', 'greetee'))
                print('{0} {1}!'.format(row.greeting, row.greetee))

    def complete(self):
        return False
```

## Easy shell calls

Leverage command line tools with [`gluish.utils.shellout`](https://github.com/miku/gluish/blob/943993d29fe88d352d110620a717303b19897577/gluish/utils.py#L199). `shellout` will
take a string argument and will format it according to the keyword arguments.
The `{output}` placeholder is special, since it will be automatically assigned
a path to a temporary file, if it is not specified as a keyword argument.

The return value of `shellout` is the path to the `{output}` file.

Spaces in the given string are normalized, unless `preserve_whitespace=True` is
passed. A literal curly brace can be inserted by `{{` and `}}` respectively.

An exception is raised, whenever the commands exit with a non-zero return value.

Note: If you want to make sure an executable is available on you system before the task runs,
you *can* use a [`gluish.common.Executable`](https://github.com/miku/gluish/blob/943993d29fe88d352d110620a717303b19897577/gluish/common.py#L106) task as requirement.

```python
from gluish.common import Executable
from gluish.utils import shellout
import luigi

class GIFScreencast(DefaultTask):
    """ Given a path to a screencast .mov, generate a GIF
        which is funnier by definition. """
    filename = luigi.Parameter(description='Path to a .mov screencast')
    delay = luigi.IntParameter(default=3)

    def requires(self):
        return [Executable(name='ffmpg'),
                Executable(name='gifsicle', message='http://www.lcdf.org/gifsicle/')]

    def run(self):
        output = shellout("""ffmpeg -i {infile} -s 600x400
                                    -pix_fmt rgb24 -r 10 -f gif - |
                             gifsicle --optimize=3 --delay={delay} > {output} """,
                             infile=self.filename, delay=self.delay)
        luigi.LocalTarget(output).move(self.output().path)

    def output(self):
        return luigi.LocalTarget(path=self.path())
```

## Dynamic date parameter

Sometimes the *effective* date for a task needs to be determined dynamically.

Consider for example a workflow involving an FTP server.

A data source is fetched from FTP, but it is not known, when updates are
supplied. So the FTP server needs to be checked in regular intervals.
Dependent tasks do not need to be updated as long as there is nothing new
on the FTP server.

To map an arbitrary date to the *closest* date in the past, where an update
occured, you can use a `gluish.parameter.ClosestDateParameter`, which is just an ordinary
`DateParameter` but will invoke `task.closest()` behind the scene, to
figure out the *effective date*.

```python

from gluish.parameter import ClosestDateParameter
import datetime
import luigi

class SimpleTask(DefaultTask):
    """ Reuse DefaultTask from above """
    date = ClosestDateParameter(default=datetime.date.today())

    def closest(self):
        # invoke dynamic checks here ...
        # for simplicity, map this task to the last monday
        return self.date - datetime.timedelta(days=self.date.weekday())

    def run(self):
        with self.output().open('w') as output:
            output.write("It's just another manic Monday!")

    def output(self):
        return luigi.LocalTarget(path=self.path())

```

A short, self contained example can be found in [this gist](https://gist.github.com/miku/e72628ee54fce9f06a34).
