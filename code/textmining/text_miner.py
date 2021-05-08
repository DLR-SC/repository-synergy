from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import operator                             #Importing operator module


import pandas as pd
import re
# Gensim
import gensim
from gensim.utils import simple_preprocess

# spacy for lemmatization
import spacy
from nltk.corpus import stopwords

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
nltk.download('wordnet')

def text_miner():
    def __init__(self):
        nltk.download('wordnet')


def get_wordnet_pos(treebank_tag):
        """
        return WORDNET POS compliance to WORDENT lemmatization (a,n,r,v) 
        """
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

def lemmatize_stem(token, pos_tag):
    stemmer = SnowballStemmer("english") #pOrter, M. "An algorithm for suffix stripping."
    return stemmer.stem(WordNetLemmatizer().lemmatize(token, pos=pos_tag))

def lemmatize(token, pos_tag):
    return WordNetLemmatizer().lemmatize(token, pos=pos_tag)

def stem(token):
    stemmer = SnowballStemmer("english") #pOrter, M. "An algorithm for suffix stripping."
    return stemmer.stem(token)

# stem_lemma: 
# 1: only stem 
# 2: only lemma
# 3: stem and lemma
def preprocess(text, stem_lemma= 3):

    token_all = []
    lemma = []
    pos = []
    for sentence in sent_tokenize(text):
        sentence = sentence.replace('\n', ' ').strip()
        sentence = re.sub("((\S+)?(http(s)?)(\S+))|((\S+)?(www)(\S+))|((\S+)?(\@)(\S+)?)", " ", sentence)
        sentence = re.sub("[^a-zA-Z ]", "", sentence)
        tokens = [token for token in word_tokenize(sentence)]
        pos_tags = nltk.pos_tag(tokens)

        
        for idx in range(0,len(tokens)):
            token = tokens[idx].lower()
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token)>1:
                token_all.append(token)
                
                wordnet_pos = get_wordnet_pos(pos_tags[idx][1])
                l_ = stem(token) if stem_lemma==1 else (lemmatize(token, wordnet_pos) if stem_lemma==2 else lemmatize_stem(token, wordnet_pos))
                lemma.append(l_)
                pos.append(pos_tags[idx][1])
    return {"tokens":token_all, "lemmas": lemma, "pos": pos}


def get_top_ngrams(corpus, ngram_range=[1,3] , top=-1, min_df=0, max_df=1.0):
    corpus = [' '.join(preprocess(x, stem_lemma= 1)['lemmas']) for x in corpus]
    vectorizer = CountVectorizer(lowercase=True, max_df=max_df, min_df=min_df, ngram_range=ngram_range)
    X = vectorizer.fit_transform(corpus)

    per_feature = X.toarray().T

    res = {}
    i =0

    for feature in vectorizer.get_feature_names():
        if feature not in res.keys():
            res[feature]  = 0
        res[feature] += per_feature[i].sum()
        i+= 1

    res = (sorted(res.items(),key = operator.itemgetter(1),reverse = True))

    if top >0: res = res[:top]

    return res

def _apply_basic_features(row, extracted_df):
    if row.name  in extracted_df.index :
        r = extracted_df.loc[row.name]
        for k, v in r.items():
            row[k] = v
    return row


# returns the N-grams frequency for one aspect (e.g. pos) in a dataframe:
# parameters:
##  df: dataframe that contains the content
## 'feature': str, the column name in the df that holds the data on which the 1-3 grams will be extracted
## 'training_ids': array, contains the IDs of the training data where the Vectorizer will be fit
## 'min_df': occurrence of n-gram in at least n documents where n can be an int or between ]0, 1[
## 'max_df': occurrence of n-gram in at most n documents where n can be an int or between ]0, 1[
## 'ngram_range': a tuple that contains the range of n-grams. e.g., (1,3) extract freq for 1 to 3 grams
## 'count_type': counter or 'tf-idf'
## 'idx': the column name of the dataframe that contains the id. Default: 'id'
## 'cols_prefix': return the features with column name {cols_prefix}_
def extract_n_grams_features(df, df_train, feature, 
                             min_df=30, max_df=0.4, ngram_range=(1,3),
                             count_type='counter', idx= 'id',
                            cols_prefix=''): #pos stem token
    df_original =  df.copy()
        
    ## fit on training
    #df_train= (df[df[idx].isin(training_ids)]).copy()
    
    df_ = df.copy()
    df_ = df_.reset_index()
    extracted_df = pd.DataFrame()
    
    # Initializing vectorizer
    vectorizer = None
    if count_type == 'tf-idf':
        vectorizer = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, max_features=100 )
    elif count_type == 'counter':
        vectorizer = CountVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range )
        
    # Fitting in training data
    vectorizer.fit(df_train[feature])
    features = vectorizer.transform(df_[feature])

    extracted_df =pd.DataFrame(
        features.todense(),
        columns=vectorizer.get_feature_names()
    )
    extracted_df = extracted_df.add_prefix(cols_prefix)

    # Merging results with original df
    aid_df = df_[[idx]]

    extracted_df = extracted_df.merge(aid_df, left_index =True, right_index=True, suffixes=(False, False), how='inner')
    extracted_df.set_index(idx, inplace=True)

    result_df = df_original.apply(_apply_basic_features, axis=1, args=(extracted_df,))
    return result_df, extracted_df 




# Define functions for stopwords, bigrams, trigrams and lemmatization
class topic_modeling_preprocess():
    
    def __init__(self, original_data, stopwords_extension=[]):
        self.stop_words  = stopwords.words('english')
        self.stop_words.extend(stopwords_extension)
        self.original = original_data
        #self.stop_words.extend(['editorial', 'editorials', 'agree', 'disagree', 'news editorial',
        #'news editorials', 'would', 'could'])
        

        self.data_words = list(self.doc_to_words(original_data))
        self.build_n_gram_models()
        # python3 -m spacy download en
        self.nlp = spacy.load('en', disable=['parser', 'ner'])

        self.preprocess_for_topic_modeling()

    def doc_to_words(self, docs):
        for doc in docs:
            yield(gensim.utils.simple_preprocess(str(doc), deacc=True))  # deacc=True removes punctuations

    def build_n_gram_models(self):
        # Build the bigram and trigram models
        bigram = gensim.models.Phrases(self.data_words, min_count=(len(self.original)*0.01), threshold=(len(self.original)*0.3)) # higher threshold fewer phrases.
        trigram = gensim.models.Phrases(bigram[self.data_words], threshold=(len(self.original)*0.3))

        # Faster way to get a sentence clubbed as a trigram/bigram
        self.bigram_mod = gensim.models.phrases.Phraser(bigram)
        self.trigram_mod = gensim.models.phrases.Phraser(trigram)

    def remove_stopwords(self):
        print('removing stop words...')
        self.data_words = [[word for word in simple_preprocess(str(doc), deacc=True) if (word not in self.stop_words)] for doc in self.data_words]

        print('end removing stop words.')
        return self.data_words 

    def make_bigrams(self):
        self.data_words = [self.bigram_mod[doc] for doc in self.data_words]
        return self.data_words 

    def make_trigrams(self):
        self.data_words = [self.trigram_mod[doc] for doc in self.data_words]
        return self.data_words 

    def lemmatization(self, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        print('lemmatization...')
        texts_out = []
        for sent in self.data_words:
            doc = self.nlp(" ".join(sent)) 
            texts_out.append([token.lemma_ for token in doc])# if token.pos_ in allowed_postags])
        print('end of lemmatization.')

        return texts_out

    def preprocess_for_topic_modeling(self):
        # Remove Stop Words
        self.remove_stopwords()

        # Form Bigrams
        self.make_bigrams()

        # Form Trigrams
        #self.make_trigrams()

        # Do lemmatization keeping only noun, adj, vb, adv
        print('calling lemmatizing:')
        self.data_lemmatized = self.lemmatization( )
