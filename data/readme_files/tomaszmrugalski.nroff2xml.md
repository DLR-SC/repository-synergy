nroff2xml
=========

Simple tool that converts nroff I-D sources into xml2rfc format (xml)

Author: Tomek Mrugalski
Licence: simplified BSD license

Usage:

python nroff2xml.py input-file.nroff

DONE:
- boilerplate xml structure
- section conversion
- text conversion
- references conversion

TODO:
- figures & tables
- RFC3315 section 5.6 is not converted (that's a bug in RFC3315)
- string trimming breaks down all formatting
- convert authors list
- convert name
- convert date

NOTE: This tool is no longer under development. It served its original
purpose of doing initial conversion of RFC3315 nroff to XML. If you are
interested in taking over its development, please drop Tomek a note.
Or just grab and run with it.
