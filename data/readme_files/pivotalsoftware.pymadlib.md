A Python wrapper for MADlib - an open source library for scalable in-database machine learning algorithms.
You can visit [PyMADlib's webpage](http://pivotalsoftware.github.io/pymadlib/) for installation and usage tutorials.

## Algorithms

PyMADlib currently has wrappers for the following algorithms in MADlib (version 0.5).

1. Linear regression
1. Logistic Regression
1. SVM (regression & classification)
1. K-Means 
1. LDA 

Refer [MADlib User Docs](http://doc.madlib.net/v0.5/ ) for MADlib's user documentation. Please note that PyMADlib as of now is only compatible with MADlib v0.5. You can obtain MADlib v0.5 from [MADlib v0.5](https://github.com/madlib/madlib/archive/v0.5.tar.gz). We might add support to more recent versions of MADlib depending on adoption rate. Please email me if you have a strong case for an upgrade.


## Dependencies

1. You'll need the python extension _**psycopg2**_ to use PyMADlib.
1. If you have matplotlib installed, you'll see Matplotlib visualizations for Linear Regression demo.
1. If you have installed [networkx](http://networkx.github.com/download.html), you'll see a visualization of the k-means demo
1. [PyROC](https://github.com/marcelcaraciolo/PyROC) is included in the source of this distribution with permission from its developer. You'll see a visualization of the ROC curves for Logistic Regression.



 

## Configurations

To configure your DB Connection parameters
You should create a file in your home directory

>     ~/.pymadlib.config 

that should look like so :


>     [db_connection]  
>     user = gpadmin  
>     password = XXXXX  
>     hostname = 127.0.0.1 (or the IP of your DB server)  
>     port = 5432 (the port# of your DB)  
>     database = vatsandb (the database you wish to connect to)  






## Installation Instructions

PyMADlib depends on `MADlib`, `psycopg2` and `Pandas`. It is easiest to work with PyMADlib if you have `Anaconda Python`.

## Build Environment Setup on Mac OS X 10.8

* Download & install [Anaconda-1.9.0-MacOSX-x86_64.pkg] (http://repo.continuum.io/archive/Anaconda-1.9.0-MacOSX-x86_64.pkg)

* Open a terminal and check if you have Anaconda Python & the package manager conda

>     vatsan-mac$ which python
>     /Users/vatsan/anaconda/bin/python
>     vatsan-mac$ which conda
>     /Users/vatsan/anaconda/bin/conda 

* If you haven't installed PostgreSQL on your Mac already, you'll have to download & install `PostGreSQL` for Mac. This is so that we get some required libraries to compile the SQL Engine: psycopg2. The easiest way to install `PostGreSQL` on Mac is via `http://postgresapp.com/`. Once you've downloaded and installed PostGreSQL on Mac, it should typically be found under `/Library/PostgreSQL`

>     vatsan-mac$ ls /Library/PostgreSQL/9.2/
>     Library include pg_env.sh uninstall-postgresql.app
>     bin installer scripts
>     data lib share
>     doc pgAdmin3.app stackbuilder.app
I don't think the version of the `PostGreSQL` matters (9.1 or above is fine). 

* You may need to create some symlinks to `libpq` & `libssl` so that `psycopg2` is able to find it:

>     vatsan-mac$ sudo ln -s /Users/vatsan/anaconda/lib/libssl.1.0.0.dylib /usr/lib
>     vatsan-mac$ sudo ln -s /Users/vatsan/anaconda/lib/libcrypto.1.0.0.dylib /usr/lib

* Install `Psycopg2` 

>     vatsan-mac$ conda install distribute
>     vatsan-mac$ pip install psycopg2

* Now we're ready to test if the installations of the required libraries were successful.

>     vatsan-mac$ python -c 'import psycopg2'
If the above command did not error out, then installation was successful.

* You may install `PyMADlib` by downloading the source (from PyPI) and then run the following

>     sudo python setup.py build
>     sudo python setup.py install

* If you use easy_install or pip, simply run :

>     sudo easy_install pymadlib


## Usage Tutorial

Visit [PyMADlib Tutorial](http://nbviewer.ipython.org/gist/vatsan/dd88abb47c2fbd9e16bd) for a tutorial on using PyMADlib
Also visit [PyMADlib IPython NB](https://gist.github.com/vatsan/dd88abb47c2fbd9e16bd) to download the IPython NB tutorial


## Running the Demos

You may run the demo from the extracted directory of pymadlib like so :

>     python example.py

        
If you installed PyMADlib using instructions in the previous section, then simply run

>     python -c 'from pymadlib.example import runDemos; runDemos()'

Remember to close the Matplotlib windows that pop-up to continue with the rest of the demo.




## Gallery

![K-Means Cluster Visualization](https://lh3.googleusercontent.com/-bXz3gCrnQFo/UTu3lXFKbeI/AAAAAAAAKgI/Hpjsqzb_GTQ/w776-h714-p-o-k/kmeans_networkx_viz.png)

![Scatter Plot - Linear Regression (numeric attributes only)](https://lh3.googleusercontent.com/-esbS5NTl58E/UTu3lfBqUXI/AAAAAAAAKgE/tawiqnTgYLQ/w470-h353-o-k/linear_reg_scatter_1.png)

![Scatter Plot - Linear Regression (with categorical attributes)](https://lh6.googleusercontent.com/-vNTw5Q6d0pg/UTu3lVjBIzI/AAAAAAAAKgA/pbiLfGiYisw/w470-h353-o-k/linear_reg_scatter_2.png)

![ROC Curve - Logistic Regression](https://lh3.googleusercontent.com/-ymBoJ7qQo-o/UTu3l9RUBvI/AAAAAAAAKgU/_Mc0jiM_Yq0/w470-h353-o-k/logistic_reg_pyroc.png)

![Random graph visualization - Networkx](https://lh6.googleusercontent.com/-H-3h0bV8EDQ/UTu3lyED9YI/AAAAAAAAKgY/CcoJ2oSme2M/s353-c-o-k/random_networkx_viz.png)

 


## Datasets packaged with this installation

PyMADlib packages publicly available datasets from the UCI machine learning repository and other sources.

1. [Wine quality dataset from UCI Machine Learning repository](http://archive.ics.uci.edu/ml/datasets/Wine+Quality)
1. [Auto MPG dataset from UCI ML repository from UCI Machine Learning repository](http://archive.ics.uci.edu/ml/datasets/Auto+MPG)
1. [Wine quality dataset from UCI Machine Learning repository](http://archive.ics.uci.edu/ml/datasets/Wine+Quality)
1. Obama-Romney second presidential debate (2012) transcripts




## Questions

<vatsan.cs@utexas.edu>
