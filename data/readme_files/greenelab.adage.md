# adage
[![DOI](https://zenodo.org/badge/19060/greenelab/adage.svg)](https://zenodo.org/badge/latestdoi/19060/greenelab/adage)

This is the repository for ADAGE (Analysis using Denoising Autoencoders for Gene Expression)

This repository provides the source code in support of the manuscript: [ADAGE-Based Integration of Publicly Available Pseudomonas aeruginosa Gene Expression Data with Denoising Autoencoders Illuminates Microbe-Host Interactions](http://msystems.asm.org/content/1/1/e00025-15). J Tan, JH Hammond, DA Hogan, CS Greene. *mSystems*, 00025-15. 

############################################################

To set up ADAGE, first clone the repository. This is a short summary. Detailed instructions and steps to generate the model and reproduce analyses used in the manuscript are in pseudomonas_autoencoder.sh 

Building an ADAGE model requires installing python packages Theano and Docopt 
Instructions for Theano: http://deeplearning.net/software/theano/install.html 
Instructions for docopt: https://pypi.python.org/pypi/docopt

We provide a gene expression compendium of Pseudomonas aeruginosa that contains datasets available before 02.22.2014. To get an up-to-date compendium, follow the instructions in Section One in pseudomonas_autoencoder.sh 

Before training, first 0-1 normalize the compendium, run
python Data_collection_processing/zero_one_normalization.py Data_collection_processing/Pa_compendium_02.22.2014.pcl Train_test_DAs/train_set_normalized.pcl None

To train a denoising autoencoders, run 
python Train_test_DAs/SdA_train.py Train_test_DAs/train_set_normalized.pcl --parameters

To test a dataset on an ADAGE model, run
python Train_test_DAs/SdA_test.py Train_test_DAs/Genome-hybs_normalized.pcl --parameters
 
############################################################

Please email jie.tan.gr@dartmouth.edu if you have questions.
