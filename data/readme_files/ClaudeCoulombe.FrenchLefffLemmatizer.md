# French LEFFF Lemmatizer

### Introduction

A French Lemmatizer in Python based on the LEFFF (Lexique des Formes Fléchies du Français / Lexicon of French inflected forms) is a large-scale morphological and syntactic lexicon for French. A lemmatizer retrurns the lemma or more simply the dictionary entry of a word, In French, the lemmatization of a verb returns this verb to the infinitive and for the other words, the lemmatization returns this word to the masculine singular.

### Main reference

Sagot (2010). The Lefff, a freely available and large-coverage morphological and syntactic lexicon for French. 
In Proceedings of the 7th international conference on Language Resources and Evaluation (LREC 2010), Istanbul, Turkey.
Retrieved from [Benoît Sagot Webpage about LEFFF](http://alpage.inria.fr/~sagot/lefff-en.html)

In this project, we use the morphological lexicon only: 
.mlex file which has a simple format in CSV (4 fields separated by `\t`)

[LEFFF download hyperlink](https://gforge.inria.fr/frs/download.php/file/34601/lefff-3.4.mlex.tgz)

[Tagset](http://alpage.inria.fr/frmgwiki/content/tagset-frmg) format FRMG - from the ALPAGE project since 2004

### License

Copyright (C) 2017-2020 Claude COULOMBE

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).

> **Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.**

### Installation

1. Make sure pip is installed (https://packaging.python.org/tutorials/installing-packages/)<br/>
2. Then you can install FrenchLefffLemmatizer:<br/>
`> pip install git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git`

> ***Warning: Run under Python 3.X but could run with small modifs with Python 2.7X***

### Usage

Import

``` Python
>>> from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
```

Constructor parameters:

* **with_additional_file**: Allows to load LEFFF without the additional file. (Default: True)
* **load_only_pos**: Allows to load LEFFF with only some pos tags, WordNet pos tags [a, r, n, v]. (Default: all)

Example with default constructor
``` Python
>>> lemmatizer = FrenchLefffLemmatizer()
>>> lemmatizer.lemmatize('avions')
avion
>>> lemmatizer.lemmatize('avions','n')
avion
>>> lemmatizer.lemmatize('avions','v')
avoir
>>> lemmatizer.lemmatize('avions','all')
[('avion', 'nc'), ('avoir', 'auxAvoir'), ('avoir', 'ver')]
>>> lemmatizer.lemmatize('vous','all')
[('se', 'clr'), ('le', 'cla'), ('lui', 'pro'), ('il', 'cln'), ('lui', 'cld')]
>>> lemmatizer.lemmatize('la','all')
[('la', 'nc'), ('le', 'det'), ('le', 'cla')]
```

Additional example with parameters
``` Python
>>> lemmatizer = FrenchLefffLemmatizer(with_additional_file=False, load_only_pos=['n', 'a'])
>>> lemmatizer.lemmatize('avions')
avion
>>> lemmatizer.lemmatize('avions','n')
avion
>>> lemmatizer.lemmatize('avions','all')
[('avion', 'nc')]
```

