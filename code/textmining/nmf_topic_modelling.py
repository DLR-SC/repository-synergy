# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:12:51 2020

"""

import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        top_ids = topic.argsort()[:-n_top_words - 1:-1]
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i] for i in top_ids])
        print(message)
    print()
    
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def nmf_topics(texts, k):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english'). \
        fit_transform(texts)
    
def start():
    data = pd.read_csv("repositories_with-readme_what-why-code_content.csv")
    topics = nmf_topics(data.content_text_w_o_tags)