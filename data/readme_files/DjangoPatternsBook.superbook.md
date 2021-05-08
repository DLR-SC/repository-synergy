# SuperBook

SuperBook is a social network for superheroes built with [Python][0] using the [Django Web Framework][1].

## Chapters

These are the chapters containing Django code samples from the book 'Django Design Patterns and Best Practices' by Arun Ravindran:

*  [Chapter 3](https://github.com/DjangoPatternsBook/superbook/tree/chapter03)
*  [Chapter 4](https://github.com/DjangoPatternsBook/superbook/tree/chapter04)
*  [Chapter 5](https://github.com/DjangoPatternsBook/superbook/tree/chapter05)
*  [Chapter 6](https://github.com/DjangoPatternsBook/superbook/tree/chapter06)
*  [Chapter 7](https://github.com/DjangoPatternsBook/superbook/tree/chapter07)
*  [Chapter 9](https://github.com/DjangoPatternsBook/superbook/tree/chapter09)

# Installation

The installation instructions have been split into the following sections:

* Creation of a new Virtual Environment (read your OS-specific section)
* Installation of the superbook project (common for all OS)

## Creation of a new Virtual Environment

Virtual environment module is now bundled with Python 3.4. As it is fairly new, most users might not be familiar with using it. Hence, OS-specific installation instructions are given below.

If you OS or distribution is missing here, please skip to 'Others' section.

### Windows 7 or 8

Follow this [detailed guide](http://arunrocks.com/guide-to-install-python-or-pip-on-windows/). In summary:

1. If you don't have Python 3.4 then download the Python MSI installer from http://www.python.org/download/
2. Run the installer. Be sure to check the option to add Python to your PATH while installing.
3. Open PowerShell as admin by right clicking on the PowerShell icon and selecting ‘Run as Admin’
4. To solve permission issues, run the following command:

		Set-ExecutionPolicy Unrestricted

5. Enter the following commands in PowerShell to download the bootstrap scripts for easy_install and pip:

		mkdir c:\envs
		cd c:\envs

		(new-object System.Net.WebClient).DownloadFile('https://bootstrap.pypa.io/ez_setup.py',   'c:\envs\distribute_setup.py')

		(new-object System.Net.WebClient).DownloadFile('https://raw.github.com/pypa/pip/master/contrib/get-pip.py', 'c:\envs\get-pip.py')

		python c:\envs\distribute_setup.py
		python c:\envs\get-pip.py

	Now typing easy_install or pip should work

6. Check that you have the correct version of Python i.e. Python 3.4 and above:

		$ python --version
		Python 3.4.0

7. To create a Virtual Environment, use the following commands:

		python -m venv sbenv
		.\sbenv\Scripts\Activate.bat

### ArchLinux

Check that you have the correct version of Python i.e. Python 3.4 and above:

	$ python --version
	Python 3.4.0

Create a new virtual environment called `sbenv` and activate it:

	$ python -m venv sbenv
	$ source sbenv/bin/activate

### Ubuntu (14.10 and below)

Install Python 3.4:

	$ sudo apt-get update
	$ sudo apt-get install python3.4

Check that you have the correct version of Python i.e. Python 3.4 and above. Note that you need to mention `python3` command or Python 2 will be executed:

	$ python3 --version
	Python 3.4.2

Create a new virtual environment called `sbenv` (without pip) and activate it:

	$ python3 -m venv --without-pip sbenv
	$ source sbenv/bin/activate

Now you need to install pip. This command need `wget` to be installed first.

	$ wget bootstrap.pypa.io/get-pip.py -O - | python

## Installation of the project

Upgrade your version of pip:

	$ pip install -U pip

**Note**: If `pip` command fails, then you may have to run `python -m ensurepip`

Make sure that `git` is installed before running the next command. Clone the example project from github and install the dependencies.

	$ git clone https://github.com/DjangoPatternsBook/superbook.git
	$ cd superbook
	$ pip install -r requirements.txt

If pip installation fails, especially if you are on Windows, then try forcing the installation of wheels:

	$ pip install --use-wheel -r requirements.txt 

## Running each chapter

Each chapter is a seperate git branch with the naming convention `chapternn`; for e.g. `chapter04`. Once you checkout the chapter don't forget to read the README.md file (which changes) and run the migrate command if applicable:

	$ git checkout chapter04
	$ git clean -f -d
    $ cd src

Now you can read the relevant source code. Each chapter is a standalone running site. So to run the site on the test server, run the following commands:

	$ python manage.py migrate
	$ python manage.py createsuperuser
	$ python manage.py runserver

## Finished Site
	
If you would like to have a look at the finished SuperBook website, just run migrate and start the test server:

	$ git checkout final
	$ python manage.py migrate
	$ python manage.py createsuperuser
	$ python manage.py runserver

**DEMO SITE UNDER CONSTRUCTION**

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
