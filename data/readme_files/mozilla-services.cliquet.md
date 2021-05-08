Deprecation Notice
==================

Cliquet has been folded into the `Kinto
<https://github.com/Kinto/kinto/>`_ package under the new name
``kinto.core``. You should update your code to import ``kinto.core``
instead of ``cliquet``, and all ``cliquet.*`` settings are now
prefixed with ``kinto`` instead. See
https://mail.mozilla.org/pipermail/kinto/2016-May/000119.html for more
about the background for this decision.


Cliquet
=======

|pypi| |travis| |master-coverage| |readthedocs|

.. |pypi| image:: https://img.shields.io/pypi/v/cliquet.svg
    :target: https://pypi.python.org/pypi/cliquet

.. |travis| image:: https://travis-ci.org/mozilla-services/cliquet.svg?branch=master
    :target: https://travis-ci.org/mozilla-services/cliquet

.. |readthedocs| image:: https://readthedocs.org/projects/cliquet/badge/?version=latest
    :target: http://cliquet.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |master-coverage| image::
    https://coveralls.io/repos/mozilla-services/cliquet/badge.svg?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/mozilla-services/cliquet


*Cliquet* is a toolkit to ease the implementation of HTTP microservices,
such as data-driven REST APIs.

* `Online documentation <http://cliquet.readthedocs.io/en/latest/>`_
* `Issue tracker <https://github.com/mozilla-services/cliquet/issues>`_
* `Contributing <http://cliquet.readthedocs.io/en/latest/contributing.html>`_
* Talks `at PyBCN <http://mozilla-services.github.io/cliquet/talks/2015.07.pybcn/>`_
  and `at PyConFR <http://mozilla-services.github.io/cliquet/talks/2015.10.pyconfr/>`_
