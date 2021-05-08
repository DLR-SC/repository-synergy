#Overview
Here's another library based on the LinkedIn API, OAuth and JSON responses.

Hope this documentation explains everything you need to get started. Any questions feel free to email me or inbox me.

#Install through pip...
```
pip install linkedin
```

If `linkedin` is already installed, pass `-I` to your install:
```
pip install -I linkedin
```

#Import LinkedIn library
```
from linkedin import *
```

#Authorization URL

*Get an authorization url for your user*

```python
l = LinkedinAPI(api_key='*your app key*',
              api_secret='*your app secret*',
              callback_url='http://www.example.com/callback/',
              permissions=["r_network"])

auth_props = l.get_authentication_tokens()
auth_url = auth_props['auth_url']

#Store this token in a session or something for later use in the next step.
oauth_token_secret = auth_props['oauth_token_secret']

print 'Connect with LinkedIn via: %s' % auth_url
```
If you leave callback_url blank, you can get the oauth_verifier from the web browser. It is a five-digit integer.

The permissions parameter is optional. It can be a list or string. The [list of permissions](https://developer.linkedin.com/documents/authentication) is in the LinkedIn API documentation.

Once you click "Allow" be sure that there is a URL set up to handle getting finalized tokens and possibly adding them to your database to use their information at a later date. \n\n'

#Handling the callback
```python
# In Django, you'd do something like
# oauth_token = request.GET.get('oauth_token')
# oauth_verifier = request.GET.get('oauth_verifier')

oauth_token = *Grab oauth token from URL*
oauth_verifier = *Grab oauth verifier from URL*

#Initiate the LinkedIn class in your callback.
l = LinkedinAPI(api_key='*your app key*',
              api_secret='*your app secret*',
              oauth_token=oauth_token,
              oauth_token_secret=session['linkedin_session_keys']['oauth_token_secret'])

authorized_tokens = l.get_access_token(oauth_verifier)

final_oauth_token = authorized_tokens['oauth_token']
final_oauth_token_secret = authorized_tokens['oauth_token_secret']

# Save those tokens to the database for a later use?
```

#Getting some user information, search results, network updates.
```python
# Get the final tokens from the database or wherever you have them stored

l = LinkedinAPI(api_key = '*your app key*',
              api_secret = '*your app secret*',
              oauth_token=final_tokens['oauth_token'],
              oauth_token_secret=final_tokens['oauth_token_secret'])

# Get your profile information (first name, last name)
profile = l.get('people/~', fields='first-name,last-name')
print profile

# Get search results
search = l.get('people-search', params={'keywords':'Hacker'})
print search

# Get your network updates
feed = l.get('people/~/network/updates')
print feed
```

# POST a network update
```python
share_content = { 
       "comment": "Posting from the API using JSON", 
       "content": { 
               "title": "A title for your share", 
               "submitted-url": "http://www.linkedin.com", 
               "submitted-image-url": "http://lnkd.in/Vjc5ec" 
       }, 
       "visibility": { 
               "code": "anyone" 
       } 
}

share_update = l.post('people/~/shares', params=share_content)
print share_update
```
