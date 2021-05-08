Wikipedia NER
-------------

Tool to train and obtain named entity recognition labeled examples
from Wikipedia dumps.

Usage in [IPython notebook](http://nbviewer.ipython.org/github/JonathanRaiman/wikipedia_ner/blob/master/Wikipedia%20to%20Named%20Entity%20Recognition.ipynb) (*nbviewer* link).

## Usage

Here is an example usage with the first 200 articles from the english wikipedia dump (dated lated 2013):

	parseresult = wikipedia_ner.parse_dump("enwiki.bz2",
                            max_articles = 200)
    most_common_category = wikipedia_ner.ParsedPage.categories_counter.most_common(1)[0][0]

    most_common_category_children = [
			parseresult.index2target[child] for child in list(wikipedia_ner.ParsedPage.categories[most_common_category].children)
			]
	
	"In '%s' the children are %r" % (
		most_common_category,
		", ".join(most_common_category_children)
		)

	#=> "In 'Category : Member states of the United Nations' the children are 'Afghanistan, Algeria, Andorra, Antigua and Barbuda, Azerbaijan, Angola, Albania'"