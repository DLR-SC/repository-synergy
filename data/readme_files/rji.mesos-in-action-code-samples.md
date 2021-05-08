# Mesos in Action
This repository contains supplementary code for the book "Mesos in Action",
written by Roger Ignazio and published by Manning Publications.

<http://www.mesosinaction.com>

## How this repository is organized
In this repo, I've organized specific code samples into directories based on
the chapters and appendices in the book. Each directory contains its own README
which provides additional details about how to use each of the files contained
within.

In a few cases, there are some examples that aren't organized by chapter. These
include:

  * keys-values-app
  * output-env-app
  * wordcount-example
  * email-weather-forecast.py

These examples are included at the top level of this repository because they
are, or can be, used with topics and projects covered in multiple chapters.

## License
The contents of this repository are licensed under the MIT License. See the
included [LICENSE](LICENSE) file at the root of this repository.

## Releases
The `master` branch of this repo will always contain the latest changes, which
may or may not map to a currently-released version of Mesos In Action.

Tagged releases will follow published versions of the books using a
[Semantic Versioning][semver]-like approach:

    EDITION.UPDATE.FIX

EDITION and UPDATE will only be incremented when a new version of the book
itself is warranted. Otherwise, trivial changes to code, configurations,
and/or examples (due to bugs, enhancements, etc) will increment the value of
FIX.

[semver]: http://semver.org/
