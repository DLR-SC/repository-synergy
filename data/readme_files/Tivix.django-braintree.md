================
django-braintree
================


Installation
------------

- Install django_braintree (ideally in your virtualenv!) using pip or simply getting a copy of the code and putting it in a directory in your codebase.

    ``pip install tivix-django-braintree``


- Add ``django_braintree`` to your Django settings ``INSTALLED_APPS``::

	INSTALLED_APPS = [
        # ...
        "django_braintree",
    ]

- Add these lines in settings.py file::

    BRAINTREE_MERCHANT = 'your_merchant_key'
    BRAINTREE_PUBLIC_KEY = 'your_public_key'
    BRAINTREE_PRIVATE_KEY = 'your_private_key'

    from braintree import Configuration, Environment

    Configuration.configure(
        Environment.Sandbox,
        BRAINTREE_MERCHANT,
        BRAINTREE_PUBLIC_KEY,
        BRAINTREE_PRIVATE_KEY
    )

- Add url to urls.py::

    url(r'', include('django_braintree.urls')),

- If you're using South for schema migrations run ``python manage.py migrate django_braintree`` or simply do a ``syncdb``.


Additional Information
----------------------

- Braintree uses default templates::

    django_braintree/payments_billing.html
    django_braintree/fragments/cc_form.html
    django_braintree/fragments/current_cc_info.html
    django_braintree/fragments/pay.html
    django_braintree/fragments/payments_billing.html

- Braintree requires including the js from ``django_common`` that enables ajax forms etc. ``django_common`` is available at https://github.com/Tivix/django-common
- If a template variable ``cc_form_post_url`` is passed to the template then this form posts to it, otherwise it posts to the url ``payments_billing``.
- If a template variable ``cc_form_success_redirect_url`` is passed it takes user to that url then after form post has succeeded.
- Braintree is set up to sandbox mode at default. To change this you must switch ``Environment.Sandbox`` to ``Environment.Production`` in settings file.


Revision History
----------------

    - v0.1.2 Changed urls.py to be compatible with Django 1.4+


This opensource app is brought to you by Tivix, Inc. ( http://tivix.com/ )
