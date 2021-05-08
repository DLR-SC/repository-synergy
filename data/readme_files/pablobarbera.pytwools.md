`pytwools`: python tools for the analysis of Twitter data
=======

This repository contains a series of scripts I often use to analyze Twitter data in JSON format or in MongoDB collections. Usage examples are provided below. To collect your own dataset of tweets, see my tutorial on how to use my R package, `streamR`, [here](https://github.com/pablobarbera/streamR).

# Usage examples

## `print-tweets.py`

Prints basic information about tweets in console

```
## prints text of first 10 tweets
python print-tweets.py -o text -f tweets.json -k 10  
## prints coordinates and text of first 10 geolocated tweets
python print-tweets.py -o geo -f tweets.json -k 10 

```

## `top-tweets.py`

Computes summary statistics about top tweets, users, hashtags

```
## find 10 most retweeted tweets (>25 RTs)
## (only automatic retweets)
python top-tweets.py -v retweets -f tweets.json -k 10 -n 25

## find 10 most active users (>5 tweets)
python top-tweets.py -v users -f tweets.json -k 10 -n 5

## find 10 most used hashtags
python top-tweets.py -v hashtags -f tweets.json -k 10

```

## `tweets-to-mongo.py`

Parses tweets in json and exports to a Mongo DB collection, adding extra fields for faster querying

```
### import tweets from file "tweets.json"
python tweets-to-mongo.py -f tweets.json -host localhost -u "" -pwd "" -db tweets -c example -b False

### import tweets from file "tweets.json" in batches of 1000 (faster for larger json files)
python tweets-to-mongo.py -f tweets.json -host localhost -u "" -pwd "" -db tweets -c example -b True

```


## `export-user-list.py`

Exports user information from a MongoDB tweet collection, after filtering tweets by date and users according to their number of friends/followers

```
### export users who tweeted between January 1st, 2014 and April 15
### who have 50+ followers and 100+ friends
python export-user-list.py -host localhost -db tweets -c example -o 'users.csv' \
    -minfollowers 50 -minfriends 100 -mindate 2014-01-01 -maxdate 2014-04-15

```

## `export-network-data.py`

Exports nodes and edges from tweets (either from retweets or mentions) in json format, and saves them in a file format compatible with Gephi

```
### extract retweet nodes and edges
python export-network-data.py -f tweets.json -et retweets -oe edges.csv -on nodes.csv
### extract mention edges
python export-network-data.py -f tweets.json -et mentions -oe edges.csv -on nodes.csv

```

## `subset-geolocated-tweets.py`

Takes a large file with geolocated tweets and returns another file with tweets sent from within a given bounding box

```
### extract retweets sent from Scotland
python subset-geolocated-tweets.py -f 'geotweets.json' -o 'scotland-tweets.json' \ 
    -swlat 54.184 -swlong -5.734 -nelat 59.03 -nelong 1.120

```


## `count-tweets.py`

Counts number of tweets over time, either from a file in json format, or from a MongoDB collection of tweets

```
## count tweets in a file (tweets in json format), by minute
python count-tweets -f tweets.json -t minute

## count tweets in a file (tweets in json format), by hour
python count-tweets.py -f tweets.json -t hour

## count tweets in a MongoDB collection, by minute
python count-tweets.py -host localhost -db tweets -c example -t minute

```






