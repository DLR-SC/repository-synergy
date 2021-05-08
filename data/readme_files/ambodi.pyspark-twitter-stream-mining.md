## Real-Time Twitter Mining with Apache Spark (PySpark)

### Motivation
I love python and I love Machine Learning, specially in real-time. Up to now, Apache Spark does not have any Twitter Stream integration, so I put up a little workaround to be able to use spark on twitter data. Even better, I integrated the result into visualizations. So far, there is only a d3 wordcloud but I am planning to add more.

### Getting Started
* Install Docker and Docker-compose
* Install Python and Pip
* Install dependecies: ```pip install psutil``` && ```pip install tweepy``` && ```pip install websockets```
* Make sure you have Apache Spark installed. This repo works with spark-1.5.1-bin-hadoop2.6 verison perfectly. After that, you just need to remember where you extracted spark, we call it ```$SPARK_HOME```, Ogey?
* Get your API keys from [https://dev.twitter.com/](Twitter Developers) and put them in ```data/config.json```.
* set `docker` in your `etc/hosts` to point to your machine

### How to Run the Example?
First, run the Kafka server with the following command:

```bash
docker-compose up

```
Then, fire up the stream source:


```bash
python twitter_stream.py
```


Now submit the ```trending_keywords_sparkjob.py``` to ```spark-submit```:

```bash
$SPARK_HOME/bin/spark-submit --jars jar/spark-streaming-kafka-assembly_2.10-1.5.1 sparkjob.py
```

You will start to see the most frequently used words in the tweets from your opened stream like this: 

```bash
-------------------------------------------
Time: 2015-12-18 21:11:17
-------------------------------------------
(u'python', 461)
(u'url', 282)
(u'#python', 125)
(u'user', 102)
(u'como', 70)
(u'de', 59)
(u'con', 43)
(u'monty', 42)
(u'este', 36)
(u'culebra', 35)
...
```

After that, you are gonna have a stateful count of all realtime feed of twitter stream with most used words (stop words and non-alpha numeric words are striped). The log will show you the top 10 words sorted by number of appearence. Note that spark will create a folder called ```twitter-checkpoint``` to keep state of the application and puts some rules for failover computation there.


You should see the most frequent words in Tweets that have ```Python``` in them. Why Python? Becuase it's awesome! For now, change the query [here](https://github.com/ambodi/realtime-spark-twitter-stream-mining/blob/master/tweet.py#L19). Also, [change the `topic` in the Kafka example] ().

###Real-time D3.js WordCloud

First, make sure that all the previous steps are running simultaneously. Then:

```bash
cd html

bower install

python -m SimpleHTTPServer 9000
```
Go to [http://localhost:9000]() and see the running wordcloud updating every 10 seoncds.


###Share & Support 
Please help me make this repo a better project by sharing your ideas, forks, creating issues and features you need, I will appreciate any feedbacks. Send me a tweet at [https://twitter.com/_ambodi](_ambodi @ Twitter ).

###License
See the LICENSE file for license rights and limitations (MIT).
