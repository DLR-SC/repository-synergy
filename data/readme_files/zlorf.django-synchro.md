==============
django-synchro
==============


Aim & purpose
=============

This app is for synchronization of django objects between databases.

It logs information about objects' manipulations (additions, changes, deletions).
When synchronization is launched, all objects logged from the last checkpoint are synced to another database.

**Important note**: This app doesn't log detailed information about changes (e.g. which fields were updated),
just that such manipulation occured. When the synchronization is performed, the objects are synced with their newest, actual values.
(however, you can specify some fields to be `skipped` during synchronization, see below__).

__ `Skipping fields`_

Example 1
---------

Consider scenario:

- there is one production project deployed on the web
- and the same project is deployed on some office computer in case of main server failure

Assuming that the local database is regularly synced (eg. once a day the main database is exported and imported into the local system),
in case of a long main server downtime the staff may use the local project (inserting objects etc.).

After the server is up again, the local changes (from the point of the last checkpoint) can be painlessly synchronized to the remote server.

Example 2
---------

You can also synchronize databases both ways, not only in the slave-master model like in the previous example.

However, it is probably better (if possible) to have a common database rather than to have
one for every project deployment and to perform synchronization between them.


Requirements
============

The app is tested to work with Django 1.7 - 1.11. If you want to use app in older versions of Django,
use the 0.6 release.

The app needs ``django-dbsettings`` to store the time of last synchronization.

Installation
============

1. Install app (**note**: ``django-dbsettings`` is required and please view its install notes,
   such as `cache backend` important remarks)::

   $ pip install django-synchro

   or download it manually along with dependencies and put in python path.

#. Configure ``DATABASES``.

#. Add ``synchro`` and ``dbsettings`` to ``INSTALLED_APPS``.

#. Specify in your ``settings.py`` what is `remote database` name and which models should be watched and synchronized::

    SYNCHRO_REMOTE = 'remote'
    SYNCHRO_MODELS = (
        'my_first_app', # all models from my_first_app
        ('my_second_app', 'model1', 'model2'), # only listed models (letter case doesn't matter)
        'my_third_app', # all models again
        'django.contrib.sites', # you may specify fully qualified name...
        'auth',                 # or just app label
    )

Later, `REMOTE` will mean `remote database`.


Usage
=====

Synchronization
---------------

Just invoke ``synchronize`` management command::

    $ ./manage.py synchronize

Admin synchro view
------------------

In order to allow performing synchronization without shell access, you can use special admin view.

Include in your urls::

    url(r'^synchro/', include('synchro.urls', 'synchro', 'synchro')),

Then the view will be available at reversed url: ``synchro:synchro``.

The view provides two buttons: one to perform synchronization, and the other to
`reset checkpoint`__. If you would like to disable the reset button, set
``SYNCHRO_ALLOW_RESET = False`` in your ``settings.py``.

Debugging
---------

In order to track a cause of exception during synchronization, set ``SYNCHRO_DEBUG = True``
(and ``DEBUG = True`` as well) in your ``settings.py`` and try to perform synchronization by admin view.

__ Checkpoints_

``SYNCHRO_REMOTE`` setting
--------------------------

Generally, ``SYNCHRO_REMOTE`` setting can behave in 3 different ways:

1. The most naturally: it holds name of `REMOTE` database. When ``synchronize`` is called, ``sychro`` will
   sync objects from `LOCAL` database to `REMOTE` one.
#. When ``SYNCHRO_REMOTE`` is ``None``: it means that no `REMOTE` is needed as ``synchro`` will only store
   logs (see below__). It's useful on `REMOTE` itself.
#. When ``SYNCHRO_REMOTE`` is not specified at all, it behaves just like above (as if it was ``None``), but
   will show a RuntimeWarning.

__ synchro_on_remote_


Remarks and features
====================

QuerySet ``update`` issue
-------------------------

Django-synchro logs information about objects modifications and later use it when asked for synchronization.

The logging take place using the ``post_save`` and ``post_delete`` signal handlers.

That means that actions which don't emmit those signals (like ``objects.update`` method) would result
in no log stored, hence no synchronization of actions' objects.

**So, please remind**: objects modified via ``objects.update`` won't be synchronized unless some special code is prepared
(eg. calling ``save`` on all updated objects or manually invoking ``post_save`` signal).

Natural keys
------------

For efficient objects finding, it is **highly suggested** to provide ``natural_key`` object method
and ``get_by_natural_key`` manager method.
This will allow easy finding whether the synchronized object exists in `REMOTE` and to prevent duplicating.

Although adding ``natural_key`` to model definition is relatively quick, extending a manager may
require extra work in cases when the default manager is used::

    class MyManager(models.Manager):
        def get_by_natural_key(self, code, day):
            return self.get(code=code, day=day)

    class MyModel(models.Model):
        ...
        objects = MyManager()
        def natural_key(self):
            return self.code, self.day

To minimalize the effort of implementing a custom manager, a shortcut is provided::

    from synchro.core import NaturalManager

    class MyModel(models.Model):
        ...
        objects = NaturalManager('code', 'day')
        def natural_key(self):
            return self.code, self.day

Or even easier (effect is exactly the same)::

    from synchro.core import NaturalKeyModel

    class MyModel(NaturalKeyModel):
        ...
        _natural_key = ('code', 'day')

``NaturalManager`` extends the built-in Manager by default; you can change its superclass using ``manager`` keyword::

    from synchro.core import NaturalManager

    class MyVeryCustomManager(models.Manager):
        ... # some mumbo-jumbo magic

    class MyModel(models.Model):
        ...
        objects = NaturalManager('code', 'day', manager=MyVeryCustomManager)
        def natural_key(self):
            return self.code, self.day

When using ``NaturalKeyModel``, ``NaturalManager`` will extend the defined (``objects``) manager::

    from synchro.core import NaturalKeyModel

    class MyVeryCustomManager(models.Manager):
        ... # some mumbo-jumbo magic

    class MyModel(NaturalKeyModel):
        ...
        _natural_key = ('code', 'day')
        objects = MyVeryCustomManager()

Side note: in fact invoking ``NaturalManager`` creates a new class being ``NaturalManager``'s subclass.

The purpose of a natural key is to *uniquely* distinguish among model instances;
however, there are situations where it is impossible. You can choose such fields that will cause
``get_by_natural_key`` to find more than one object. In such a situation, it will raise
``MultipleObjectsReturned`` exception and the synchronization will fail.

But you can tell ``NaturalManager`` that you are aware of such a situation and that it
should just take the first object found::

    class Person(models.Model):
        ...
        # combination of person name and city is not unique
        objects = NaturalManager('first_name', 'last_name', 'city', allow_many=True)
        def natural_key(self):
            return self.first_name, self.last_name, self.city

Or with ``NaturalKeyModel``::

    class Person(NaturalKeyModel):
        ...
        # combination of person name and city is not unique
        _natural_key = ('first_name', 'last_name', 'city')
        _natural_manager_kwargs = {'allow_many': True}  # I know, it looks quite ugly

Don't use ``allow_many`` unless you are completely sure what you are doing and what
you want to achieve.

Side note: if ``natural_key`` consist of only one field, be sure to return a tuple anyway::

    class MyModel(models.Model):
        ...
        objects = NaturalManager('code')
        def natural_key(self):
            return self.code,  # comma makes it tuple

Or to assign tuple in ``NaturalKeyModel``::

    _natural_key = ('code',)

Previously, there were ``natural_manager`` function that was used instead of ``NaturalManager``
- however, it's deprecated.

Skipping fields
---------------

If your model has some fields that should not be synchronized, like computed fields
(eg. field with payment balances, which is updated on every order save - in ``order.post_save`` signal),
you can exclude them from synchronization::

    class MyModel(models.Model):
        ...
        SYNCHRO_SKIP = ('balance',)

When a new object is synchronized, all its skipped fields will be reset to default values on `REMOTE`.
Of course, the `LOCAL` object will stay untouched.

Temporary logging disabling
---------------------------

If you don't want to log some actions::

    from synchro.core import DisableSynchroLog

    with DisableSynchroLog():
        mymodel.name = foo
        mymodel.save()

Or, in a less robust way, with a decorator::

    from synchro.core import disable_synchro_log

    @disable_synchro_log
    def foo(mymodel):
        mymodel.name = foo
        mymodel.save()

Signals
-------

That's a harder part.

If your signal handlers modify other objects, such an action will be probably reproduced twice:

- first, when the model will be updated on `REMOTE`, then normal `REMOTE` signal handler will launch
- second time, because the original signal handler's action was logged, the whole modified object will be synchronized;
  this is probably undesirable.

Consider a bad scenario:

1. Initially databases are synced. There is an object ``A`` in each of the databases. ``A.foo`` and ``A.bar`` values are both 1.
#. On `REMOTE`, we change ``A.foo`` to 42 and save.
#. On `LOCAL`, we save object ``X``. In some ``X`` signal handler, ``A.bar`` is incremented.
#. We perform synchronization:

   a. ``X`` is synced.
   #. ``X`` signal handler is invoked on `REMOTE`, resulting in `REMOTE`'s ``A.bar`` incrementation.
      So far so good. `REMOTE`'s ``A.bar == 2`` and ``A.foo == 42``, just like it should.
   #. Because ``A`` change (during step 3) was logged, ``A`` is synced. *Not good* -
      `REMOTE` value of ``A.foo`` will be overwritten with 1
      (because `LOCAL` version is considered newer, as it was saved later).

It happened because the signal handler actions were logged.

To prevent this from happening, wrap handler with ``DisableSynchroLog``::

    @receiver(models.signals.post_delete, sender=Parcel)
    def update_agent_balance_delete(sender, instance, *args, **kwargs):
        with DisableSynchroLog():
            instance.agent.balance -= float(instance.payment_left))
            instance.agent.save()

Or with the decorator::

    @receiver(models.signals.post_delete, sender=Parcel)
    @disable_synchro_log
    def update_agent_balance_delete(sender, instance, *args, **kwargs):
        instance.agent.balance -= float(instance.payment_left))
        instance.agent.save()

If using the decorator, be sure to place it after connecting to the signal, not before - otherwise it won't work.

``Update`` issue again
......................

One can benefit from the fact that ``objects.update`` is not logged and use it in signal handlers instead of ``DisableSynchroLog``.

Signal handlers for multi-db
............................

Just a reminder note.

When a synchronization is performed, signal handlers are invoked for created/updated/deleted `REMOTE` objects.
And those signals are of course handled on the `LOCAL` machine.

That means: signal handlers (and probably other part of project code) must be ready to handle both `LOCAL`
and `REMOTE` objects. It must use ``using(...)`` clause or ``db_manager(...)`` to ensure that the proper database
is used::

    def reset_specials(sender, instance, *args, **kwargs):
        Offer.objects.db_manager(instance._state.db).filter(date__lt=instance.date).update(special=False)

Plain ``objects``, without ``db_manager`` or ``using``, always use the ``default`` database (which means `LOCAL`).

But that is normal in multi-db projects.

.. _synchro_on_remote:

Synchro on `REMOTE` and time comparing
--------------------------------------

If you wish only to synchronize one-way (always from `LOCAL` to `REMOTE`), you may be tempted not to include
``synchro`` in `REMOTE` ``INSTALLED_APPS``.

Yes, you can do that and you will save some resources - logs won't be stored.

But keeping ``synchro`` active on `REMOTE` is a better idea. It will pay at synchonization: the synchro will look
at logs and determine which object is newer. If the `LOCAL` one is older, it won't be synced.

You probably should set ``SYNCHRO_REMOTE = None`` on `REMOTE` if no synchronizations will be
performed there (alternatively, you can add some dummy sqlite database to ``DATABASES``).

Checkpoints
-----------

If you wish to reset sychronization status (that is - delete logs and set checkpoint)::

    from synchro.core import reset_synchro

    reset_synchro()

Or raw way of manually changing synchro checkpoint::

    from synchro.models import options

    options.last_check = datetime.datetime.now()  # or any time you wish

----------

Changelog
=========

**0.7** (12/11/2017)
    - Support Django 1.8 - 1.11
    - Dropped support for Django 1.6 and older
    - Backward incompatibility:
      you need to refactor all `from synchro import ...`
      into `from synchro.core import ...`

**0.6** (27/12/2014)
    - Support Django 1.7
    - Fixed deprecation warnings

**0.5.2** (29/07/2014)
    - Fixed dangerous typo
    - Added 'reset' button to synchro view and SYNCHRO_ALLOW_RESET setting
    - Prepared all texts for translation
    - Added PL, DE, FR, ES translations
    - Added ``SYNCHRO_DEBUG`` setting

**0.5.1** (28/02/2013)
    Fixed a few issues with 0.5 release

**0.5** (27/02/2013)
    - Refactored code to be compatible with Django 1.5
    - Required Django version increased from 1.3 to 1.4 (the code was already using some
      1.4-specific functions)
    - Removed deprecated natural_manager function

**0.4.2** (18/10/2012)
    - Fixed issue with app loading (thanks to Alexander Todorov for reporting)
    - Added 1 test regarding the issue above

**0.4.1** (23/09/2012)
    - Fixed symmetrical m2m synchronization
    - Added 1 test regarding the issue above

**0.4** (16/09/2012)
    - **Deprecation**: natural_manager function is deprecated. Use NaturalManager instead
    - Refactored NaturalManager class so that it plays well with models involved in m2m relations
    - Refactored NaturalManager class so that natural_manager function is unnecessary
    - Added NaturalKeyModel base class
    - Fixed bug with m2m user-defined intermediary table synchronization
    - Fixed bugs with m2m changes synchronization
    - Added 3 tests regarding m2m aspects

**0.3.1** (12/09/2012)
    - ``SYNCHRO_REMOTE`` setting is not required anymore.
      Its lack will only block ``synchronize`` command
    - Added 2 tests regarding the change above
    - Updated README

**0.3** (04/09/2012)
    - **Backward incompatible**: Changed ``Reference`` fields type from ``Integer`` to ``Char`` in
      order to store non-numeric keys
    - Included 24 tests
    - Refactored NaturalManager class so that it is accessible and importable
    - Exception is raised if class passed to natural_manager is not Manager subclass
    - Switched to dbsettings-bundled DateTimeValue
    - Updated README

**0.2** (10/06/2012)
    Initial PyPI release

**0.1**
    Local development

----------

:Author: Jacek Tomaszewski
:Thanks: to my wife for text correction
