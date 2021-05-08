# DoNotSnap
<img src="https://raw.githubusercontent.com/AVGInnovationLabs/DoNotSnap/master/dns_logo.png" height="400">

An experiment in detecting DoNotSnap badges in photos, to protect privacy.  

<div style="text-align:center"><p align="center"><img src="https://raw.githubusercontent.com/AVGInnovationLabs/DoNotSnap/master/dns_badge.png" height="200"></p></div>

This program allows you to detect and identify DoNotSnap badges via a sliding-window decision tree classifier (custom heuristics are used to reduce search space).
The classifier is trained by matching samples against image templates using Affine-transform invariant SURF features.

You can find examples of using the classifier in `classify.py` and training a new classifier in `train.py`

A pre-trained classifier can be found in `classifier.pkl`
Alternative versions of the same classifier are in `classifier_alt_1.pkl` and `classifier_alt_2.pkl`
## Running classification
Run `python classify.py <path-image-to-be-tested>`
This will deserialize the classifier from `classifier.pkl` and run it on the image you supplied. A sample image could be found in `sample.jpg`
## Training your own classifier
Run `python train.py <output-file> <total-number-of-samples>`
This will read the sample filenames from `positive.txt` and `negative.txt` files.
Templates filenames are specified in `templates.txt`. A sample template could be found in `template.png`
The output is a `<output-file>.pkl` with serialized classifier.
## Dependencies
  * opencv
  * numpy
  * sklearn
  * matplotlib
  * PIL

## DoNotSnap sticker templates
In the repository you can find templates for printing DoNoSnap stickers.

`avery_8254.pdf` contains design compatible with US format paper. Compatible Avery templates:
  * 15664
  * 18664
  * 45464
  * 48264
  * 48464
  * 48864
  * 5164
  * 5264
  * 55164
  * 5524
  * 55264
  * 55364
  * 55464
  * 5664
  * 58164
  * 58264
  * 8164
  * 8254
  * 8464
  * 8564
  * 15264
  * 95940
  * 95905

`A-0004-01_P.pdf` contains design compatible with A4-format paper. Compatible Avery templates:
  * J8165
  * J8165-10
  * J8165-25
  * J8165-40
  * J8165-100
  * J8165-250
  * J8165-500
  * J8365
  * J8565
  * J8565-25
  * L7165
  * L7165-40
  * L7165-100
  * L7165-250
  * L7165-500
  * LR7165-100
  * L7165X
  * L7165X-100
  * L7165X-250
  * L7565
  * L7565-25
  * L7965
  * L7965-100
  * L7993
  * L7993-25
  * LR7165
  * LR7165-100
