Summary
-------

Compares two audio files or directories of audio files to gauge their
similarity. A file that is likely to have been derived from another
is flagged as a match.

To run the program, type one of:
* ./audiocompare -f _file1_ -f _file2_
* ./audiocompare -f _file1_ -d _dir1_
* ./audiocompare -d _dir1_ -f _file1_
* ./audiocompare -d _dir1_ -d _dir2_

Arguments following a "-f" argument must be a filename,
and arguments following a "-d" argument must be a directory
containing only audio files. Input files must be WAVE or MP3 files.
You may list the same file or directory twice.

If errors are found, appropriate error messages
will be printed, and the program may continue if it can.
Match results will be printed as "NO MATCH" if two
non-matching files were compared, and "MATCH ..."
if two matching files were compared, listing the two
files that matched, and giving the match score.

This program is intended to run on Linux. Compatibility with OS X
or Windows would not be difficult, but has not been attempted yet.

Dependencies
------------

* Python 2.7
* NumPy

History
-------

The program was written as the semester project
for CS 4500, Fall 2013, with Professor William Clinger
at Northeastern University.

The team members were:
* An Dang (@dangan249)
* Cory Finger (@fingerco)
* Zheng Hui Er (@zh-er)
* Charles Connell (@charlesconnell)


Third-Party Software Acknowledgements
-------------------------------------

There are about 15 lines of code in FFT.py that
are a modified version of code inside
matplotlib. The file
LICENSE.matplotlib license found in this directory
is the matplotlib license, included as required
when creating derivative works. More information
can be found in FFT.py.

Notes
-----

Tests in the test directory depend on files that aren't in this source tree,
so don't expect them to pass for you. The files are not included because
many are copyrighted, and they are too big to reasonably store in Git.
