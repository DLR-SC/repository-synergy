# Pyfb - A Python Interface to the facebook Graph API

### This is an Easy to Use Python Interface to the Facebook Graph API

It gives you methods to access your data on facebook and
provides objects instead of json dictionaries!


## Django Facebook Integration Using Pyfb

It's easy to integrate pyfb with Django. Just see the following example:

### settings.py

```python

# Facebook related Settings
FACEBOOK_APP_ID = 'YOUR_APP_ID'
FACEBOOK_SECRET_KEY = 'YOUR_APP_SECRET_CODE'
FACEBOOK_REDIRECT_URL = 'http://www.YOUR_DOMAIN.com/facebook_login_success'

```

### views.py

```python

from pyfb import Pyfb
from django.http import HttpResponse, HttpResponseRedirect

from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY, FACEBOOK_REDIRECT_URL

def index(request):
    return HttpResponse("""<button onclick="location.href='/facebook_login'">Facebook Login</button>""")

#This view redirects the user to facebook in order to get the code that allows
#pyfb to obtain the access_token in the facebook_login_success view
def facebook_login(request):

    facebook = Pyfb(FACEBOOK_APP_ID)
    return HttpResponseRedirect(facebook.get_auth_code_url(redirect_uri=FACEBOOK_REDIRECT_URL))

#This view must be refered in your FACEBOOK_REDIRECT_URL. For example: http://www.mywebsite.com/facebook_login_success/
def facebook_login_success(request):

    code = request.GET.get('code')

    facebook = Pyfb(FACEBOOK_APP_ID)
    facebook.get_access_token(FACEBOOK_SECRET_KEY, code, redirect_uri=FACEBOOK_REDIRECT_URL)
    me = facebook.get_myself()

    welcome = "Welcome <b>%s</b>. Your Facebook login has been completed successfully!"
    return HttpResponse(welcome % me.name)

```

### urls.py

```python

urlpatterns = patterns('',

    (r'^$', 'djangoapp.django_pyfb.views.index'),
    (r'^facebook_login/$', 'djangoapp.django_pyfb.views.facebook_login'),
    (r'^facebook_login_success/$', 'djangoapp.django_pyfb.views.facebook_login_success'),
)

```


## Integration with JS SDK

You can also use the JS SDK for the facebook login (without making a redirection to facebook, just by opening a popup login window) and Pyfb for backend api calls. Here is how to do it:

### index.html

```html

<html>
    <head>

    </head>
    <div id="fb-root"></div>
    <script>

        function isConnected(response) {
            return response.status == 'connected';
        }

        function getLoginStatus(FB) {

            FB.getLoginStatus(function(response) {

                if (isConnected(response)) {
                    onLogin(response);
                }
                else {
                    FB.login(onLogin);
                }
            });
        }

        function onLogin(response) {

            if (isConnected(response)) {
                location.href = '/facebook_javascript_login_sucess?access_token=' + response.authResponse.accessToken;
            }
        }

        window.fbAsyncInit = function() {

            FB.init({
                appId      : '{{FACEBOOK_APP_ID}}',
                channelUrl : 'http://localhost:8000/media/channel.html',
                status     : true,
                cookie     : true,
                xfbml      : true,
                oauth      : true,
            });

        };

        (function(d){
             var js, id = 'facebook-jssdk'; if (d.getElementById(id)) {return;}
             js = d.createElement('script'); js.id = id; js.async = true;
             js.src = "http://connect.facebook.net/en_US/all.js";
             d.getElementsByTagName('head')[0].appendChild(js);
        }(document));

    </script>

    <body>
        <button onclick="location.href='/facebook_login'">Facebook Python Login</button><br/><br/>
        <button onclick="getLoginStatus(FB)">Facebook Javascript Login</button>
    </body>
</html>

```

### views.py

```python

from pyfb import Pyfb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY, FACEBOOK_REDIRECT_URL

def index(request):
    return render_to_response("index.html", {"FACEBOOK_APP_ID": FACEBOOK_APP_ID})


#This view redirects the user to facebook in order to get the code that allows
#pyfb to obtain the access_token in the facebook_login_success view
def facebook_login(request):

    facebook = Pyfb(FACEBOOK_APP_ID)
    return HttpResponseRedirect(facebook.get_auth_code_url(redirect_uri=FACEBOOK_REDIRECT_URL))


#This view must be refered in your FACEBOOK_REDIRECT_URL. For example: http://www.mywebsite.com/facebook_login_success/
def facebook_login_success(request):

    code = request.GET.get('code')

    facebook = Pyfb(FACEBOOK_APP_ID)
    facebook.get_access_token(FACEBOOK_SECRET_KEY, code, redirect_uri=FACEBOOK_REDIRECT_URL)

    return _render_user(facebook)



#Login with the js sdk and backend queries with pyfb
def facebook_javascript_login_sucess(request):

    access_token = request.GET.get("access_token")

    facebook = Pyfb(FACEBOOK_APP_ID)
    facebook.set_access_token(access_token)

    return _render_user(facebook)


def _render_user(facebook):

    me = facebook.get_myself()

    welcome = "Welcome <b>%s</b>. Your Facebook login has been completed successfully!"
    return HttpResponse(welcome % me.name)

```

### urls.py

```python
urlpatterns = patterns('',
    (r'^$', 'djangoapp.django_pyfb.views.index'),
    (r'^facebook_login/$', 'djangoapp.django_pyfb.views.facebook_login'),
    (r'^facebook_login_success/$', 'djangoapp.django_pyfb.views.facebook_login_success'),
    (r'^facebook_javascript_login_sucess/$', 'djangoapp.django_pyfb.views.facebook_javascript_login_sucess'),
)
```

## Facebook paginated lists (Included in version 0.4.0)

```python

from pyfb import Pyfb

(...)
# Do the oauth authentication (see the django example above)
(...)

photos = pyfb.get_photos()

print "These are my photos:\n"
for photo in photos:
    print photo.picture

#Just call the "next" method to get the next page of photos!
more_photos = photos.next()

print "\nMore photos:\n"
for photo in more_photos:
    print photo.picture

more_more_photos = more_photos.next()

print "\nDo you want more?:\n"
for photo in more_more_photos:
    print photo.picture

```
