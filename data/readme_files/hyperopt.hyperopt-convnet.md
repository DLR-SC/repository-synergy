Hyperparameter Optimization for Convolutional Vision Architectures
==================================================================

This package provides a [Theano](http://www.deeplearning.net/software/theano)-based implementation of convolutional networks
as described in (Bergstra, Yamins, and Cox, 2013), which exposes many
architectural hyperparameters for optimization by
[hyperopt](http://jaberg.github.com/hyperopt).

# Installation

1. Requirements:


   * A Python/Numpy/Scipy stack.
     The Python package requirements are listed in
     requirements.txt.

   * Optional (but strongly recommended) is an NVIDIA GPU device at least as
     fast as, say, a GTX280, and CUDA. See Theano's documentation for setting
     up Theano to use a GPU device.

   * Optional (but strongly recommended) is the MongoDB database software,
     which allows hyperopt to support parallel optimization.

2. Check out this project

   `git clone https://github.com/jaberg/hyperopt-convnet.git`.

3. Install it as a Python package. This installation makes the code files
   importable, which is required when running asynchronous hyperparameter
   optimization (i.e. with hyperopt-mongo-worker, as explained below).

   `python setup.py install`

   Consider installing this within your user account (`--user`) or within a
   virtualenv to avoid installing this package system-wide, and to avoid
   needing root privileges.

   Installing hyperopt-convnet will install a pile of Python packages,
   which are listed in requirements.txt.
   On my computer, I had to explicitly install a few packages, because
   whatever the setup.py script was doing wasn't working (I still don't
           understand python packaging...):
   * `pip install numpy`,
   * `pip install scipy`,
   * `pip install matplotlib`

4. Replace sklearn < 0.13 with git version (we need some new stuff in SVC).


# Testing

If installation goes well, then you will now be able to import the `hpconvnet`
module. The easiest way to test your installation is


```bash
THEANO_FLAGS=device=gpu shovel lfw.random_driver  --max_n_per_class=20
```

This command should not crash, it should (i) download LFW if necessary and
then (ii) loop indefinitely doing random search on a tiny subset of the LFW
training data.



# Running An Experiment in Parallel with MongoDB

Running hyperparameter optimization on large convolutional networks for data
sets such as [LFW](http://vis-www.cs.umass.edu/lfw/)
and [CIFAR10](http://www.cs.toronto.edu/~kriz/cifar.html) takes a significant amount of time:
expect a search of a few hundred points to take about a GPU-week.
This cannot be completely parallelized (Bayesian optimization works on the
basis of feedback about the fitness landscape after all), but in my experience
it can easily be parallelized 5-fold to 10-fold.
So if you have access to a small cluster you can see significant progress in
an hour or two, and be done in a day.

What follows here is a sketch of the unix commands you would need to do to
make this happen.
To get more of a sense about what's going on, read through
[hyperopt documentation on using
mongo](https://github.com/jaberg/hyperopt/wiki/Parallelizing-search).


1. Set up a mongodb process for inter-process communication.

   `
    mongod --dbpath . --port PORT --directoryperdb --fork --journal --logpath log.log --nohttpinterface
   `

    If this machine is visible to the internet, you should either bind mongod
    to the local loopback address and connect to the database via an ssh
    tunnel, or set up mongodb for password-protected access.

2. Start an asynchronous search process, that connects to the mongodb and
   polls a work queue created there.

   `
    shovel cifar10.tpe_driver localhost PORT 0.0
   `

3. Start one or more generic hyperopt worker processes to crank through the
   trials of the experiment, pointing at the database that's written into the
   shovel script, in this case:

   `
    ssh WORKNODE hyperopt-mongo-worker --mongo=localhost:PORT/DBNAME
   `

   The PORT should match the one used to launch mongodb.
   The DBNAME should match the one used in shovel/cifar10.py:make_trials,
   which is "dbname" by default.

   If you have a cluster with a queue system (e.g. Torque, PBS, etc.) then use
   that system to schedule a few hyperopt-mongo-worker processes. When they
   start, they will connect to the database and reserve an experiment trial.
   These processes will loop indefinitely by default, dequeueing/reserving trials
   and storing the results back to the database. They will stop when the
   search process no longer adds new trials to the database, or when several
   (4) consecutive trials fail to complete successfully (i.e. your trial
   evaluation code is faulty and you should either fix it or at least catch the
   terminating exceptions).

# Rough Guide to the Code

* `shovel/{cifar10,lfw,mnist}.py` driver code for various data sets.
  When you type `shovel lfw.foo` in bash, it will try to run the `foo` task in
  the lfw.py file.

* `hpconvnet/lfw.py` describes the search space and the objective function
  that hyperopt.fmin requires to optimize LFW's view 1 data set.

* `hpconvnet/cifar10.py` describes the search space and the objective function
  that hyperopt.fmin requires to optimize CIFAR10 validation performance.

* `hpconvnet/slm_visitor_esvc.py` provides a LearningAlgo (skdata-style) derived
  from `SLM_Visitor` that does classification based on sklearn's SVC binary
  SVM and a precomputed kernel. This is generally a good choice for data sets
  without too many examples. The LFW experiments use this class.

* `hpconvnet/slm_visitor_primal.py` has a LearningAlgo (skdata-style) derived
  from `SLM_Visitor` that does classification based on a primal SVM solver.
  This is generally a good choice for data sets with larger numbers of
  examples. The MNIST and CIFAR10 experiments use this class.

* `hpconvnet/slm_visitor.py` provides `SLM_Visitor`,
  a LearningAlgo (skdata-style) base class
  with image feature extraction code and several LearningAlgo interface
  methods.

* `hpconvnet/slm.py` - creates the "pipeline" part of the search space, which
  describes the full set of possibilities for image feature extraction (the
  full set of convolutional architectures). The `uslm_domain` function
  returns this search space as a pyll graph.
  Note also the `call_catching_pipeline_errors` function, which includes
  `except` clauses for all known errors which may arise in the course of
  evaluating that pyll graph.

* `hpconvnet/pyll_slm.py` - defines many custom pyll.scope functions which
  serve to describe the `uslm_domain` search space.

The basic idea of the code is that the driver code (e.g. in shovel/lfw.py)
defines a search space and an objective function for hyperopt.

The search space is relatively complex, not only in terms of its size (238
hyperparameters) but also in its internal logic: a "sample" from the search
space is a dictionary that alongside some some simpler key-value pairs,
contains a "pipeline" key whose value is itself a pyll graph (seriously, pyll
has support for lambda expressions),
which evaluates to a theano function, which can process images.

The objective function is implemented by e.g. lfw.slm_visitor_lfw which
allocates a LearningAlgo (an SLM_Visitor_ESVC instance called `visitor`)
to handle most of the work.
The lfw.slm_visitor_lfw routine passes a LearningAlgo
to the LFW data set's "protocol" function, which
walks the LearningAlgo through the various steps of an LFW experiment: showing
it the right data at the right time, asking it to compute various statistics,
and so on.
When that's all done, lfw.slm_visitor_lfw asks the LearningAlgo to make
a report (`visitor.hyperopt_rval()`) in the form of a dictionary.
That dictionary is augmented with what hyperopt needs to see (loss and status
keys) and passed back to hyperopt.


There are other files too in the hpconvnet folder, but these ones summarize
the logic and control flow.


# References

* J. Bergstra, D. Yamins, D. D. Cox (2013).
  [Making a Science of Model Search: Hyperparameter Optimization in Hundreds of Dimensions for Vision Architectures](http://jmlr.csail.mit.edu/proceedings/papers/v28/bergstra13.pdf),
  in Proc. ICML2013. -- This paper describes the convolutional architectures
  implemented in this software package, and the results you should expect from
  hyperparameter optimization.

* J. Bergstra, R. Bardenet, Y. Bengio, B. Kegl (2011).
  [Algorithms for Hyper-parameter Optimization](http://books.nips.cc/papers/files/nips24/NIPS2011_1385.pdf)
  In Proc. NIPS2011. -- This paper introduces the TPE hyperparameter optimization algorithm.
