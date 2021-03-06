![Check codestyle and test build](https://github.com/NiaOrg/NiaPy/workflows/Check%20and%20Test/badge.svg)
[![PyPI Version](https://img.shields.io/pypi/v/NiaPy.svg)](https://pypi.python.org/pypi/NiaPy)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/NiaPy.svg)
![PyPI - Status](https://img.shields.io/pypi/status/NiaPy.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/NiaPy.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/NiaOrg/NiaPy.svg)
[![Anaconda-Server Badge](https://anaconda.org/niaorg/niapy/badges/installer/conda.svg)](https://conda.anaconda.org/niaorg)
[![Documentation Status](https://readthedocs.org/projects/niapy/badge/?version=latest)](http://niapy.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/NiaOrg/NiaPy.svg)](https://github.com/NiaOrg/NiaPy/blob/master/LICENSE)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/NiaOrg/NiaPy/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/NiaOrg/NiaPy/?branch=master)
[![Coverage Status](https://img.shields.io/coveralls/NiaOrg/NiaPy/master.svg)](https://coveralls.io/r/NiaOrg/NiaPy)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/NiaOrg/NiaPy.svg)
[![Updates](https://pyup.io/repos/github/NiaOrg/NiaPy/shield.svg)](https://pyup.io/repos/github/NiaOrg/NiaPy/)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/NiaOrg/NiaPy.svg)](http://isitmaintained.com/project/NiaOrg/NiaPy "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/NiaOrg/NiaPy.svg)](http://isitmaintained.com/project/NiaOrg/NiaPy "Percentage of issues still open")
![GitHub contributors](https://img.shields.io/github/contributors/NiaOrg/NiaPy.svg)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1205048.svg)](https://doi.org/10.5281/zenodo.1205048)
[![DOI](http://joss.theoj.org/papers/10.21105/joss.00613/status.svg)](https://doi.org/10.21105/joss.00613)

# About

Nature-inspired algorithms are a very popular tool for solving optimization problems. Numerous variants of [nature-inspired algorithms have been developed](https://arxiv.org/abs/1307.4186) since the beginning of their era. To prove their versatility, those were tested in various domains on various applications, especially when they are hybridized, modified or adapted. However, implementation of nature-inspired algorithms is sometimes a difficult, complex and tedious task. In order to break this wall, NiaPy is intended for simple and quick use, without spending time for implementing algorithms from scratch.

<p align="center"><img src=".github/imgs/NiaPyLogo.png" alt="NiaPy" title="NiaPy"/></p>

# Mission

Our mission is to build a collection of nature-inspired algorithms and create a simple interface for managing the optimization process. NiaPy will offer:

- numerous benchmark functions implementations,
- use of various nature-inspired algorithms without struggle and effort with a simple interface,
- easy comparison between nature-inspired algorithms and
- export of results in various formats (LaTeX, JSON, Excel).

# Overview

Python micro framework for building nature-inspired algorithms. Official documentation is available [here](https://niapy.readthedocs.io/en/stable/).

The micro framework features following algorithms:

- basic:
  - Artificial bee colony algorithm ([see example](examples/run_abc.py))
  - Bat algorithm ([see example](examples/run_ba.py))
  - Camel algorithm ([see example](example/run_ca.py))
  - Cuckoo search ([see example](examples/run_cs.py))
  - Differential evolution algorithm ([see example](examples/run_de.py))
  - Evolution Strategy ([see example](example/run_es1p1.py), [see example](example/run_esMp1.py), [see example](example/run_esMpL.py), [see example](example/run_esML.py))
  - Firefly algorithm ([see example](examples/run_fa.py))
  - Fireworks algorithm ([see example](examples/run_fwa.py), [see example](examples/run_efwa.py), [see example](examples/run_dfwa.py), [see example](examples/run_bbfwa.py))
  - Flower pollination algorithm ([see example](examples/run_fpa.py))
  - Forest optimization algorithm ([see example](examples/run_foa.py))
  - Genetic algorithm ([see example](examples/run_ga.py))
  - Glowworm Swarm Optimization ([see example](examples/run_gso.py), [see example](examples/run_gsov1.py), [see example](examples/run_gsov2.py), [see example](examples/run_gsov3.py))
  - Grey wolf optimizer ([see example](examples/run_gwo.py))
  - Monarch butterfly optimization ([see example](examples/run_mbo.py))
  - Moth flame optimizer ([see example](examples/run_mfo.py))
  - Harmony Search Algorithm ([see example](examples/run_hs.py))
  - Krill Herd Algorithm ([see example](examples/run_khv1.py), [see example](examples/run_khv2.py), [see example](examples/run_khv3.py), [see example](examples/run_khv4.py), [see example](examples/run_khV11.py))
  - Monkey King Evolution ([see example](examples/run_mkev1.py), [see example](examples/run_mkev2.py), [see example](examples/run_mkev3.py))
  - Particle swarm optimization ([see example](examples/run_pso.py))
  - Sine Cosine Algorithm ([see example](examples/run_sca.py))
- modified:
  - Hybrid bat algorithm ([see example](examples/run_hba.py))
  - Self-adaptive differential evolution algorithm ([see example](examples/run_jde.py))
  - Dynamic population size self-adaptive differential evolution algorithm ([see example](examples/run_dynnpjde.py))
- other:
  - Anarchic society optimization ([see example](examples/run_aso.py))
  - Hill climb algorithm ([see example](examples/run_hc.py))
  - Multiple trajectory search ([see example](examples/run_mts.py), [see example](examples/run_mtsv1.py))
  - Nelder mead method ([see example](examples/run_nmm.py))
  - Simulated annealing algorithm ([see example](examples/run_sa.py))

Other examples:
- Using different termination conditions (nFES, nGEN, reference value) ([see example](examples/stopping_criterions.py))
- Basic statistics example (min, max, mean, median, std) ([see example](examples/basic_stats.py))
- Storing improvements during the evolutionary cycle ([see example](examples/log_results.py))
- Custom initialization of initial population ([see example](examples/custom_init_population.py))

The following benchmark functions are included in NiaPy:
- Ackley
- Alpine
  - Alpine1
  - Alpine2
- Bent Cigar
- Chung Reynolds
- Csendes
- Discus
- Dixon-Price
- Elliptic
- Griewank
- Happy cat
- HGBat
- Katsuura
- Levy
- Michalewicz
- Perm
- Pint??r
- Powell
- Qing
- Quintic
- Rastrigin
- Ridge
- Rosenbrock
- Salomon
- Schumer Steiglitz
- Schwefel
  - Schwefel 2.21
  - Schwefel 2.22
- Sphere
  - Sphere2 -> Sphere with different powers
  - Sphere3 -> Rotated hyper-ellipsoid
- Step
  - Step2
  - Step3
- Stepint
- Styblinski-Tang
- Sum Squares
- Trid
- Weierstrass
- Whitley
- Zakharov

# Setup

## Requirements

- Python 3.6.x or 3.7.x (backward compatibility with 2.7.x)
- Pip

### Dependencies

- numpy >= 1.16.2
- scipy >= 1.2.1
- enum34 >= 1.1.6 (if using python version < 3.4)
- xlsxwriter >= 1.1.6
- matplotlib >= 2.2.4

List of development dependencies and requirements can be found [here](CONTRIBUTING.md#development-dependencies).

## Installation

Install NiaPy with pip:

### Latest version (2.0.0rc5)
```sh
$ pip install NiaPy==2.0.0rc5
```

### Latest stable version
```sh
$ pip install NiaPy
```

Install NiaPy with conda:

```sh
conda install -c niaorg niapy
```

or directly from the source code:

```sh
$ git clone https://github.com/NiaOrg/NiaPy.git
$ cd NiaPy
$ python setup.py install
```

# Usage

After installation, the package can be imported:

```sh
$ python
>>> import NiaPy
>>> NiaPy.__version__
```

For more usage examples please look at **examples** folder.

More advanced examples can also be found in the [NiaPy-examples repository](https://github.com/NiaOrg/NiaPy-examples).

# Cite us

Are you using NiaPy in your project or research? Please cite us!

- Plain format

```
      Vrban??i??, G., Brezo??nik, L., Mlakar, U., Fister, D., & Fister Jr., I. (2018).
      NiaPy: Python microframework for building nature-inspired algorithms.
      Journal of Open Source Software, 3(23), 613\. <https://doi.org/10.21105/joss.00613>
```

- Bibtex format

```
    @article{NiaPyJOSS2018,
        author  = {Vrban{\v{c}}i{\v{c}}, Grega and Brezo{\v{c}}nik, Lucija
                  and Mlakar, Uro{\v{s}} and Fister, Du{\v{s}}an and {Fister Jr.}, Iztok},
        title   = {{NiaPy: Python microframework for building nature-inspired algorithms}},
        journal = {{Journal of Open Source Software}},
        year    = {2018},
        volume  = {3},
        issue   = {23},
        issn    = {2475-9066},
        doi     = {10.21105/joss.00613},
        url     = {https://doi.org/10.21105/joss.00613}
    }
```

- RIS format

```
    TY  - JOUR
    T1  - NiaPy: Python microframework for building nature-inspired algorithms
    AU  - Vrban??i??, Grega
    AU  - Brezo??nik, Lucija
    AU  - Mlakar, Uro??
    AU  - Fister, Du??an
    AU  - Fister Jr., Iztok
    PY  - 2018
    JF  - Journal of Open Source Software
    VL  - 3
    IS  - 23
    DO  - 10.21105/joss.00613
    UR  - http://joss.theoj.org/papers/10.21105/joss.00613
```

## Contributors ???

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/GregaVrbancic"><img src="https://avatars0.githubusercontent.com/u/1894788?v=4" width="100px;" alt="Grega Vrban??i??"/><br /><sub><b>Grega Vrban??i??</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=GregaVrbancic" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=GregaVrbancic" title="Documentation">????</a> <a href="https://github.com/NiaOrg/NiaPy/issues?q=author%3AGregaVrbancic" title="Bug reports">????</a> <a href="#example-GregaVrbancic" title="Examples">????</a> <a href="#maintenance-GregaVrbancic" title="Maintenance">????</a> <a href="#platform-GregaVrbancic" title="Packaging/porting to new platform">????</a> <a href="#projectManagement-GregaVrbancic" title="Project Management">????</a> <a href="#review-GregaVrbancic" title="Reviewed Pull Requests">????</a></td>
    <td align="center"><a href="https://github.com/firefly-cpp"><img src="https://avatars2.githubusercontent.com/u/1633361?v=4" width="100px;" alt="firefly-cpp"/><br /><sub><b>firefly-cpp</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=firefly-cpp" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=firefly-cpp" title="Documentation">????</a> <a href="https://github.com/NiaOrg/NiaPy/issues?q=author%3Afirefly-cpp" title="Bug reports">????</a> <a href="#example-firefly-cpp" title="Examples">????</a> <a href="#review-firefly-cpp" title="Reviewed Pull Requests">????</a></td>
    <td align="center"><a href="https://github.com/lucijabrezocnik"><img src="https://avatars2.githubusercontent.com/u/36370699?v=4" width="100px;" alt="Lucija Brezo??nik"/><br /><sub><b>Lucija Brezo??nik</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=lucijabrezocnik" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=lucijabrezocnik" title="Documentation">????</a> <a href="https://github.com/NiaOrg/NiaPy/issues?q=author%3Alucijabrezocnik" title="Bug reports">????</a> <a href="#example-lucijabrezocnik" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/mlaky88"><img src="https://avatars1.githubusercontent.com/u/23091578?v=4" width="100px;" alt="mlaky88"/><br /><sub><b>mlaky88</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=mlaky88" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=mlaky88" title="Documentation">????</a> <a href="#example-mlaky88" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/rhododendrom"><img src="https://avatars1.githubusercontent.com/u/3198785?v=4" width="100px;" alt="rhododendrom"/><br /><sub><b>rhododendrom</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=rhododendrom" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=rhododendrom" title="Documentation">????</a> <a href="#example-rhododendrom" title="Examples">????</a> <a href="https://github.com/NiaOrg/NiaPy/issues?q=author%3Arhododendrom" title="Bug reports">????</a> <a href="#review-rhododendrom" title="Reviewed Pull Requests">????</a></td>
    <td align="center"><a href="https://github.com/kb2623"><img src="https://avatars3.githubusercontent.com/u/7480221?s=460&v=4" width="100px;" alt="Klemen"/><br /><sub><b>Klemen</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=kb2623" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=kb2623" title="Documentation">????</a> <a href="#example-kb2623" title="Examples">????</a> <a href="https://github.com/NiaOrg/NiaPy/issues?q=author%3Akb2623" title="Bug reports">????</a> <a href="#review-kb2623" title="Reviewed Pull Requests">????</a></td>
    <td align="center"><a href="https://github.com/flyzoor"><img src="https://avatars2.githubusercontent.com/u/38717032?s=40&v=4" width="100px;" alt="Jan Popi??"/><br /><sub><b>Jan Popi??</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=flyzoor" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=flyzoor" title="Documentation">????</a> <a href="#example-flyzoor" title="Examples">????</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/lukapecnik"><img src="https://avatars1.githubusercontent.com/u/23029992?s=460&v=4" width="100px;" alt="Luka Pe??nik"/><br /><sub><b>Luka Pe??nik</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=lukapecnik" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=lukapecnik" title="Documentation">????</a> <a href="#example-lukapecnik" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/bankojan"><img src="https://avatars3.githubusercontent.com/u/44372016?s=460&v=4" width="100px;" alt="Jan Banko"/><br /><sub><b>Jan Banko</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=bankojan" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=bankojan" title="Documentation">????</a> <a href="#example-bankojan" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/RokPot"><img src="https://avatars0.githubusercontent.com/u/23029990?s=460&v=4" width="100px;" alt="RokPot"/><br /><sub><b>RokPot</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=RokPot" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=RokPot" title="Documentation">????</a> <a href="#example-RokPot" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/mihael-mika"><img src="https://avatars2.githubusercontent.com/u/22932805?s=460&v=4" width="100px;" alt="mihaelmika"/><br /><sub><b>mihaelmika</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=mihael-mika" title="Code">????</a> <a href="https://github.com/NiaOrg/NiaPy/commits?author=mihael-mika" title="Documentation">????</a> <a href="#example-mihael-mika" title="Examples">????</a></td>
    <td align="center"><a href="https://github.com/jacebrowning"><img src="https://avatars1.githubusercontent.com/u/939501?s=460&v=4" width="100px;" alt="Jace Browning"/><br /><sub><b>Jace Browning</b></sub></a><br /><a href="https://github.com/NiaOrg/NiaPy/commits?author=jacebrowning" title="Code">????</a></td>
    <td align="center"><a href="https://github.com/musawakiliML"><img src="https://avatars1.githubusercontent.com/u/19978292?v=4" width="100px;" alt="Musa Adamu Wakili"/><br /><sub><b>Musa Adamu Wakili</b></sub></a><br /><a href="#question-musawakiliML" title="Answering Questions">????</a></td>
    <td align="center"><a href="http://www.uni-kassel.de/eecs/en/faculties/e2n/staff/florian-schaefer.html"><img src="https://avatars2.githubusercontent.com/u/23655422?v=4" width="100px;" alt="Florian Schaefer"/><br /><sub><b>Florian Schaefer</b></sub></a><br /><a href="#ideas-FlorianShepherd" title="Ideas, Planning, & Feedback">????</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://www.jhmenke.de"><img src="https://avatars0.githubusercontent.com/u/25080218?v=4" width="100px;" alt="Jan-Hendrik Menke"/><br /><sub><b>Jan-Hendrik Menke</b></sub></a><br /><a href="#question-jhmenke" title="Answering Questions">????</a></td>
    <td align="center"><a href="https://github.com/brett18618"><img src="https://avatars2.githubusercontent.com/u/44141573?v=4" width="100px;" alt="brett18618"/><br /><sub><b>brett18618</b></sub></a><br /><a href="#question-brett18618" title="Answering Questions">????</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

## Contributing

[![Open Source Helpers](https://www.codetriage.com/niaorg/niapy/badges/users.svg)](https://www.codetriage.com/niaorg/niapy)

We encourage you to contribute to NiaPy! Please check out the [Contributing to NiaPy guide](CONTRIBUTING.md) for guidelines about how to proceed.

Everyone interacting in NiaPy's codebases, issue trackers, chat rooms and mailing lists is expected to follow the NiaPy [code of conduct](CODE_OF_CONDUCT.md).

## Licence

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!
