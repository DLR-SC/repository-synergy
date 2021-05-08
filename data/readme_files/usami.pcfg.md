# Probabilistic Context-Free Grammar Parser
It is an implementation of Probabilistic Context-Free Grammar Parser.
pcfg\_parser.py reads lines from stdin, and outputs parsed trees.

## Usage
Here is an example usage of this parser.

    echo "the man saw the dog with the telescope" | python pcfg_parser.py counts_file.sample
    ["S", ["NP", ["DET", "the"], ["NOUN", "man"]], ["VP", ["VERB", "saw"], ["NP", ["NP", ["DET", "the"], ["NOUN", "dog"]], ["PP", ["ADP", "with"], ["NP", ["DET", "the"], ["NOUN", "telescope"]]]]]]

This parser outputs the parsed tree under the probabilistic model derived from the passed count file.
A parsed tree is represented as a nested list in JSON format.

## Counts File
If you want to train your own model, you need to prepare a counts file which contains the frequency of each word and rule in your training corpus.
The format of counts file is as follows:

    1 NONTERMINAL ADVP+DET
    14 UNARYRULE NP+NOUN Stocks
    37 BINARYRULE VP VERB NP+PRON

The first and second columns represents the number of counts and the type of entry, respectively.
There are three types of entry and three formats for each type.
##### NONTERMINAL
This is a type for nonterminals such as S, VP, NP and so on.
This type of entry has one more column for a specific nonterminal symbol.
##### UNARYRULE
This is a type for unary rules, which means assignments of nonterminals for terminal words. e.g. VERB -> said, VERB -> look, ADP -> after and NOUN -> point.
This type of entry has two more columns: nonterminal rule and terminal symbol.
##### BINARYRULE
This is a type for binary rules such as S -> NP + VP.
This type of entry has tree more columns: the leftmost item can be composed of the next item followed by the last item.
