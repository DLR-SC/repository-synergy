### Document Processing Toolkit

[![Coverage Status](https://coveralls.io/repos/18F/doc_processing_toolkit/badge.png)](https://coveralls.io/r/18F/doc_processing_toolkit)

##### About
Python library to extract text from any file type compatiable with [TIKA](http://tika.apache.org/). It defaults to OCR when text extraction of a PDF file fails.

##### Dependencies
- [Apache Tika](http://tika.apache.org/)
- [Ghostscript](http://www.ghostscript.com/)
- [Tesseract](https://code.google.com/p/tesseract-ocr/)
- [Xpdf](http://www.foolabs.com/xpdf/)

##### Installation
1. Download tika-server-1.7.jar from [Apache Tika](http://www.apache.org/dyn/closer.cgi/tika/tika-server-1.7.jar)
2. Mac: `brew install ghostscripts` Ubuntu: `sudo apt-get install ghostscript`
3. Mac: `brew install tesseract` Ubuntu: `sudo apt-get install tesseract-ocr`
4. Mac: `brew tap homebrew/x11` and `brew install xpdf` Ubuntu: `sudo apt-get install poppler-utils`
5. Install Python dependencies with `pip install -r requirements.txt`

##### Usage
These script assume that an instance of Tika server is running.
Starting Tika Servers
`java -jar tika-server-1.7.jar --port 9998`

In Python script
```python
from textextraction.extractors import text_extractor
text_extractor(doc_path=doc_path, force_convert=False)
```

##### Tests
In order to run tests:
1. All requirements must be installed
2. Both Tika servers need to be running

Tests are run with nose
Installation
`pip install -r test-requirements.txt`
Running tests
`nosetests`

##### OCR methodology
Documents are converted to gray PNGs with a DPI of 300 using [Ghostscript](http://www.ghostscript.com/) and then OCRed with [Tesseract](https://code.google.com/p/tesseract-ocr/).
Settings for OCR adapted from [OPTIMAL IMAGE CONVERSION SETTINGS FOR TESSERACT OCR](https://mazira.com/blog/optimal-image-conversion-settings-tesseract-ocr) and [The Free Law Project's Courtlistener](https://github.com/freelawproject/courtlistener).
