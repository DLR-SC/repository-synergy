NOISY TEXT "CLEANSER"
Author: Stephan Gouws
Contact: stephan@ml.sun.ac.za

INTRODUCTION
------------

User-generated text in online social media sites such as Twitter are typically very different from 'standard English orthography'. The goal of this code is to 'normalise' lexically ill-formed text to its most likely standard English representation, e.g. "c u at da club 2nite" -> "see you at the club tonight".
This package is a bare-bones implementation of the text normalisation system described in the paper

@conference{gouws2011contextual,
	Author = {Gouws, S. and Metzler, D. and Cai, C. and Hovy, E.},
	Booktitle = {Proceedings of the ACL-11 Workshop on Language in Social Media},
	Organization = {Association for Computational Linguistics},
	Title = {{Contextual Bearing on Linguistic Variation in Social Media}},
	Year = {2011}
}

Please cite this paper if you write a research paper that makes use of this software. Feel free to contact me at stephan@ml.sun.ac.za if you find any bugs or if you have any questions.

LICENCE:
-------

This code is made available under the GNU general public licence. Please see the file LICENCE.

INSTALLATION INSTRUCTIONS:
-------------------------

1) Download and compile the SRI-LM toolkit from (http://www-speech.sri.com/projects/srilm/download.html).

2) Check out the latest version of the TextCleanser package to some directory we'll call $TEXT_CLEANSER_HOME 
    from here on, with the command: "git clone git@github.com:gouwsmeister/TextCleanser.git"

3) Update the LATTICE_TOOL_DIR constant in $TEXT_CLEANSER_HOME/decoder.py and in start_ngram_server.sh with the correct location to the SRI-LM "lattice-tool".

4) Update the LM_DIR constant in $TEXT_CLEANSER_HOME/decoder.py and start_ngram_server.sh to point to the $TEXT_CLEANSER_HOME/data directory where the SRI-LM language models reside.

5) Start the language model in server mode by running "./start_ngram_server.sh". Wait around 30s for the server to finish loading. This only needs to be done once; the server will sit dormant until it gets killed or you restart.

6) Run cleanser.py to test the output on some example tweets.

7) Run cli_cleanser.py and start typing something followed by return to test it out interactively.

SOME DETAILS ON THE CODE:
------------------------

The three main classes are TextCleanser in cleanser.py, Generator in generator.py and Decoder in decoder.py. Normalisation proceeds in three steps:

1) out-of-vocabulary (OOV) detection
2) candidate enumeration/selection
3) decoding.

1. OOV detection is performed as a simple lexicon lookup. This must be improved (see Future Improvements section). For twitter, @usernames and #tags are also considered in-vocabulary as a simple first approach.
2. Candidate enumeration proceeds by comparing a noisy token to all or part of the lexicon, based on some similarity function. I have implemented a few simple similarity functions, namely a phonetic edit distance-based function (based on the double metaphone representations of words), a heuristic string similarity function, and a subsequence overlap function. The output of this step creates a word mesh which contains the most likely clean candidates for each word.
3. Finally this lattice is rescored with a clean langauge language model and the most likely posterior path then connects the most likely clean tokens. 

An example usage is shown in cleanser.py.
The evaluator.py file can be used and adapted for testing a method's WER accuracy. It currently makes use of Bo Han's Twitter dataset (http://www.csse.unimelb.edu.au/research/lt/resources/lexnorm/). You can add your own and tweak it to your own purpose.

FUTURE IMPROVEMENTS:
-------------------

This version is a bare-bones implementation with very little tweaking or customisation so as to provide the framework for future work to improve on without having to reinvent the wheel each time. The quality of the normalisations will depend strongly on: the quality of the lexicon, the suitability of the chosen similarity function, and the relevance of the language models to the specific text your are working with. For best results it is also recommended to play around with different options and to develop a domain-specific lexicon and language models.

There are many possible improvements:

1) Improve the OOV detection. For this one may consider using the method employed by Bo Han and Tim Baldwin in their paper "Makn Sens a #Twitter" by training an SVM classifier to identify OOV words, instead of the current simple dictionary-lookup.
2) Improve the candidate selection process by using a better string-similarity/phonetic similarity/hybrid method. The best method for the job is usually domain-specific.
3) Refactor the code to allow one-to-many normalisation, as in "afaik"->"as far as I know"
4) Implement a recaser to capitalise as necessary
5) Detect and handle runon-words such as "theres"-> "there is", "cu at johns place"->"see you at johns place"
6) Detect IV-but-invalid tokens, i.e. when a lexical transformation/spelling error transforms one word into another valid word, e.g. "hear"->"here" or "train"->"rain"
7) Add caching on all the string-similarities
8) Add unit tests

FUTURE REFACTORS:
----------------

1) Move string functions in generator.py out to string_functions.py

