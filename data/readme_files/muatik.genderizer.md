Genderizer
======================

Genderizer is a language independent module which tries to detect gender by looking at given first names and/or analyzing sample texts. 

***Always remember***:

> Data-driven predictions can succeed --and they can fail. It is when we
> deny our role in the process that the odds of failure rise. Before we
> demand more of our  data, we need to demand more of ourselves.
> -- The Signal and The Noise by Nate Silver

##Installation
You can install this package using the following ```pip``` command:

```sh
$ sudo pip install genderizer
```


##Examples

```python
from genderizer.genderizer import Genderizer

print Genderizer.detect(firstName = 'John')
# >>> male

print Genderizer.detect(firstName = 'Marry')
# >>> female

print Genderizer.detect(firstName = 'mustafa')
# >>> male

print Genderizer.detect(firstName = 'fatma')
# >>> female

print Genderizer.detect(firstName = 'fikret')
# >>> None

print Genderizer.detect(firstName = 'fikret', text='galatasary maçı kaçmaz')
# >>> male

print Genderizer.detect(firstName = 'fikret', text='annemlerle yemek yedik')
# >>> female

print Genderizer.detect(text='askerlik yoklamasını kaçırdım mk')
# >>> male

print Genderizer.detect(text='bana çiçek alan erkek için canım feda')
# >>> female

print Genderizer.detect(firstName='fatma', text='askerlik yoklamasını kaçırdım mk')
# >>> female

print Genderizer.detect(text='futbol sevgi')
# >>> None

print Genderizer.detect(text='lan bi siktir git')
# >>> male

```
***Note***: You may claim that women can say ```lan bi siktir git```, of course. But the probability of being female is less than the probability of being male according to the trained data of the classifier.

So it is obvious that the success of detection depends on the trained data.

By the way, in Turkish saying 'lan bi siktir git' makes you quite rude.


## How It Works
Genderizer is a module which tries to detect gender by looking given first names and/or analyzing sample text of a person. 

If a first name is definitely used for only one gender, the system will accept this gender and will not make any further analysis. For example, while 'Mustafa', 'Osman', 'Hasan' is used in Turkish only for male; 'Fatma', 'Ceyda', 'Elif' only for female.

When looking at first names does not infer any gender for sure, the system will make text analysis if it is given. For example; 'Ekim', 'Meric', or 'Tümay' is used for both male and female.

The text analysis is the classification of sample texts. It simply try to compute the probability of being male or female mining the sample text. In this system Naive Bayesian Classification is adopted and [naiveBayesClassifier][1] is used.

## How To Improve It
TODO: write a step by step guide

##Preparing Language Dependent Training Sets
TODO: give a few examples

## Customization and Optimization

### Using Memcached For Speed
```python
"""
Under heavy usage, for example tens of thousands detection request
in a few seconds the default configuration could not meet the
demand. By the default configurations, genderize will load necessary
data from files and this is well known to be slow. Instead of each
time loading data into memory, doing this one time will be clever
approach. One of the best way of this approach is to use memcached.
For more information have a look at the documentation of memcached.

Genderizer provides a memcached interface to store first names in 
memory. To active this interface, you need to instantiate 
memcachedNamesCollection interface and pass it to genderizer while 
initializing it.
"""

from genderizer.memcachedNamesCollection import MemcachedNamesCollection

#For memcached, do not forget to setup the memcached server.
MemcachedNamesCollection.memcacheHost = '127.0.0.1:11211'
Genderizer.init(
    namesCollection=MemcachedNamesCollection
)
print Genderizer.detect(firstName = 'John')
```

### Using Mongodb
```python
"""
If you want to use Genderize on Mongodb for arbitrary reasons, the
MongoNamesCollection first names collection interface will do much
of the necessary works for you.
"""
from genderizer.mongoNamesCollection import MongoNamesCollection

MongoNamesCollection.mongodbURL = 'mongodb://192.168.1.170'
Genderizer.init(
    namesCollection=MongoNamesCollection
)
print Genderizer.detect(firstName = 'Marry')

```

### Custom Text Classifier
```python
"""
NaiveBayesClassifier is adopted as the default classifier. But you
can use another, entirely different classifier; as long as the
classifier has a 'classify' method taking text as a parameter.

For more information please have a look at the naiveBayesClassifier
project's documentation.
https://github.com/muatik/naive-bayes-classifier
"""

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.classifier import Classifier
from cachedModel import CachedModel

Genderizer.init(
    lang='en',
    classifier=Classifier(CachedModel.get('en'), tokenizer)
)

print Genderizer.detect(firstName = 'fikret', text='annemle kahve keyfi')
```


## TODO
* inline docs
* unit-tests

## AUTHORS
* Mustafa Atik [@muatik][2]
* Nejdet Yucesoy @nejdetckenobi


  [1]: https://github.com/muatik/naive-bayes-classifier
  [2]: https://twitter.com/muatik2