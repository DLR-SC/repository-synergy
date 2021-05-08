alchemyapi-recipes-twitter
==========================

Welcome to the AlchemyAPI Twitter analysis recipe!

For the walkthrough on how this software works, visit: http://www.alchemyapi.com/developers/getting-started-guide/twitter-sentiment-analysis/

In short, this recipe will:
- Connect to Twitter's API
- Run a search and gather Tweets
- Enrich Tweets with sentiment analysis of the message body
- Store data in a MongoDB instance
- Visualize sentiment of the data

#### Related Links ####

- For more information on AlchemyAPI's sentiment analysis API: http://www.alchemyapi.com/products/features/sentiment-analysis/
- For more information on Twitter's API: https://dev.twitter.com/rest/public
- For more information on MongoDB: http://www.mongodb.org/
- For more information on R: http://www.r-project.org/

## Requirements ##
- An API key from AlchemyAPI -- register for one at: http://www.alchemyapi.com/api/register.html
- Credentials for Twitter API -- the Consumer Key and Consumer Secret (create a new application at: https://dev.twitter.com/apps)
- An installation of MongoDB -- http://www.mongodb.org/downloads
- An installation of R, and the "ggplot2" package -- see e.g., http://cran.cnr.berkeley.edu/ and http://www.r-bloggers.com/installing-r-packages/

### Quick start for users running Ubuntu 14.04 
Here is a simple set of commands that will ensure you have all the necessary
tools and modules needed to successfully run this recipe:

```bash
sudo easy_install pymongo datetime
sudo apt-get update
sudo apt-get install r-base-dev
sudo R
R> install.packages("ggplot2")
R> <Ctrl-D>
sudo apt-get install mongodb-org
# Starting your MongoDB daemon
# Alternatively, run as root: service mongodb start
mkdir -p data/db
mongod --dbpath data/db --smallfiles --quiet &
```
## STEP 1: Gather and enrich the data ##

To run this tool, simply call with a search term and an integer reflecting
the number of Tweets to analyze:

```bash
python recipe.py "<SEARCH_TERM>" <NUM_TWEETS>
```

- **Credentials**:
    You must have API credentials for both Twitter and AlchemyAPI to successfully
    run this tool. Edit the file credentials.py before executing recipe.py to 
    prevent any errors. Inside the file `credentials.py`, there are three
    parameters. Replace each of these with your respective values to run the analysis smoothly:
    

    ```bash
    twitter_consumer_key='YOUR_TWITTER_CONSUMER_KEY' 
    twitter_consumer_secret='YOUR_TWITTER_CONSUMER_SECRET'
    alchemy_apikey='YOUR_ALCHEMY_API_KEY'
    ```


- **Dependencies** (see above for installation tips):
  - `pymongo` Python module: install with `easy_install`
  - `mongodb`: install with `apt-get` (Ubuntu) or check here: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/


## STEP 2: Visualize the data

With your MongoDB instance created and filled, you now have access to well-tabulated results! We can proceed
with some Python and R scripts to write results to disk and visualize them.

- **Write your data**:
    Here, we will write two types of files: one containing the raw scores of sentiment for each Tweet, and
    one containing timestamps for each Tweet. We will do this separately for positive and negative Tweets.
    To write these files, just call:

    ```bash
    $> python write.py
    ```

    This will result in a total of 4 text files being written: *scores.pos*, *scores.neg*, *times.pos*, and *times.neg*.

- **Dependencies**:
    This tool requires the `pymongo` Python module, as well as the `datetime` module (see above).

- **Visualize your data**:
    Here, we want to make some plots showing the data we wrote out in the previous steps. 
    To do this, simply invoke the included R script as follows:

    ```bash
    R < plot.R --vanilla
    ```
    
    This tool will write 3 image files to disk: 
  - *twitter_sentiment_raw.png*: a histogram showing the positive and negative Tweet scores
  - *twitter_sentiment_kernel.png*: a kernel density function corresponding to the above histograms
  - *twitter_sentiment_volume.png*: a plot showing Tweet volume (separated by sentiment) as a function
                                        of the hour in a day

- **Dependencies**:
  - You must have R installed on your system to run this tool.
  - You must also install the 'ggplot2' library for R (see above). 

## STEP 3: (OPTIONAL) Delete your data

From time to time, it's good to empty out your cache! If you want to wipe
the `twitter_db` instance in MongoDB that was created in STEP 1, run the following command:

```bash
python delete.py
```


