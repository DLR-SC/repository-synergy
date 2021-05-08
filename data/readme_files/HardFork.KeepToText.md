# KeepToText

Convert a Google Takeout zip file containing Google Keep notes to a
directory of text files, suitable for import into systems such as Evernote

Use Google Takeout to get a zip file, which will contain your Keep notes

**NOTE**: Be sure that *only* Keep files are included in the Google Takeout zip file, not contacts or any other Google data

Usage:

  simple usage: `python keepToText.py zipFile`
  
  full usage: `python keepToText.py [-h] [--encoding ENCODING] [--system-encoding]
                     [--format {Evernote,CintaNotes}]
                     zipFile`

By default, the text files will be placed in a directory called `Text`, under the same
directory as the zip file. You may import that folder into Evernote.

If you specify `--format CintaNotes`, a single `cintanotes.xml` file containing all your notes will be
created in the same directory as the zip file. You may import that folder into CintaNotes.

Works with Python 2 or 3

**Options**:
  
  Use the `--encoding` option to specify an output encoding, for example, `--encoding latin_1`
  
  Use the `--system-encoding` option to use your operating system's current encoding
  
  The default output encoding is `utf-8`
  
  Use the `--format` option to choose between Evernote and CintaNotes, for example, `--format CintaNotes`
  
  The default format is Evernote
    
**Module dependencies**:

   For Evernote format: HTMLParser
   
   For CintaNotes format: lxml, mako, and python-dateutil
   
   To install a dependency, use: `python -m pip install [dependency]`
