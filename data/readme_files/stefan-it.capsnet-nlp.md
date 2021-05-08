# *CapsNet* for Natural Language Processing

> A capsule is a group of neurons whose activity vector represents the
> instantiation parameters of a specific type of entity such as an object or an
> object part.

This repository shows how to use a *CapsNet* architecture for Natural Language
Prcoessing tasks like sentiment analysis.

*Capsules* are introduced by Geoffrey Hinton. We use a *CapsNet*
implementation from 苏剑林 as git submodule. The implementation can be found
[here](https://github.com/bojone/Capsule).

## Related work

Here are some papers where *capsules* and the *CapsNet* architecture are
introduced:

| Paper                              | Authors                                         | Link
| ---------------------------------- | ----------------------------------------------- | -------------------------------------------------------------
| *Dynamic Routing Between Capsules* | Sara Sabour, Nicholas Frosst, Geoffrey E Hinton | [here](https://arxiv.org/abs/1710.09829)
| *Matrix capsules with EM routing*  | Geoffrey E Hinton et al.                        | [here](https://openreview.net/forum?id=HJWLfGWRb)
| *Transforming Auto-encoders*       | Geoffrey E. HintonAlex Krizhevsky, Sida D. Wang | [here](http://www.cs.toronto.edu/~fritz/absps/transauto6.pdf)

## Submodules

The *CapsNet* implementation is included via git submodule. So the **first**
step after cloning *this* repository is to initialize the git submodules. This
can be done via:

```bash
git submodule update --init --recursive
```

# *IMDB*

We use the *IMDB* dataset for sentiment analysis with *CapsNet*. We use a
bidirectional GRU before the *capsnet* layer.

The training can be started with:

```bash
python3 main.py
```

It takes several minutes per epoch. It is highly recommended to use a GPU for
training. All experiments are done with a GTX 1060 (6GB).

## Results

The following experiments are done on *IMDB* dataset:

* Model a): we use a bidirectional GRU with a hidden size of 256. Number of
  capsule is set to 10. Number of routings is set to 3.

| Model | Best accuracy
| ----- | -------------
| a     | 88,98 %

# Requirements

A recent version of *Keras*, *TensorFlow* and *h5py* is needed. Only Python 3.x
is currently supported.

# Contact (Bugs, Feedback, Contribution and more)

For questions about the *capsnet-nlp* repository, please open an issue [here](https://github.com/stefan-it/capsnet-nlp/issues). 
If you want to contribute to the project
please refer to the [Contributing](CONTRIBUTING.md) guide!

# License

To respect the Free Software Movement and the enormous work of Dr. Richard Stallman
the software in this repository is released under the *GNU Affero General Public License*
in version 3. More information can be found [here](https://www.gnu.org/licenses/licenses.html)
and in `COPYING`.
