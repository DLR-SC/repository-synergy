Waldo is a lightweight and multithreaded directory and subdomain bruteforcer implemented in Python. It can be used to locate hidden web resources and undiscovered subdomains of the specified target.

Key Features
------------

- Quickly and easily generate a list of all subdomains of target domain
- Discover hidden web resources that can be potentially leveraged as part of an attack
- Written in Python and very portable
- Fast, multithreaded design

Setup
-----

Dependencies can be installed by running:

	$ pip install -r pip.req

To run the waldo:

	$ python waldo.py

Usage
-----

To enumerate subdomains at some-fake-site.example, execute the following:

	$ python waldo.py -m s -d some-fake-site.example

To enumerate directories at some-fake-site.example, execute the following:

	$ python waldo.py -m d -d some-fake-site.example

By default, output will be logged to waldo-output.txt. To specify a custom
output file, use the -l flag:

	$ python waldo.py -m s -l my-log-file.txt -d some-fake-site.example

Waldo uses 4 threads by default. To specify a custom threadpool size, use
the -t flag:

	$ python waldo.py -m s -d some-fake-site.example -t 15
