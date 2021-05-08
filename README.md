

# Repository-pair Synergies


This is the code for the SEKE 2021 paper *Quantifying Synergy between Software Projects using README Files Only*.

Roxanne El Baff, Sivasurya Santhanam and Tobias Hecking

      @InProceedings{elbaff:2021,
        author =  {Roxanne {El Baff} and Sivasurya Santhanam and Tobias Hecking},

        title     = {Quantifying Synergy between Software Projects using {README} Files Only},
        booktitle = {The 33rd International Conference on Software Engineering and Knowledge
                   Engineering, {SEKE} 2021, {KSIR} Virtual Conference Center, USA, July
                   1-10, 2021},
        publisher = {{KSI} Research Inc.},
        year      = {2021},
        url       = {https://doi.org/10.18293/SEKE2021-162},
        doi       = {10.18293/SEKE2021-162},
        }


## Dataset

We use the following data: 

* (1) **data/processed/final_repo_english_whatwhy.csv** contains all repos we use and 
* (2) original readmefiles (md version with tags) in **data/readme_files/**
* (3) *data/extracted_features/...* contains extracted topics from the readme files
* (4) data/evaluation/... contains files that will be used for the evaluation of the approach 


The csv file (1) contains **13K repos** with the following characteristics and  **24,988** WhatWhy readme sections:
    

*  Python as main language
*  Not deleted and not a fork
*  At least 50 watchers
*  Updated in 2019
*  English README
*  Availability of Readme files and has sections that describe features and repo purpose based on on the [READMEClassifer](https://github.com/gprana/READMEClassifier), *What, Why* section codes.


## 0. Data Preparation
#### reproducibility: 
 - check code/0_data-preparation: 1) fetch data from ghtorrent, 2) get readme files 

###### 1. Fetching GitHub Dump from GHTorrent


1.  We downloaded a dump from ghtorrent. We use only *Python* repositories that are not *deleted* and that they were *updated* in *2019*.
2.  We then loaded the repositories tables into a postgres database using ghtorrent sql script.

ghtorrent data is saved under *data/ghtorrent_python_notdeleted_repos_updated2019*.

###### 2. Fetching READMEFiles

We fetched the readme files using [PyGithub](https://github.com/PyGithub/PyGithub) for repositories that has at least *50 watchers* and we dismiss duplicate repos (11 duplicates).

We ended up with 20 509, saved in *data/processed/repositories_with-readme.csv*.

The readme files are saved under *data/readme_files*


## 1. Software Features Extraction
We use the project [READMEClassifer](https://github.com/gprana/READMEClassifier) to classify the sections in the readme files under *data/readme_files*.

The classifications are saved under *data/ghtorrent_readme_classifications*.

#### reproducibility: 
 - check code/1_software-features-extraction : 1) process the clasified readme sections, 2) extract WhatWhy readme sections and filter out non English


The READMEClassifier extracts the contents of the readme files as a preprocessing step. They save the result in LightSql database. 

We exported the data into csv an saved them under *data/ghtorrent\_readme\_classifications/generated_data/* folder.

We then created 1 csv file with all the needed info using *5_extracting_readme_content.ipynb* and saved them here *data/processed/repositories_with-readme_what-why-code_content.csv*.

## 2. Software Features Modeling
#### reproducibility: 
 - check code/2_software-features-modeling: extracting features using NMF/LDA and then comparing the results

## 3. Synergy Discovery
#### reproducibility: 
 - check code/3_synergy-discovery: 1) randing usig lda/nmf with multiplicative/random walk and 2) evaluation using stargazing


## 4. Manual Evaluation 
#### reproducibility: 
 - check code/4_manual-evaluation 1) creating 3 batches with 10 pairs for each algorithm (random, lda_rwr for d=0.0 and d=0.2), 2) evaluating the annotations


## Pre-requisites

For reproducing the data creation:
     
1. Install pygithub
 `pip install PyGithub`
2. Get Github Personal Access Token
    * Github restricts default requests to be 60 req/hr. with PAT, 5000 requests/hr is possible. 
    * Go to https://github.com/settings/tokens and generate a new token
    * set the token with environment variable 'PAT' eg. set PAT=xxxxxxxxxxxxxxxxxxxxxx


