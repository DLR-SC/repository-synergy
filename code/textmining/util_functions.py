# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:12:51 2020

"""

import nltk
import numpy as np
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from nltk.stem.porter import PorterStemmer

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        top_ids = topic.argsort()[:-n_top_words - 1:-1]
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i] for i in top_ids])
        print(message)
    print()
    
def tokenize(text):
    tokens = [w.lower() for w in nltk.word_tokenize(text) if not bool(re.search("[*\W*|_]", w))]
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems