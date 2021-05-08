[![Documentation Status](https://readthedocs.org/projects/solrclient/badge/?version=latest)](http://solrclient.readthedocs.org/en/latest/?badge=latest)

# SolrClient
SolrClient 0.2.2
----------
SolrClient is a simple python library for Solr; built in python3 with support for latest features of Solr 5 and 6. Development is heavily focused on indexing as well as parsing various query responses and returning them in native python data structures. Several helper classes will be built to automate querying and management of Solr clusters.

Enhancements in version 0.2.0:
* Basic parsing for json.facet output
* Better support for grouped results (SolrResponse)
* Other minor enhancements to SolrClient
* Fixed SolrClient.index method

Planned enhancements in version 0.3.0:
* Solr node query routing (by @ddorian)
* Streaming Expressions Support
*

Requirements
----------
* python 3.3+
* requests library (http://docs.python-requests.org/en/latest/)
* Solr
* kazoo for working with zookeeper (optional)


Features
----------
* Flexible and simple query mechanism
* Response Object to easily extract data from Solr Response
* Cursor Mark support
* Indexing (raw JSON, JSON Files, gzipped JSON)
* Specify multiple hosts/IPs for SolrCloud for redundancy
* Basic Managed Schema field management
* IndexManager for storing indexing documents off-line and batch indexing them

Getting Started
----------
Installation:

	pip install SolrClient

Basic usage:

	>>> from SolrClient import SolrClient
	>>> solr = SolrClient('http://localhost:8983/solr')
	>>> res = solr.query('SolrClient_unittest',{
                'q':'product_name:Lorem',
                'facet':True,
                'facet.field':'facet_test',
        })
	>>> res.get_results_count()
	4
	>>> res.get_facets()
	{'facet_test': {'ipsum': 0, 'sit': 0, 'dolor': 2, 'amet,': 1, 'Lorem': 1}}
	>>> res.get_facet_keys_as_list('facet_test')
	['ipsum', 'sit', 'dolor', 'amet,', 'Lorem']
	>>> res.docs
	[{'product_name_exact': 'orci. Morbi ipsum
	..... all the docs ....
	 'consectetur Mauris dolor Lorem adipiscing'}]

See, easy.... you just need to know the Solr query syntax.


Roadmap
----------
* Better test coverage
* Solr Streaming

Contributing
----------
I've realized that that there isn't really a well maintained Solr Python library I liked so I put this together. Contributions (code, tests, documentation) are definitely welcome; if you have a question about development please open up an issue on github page. If you have a pull request, please make sure to add tests and that all of them pass before submitting. See tests README for testing resources.


Documentation:
http://solrclient.readthedocs.org/en/latest/
