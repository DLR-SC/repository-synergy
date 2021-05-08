# Learning Language Representations for Typology Prediction

Code accompanying the paper Learning Language Representations for Typology Prediction (To Appear at EMNLP 2017)

## Abstract

One central mystery of neural NLP is what neural models ``know'' about their subject matter.  When a neural machine translation system learns to translate from one language to another, does it learn the syntax or semantics of the languages?  Can this knowledge be extracted from the system to fill holes in human scientific knowledge?
Existing typological databases contain relatively full feature specifications for only a few hundred languages.
Exploiting the existance of parallel texts in more than a thousand languages, we build a massive many-to-one NMT system from 1017 languages into English, and use this to predict information missing from typological databases.
Experiments show that the proposed method is able to infer not only syntactic, but also phonological and phonetic inventory features, and improves over a baseline that has access to information about the languages' geographic and phylogenetic neighbors.

The URIEL database is available at http://www.cs.cmu.edu/~dmortens/uriel.html

Learned Vectors: https://drive.google.com/open?id=0B47fwl2TZnQaa0s5bDJESno0OTQ

After downloading and unzipping the above file, you may access the learned vectors as below:

    import numpy as np
    # language vectors
    vecs = np.load("lang_vecs.npy")
    vecs.item()['optsrc'+'fra']  # For French
    vecs.item()['optsrc'+'ita']  # For Italian

    # language cell states
    cell_states = np.load("lang_cell_states.npy")
    cell_states.item()['fra'][0]  # For French
    cell_states.item()['ita'][0]  # For Italian

## Bibtex: 

@inproceedings{malaviya17emnlp,
    title = {Learning Language Representations for Typology Prediction},
    author = {Chaitanya Malaviya and Graham Neubig and Patrick Littell},
    booktitle = {Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    address = {Copenhagen, Denmark},
    month = {September},
    year = {2017}
}
