Techu v0.2-beta
===============

RESTful search built on top of Sphinx full-text search engine. 

- Organize your Sphinx configurations with Techu database schema
- Re-use index and searchd parameters
- Automatically regenerate configurations and restart searchd
- Easy & efficient document indexing using HTTP calls and passing data in JSON format
- Asynchronous execution of statements using Redis as a buffer
- Bulk insert feature for fast index rebuilding
- Perform full-text search fast using JSON to provide attribute filters, sorting parameters and grouping
- Retrieve highlighted excerpts (snippets) from documents, compliant with the search query syntax
- Cache search results and excerpts directly to Redis

## Components ##

* Realtime indexes
* Django Framework
* Nginx web server
* Redis in-memory key-value storage
* MySQL

Take a look at the [overview page](http://techusearch.org).

-----

Still a beta version and requires a lot of work to be done (and much more documentation as well, especially regarding the */search* request!). I am also preparing some benchmarks. I would be very thankful for any constructive criticism and anyone willing to test it!

Stay tuned!


