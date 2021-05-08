![Header logo](artwork/header@2x.png)

Cookiecutter template for bleeding edge Python development. See [@audreyr/cookiecutter][cookiecutter].

The template aspires adoption of new and exciting developer tools. Focus is on automation and keeping your repo DRY. Whenever justifiable, new and Python-native is preferred over "tried and true".

### Automation
Automate everything. Banish tedious tasks. Ensure reproducibility. Minimize errors.

- [pytest][pytest] for test discovery and automation
- [Travis][travis] for continuous integration
- [bumpversion][bumpversion] for updating version numbers with *one* command
- [Invoke][invoke] for task execution as a Python-native Make replacement
- [Coveralls.io][coveralls] for integrating test coverage with GitHub 

### Standardization
Embrace conventions. Don't fret details when you don't have to. Make it easy for others to help you out.

- [EditorConfig][editorconfig] for maintaing consistent coding styles
- [wheel][wheel] for the future standard in Python packaging
- Sensible conventions with first class GitHub support like ``CONTRIBUTING.md``
- Let setuptools generate virutal scripts for you by deep linking into your package (see ``setup.py`` for more details)

### Comparmentalization
Level out inconsistencies between platforms. Virtualize. Simplify development. Inspire experimentation.

- [conda][conda] as an optional, improved "virtualenv" replacement
- [Vagrant][vagrant] to define and share development environments, provisioned by [Ansible][ansible].

### Python 2 vs. 3
Python 2.7.x isn't bleeding edge but it would be crazy to not officially support it. The compromise is developing for Python 3 first and ensure backwards compatability through a lightweight ``_compat.py`` module.


## Usage
In your projects folder, scaffold a brand new Python project:

```bash
$ cookiecutter https://github.com/robinandeer/cookiecutter-pyvanguard.git
```

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Sign up and activate your repo at [coveralls.io][coveralls].
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987


## Not feeling adventurous?
Don't worry, you have options; fork, remix, and pull requests!

### Similar Cookiecutter Templates

* [Nekroze/cookiecutter-pypackage][nekroze]: with PyTest test runner, strict flake8 checking with Travis/Tox, and some docs and *setup.py* differences.

* [tony/cookiecutter-pypackage][tony]: with py2.7+3.3 optimizations. Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions. See ``README.rst`` or the [github comparison view][github-comparison] for exhaustive list of additions and modifications.

* Also see the [network][network] and [family tree][family-tree] for this repo. (If you find anything that should be listed here, please add it and send a pull request!)

### Fork This / Create Your Own
If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

### Or Submit a Pull Request
I also accept pull requests on this repository provided they are small, atomic, and if they make the overall packaging experience better.


[ansible]: http://www.ansible.com/home
[bumpversion]: https://github.com/peritus/bumpversion
[conda]: http://conda.pydata.org/docs/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[coveralls]: https://coveralls.io/
[editorconfig]: http://editorconfig.org/
[family-tree]: https://github.com/robinandeer/cookiecutter-pyvanguard/network/members
[github-comparison]: https://github.com/tony/cookiecutter-pypackage/compare/robinandeer:master...master
[inspiration]: http://thenounproject.com/term/cutting-edge/14935/
[invoke]: http://invoke.readthedocs.org/en/latest/
[nekroze]: https://github.com/Nekroze/cookiecutter-pypackage
[network]: https://github.com/robinandeer/cookiecutter-pyvanguard/network
[pytest]: http://pytest.org/latest/
[tony]: https://github.com/tony/cookiecutter-pypackage
[travis]: https://travis-ci.org/
[vagrant]: http://www.vagrantup.com/
[wheel]: http://wheel.readthedocs.org/en/latest/
