# Natural-Language-Processing-Course
* NLP course taught by [Zhou Yu](http://www.cs.cmu.edu/~zhouyu/) in UC Davis
* Zhou Yu leads our Davis Team Gunrock was awarded $500,000 to compete in Amazon Alexa Prize.
* Texbook: [Speech and Language Processing (3rd ed. draft) by Dan Jurafsky and James H. Martin](http://web.stanford.edu/~jurafsky/slp3/)

## HW 1: Spell Correction
* Implement Noisy Channel
* Test 6 language models with training and dev data
* 6 Language Models: 
  1. Unigram Model
  2. Bigram Model 
  3. Smooth Unigram Model 
  4. Smooth Bigram Model
  5. Backoff Model: implemented with unsmoothed bigram and smoothed unigram
  6. Custom Model: implemented unsmooth trigram, unsmooth bigram, and smoothed unigram in backoff model
  
## HW 2: POS Tagging
* Implement Trigram Backoff HMM with deleted-interpolation
* Implement Trigram Viterbi Algorithm
* Train and test lanague model on English, Japanese, and Bulgarian
* Achieve 95% accuracy on English POS Tagging test data
* Achieve 94% accuracy on Japanese POS Tagging test data
* Achieve 89% accuracy on Bulgarian POS Tagging test data

## HW 3: Probabilistic Context Free Grammar
* Designed lexicon and grammar for parsing sentences
* Generated sentences using self-designed PCFG
* Improved accuracy by 40%

## HW 4: Sentiment Analysis with IMDB Movie Reviews 
* Predicted moview review sentiment using Naive Bayes
* Implement Multinomial Naive Bayes Classifer with 81% accuracy
* Implement Binarized Naive Bayes Classifer with 84.15% accuracy
