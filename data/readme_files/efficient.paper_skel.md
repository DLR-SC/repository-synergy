A basic, USENIX and ACM style compliant LaTeX paper skeleton.
The default output looks like this:

  http://www.cs.cmu.edu/~dga/paper_skel_lorem.pdf

But is easily tweaked using the standard packages that are invoked
in paper.tex.

The supplied Makefile uses a LaTeX build system called rubber,
which _greatly_ simplifies the build process.  The hard way (multiple
pdflatex/bibtex incantations) will also work. rubber is available at

  https://launchpad.net/rubber/

This assumes that your biblio file is named 'ref.bib'.  Change in paper.tex
as appropriate.

A note:  The given Makefile tries to ensure that all fonts are embedded.
You can double-check by running 'pdffonts' on the final paper.pdf or an
individual figure.

#
# The skeleton for this paper comes from
# https://github.com/efficient/paper_skel.git
# When editing paper_skel, please ensure that your changes are 
# clean and apply to future papers in general, not just one
# specific paper.

Authors:
Michael Kaminsky
David G. Andersen
A cast of thousands (okay, at least dozens!) of students and co-authors
who've found bugs, made or suggested improvements, etc.
