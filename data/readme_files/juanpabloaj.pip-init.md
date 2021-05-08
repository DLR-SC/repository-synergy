========
pip-init
========

.. image:: https://travis-ci.org/juanpabloaj/pip-init.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/pip-init

Generate a base setup.py file to upload a python package to `pypi <https://pypi.python.org/pypi>`_

Install
=======

::

    pip install pip-init

Usage
=====

::

    pip-init

.. image:: http://i.imgur.com/1Wg46cR.gif

I created a setup.py file, what are the next steps?
====================================================

What are the next steps to upload a package to `pypi <https://pypi.python.org/pypi>`_?

* Create or edit the python code of your package: ::

    mkdir package_code
    $EDITOR package_code/__init__.py

* Create an account on the `PyPI website <https://pypi.python.org/pypi?%3Aaction=register_form>`_.
* Create a ~/.pypirc file ::

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <username>
    password = <password>

* Register and upload your package to pypi ::

    python setup.py register
    python setup.py sdist upload -r pypi

References
==========
* `Packaging and Distributing Projects, pypa. <https://packaging.python.org/en/latest/distributing.html>`_
* `Sharing Your Labor of Love: PyPI Quick and Dirty, Hynek Schlawack. <https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/>`_
* `Open Sourcing a Python Project the Right Way, Jeff Knupp. <http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`_
* `Empaquetando y distribuyendo código python con pip (spanish), JuanPabloAJ. <https://speakerdeck.com/juanpabloaj/empaquetando-y-distribuyendo-codigo-python-con-pip>`_
* `setup.py vs requirements.txt, Donald Stufft. <https://caremad.io/2013/07/setup-vs-requirement>`_
* `Pypi classifiers list. <https://pypi.python.org/pypi?%3Aaction=list_classifiers>`_

Contributors
============

- `JuanPablo AJ <https://github.com/juanpabloaj>`_
- `David Yen <https://github.com/davidyen1124>`_
- `Tom Viner <https://github.com/tomviner>`_
- `Krisztián Fekete <https://github.com/krisztianfekete>`_
- `Kevin J. Qiu <https://github.com/kevinjqiu>`_
