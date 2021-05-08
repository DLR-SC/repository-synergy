# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:08:18 2020

"""

import numpy as np
import time
def normalise_matrix(X):
    
    return np.nan_to_num((X.T / np.sum(X, axis=1)).T)
    
def rank_repositories_multiplicative(X, Xneg, M, O):
    
    return (X.dot(np.exp(-M)) * Xneg).dot(X.T) * O
    
def rank_repositories_rwr(X, Xneg, M, O, d=0.5):
    Xt = normalise_matrix(X.T) 
    
    return (1 - d) * X.dot(Xt) + d * (X.dot(np.exp(-M)) * Xneg).dot(Xt)

def rank_repositories(repo_feature_matrix, ranking_function, **kwargs):
    start = time.time()
    print("start")
    print("normalisation")
    X = normalise_matrix(repo_feature_matrix)
    M = normalise_matrix(repo_feature_matrix.T.dot(repo_feature_matrix))
    Xneg = 1 - X #csr_matrix(1 - X)
    O = normalise_matrix(repo_feature_matrix.dot(repo_feature_matrix.T))
    
    print("ranking")
    couplings = ranking_function(X, Xneg, M, O, **kwargs)
    ranking = (-couplings).argsort(axis=None)
    print("done in {} seconds.".format(time.time() - start))
    return np.unravel_index(ranking, (couplings.shape[0], couplings.shape[1])) + (couplings.flatten()[ranking],)
    