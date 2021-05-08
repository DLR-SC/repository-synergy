#Joint Optimization of Algorithmic Suites for EEG Analysis
This code was used to generate the results of the paper at EMBC 2014. The author's copy of the paper can be found at [CNEL's website](http://cnel.ufl.edu/people/people.php?name=eder)

## Abstract
Electroencephalogram (EEG) data analysis algorithms consist of multiple processing steps each with a number of free parameters. A joint optimization methodology can be used as a wrapper to fine-tune these parameters for the patient or application. This approach is inspired by deep learning neural network models, but differs because the processing layers for EEG are heterogeneous with different approaches used for processing space and time. Nonetheless, we treat the processing stages as a neural network and apply backpropagation to jointly optimize the parameters. This approach outperforms previous results on the BCI Competition II - dataset IV; additionally, it outperforms the common spatial patterns (CSP) algorithm on the BCI Competition III dataset IV. Also, the optimized parameters in the architecture are still interpretable.

##Prerequisites
1. numpy
2. scipy
3. scikit-learn
4. matplotlib
5. theano

They are all available for pip install. We also used the LogisticRegression class from LISA-Lab's [Deep Learning Tutorials](https://github.com/lisa-lab/DeepLearningTutorials).

##Data
The dataset used here was downloaded from http://www.bbci.de/competition/ii/ .

##Running the experiments
We suggest running the experiments at an IPython section:  
`run piecewise_deep_csp`  
To visualize the temporal projection, run  
`plot(avg_v.get_value())`

##Platform
We ran the experiments reported on the paper using a MacBook Air OS 10.8 with
1. numpy 1.6
2. scipy 0.13
3. scikit-lern 0.13
4. We had no user defined theano flags. Most importantly, this means that the experiments ran on CPU with float64 precision.
