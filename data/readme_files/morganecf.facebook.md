# facebook
Be the master of your own private Facebook data. 

### get_friends.py

Get all of your friend's Facebook user ids from your messaging history. 

```
Usage: python get_friends.py username password output_file
```
 
The output has the following format: id \t name \t username 

This script uses a browser automation library and the Phantom JS browser.
+ brew install phantomjs 
+ pip install splinter 

### collect_conversations.py
Downloads your entire Facebook messaging history. 

```
Usage: python collect_conversations.py username password your_facebook_id friend_file output_dir 
```
You can find your Facebook ID by digging in the HTML. This script will store each conversation in a .txt file named after your friend's username, in the provided output directory. This script also takes as input a tab-delimited file containing your friends' user ids, names, and usernames. You can manually compile this or generate it using the get_friends.py script.  
