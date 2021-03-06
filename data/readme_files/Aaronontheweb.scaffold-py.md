h1. Scaffold for Python

Inspired by "Zed Shaw's":http://www.zedshaw.com/ recommended Python project structure from "Learn Python the Hard Way":http://learnpythonthehardway.org/ exercise "#46":http://learnpythonthehardway.org/book/ex46.html.

Each project you scaffold will create the following directory structure:

<pre>
/[projectname]/
/[projectname]/setup.py
/[projectname]/bin
/[projectname]/docs
/[projectname]/[projectname]
/[projectname]/[projectname]/__init__.py
/[projectname]/tests
/[projectname]/tests/__init__.py
/[projectname]/tests/[projectname]_tests.py
</pre>

Both @setup.py@ and @[projectname]_tests.py@ are set up automatically to reference your project name as a module. The rest is up to you!

h2. Installing Scaffold

You can view the scaffold package on PyPi here: "http://pypi.python.org/pypi/Scaffold/0.1.3":http://pypi.python.org/pypi/Scaffold/0.1.3

To install, simply use @pip install scaffold@

h2. Running Scaffold

Scaffold installs itself as an executable Python script, so just enter the @pyscaffold@ command on your favorite terminal:

<pre>pyscaffold -p "projectname" [-d {base directory}]</pre>

You can also run scaffold as a python module if needed:

<pre>python -m scaffold -p "projectname" [-d {base directory}]</pre>

The @-p@ parameter is the name of your project and is a required field. If you don't specify a base directory with the @-d@ parameter, scaffold will assume that you want to create your project skeleton in your current working directory.

h3. Sample Usage:

Just to give you an idea of what works and what doesn't...

<pre>pyscaffold -p "http-utils" -d /c/repositories/
pyscaffold -p "mutliplex-py"
pyscaffold -p "lazarus" -d ../</pre>

h2. Virtualenvwrapper support

Alternatively, if (the excellent) "virtualenvwrapper":http://virtualenvwrapper.readthedocs.org is installed, Scaffold also works as a "project template":https://virtualenvwrapper.readthedocs.org/en/latest/projects.html#using-templates named _base_. So you could run:

<pre>mkproject -t base projectname</pre>

Then virtualenvwrapper will create the virtualenv and the project root and Scaffold will do the rest.

h2. License

Licensed under Apache 2.0 - see license.txt for details.

h2. Contribution

I'm not the most experienced Python programmer on the planet, so patches are most certainly welcome :)
-"Aaron Stannard":http://www.aaronstannard.com/
