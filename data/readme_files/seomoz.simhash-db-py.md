Inserting and Querying Simhashes
================================
Rather than take the time to build a data store as described in the Google
paper on efficient simhash querying, we wanted to use an existing database
to accomplish the same thing. To this end, we were willing to take a slight
performance hit to avoid having to spend the development time working on a
more performant solution.

![Status: Production](https://img.shields.io/badge/status-production-green.svg?style=flat)
![Team: Big Data](https://img.shields.io/badge/team-big_data-green.svg?style=flat)
![Scope: External](https://img.shields.io/badge/scope-external-green.svg?style=flat)
![Open Source: Yes](https://img.shields.io/badge/open_source-MIT-green.svg?style=flat)
![Critical: Yes](https://img.shields.io/badge/critical-yes-red.svg?style=flat)

Backends
========
We tried a few backends, including `cassandra`, `mongodb` and `riak`. Because
we have elected to not install the dependencies of all of these clients, you'll
have to make sure you have the appropriate client library (`pycassa`,
`pymongo`, `riak-python-client`) installed before using your selected backend.

Usage
=====
First, you'll have to make a client, providing your chosen backend, the name
of the collection of hashes you'd like to use, the number of blocks you'd like
to use, the threshold for number of differing bits before considering
documents near-duplicates, and any initializing arguments to create that
client (such as a list of servers):

    from simhash_db import Client as Simdbclient

    # Connect to Riak
    client = Simdbclient('riak', name='testing', num_blocks=6, num_bits=3,
        host='...', port=...,)

With a client in hand, you can begin to insert simhashes into the database:

    # Insert a single value
    client.insert(12345)

    # Insert multiple values
    client.insert([12345, 54321, ..., ...])

In some cases, it's only necessary to find a single near-duplicate simhash, in
which case you can `find_one`:

    # Find one near-duplicate hash of my query
    match = client.find_one(12346)

    # If the provided argument is a list, then a list is returned where each
    # position in the resultant array is associated with the corresponding
    # position in the query
    query = [12346, 64321, ..., ...]
    matches = client.find_one(query)

    # This is amenable to turning into a dictionary, for example:
    results = dict(zip(query, matches))

In other cases, where we'd like to find all near-duplicates of a query:

    # Find all near-duplicates of the provided hash
    matches = client.find_all(12346)

    # Same as `find_one`, `find_all` can accept a list argument
    matches = client.find_all([12346, 64321, ..., ...])
