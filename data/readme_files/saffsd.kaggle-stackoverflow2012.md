Code submission for Kaggle Stack Overflow challenge
Initial development was based on
http://fastml.com/predicting-closed-questions-on-stack-overflow/

And some of the code is derived from there. The data extraction (data2vw.py)
was rewritten from scratch, integrating the two scripts from the above post.

Another area I expanded was to automate the whole process using a Makefile, 
and additionally introducing cross-validation implemented entirely using
shell tools (GNU parallel was very useful).

I generated an expanded set of features, based on segmenting the documents
into code and non-code sections. The non-code section was further segmented
into sentences, and then into words (using NLTK). I also looked at some
metrics about the user, as well as some aspects of the sentence structure,
such as number of questions, exclamations etc.

Marco Lui <saffsd@gmail.com>, October-November 2012
