# Backdoor-pyc

Replace pyc files with malicious pyc files.


## Change Log

####11/10/2015
* No more writing to tmp, just edit the pyc file directly
* Bug fixes 

## Prior work


	https://www.virusbtn.com/virusbulletin/archive/2011/07/vb201107-reversing-Python#id3072912
	https://github.com/jgeralnik/Pytroj
	http://www.slideshare.net/iamit/infecting-python-bytecode

## Usage

	python27|python3X ./backdoor-pyc27.py -h

	Usage: backdoor-pyc27.py [-h] [-p PATH] [-l NIX] [-w WINDOWS]

	To replace utf_8.pyc with your code...

	optional arguments:
	  -h, --help            show this help message and exit
	  -p PATH, --path PATH  path to utf_8.pyc
	  -l NIX, --nix NIX     payload for nix
	  -w WINDOWS, --windows WINDOWS
	                        payload for windows



	*Make edits to the testing27.py file [HOST]*

	For python27
	python ./backdoor-pyc27.py -l testing27.py -p /usr/lib/python27/encodings/utf_8.py


	For python3.X 
	python3 ./backdoor-pyc3X.py -l testing3X.py -p /usr/lib/python3/rlcompleter.py -v 34  #notice version for python3



## Contributing

Pull requests welcome

