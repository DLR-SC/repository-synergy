================
OpenFermion-Psi4
================

.. image:: https://badge.fury.io/py/openfermionpsi4.svg
    :target: https://badge.fury.io/py/openfermionpsi4

.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5%2C%203.6-brightgreen.svg

`OpenFermion <http://openfermion.org>`__ is an open source library (licensed under Apache 2) for compiling and analyzing quantum algorithms which simulate fermionic systems.
This plugin library allows the electronic structure package `Psi4 <http://psicode.org>`__ (licensed under GNU Lesser General Public License version 3) to interface with OpenFermion.

Installation
------------

To start using OpenFermion-Psi4, first install `Psi4 <http://psicode.org>`__.
Note that Psi4 is designed specifically for the
`Anaconda <https://www.anaconda.com/download>`__ python distribution.
While it is possible to install Psi4 without Anaconda, if one does use Anaconda python
the following commands will install Psi4 and pip (used to install OpenFermion-Psi4):

.. code-block:: bash

  conda config --add channels http://conda.anaconda.org/psi4
  python -m conda install psi4
  python -m conda install pip

To install the latest versions of OpenFermion and OpenFermion-Psi4 (in development mode):

.. code-block:: bash

  git clone https://github.com/quantumlib/OpenFermion-Psi4
  cd OpenFermion-Psi4
  python -m pip install -e .

Alternatively, to install the latest PyPI releases as libraries (in user mode):

.. code-block:: bash

  python -m pip install --user openfermionpsi4

Also be sure to take a look at the `ipython notebook demo <https://github.com/quantumlib/OpenFermion-Psi4/blob/master/examples/openfermionpsi4_demo.ipynb>`__.

How to contribute
-----------------

We'd love to accept your contributions and patches to OpenFermion-Psi4.
There are a few guidelines you need to follow.
Contributions to OpenFermion-Psi4 must be accompanied by a Contributor License Agreement.
You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as part of the project.
Head over to https://cla.developers.google.com/
to see your current agreements on file or to sign a new one.

All submissions, including submissions by project members, require review.
We use GitHub pull requests for this purpose. Consult
`GitHub Help <https://help.github.com/articles/about-pull-requests/>`__ for
more information on using pull requests.
Furthermore, please make sure your new code comes with extensive tests!
We use automatic testing to make sure all pull requests pass tests and do not
decrease overall test coverage by too much. Make sure you adhere to our style
guide. Just have a look at our code for clues. We mostly follow
`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ and use
the corresponding `linter <https://pypi.python.org/pypi/pep8>`_ to check for it.
Code should always come with documentation.

Authors
-------

`Ryan Babbush <http://ryanbabbush.com>`__ (Google),
`Jarrod McClean <http://jarrodmcclean.com>`__ (Google),
`Kevin Sung <https://github.com/kevinsung>`__ (University of Michigan),
`Ian Kivlichan <http://aspuru.chem.harvard.edu/ian-kivlichan/>`__ (Harvard),
`Dave Bacon <https://github.com/dabacon>`__ (Google),
`Yudong Cao <https://github.com/yudongcao>`__ (Harvard),
`Chengyu Dai <https://github.com/jdaaph>`__ (University of Michigan),
`E. Schuyler Fried <https://github.com/schuylerfried>`__ (Harvard),
`Craig Gidney <https://github.com/Strilanc>`__ (Google),
`Brendan Gimby <https://github.com/bgimby>`__ (University of Michigan),
`Pranav Gokhale <https://github.com/singular-value>`__ (University of Chicago),
`Thomas H??ner <https://github.com/thomashaener>`__ (ETH Zurich),
`Tarini Hardikar <https://github.com/TariniHardikar>`__ (Dartmouth),
`Vojt??ch Havl????ek <https://github.com/VojtaHavlicek>`__ (Oxford),
`Oscar Higgott <https://github.com/oscarhiggott>`__ (University College London),
`Cupjin Huang <https://github.com/pertoX4726>`__ (University of Michigan),
`Josh Izaac <https://github.com/josh146>`__ (Xanadu),
`Zhang Jiang <https://ti.arc.nasa.gov/profile/zjiang3>`__ (NASA),
`Xinle Liu <https://github.com/sheilaliuxl>`__ (Google),
`Sam McArdle <https://github.com/sammcardle30>`__ (Oxford),
`Matthew Neeley <https://github.com/maffoo>`__ (Google),
`Thomas O'Brien <https://github.com/obriente>`__ (Leiden University),
`Bryan O'Gorman <https://ti.arc.nasa.gov/profile/bogorman>`__ (UC Berkeley, NASA),
`Isil Ozfidan <https://github.com/conta877>`__ (D-Wave Systems),
`Max Radin <https://github.com/max-radin>`__ (UC Santa Barbara),
`Jhonathan Romero <https://github.com/jromerofontalvo>`__ (Harvard),
`Nicholas Rubin <https://github.com/ncrubin>`__ (Google),
`Daniel Sank <https://github.com/DanielSank>`__ (Google),
`Nicolas Sawaya <https://github.com/nicolassawaya>`__ (Harvard),
`Kanav Setia <https://github.com/kanavsetia>`__ (Dartmouth),
`Hannah Sim <https://github.com/hsim13372>`__ (Harvard),
`Damian Steiger <https://github.com/damiansteiger>`__ (ETH Zurich),
`Mark Steudtner <https://github.com/msteudtner>`__  (Leiden University),
`Qiming Sun <https://github.com/sunqm>`__ (Caltech),
`Wei Sun <https://github.com/Spaceenter>`__ (Google),
`Daochen Wang <https://github.com/daochenw>`__ (River Lane Research),
`Chris Winkler <https://github.com/quid256>`__ (University of Chicago) and
`Fang Zhang <https://github.com/fangzh-umich>`__ (University of Michigan).

How to cite
-----------
When using OpenFermion-Psi4 for research projects, please cite:

    Jarrod R. McClean, Kevin J. Sung, Ian D. Kivlichan, Yudong Cao,
    Chengyu Dai, E. Schuyler Fried, Craig Gidney, Brendan Gimby,
    Pranav Gokhale, Thomas H??ner, Tarini Hardikar, Vojt??ch Havl????ek,
    Oscar Higgott, Cupjin Huang, Josh Izaac, Zhang Jiang, Xinle Liu,
    Sam McArdle, Matthew Neeley, Thomas O'Brien, Bryan O'Gorman, Isil Ozfidan,
    Maxwell D. Radin, Jhonathan Romero, Nicholas Rubin, Nicolas P. D. Sawaya,
    Kanav Setia, Sukin Sim, Damian S. Steiger, Mark Steudtner, Qiming Sun,
    Wei Sun, Daochen Wang, Fang Zhang and Ryan Babbush.
    *OpenFermion: The Electronic Structure Package for Quantum Computers*.
    `arXiv:1710.07629 <https://arxiv.org/abs/1710.07629>`__. 2017.

as well as

    Robert M. Parrish, Lori A. Burns, Daniel G. A. Smith, Andrew C. Simmonett, A. Eugene DePrince III,
    Edward G. Hohenstein , U??ur Bozkaya, Alexander Yu. Sokolov, Roberto Di Remigio, Ryan M. Richard,
    J??r??me F. Gonthier, Andrew M. James, Harley R. McAlexander, Ashutosh Kumar, Masaaki Saitow, Xiao Wang,
    Benjamin P. Pritchard, Prakash Verma, Henry F. Schaefer III , Konrad Patkowski, Rollin A. King,
    Edward F. Valeev, Francesco A. Evangelista, Justin M. Turney, T. Daniel Crawford and C. David Sherrill.
    *Psi4 1.1: An Open-Source Electronic Structure Program Emphasizing Automation, Advanced Libraries, and Interoperability*.
    `Journal of Chemical Theory and Computation <http://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00174>`__.
    2017.

We are happy to include future contributors as authors on later OpenFermion releases.

Disclaimer
----------
Copyright 2017 The OpenFermion Developers.
This is not an official Google product.
