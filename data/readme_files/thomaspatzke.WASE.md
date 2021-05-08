# WASE

WASE is a shortcut for Web Audit Search Engine. It's a framework for indexing HTTP requests/responses while web
application audits in an ElasticSearch instance and enriching it with useful data. The indexed data can then be searched
and aggregated with ElasticSearch queries or with Kibana.

Currently WASE contains the following parts:

* doc\_HttpRequestResponse.py: a library that implements the DocHTTPRequestResponse class. This class is an
  elasticsearch\_dsl-based storage class of HTTP requests/responses (derived from Burps data structures and API).
* ElasticBurp: a Burp plugin that feeds requests/responses into ElasticSearch.

## ElasticBurp

Scared about the weak searching performance of Burp Suite? Are you missing possibilities to search in Burp? ElasticBurp
combines Burp Suite with the search power of ElasticSearch. It can be installed directly from the [Burp BApp
Store](https://portswigger.net/bappstore/ShowBappDetails.aspx?uuid=67f5c31f93d04ad3a3b0a1808b3648fa).


### Installation

1. Install ElasticSearch and Kibana.
2. Configure both - For security reasons it is recommend to let them listen on localhost:
  * Set `network.host: 127.0.0.1` in `/etc/elasticsearch/elasticsearch.yml`.
  * Set `host: "127.0.0.1"` in `/opt/kibana/config/kibana.yml`.
3. Install dependencies in the Jython environment used by Burp Extender with: `$JYTHON_PATH/bin/pip install -r
   requirements.txt`
4. Load ElasticBurp.py as Python extension in Burp Extender.

Currently there seem to be incompatibilities with the new Python Elasticsearch packages. Specify the 2.2 version when installing
with pip: `$JYTHON_HOME/bin/pip install elasticsearch_dsl==2.2`

### Usage

See [this blog article](https://patzke.org/an-introduction-to-wase-and-elasticburp.html) for usage examples.

## WASEProxy

A generic intercepting HTTP(S) proxy server that stores extracted data into an ElasticSearch index.

Installation with pip: `pip install -r requirements-proxy.txt`

## WASEQuery

Search ElasticSearch indices created by WASE for

* responses with missing headers
* responses with missing parameters
* all values that were set for a header (e.g. X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, Content-Security-Policy, ...)

...or do arbitrary search queries.

Invoke WASEQuery.py for help message. [This blog
article](https://patzke.org/analyzing-web-application-test-data-with-wasequery.html) shows some examples for usage of
WASEQuery.
