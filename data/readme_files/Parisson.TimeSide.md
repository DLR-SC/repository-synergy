==================================================
TimeSide : audio processing framework for the web
==================================================

TimeSide is a python framework enabling low and high level audio analysis, imaging, transcoding, streaming and labelling. Its high-level API is designed to enable complex processing on very large datasets of any audio or video assets with a plug-in architecture, a secure scalable backend and an extensible dynamic web frontend.


Use cases
==========

* Scaled audio computing (filtering, machine learning, etc)
* Web audio visualization
* Audio process prototyping
* Realtime and on-demand transcoding and streaming over the web
* Automatic segmentation and labelling synchronized with audio events


Goals
=====

* **Do** asynchronous and fast audio processing with Python,
* **Decode** audio frames from **any** audio or video media format into numpy arrays,
* **Analyze** audio content with some state-of-the-art audio feature extraction libraries like Aubio, Yaafe and VAMP as well as some pure python processors
* **Visualize** sounds with various fancy waveforms, spectrograms and other cool graphers,
* **Transcode** audio data in various media formats and stream them through web apps,
* **Serialize** feature analysis data through various portable formats,
* **Playback** and **interact** **on demand** through a smart high-level HTML5 extensible player,
* **Index**, **tag** and **annotate** audio archives with semantic metadata (see `Telemeta <http://telemeta.org>`__ which embed TimeSide).
* **Deploy** and **scale** your own audio processing engine through any infrastructure


Funding and support
===================

To fund the project and continue our fast development process, we need your explicit support. So if you use TimeSide in production or even in a development or experimental setup, please let us know by:

* staring or forking the project on `GitHub <https://github.com/Parisson/TimeSide>`_
* tweeting something to `@parisson_studio <https://twitter.com/parisson_studio>`_ or `@telemeta <https://twitter.com/telemeta>`_
* drop us an email <support@parisson.com>

Thanks for your help!

News
=====

0.9
---

* Upgrade all python dependencies
* Add Vamp, Essentia, Yaafe, librosa, PyTorch, Tensorflow libs and wrappers
* Add a few analyzing plugins (Essentia Dissonance, Vamp Constant Q, Vamp Tempo, Vamp general wrapper, Yaafe general wrapper)
* Add processor parameter management
* Add processor inheritance
* Improve HTML5 player with clever data streaming
* Improve REST API and various serialzers
* Improve unit testing
* Various bug fixes


0.8
---

* Add *Docker* support for instant installation. This allows to run TimeSide now on *any* OS platform!
* Add `Jupyter Notebook <http://jupyter.org/>`_ support for easy prototyping, experimenting and sharing (see the examples in the doc).
* Add an experimental web server and REST API based on Django REST Framework, Redis and Celery. This now provides a real web audio processing server with high scaling capabilities thanks to Docker (clustering) and Celery (multiprocessing).
* Start the development of a new player interface thanks to Angular and WavesJS.
* Huge cleanup of JS files. Please now use bower to get all JS dependencies as `listed in settings <https://github.com/Parisson/TimeSide/blob/dev/app/sandbox/settings.py#L199>`_.
* Add metadata export to Elan annotation files.
* Fix and improve some data structures in analyzer result containers.
* Many various bugfixes.

0.7.1
-----

* fix django version to 1.6.10 (sync with Telemeta 1.5)

0.7
----

* Code refactoring:

   - Create a new module `timeside.plugins` and move processors therein: timeside.plugins.decoder,analyzer, timeside.plugins.encoder, timeside.plugins.fx
   - WARNING: to properly manage the namespace packages structure, the TimeSide main module is now `timeside.core` and code should now be initialized with `import timeside.core`
   - `timeside.plugins` is now a `namespace package <https://pythonhosted.org/setuptools/setuptools.html#namespace-packages>`_ enabling external plugins to be **automatically** plugged into TimeSide (see for example `timeside-diadems <https://github.com/ANR-DIADEMS/timeside-diadems>`_). This now makes TimeSide a **real** plugin host, yeah!
   - A dummy timeside plugin will soon be provided for easy development start.

* Move all analyzers developped by the partners of the Diadems project to a new repository: `timeside-diadems <https://github.com/ANR-DIADEMS/timeside-diadems>`_
* Many fixes for a better processing by `Travis-CI <https://travis-ci.org/Parisson/TimeSide>`_
* Add a dox file to test the docker building continously on `various distributions <https://github.com/Parisson/Docker>`_

For older news, please visit: https://github.com/Parisson/TimeSide/blob/master/NEWS.rst

Documentation
==============

* General documentation : http://parisson.github.io/TimeSide/
* Tutorials : http://parisson.github.io/TimeSide/tutorials/index.html
* API : http://parisson.github.io/TimeSide/api/index.html
* Publications : https://github.com/Parisson/Telemeta-doc
* Some online notebooks : http://mybinder.org/repo/thomasfillon/Timeside-demos
* Player UI (v1) wiki : https://github.com/Parisson/TimeSide/wiki/Ui-Guide
* A player example : http://archives.crem-cnrs.fr/archives/items/CNRSMH_E_2004_017_001_01/

Install
=======

Thanks to Docker, Timeside is now fully available as a docker composition ready to work. The docker based composition bundles some powerfull applications and modern frameworks out-of-the-box like: Python, Conda, Numpy, Jupyter, Gstreamer, Django, Celery, Haystack, ElasticSearch, MySQL, Redis, uWSGI, Nginx and many more.

First, install `Docker <https://store.docker.com/search?offering=community&q=&type=edition>`_ and `docker-compose <https://docs.docker.com/compose/>`_

Then clone TimeSide::

    git clone --recursive https://github.com/Parisson/TimeSide.git
    cd TimeSide
    docker-compose pull

That's it! Now please go to the documentation to see how to use it.

.. note ::

If you need to use TimeSide outside a docker image please refer to the rules of the Dockerfile which is based on a Debian stable system. But we do not provide any kind of free support in this usercase anymore (the dependency list is now huge). To get commercial support in more various usecases, please reach the Parisson dev team.

Sponsors and Partners
=====================

* `Parisson <http://parisson.com>`_
* `CNRS <http://www.cnrs.fr>`_ (National Center of Science Research, France)
* `Huma-Num <http://www.huma-num.fr/>`_ (big data equipment for digital humanities, ex TGE Adonis)
* `CREM <http://www.crem-cnrs.fr>`_ (french National Center of Ethomusicology Research, France)
* `Universit?? Pierre et Marie Curie <http://www.upmc.fr>`_ (UPMC Paris, France)
* `ANR <http://www.agence-nationale-recherche.fr/>`_ (CONTINT 2012 project : DIADEMS)
* `MNHN <http://www.mnhn.fr>`_ : Museum National d'Histoire Naturelle (Paris, France)
* `C4DM <http://c4dm.eecs.qmul.ac.uk/>`_ : Center for Digital Music, Queen Mary University (London, United Kingdom)
* `NYU Steinhardt <http://steinhardt.nyu.edu/music/>`_ : Music and Performing Arts Professions, New York University (New York, USA)

Related projects
=================

* `Telemeta <http://telemeta.org>`__ : Open web audio platform
* `Sound archives of the CNRS <http://archives.crem-cnrs.fr/>`_, CREM and the "Mus??e de l'Homme" in Paris, France.
* `DIADEMS <http://www.irit.fr/recherches/SAMOVA/DIADEMS/en/welcome/>`_ sponsored by the ANR.
* `DaCaRyh <http://gtr.rcuk.ac.uk/projects?ref=AH/N504531/1>`_, Data science for the study of calypso-rhythm through history
* `KAMoulox <https://anr-kamoulox.github.io/>`_ Online unmixing of large historical archives
* NYU/CREM/Parisson : arabic music analysis

Copyrights
==========

* Copyright (c) 2006, 2018 Parisson Sarl
* Copyright (c) 2006, 2018 Guillaume Pellerin
* Copyright (c) 2013, 2017 Thomas Fillon
* Copyright (c) 2016, 2017 Eric Debeir
* Copyright (c) 2010, 2014 Paul Brossier
* Copyright (c) 2013, 2014 Maxime Lecoz
* Copyright (c) 2013, 2014 David Doukhan
* Copyright (c) 2006, 2010 Olivier Guilyardi


License
=======

TimeSide is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TimeSide is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

Read the LICENSE.txt file for more details.
