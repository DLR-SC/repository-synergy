Shuca
====

## Introduction
Shuca is an automatic summarization software. 
It can summarize a single document (Single-Document Summarization) and multiple documents (Multi-Document Summarization) as an input.
As for summarizing documents written in Japanese, see README.ja.md.

## Feature
* Shuca extracts important sentences from among input sentences in an input so as to maximize the sum of importance of those within the given length limitation.

### Sindle Document Summarization
* Shuca regards a task of single-document summarization as an instance of knapsack problem; it hence searches for a best combination of an input through the dynamic programming knapsak algorithm.

### Multi-Document Summarization
* Shuca regards a task of multi-document summarization as an instance of maximum coverage knapsack problem; it hence searches for an approximate solution of a best comination of input sentences through the greedy algorithm.

## Prerequisite
* Each line in an input must be one sentence; Shuca processes each line as an unit of summarization.
* As preprocess words in an input should be stemmed beforehand.

## Install
Download and put files in your directory; no installation is needed.

## Usage
In `dat` directory, there are some sample files. `automatic_summarization.txt` is a text file in which the first two paragraphs of an wikipedia article, ``Automatic Summarization", is.
`automatic_summarization.sent.txt` and `automatic_summarization.sent.stem.txt` are a sentence-splitted and stemmed version of that respectively.
Please test a following command:

    $ ./lib/Shuca.py -e < ./dat/automatic_summarization.sent.stem.txt

* `-d` Specify an external dictionary. In default setting, Shuca uses a default dictionary.
* `-e` To summarize texts written in English, `-e` option must be specified.
* `-l` Specify summarization length in the number of words. For Instance, If speficy `-l 200`, Shuca outputs a summary within 200 words. Default summarization length is 200 words.
* `-m` Perform multi-document summarization. Without this option, single-document summarization is performed.
* `-s` Set summarization length with the number of sentences. For instance, If specify `-s 3`, three sentences will be output as an output summary.

## Miscellaneous
* Parameters packed together with the software are now roughly set by the developer, and will be replaced with ones estimated through machine learning.

## Developer
Hitoshi Nishikawa

* E-Mail: hitoshi [at] nishikawa [dot] name
* GitHub: [hitoshin](https://github.com/hitoshin)
* Website: [Hitoshi's Home Page](http://www.hitoshi.nishikawa.name)
