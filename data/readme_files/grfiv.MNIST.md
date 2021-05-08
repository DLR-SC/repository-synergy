# Analyses of MNIST database of handwritten digits

This project is an attempt to beat the benchmarks set for the algorithms described in the 1998 paper by [LeCun et al.](http://yann.lecun.com/exdb/mnist/), plus some newer algorithms that have become popular, using the MNIST database of handwritten digits. I then tried each algorithm in the Kaggle Handwritten Digit contest.

As of August 2015 I have gotten through all of the algorithms and achieved 0.99257 on Kaggle using a Theano multi-layer neural network running on a GPU at AWS, placing 28th out of 646 entrants.

See [MNIST.pdf](https://github.com/grfiv/MNIST/blob/master/MNIST.pdf) for the detailed documentation.

The data is very large so I zipped up the /data/ folder and uploaded it to AWS S3; download the file and extract it inside the /MNIST/ folder produced by git pull.

https://s3.amazonaws.com/grfiv-mnist/data.zip


[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.18768.svg)](http://dx.doi.org/10.5281/zenodo.18768)
