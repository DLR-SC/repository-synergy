## django-devrecargar ##
During the development of a Django application, do you get tired of:

1. Making a change to source code
1. Alt-tab to your browser
1. Refresh
1. Rinse and repeat

This project aims to make you more productive by keeping you in the text editor by automatically refreshing the browser after any file modification within your Django project (even CSS, JS or HTML).

#### Why devrecargar over other solutions? ####
1. Python only
1. No browser plugins
1. Easier for remote workflows where you are SSH'ed into a development server making changes but viewing the site with a browser on your local PC.

### Installation ###
    
    pip install devrecargar

### Usage ###
1. Add `devrecargar` to `INSTALLED_APPS` in `settings.py`
1. Add an entry to `urls.py`:

        url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar'))
1. Add a javascript snippet to a base template:

         <script>{% include "devrecargar/devrecargar.js" %}</script>

### Configuration ###
devrecargar looks for `BASE_DIR` within `settings.py` as the default directory to recursively watch for file changes. If `BASE_DIR` doesn't exist then you need to set `DEVRECARGAR_PATHS_TO_WATCH` within `settings.py`. This should be a list of dictionaries like so:

       DEVRECARGAR_PATHS_TO_WATCH = [{
            'path': <an absolute path you want to watch>,  # required
            'recursive': True,  # not required, default is shown here
            'patterns': ['*.html', '*.js', '*.css']  # not required, default is shown here
            'ignore_directories': True,  # not required, default is shown here
       }]
        
If devrecargar doesn't find either of these variables then `django.core.exceptions.ImproperlyConfigured` will be raised. 

### FAQ ####
#### How It Works ####
The javascript snippet makes a Server-Sent Event (SSE) request to the Django devserver. Anytime the devserver process restarts the SSE request is disconnected within the browser and it will try to automatically reconnect. SSE will send an `open` event after the browser re-establishes the connection to the devserver after it's been restarted.  The javascript snippet listens for the `open` event and issues a `location.reload()` that refreshes the browser.

After modifying a python file the devserver restarts automatically.  To get CSS, JS, HTML support we use the [watchdog](http://pythonhosted.org/watchdog/) module to listen for any file modifications. When a `watchdog` modification event happens an `__init__.py` file within the devrecargar project is "touched" which the devserver process notices because it's a python file and restarts itself, which triggers the SSE `open` event to fire.

#### How can I keep this out of my production environment? ####
* In the HTML template wrap the javascript snippet in a `debug` conditional. 

	    {% if debug %}<script>{% include "devrecargar/devrecargar.js" %}</script>{% endif %}
	    
* You need `django.template.context_processors.debug` added to `TEMPLATE_CONTEXT_PROCESSORS` in `settings.py`. If you don't have `TEMPLATE_CONTEXT_PROCESSORS` defined then by default [Django includes it](https://docs.djangoproject.com/en/1.9/ref/settings/#template-context-processors).
* Be sure your IP address is listed in `INTERNAL_IPS ` within `settings.py`
* In `urls.py` only add the route if `DEBUG=True`
 
        from django.conf import settings
        from django.conf.urls import include, patterns, url
        urlpatterns = patterns()  # all your other routes
        if settings.DEBUG:
            urlpatterns += (
                url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar')
            )

#### Where does the name devrecargar come from? ####
Recargar is Spanish for "reload".
