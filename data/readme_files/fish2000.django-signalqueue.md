[![Build Status](https://travis-ci.org/fish2000/django-signalqueue.png?branch=master)](https://travis-ci.org/fish2000/django-signalqueue)

django-signalqueue
==================

After a certain amount of time anyone concerning themselves with the Django framework is going
to ask the question: *I love Django's signals, indeed. But if only I could dispatch them asynchronously.
Like, on some other thread or something, I don't really know.... Is that somehow possible?*

Well, now you can easily do that! One contrived yet demonstrative example of such is this:
you want to update an event log in your app when a user saves a form, but the update function you wrote does some gnarly aggregation so you can see each datum reflected in real-time. If you call it in a view it beachballs
both the running app process and your users' patience.

That's where django-signalqueue comes in. After you set it up, this is all you need to do:


    # yourapp/signals.py

    from signalqueue import dispatch
    from yourapp.logs import inefficient_log_update_function as log_update

    form_submit = dispatch.AsyncSignal(
        providing_args=['instance'])            # define an asynchronous signal

    form_submit.connect(log_update)             # doesn't have to be right here, as long
                                                # as it runs when the app starts up

Now you can call the function in a view without blocking everything:

    # yourapp/views.py

    from yourapp import signals, models

    def process_form(request):
        pk = save_user_form(request)            # your logic here
        obj = models.MyModl.objects.get(pk=pk)
        signals.form_submit.send(instance=obj)  # returns quickly!
        return an_http_response_object          # eventually return an HttpResponse


Django-signalqueue sticks to Django's naming and calling conventions for signals. It gets out of your
way and feels familiar, while granting you the power of async calls.


With django-signalqueue, asynchronous dispatch is not even a thing &mdash; that's how easy it is.
=================================================================================================

Setting It Up
-------------

Watch, I'll show you. First, install django-signalqueue:

    $ pip install django-signalqueue                                # pulls in tornado and django-delegate, if need be

... you may also want some of these optional packages, if you don't have them already:

    $ brew install redis                                            # s/brew/apt-get/ to taste
    $ pip install redis hiredis                                     # recommended
    $ pip install ujson                                             # recommended
    $ brew install yajl && pip install czjson yajl simplejson       # these work too
    $ pip install nose rednose django-nose                          # for the tests

Add django-signalqueue to your `INSTALLED_APPS`, and the settings for a queue, while you're in your `settings.py`:

    # settings.py

    INSTALLED_APPS = [
        'signalqueue', # ...
    ]

    SQ_QUEUES = {
        'default': {                                                # a 'default' queue in SQ_QUEUES is required
            'ENGINE': 'signalqueue.worker.backends.RedisSetQueue',  # also required - the queue's driver
            'INTERVAL': 30,                                         # required - the polling interval (30 <= ~1/3 sec)
            'OPTIONS': dict(),
        },
    }
    SQ_RUNMODE = 'SQ_ASYNC_REQUEST'                                 # use async dispatch by default
    SQ_WORKER_PORT = 11231                                          # port to which the worker process binds

Besides all that, you just need a call to `signalqueue.autodiscover()` in your root URLConf:

    # urls.py

    import signalqueue
    signalqueue.autodiscover()

Now you can define async signals!
---------------------------------

Asynchronous signals are instances of `signalqueue.dispatch.AsyncSignal` that you've defined in one of the following places:

* `your_app/signals.py` (it's fine if you already use this file, as many do)
* Modules named in a `settings.SQ_ADDITIONAL_SIGNALS` list or tuple
* *Coming soon:* `signalqueue.register()` *-- so you can put them anywhere else.*

AsyncSignals are subclasses of the familiar `django.dispatch.Signal` class. As such, you define AsyncSignals much like the Django signals you know and love:

    # yourapp/your_callbacks.py

    # the callback definition can go anywhere
    def callback(sender, **kwargs):
        print "I, %s, have been hereby dispatched asynchronously by %s, thanks to django-signalqueue." % (
            str(kwargs['instance']),
            sender.__name__)


    # yourapp/signals.py

    from signalqueue.dispatch import AsyncSignal
    from yourapp.your_callbacks import callback

    my_signal = AsyncSignal(providing_args=['instance'])                # the yuge.

    # while you can put your callbacks anywhere, be sure they're connect()-ed to your signals in
    # yourapp/signals.py or another module that loads when the app starts (e.g. models.py)

    my_signal.connect(callback)

At the time of writing, arguments specified the providing_args list are assumed to be Django model instances.
django-signalqueue serializes model instances by looking at:

* the app name - `obj._meta.app_label`,
* the model's class name - `obj.__class__.__name__.lower()`,
* and the object's primary key value - `obj.pk`.

You can define mappings for other object types (the curious can have a look in `signalqueue/mappings.py` for
how that works) -- this part of the API is currently in flux as we're working towards the simplest,
programmer-user-friendliest, most-dependency-unshackled method of implementation for the type stuff.

BUT SO ANYWAY. To start up a worker, use the management command `runqueueserver`:

    $ python ./manage.py runqueueserver localhost:2345
    +++ django-signalqueue by Alexander Bohn -- http://objectsinspaceandtime.com/

    Validating models...0 errors found

    Django version 1.4 pre-alpha SVN-16857, using settings 'settings'
    Tornado worker for queue "default" binding to http://127.0.0.1:11231/
    Quit the server with CONTROL-C.
    2011-09-30 15:25:21,098 [INFO] signalqueue: Dequeueing signal: None
    2011-09-30 15:25:21,400 [INFO] signalqueue: Dequeueing signal: None
    2011-09-30 15:25:21,701 [INFO] signalqueue: Dequeueing signal: None
    [... et cetera, ad nauseum]


The `runqueueserver` process will sit in the foreground and blurt its output to stdout every time it polls
the queue (in ANSI color!) which is handy for debugging your setup.

Once you've got a worker process running, you can fire one of your signal asynchronously like so:

    >>> from yourapp.signals import my_signal
    >>> my_signal.send(sender=AModelClass, instance=a_model_instance)

send() returns immediately after enqueueing the call, which is pushed onto a stack. The worker process,
running in its own process, pops any available signals off the stack and executes them in its own instance
of your Django app.

You can fire async signals synchronously using send_now() -- the call will block until all of the connected
callback handlers return (just like a call to a standard signals' send() method):

    >>> my_signal.send_now(sender=AModelClass, instance=a_model_instance)
    >>> my_signal.send_now(instance=a_model_instance)

As with `django.dispatch.Signal.send()`, the sender kwarg is optional if your callback handlers don't expect it.

*Tune in tomorrow for the astonishing conclusion of... the django-signalqueue README!!!!!!*


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/fish2000/django-signalqueue/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

