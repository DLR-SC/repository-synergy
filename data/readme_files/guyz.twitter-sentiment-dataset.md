# Overview

This code serves as an extension to [Sanders Analytics twitter sentiment corpus](http://www.sananalytics.com/lab/twitter-sentiment/), originally designed for training and testing Twitter sentiment analysis algorithms.
Since twitter has since deprecated their original API, the code had to be modified to support the current version (v1.1). Accordingly, support for OAuth2 has been added, and the running time of the script has been significantly improved.

Running this script will generate ~5K hand-classified tweets. For more information, please refer to 'readme.pdf'.

# Installation

1. Install python-oauth2 lib (unless already installed):  
  ```
  git clone git://github.com/simplegeo/python-oauth2/
  cd python-oauth2
  sudo python setup.py build  
  sudo python setup.py install
  ```  

2. Create a twitter app, and update the global OAuth2 properties in 'install.py'.
3. Run <code>python install.py</code>. If it fails with an SSL error, run as a superuser - <code>sudo python install.py</code>.
4. Hit enter three times to accept the defaults (make sure <b>rawdata</b> folder exists), or set your own paths.
5. Wait until completion (~9h). You should have a new file called <code>full-corpus.csv</code> with the entire labeled dataset.


#### Enjoy data-mining :)!

