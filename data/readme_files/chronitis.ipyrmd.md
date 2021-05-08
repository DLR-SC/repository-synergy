ipyrmd
======

Convert between IPython/Jupyter notebooks and R Markdown documents
------------------------------------------------------------------

This script provides conversion in both directions between the [IPython](https://github.com/ipython/ipython) [notebook format](https://ipython.org/ipython-doc/3/notebook/nbformat.html) (JSON with separate markdown and code) and the [R Markdown](https://github.com/rstudio/rmarkdown) [format](http://rmarkdown.rstudio.com) (markdown text with annotated code blocks). Conversion to and from plain R files with markdown embedded in [knitr](http://yihui.name/knitr/)-style comments (`#' markdown`) is also supported.

It only really makes sense to use it with IPython notebooks using the IPython [R kernel](http://github.com/IRkernel/IRkernel), but will work with any type of code if you insist.

Conversion should produce useful output, but is not completely lossless:

 * Inline code blocks in R Markdown (`r somecode`) are currently ignored (they remain as markdown text). Inserting code blocks for them would be a possible extension but since the main use for such blocks is to display an output value I assume ignoring them should not usually change program flow.
 * The YAML header used in R Markdown does not have a functional equivalent in IPython. The contents of the header are stored in the IPython notebook metadata dictionary (as `Rmd_header`) for round-trip conversion, but are not otherwise used.
 * Chunk options for R Markdown (```` ```{r, foo=bar}````) also do not (currently) have any functional equivalent in the IPython notebook. The option string (as text) is stored in the cell metadata (as `Rmd_chunk_options`) for round-trip conversion.
 * Since whitespace is significant in markdown, we attempt to maintain blank lines within code and markdown blocks, but the boundaries between code and markdown may not be exactly reproduced (you may get extra blank lines).
 * The IPython notebook may contain both text and rich output, but there is no way to keep this for R Markdown - you will need to re-knit the document.

Usage
-----

`python3`, `nbformat` and `pyyaml` are required.

    ipyrmd [--to R|Rmd|ipynb] [--from R|Rmd|ipynb] [-y] [-o outfile] infile

By default the output filename and mode of conversion is determined from the input filename. Notebooks are converted by default to RMarkdown unless you specify R output.

Install
-------

    pip3 install [--user] [--upgrade] ipyrmd

Alternatives, it can be installed manually by downloading the archive, extracting it then running `python3 setup.py install --user`. This should install the `ipyrmd` script in your local bin directory (probably `~/.local/bin`).

TODO
----

 * Options for how to handle inline R blocks
 * Consider using nbconvert machinery for ipynb -> Rmd conversion
 * Consider whether any chunk options can be emulated with IRdisplay calls
 * Check IPython API compatibility between IPython and Jupyter
 * De-duplicate code between R and Rmd methods

History
-------

 *  0.1 (2015-05-27) Initial release
 *  0.2 (2015-05-29) Re-structure as a python library providing script `ipyrmd`
 *  0.3 (2015-06-09) Add support for R files with markdown embedded in #' comments
 *  0.4 (2016-06-01) Added a test suite and fixed a number of round-trip bugs
 *  0.4.2 (2016-06-29) Fix missing README causing setup errors (ipyrmd#3)
 *  0.4.3 (2017-10-09) Fix installation using requirements.txt (ipyrmd#4)
