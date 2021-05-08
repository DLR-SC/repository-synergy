[![PyPI](https://img.shields.io/pypi/status/image-match.svg?maxAge=2592000)](https://pypi.python.org/pypi/image-match)
[![PyPI](https://img.shields.io/pypi/v/image-match.svg)](https://pypi.python.org/pypi/image-match)
[![Documentation Status](https://readthedocs.org/projects/image-match/badge/?version=latest)](https://image-match.readthedocs.org/en/latest/)
[![codecov](https://codecov.io/gh/edjolabs/image-match/branch/master/graph/badge.svg)](https://codecov.io/gh/edjolabs/image-match)

![image-match](https://cloud.githubusercontent.com/assets/6517700/17741093/41040a64-649b-11e6-8499-48b78ddca56b.png)

image-match is a simple (now Python 3!) package for finding approximate image matches from a
corpus.  It is similar, for instance, to [pHash](http://www.phash.org/), but
includes a database backend that easily scales to billions of images and
supports sustained high rates of image insertion: up to 10,000 images/s on our
cluster!

**PLEASE NOTE:** This algorithm is intended to find nearly duplicate images -- think copyright
violation detection.  It is **NOT** intended to find images that are conceptually similar.
For more explanation, see [this issue](https://github.com/edjo-labs/image-match/issues/62) or
[this video](https://www.youtube.com/watch?v=DfWLBzArzKE).

Based on the paper [_An image signature for any kind of image_, Wong et
al](http://www.cs.cmu.edu/~hcwong/Pdfs/icip02.ps).  There is an existing
[reference implementation](https://www.pureftpd.org/project/libpuzzle) which
may be more suited to your needs.

The folks over at [Pavlov](https://usepavlov.com/) have released an excellent
[containerized version of image-match](https://github.com/pavlovml/match) for
easy scaling and deployment.

## Quick start

### [Install and setup image-match](http://image-match.readthedocs.io/en/latest/start.html)

Once you're up and running, read these two (short) sections of the documentation to get a feel
for what image-match is capable of:

### [Image signatures](http://image-match.readthedocs.io/en/latest/signatures.html)
### [Storing and searching images](http://image-match.readthedocs.io/en/latest/searches.html)
