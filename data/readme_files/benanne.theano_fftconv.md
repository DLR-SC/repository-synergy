theano_fftconv
==============

## Current status

This have been merged in Theano. Don't use this repo anymore.

Doc: http://deeplearning.net/software/theano/library/tensor/nnet/conv.html

## History

Convolution op for Theano based on CuFFT using scikits.cuda

This is an experiment in implementing an FFT-based convolution op for Theano, using scikits.cuda. It was inspired by this paper, which shows promising speedups for FFT-based convolutions in the Torch7 framework: http://openreview.net/document/aa6ab717-ca19-47e1-a958-823b9a106ca9

Currently this is barely functional. Input is welcome!

scikits.cuda: https://github.com/lebedov/scikits.cuda

## Current status of this repo

The implementation gives the same result as a valid convolution using Theano's own conv2d. With the implementation of NativeBatchedComplexDot op, the performance seems to be quite good (several times faster than Theano's own conv2d in many cases).

The next step is to do some proper performance testing for different input/filter sizes, with a comparison to Theano's own convop and to the cuda-convnet wrappers (where applicable).