Mozilla Webdev Bootcamp
=======================
`View this document at mozweb.readthedocs.org <https://mozweb.readthedocs.org>`_

A roadmap to success as a web developer contributing to Mozilla. Now with 80%
more success!

Patches are always welcome! If you'd like to contribute, fork and make a pull
request.


Building locally
----------------
The instructions below assume you have Python and `pip`_ installed. It is also
strongly recommended that you create and activate a `virtualenv`_ first.

If you'd like to build the bootcamp locally:

.. code-block:: sh

   pip install -r requirements.txt
   make html

The resulting docs can be located under the ``_build/html`` directory.

You can also run ``make livehtml`` to launch a web server on
http://127.0.0.1:8000 to rebuild the documentation automatically when any
files are changed.

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/

Licensing
---------

Feel free to fork this repo or adapt its work for your own bootcamp. All work
is licensed under a `Creative Commons Attribution`_ license.

.. _`Creative Commons Attribution`: https://creativecommons.org/licenses/by/4.0/
