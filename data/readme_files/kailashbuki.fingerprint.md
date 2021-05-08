Fingerprint -- Document Fingerprint Generator
---------------------------------------------

Fingerprint is a signature of the document. In particular, it is a representative subset of hash values from the set of all hash values of a document. For more detail, please consider taking a look at [Winnowing: Local Algorithms for Document Fingerprinting](http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf) *(specifically Figure 2)*.

Fingerprint Module Installation
-------------------------------

The recommended way to install the `fingerprint` module is to simply use `pip`:

```console
$ pip install fingerprint
```
Fingerprint officially supports Python >= 3.0.

How to use fingerprint?
-----------------------
```pycon
>>> import fingerprint
>>> fprint = fingerprint.Fingerprint(kgram_len=4, window_len=5, base=10, modulo=1000)
>>> fprint.generate(str="adorunrunrunadorunrun")
>>> fprint.generate(fpath="../CHANGES.txt")
```

The default values for the parameters are
```python
kgram_len = 50
window_len = 100
base = 101
modulo = sys.maxint
```
