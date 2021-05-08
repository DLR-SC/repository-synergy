adience_align
========

This project provides alignment tools for faces, to be used as a preprocessing step before computer vision tasks on face images.

Homepage for the project: http://www.openu.ac.il/home/hassner/Adience/


See the test for example usage.

Specificaly, the "pipeline" test, shows how to use the full process (just remember to change the location of the model files to where you stor the *.xml and other model files)

Installation
=========
in the root of the repository:

```
python setup.py sdist
sudo pip install dist/adience-<version_number>.tar.gz
```



CopyRight
=========
(contact: Eran Eidinger (eran@adience.com), Roee Enbar (roee.e@adience.com))

See the LICENSE.txt file (basically, an MIT license).


With any publication that uses this alignment code, or it's derivative, we kindly ask that you cite the paper:
E. Eidinger, R. Enbar, and T. Hassner, Age and Gender Estimation of Unfiltered Faces, Transactions on Information Forensics and Security (IEEE-TIFS), special issue on Face Recognition in the Wild

For more details, please see:
http://www.openu.ac.il/home/hassner/Adience/publications.html

Compilation notes
========
1. The shared objects were compiled for linux 64bit on Ubuntu 13.10
2. The SO uses boost-1.53, so make sure it is installed on your system and available at /usr/local/, or use LD_LIBRARY_PATH="yourpath" to point it at the right place. Alternatively, place "libboost_system.so.1.53.0" and "libboost_filesystem.so.1.53.0". at the "adiencealign/resources/" subfolder
3. For landmarks detection, we use the file libPartsBasedDetector.so, compiled from the project https://github.com/wg-perception/PartsBasedDetector. You can either compile it yourselves, or use the version under "resources" subfolder, compiled with boost 1.53, on a linux ubuntu 14.04 machine.

We will release the source code for the shared object in the near future

Running the test
========
1. run ```./clear_test.sh``` to delete results of old tests.
2. run ```python test_pipeline.py```
3. results are in the "outputs" subfolder
