# Deep Value Network (DVN)
This code is a python reference implementation of DVNs introduced in 

  Deep Value Networks Learn to Evaluate and Iteratively Refine Structured Outputs. Michael Gygli, Mohammad Norouzi, Anelia Angelova. ICML 2017.
  __[PDF](https://arxiv.org/pdf/1703.04363.pdf)__

__Note__: This code implements the multi-layer perceptron version used for the multi-label classification experiments only (Section 5.1). The segmentation code was written while inside Google and thus not available.


### Requirements
To run this code you need to have tensorflow, numpy, liac-arff, scikit-learn and torchfile installed.
Install with 
```bash
pip install -r requirements.txt
```
### Playing around with a pre-trained Value Net
The pre-trained model for the Bibtex dataset is included in this repository.
This allows you do play around with it and it's predictions, using our __[jupyter notebook](./dvn_tutorial.ipynb)__.

### Replicating the experiments in the paper
__Bibtex__

To replicate the numbers for bibtex provided in the paper, run:
```python
import reproduce_results
# Reproduce results on the bibtex dataset
reproduce_results.run_bibtex()
```
By default, the model weights and logs are stored to `./bibtex_dvn`.
You can monitor the process using tensorboard with

`tensorboard --logdir ./bibtex_dvn/`

In order to understand the training process two quantities are important:

1. loss: The loss in estimating the true value of an output hypothesis
2. gt_f1_scores: The true f1 scores of the generated output hypothesis.

As training progresses, the generated output hypothesis should get better and better.
As such, the validation performance reported here closely matches the performance of the test set.
The curve should look something like this:
![Training curve](/learning_curve.png "f1 scores training curve")

__Bookmarks__

For Bookmarks the splits are not provided on http://mulan.sourceforge.net/datasets-mlc.html.
Thus, we use the splits provided by SPEN. To get the data, run:
```bash
cd mlc_datasets
wget http://www.cics.umass.edu/~belanger/icml_mlc_data.tar.gz
tar -xvf icml_mlc_data.tar.gz
cd ..
```
Then, you can reproduce the results with
```python
import reproduce_results
# Reproduce results on the bookmarks dataset
reproduce_results.run_bookmarks()
```
The model weights and logs are stored to `./bookmarks_dvn/`.
 
### Contributors
Michael Gygli, Mohammad Norouzi, Anelia Angelova

Code by [Michael Gygli](https://www.vision.ee.ethz.ch/~gyglim)
