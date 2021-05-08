# Deceptive IDN

[Phishers](https://www.bluecoat.com/security-blog/2014-05-22/bad-guys-using-internationalized-domain-names-idns) are still using [Internationalized Domain Names](https://en.wikipedia.org/wiki/Internationalized\_domain\_name) to trick users. This project uses computer vision to automatically check if IDNs have a deceptive reading.

## Usage

To use the tool, invoke it with python3.
```bash
$ python3 deceptiveidn.py xn--e1awd7f.com
IDN: еріс.com (xn--e1awd7f.com)
	Deceptive IDN, possible readings:
	- cpic.com 207.235.47.22
	- epic.com 199.204.56.88
```

## Dependencies

This script requires python3, pillow (the python3 imaging library), and [tesseract-ocr](https://github.com/tesseract-ocr/tesseract).

```
$ brew install python3 tesseract
$ pip3 install pillow
```


## License
This project copyright Ryan Stortz (@withzombies) and is available under the Apache 2.0 LICENSE.
