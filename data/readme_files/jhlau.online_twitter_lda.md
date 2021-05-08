This package contains scripts and python tools for running an online implementation of LDA.

Directory Structure and Files
=============================
* input: the input directory; contains example input files for testing the program.
* lda.py: main program that runs online LDA.
* run_lda.sh: script that drives the online lda system.
* stopwords.txt: a list of common stopwords to remove when generating the vocabulary.
* vocabulary.py: complementary program that manages the update of vocabulary in documents.

Running the System
==================
* Generate input files according to the input format in the input directory.
* Execute run_lda.sh.
* System output are generated in output-time_slice directories.

Input Format
============
* time_slice.text: text of the documents, one line per document;
* time_slice.time: time information of the documents, each line maps to the document that has the 
    same line number in time_slice.text.

Parameter Settings
==================
Most parameter values (number of cores to use, minimum frequency threshold of vocabulary, etc) are 
set in lda.py. The number of topics, T, is specified in run_lda.sh. The size of the sliding window is fixed at 2 
time slices. Modification of the code is required to change this parameter.

Credits & Licensing
===================
* The original author of the LDA implementation is Shuyo NAKATANI.
* License: MIT license - http://opensource.org/licenses/MIT.

Publications
------------
* Jey Han Lau, Nigel Collier and Timothy Baldwin (2012). On-line Trend
  Analysis with Topic Models: #twitter trends detection topic model online. In
  Proceedings of the 24th International Conference on Computational
  Linguistics (COLING 2012), Mumbai, India.
