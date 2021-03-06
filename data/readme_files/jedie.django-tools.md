= django-tools

Miscellaneous tools for django.

Look also at the siblings project: [[https://github.com/jedie/django-cms-tools|django-cms-tools]] (Tools/helpers around Django-CMS).

| {{https://travis-ci.org/jedie/django-tools.svg|Build Status on travis-ci.org}} | [[https://travis-ci.org/jedie/django-tools/|travis-ci.org/jedie/django-tools]] |
| {{https://codecov.io/gh/jedie/django-tools/branch/master/graph/badge.svg|Coverage Status on codecov.io}} | [[https://codecov.io/gh/jedie/django-tools|codecov.io/gh/jedie/django-tools]] |
| {{https://coveralls.io/repos/jedie/django-tools/badge.svg|Coverage Status on coveralls.io}} | [[https://coveralls.io/r/jedie/django-tools|coveralls.io/r/jedie/django-tools]] |
| {{https://landscape.io/github/jedie/django-tools/master/landscape.svg|Status on landscape.io}} | [[https://landscape.io/github/jedie/django-tools/master|landscape.io/github/jedie/django-tools/master]] |


== try-out

e.g.:
{{{
~$ git clone https://github.com/jedie/django-tools.git
~$ cd django-tools/
~/django-tools$ make install
~/django-tools$ make
help                 List all commands
install-poetry       install or update poetry
install              install django-tools via poetry
lint                 Run code formatters and linter
fix-code-style       Fix code formatting
tox-listenvs         List all tox test environments
tox                  Run pytest via tox with all environments
tox-py36             Run pytest via tox with *python v3.6*
tox-py37             Run pytest via tox with *python v3.7*
tox-py38             Run pytest via tox with *python v3.8*
pytest               Run pytest
update-rst-readme    update README.rst from README.creole
publish              Release new version to PyPi
start-dev-server     Start Django dev. server with the test project
}}}

== existing stuff

=== OverwriteFileSystemStorage

A django filesystem storage that will overwrite existing files and can create backups, if content changed.
usage:

{{{
class ExampleModel(models.Model):
    foo_file = models.FileField(
        storage=OverwriteFileSystemStorage(create_backups=True)
    )
    bar_image = models.ImageField(
        storage=OverwriteFileSystemStorage(create_backups=False)
    )
}}}

Backup made by appending a suffix and sequential number, e.g.:

* source....: foo.bar
* backup 1..: foo.bar.bak
* backup 2..: foo.bar.bak0
* backup 3..: foo.bar.bak1

Backup files are only made if file content changed. But at least one time!

=== Django Logging utils

Put this into your settings, e.g.:

{{{
from django_tools.unittest_utils.logging_utils import CutPathnameLogRecordFactory, FilterAndLogWarnings

# Filter warnings and pipe them to logging system
# Warnings of external packages are displayed only once and only the file path.
warnings.showwarning = FilterAndLogWarnings()

# Adds 'cut_path' attribute on log record. So '%(cut_path)s' can be used in log formatter.
logging.setLogRecordFactory(CutPathnameLogRecordFactory(max_length=50))

LOGGING = {
    # ...
    'formatters': {
        'verbose': {
            'format': '%(levelname)8s %(cut_path)s:%(lineno)-3s %(message)s'
        },
    },
    # ...
}
}}}
(Activate warnings by, e.g.: {{{export PYTHONWARNINGS=all}}})


==== ThrottledAdminEmailHandler

[[https://github.com/jedie/django-tools/blob/master/django_tools/log_utils/throttle_admin_email_handler.py|ThrottledAdminEmailHandler]] works similar as the origin [[https://docs.djangoproject.com/en/1.11/topics/logging/#django.utils.log.AdminEmailHandler|django.utils.log.AdminEmailHandler]]
but is will throttle the number of mails that can be send in a time range.
usage e.g.:

{{{
LOGGING = {
    # ...
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django_tools.log_utils.throttle_admin_email_handler.ThrottledAdminEmailHandler",
            "formatter": "email",
            "min_delay_sec": 20, # << -- skip mails in this time range
        },
        # ...
    },
    # ...
}
}}}


=== django_tools.template.loader.DebugCacheLoader

Insert template name as html comments, e.g.:

{{{
<!-- START 'foo/bar.html' -->
...
<!-- END 'foo/bar.html' -->
}}}

To use this, you must add **django_tools.template.loader.DebugCacheLoader** as template loader.

e.g.: Activate it only in DEBUG mode:

{{{
if DEBUG:
    TEMPLATES[0]["OPTIONS"]["loaders"] = [
        (
            "django_tools.template.loader.DebugCacheLoader", (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )
        )
    ]
}}}


=== send text+html mails

A helper class to send text+html mails used the django template library.

You need two template files, e.g.:
* [[https://github.com/jedie/django-tools/blob/master/django_tools_test_project/django_tools_test_app/templates/mail_test.txt|mail_test.txt]]
* [[https://github.com/jedie/django-tools/blob/master/django_tools_test_project/django_tools_test_app/templates/mail_test.html|mail_test.html]]

You have to specify the template file like this: {{{template_base="mail_test.{ext}"}}}

Send via Celery task:
{{{
# settings.py
SEND_MAIL_CELERY_TASK_NAME="mail:send_task"

from django_tools.mail.send_mail import SendMailCelery
SendMailCelery(
    template_base="mail_test.{ext}",
    mail_context={"foo": "first", "bar": "second"},
    subject="Only a test",
    recipient_list="foo@bar.tld"
).send()
}}}

Send without Celery:
{{{
from django_tools.mail.send_mail import SendMail
SendMail(
    template_base="mail_test.{ext}",
    mail_context={"foo": "first", "bar": "second"},
    subject="Only a test",
    recipient_list="foo@bar.tld"
).send()
}}}

See also the existing unittests:
* [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_email.py|django_tools_tests/test_email.py]]


=== Delay tools

Sometimes you want to simulate when processing takes a little longer.
There exists {{{django_tools.debug.delay.SessionDelay}}} and {{{django_tools.debug.delay.CacheDelay}}} for this.
The usage will create logging entries and user messages, if user is authenticated.

More info in seperate [[https://github.com/jedie/django-tools/blob/master/django_tools/debug/README.creole|django_tools/debug/README.creole]] file.


=== Filemanager library

Library for building django application like filemanager, gallery etc.

more info, read [[https://github.com/jedie/django-tools/blob/master/django_tools/filemanager/README.creole|./filemanager/README.creole]]

=== per-site cache middleware

Similar to [[https://docs.djangoproject.com/en/1.4/topics/cache/#the-per-site-cache|django UpdateCacheMiddleware and FetchFromCacheMiddleware]],
but has some enhancements: [[https://github.com/jedie/django-tools/blob/master/django_tools/cache/README.creole#per-site-cache-middleware|'per site cache' in ./cache/README.creole]]

=== smooth cache backends

Same as django cache backends, but adds {{{cache.smooth_update()}}} to clears the cache smoothly depend on the current system load.
more info in: [[https://github.com/jedie/django-tools/blob/master/django_tools/cache/README.creole#smooth-cache-backends|'smooth cache backends' in ./cache/README.creole]]

=== local sync cache

Keep a local dict in a multi-threaded environment up-to-date. Usefull for cache dicts.
More info, read DocString in [[https://github.com/jedie/django-tools/blob/master/django_tools/local_sync_cache/local_sync_cache.py|./local_sync_cache/local_sync_cache.py]].


=== threadlocals middleware

For getting request object anywhere, use [[https://github.com/jedie/django-tools/blob/master/django_tools/middlewares/ThreadLocal.py|./middlewares/ThreadLocal.py]]


=== Dynamic SITE_ID middleware

Note: Currently not maintained! TODO: Fix unittests for all python/django version

Set settings.SITE_ID dynamically with a middleware base on the current request domain name.
Domain name alias can be specify as a simple string or as a regular expression.

more info, read [[https://github.com/jedie/django-tools/blob/master/django_tools/dynamic_site/README.creole|./dynamic_site/README.creole]].

=== StackInfoStorage

Message storage like LegacyFallbackStorage, except, every message would have a stack info, witch is helpful, for debugging.
Stack info would only be added, if settings DEBUG or MESSAGE_DEBUG is on.
To use it, put this into your settings:

{{{
MESSAGE_STORAGE = "django_tools.utils.messages.StackInfoStorage"
}}}

More info, read DocString in [[https://github.com/jedie/django-tools/blob/master/django_tools/utils/messages.py|./utils/messages.py]].


=== limit to usergroups

Limit something with only one field, by selecting:
* anonymous users
* staff users
* superusers
* ..all existing user groups..

More info, read DocString in [[https://github.com/jedie/django-tools/blob/master/django_tools/limit_to_usergroups.py|./limit_to_usergroups.py]]

=== permission helpers

See [[https://github.com/jedie/django-tools/blob/master/django_tools/permissions.py|django_tools.permissions]]
and unittests: [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_permissions.py|django_tools_tests.test_permissions]]

=== form/model fields

* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/directory.py|Directory field]] - check if exist and if in a defined base path
* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/language_code.py|language code field with validator]]
* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/media_path.py|Media Path field]] browse existign path to select and validate input
* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/sign_separated.py|sign seperated form/model field]] e.g. comma seperated field
* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/static_path.py|static path field]]
* [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/url.py|url field]] A flexible version of the original django form URLField


== unittests helpers


=== Selenium Test Cases

There are Firefox and Chromium test cases, with and without django StaticLiveServerTestCase!

Chromium + StaticLiveServer example:
{{{
from django_tools.selenium.chromedriver import chromium_available
from django_tools.selenium.django import SeleniumChromiumStaticLiveServerTestCase

@unittest.skipUnless(chromium_available(), "Skip because Chromium is not available!")
class ExampleChromiumTests(SeleniumChromiumStaticLiveServerTestCase):
    def test_admin_login_page(self):
        self.driver.get(self.live_server_url + "/admin/login/")
        self.assert_equal_page_title("Log in | Django site admin")
        self.assert_in_page_source('<form action="/admin/login/" method="post" id="login-form">')
        self.assert_no_javascript_alert()
}}}


Firefox + StaticLiveServer example:
{{{
from django_tools.selenium.django import SeleniumFirefoxStaticLiveServerTestCase
from django_tools.selenium.geckodriver import firefox_available

@unittest.skipUnless(firefox_available(), "Skip because Firefox is not available!")
class ExampleFirefoxTests(SeleniumFirefoxStaticLiveServerTestCase):
    def test_admin_login_page(self):
        self.driver.get(self.live_server_url + "/admin/login/")
        self.assert_equal_page_title("Log in | Django site admin")
        self.assert_in_page_source('<form action="/admin/login/" method="post" id="login-form">')
        self.assert_no_javascript_alert()
}}}

Test cases without StaticLiveServer:
{{{
from django_tools.selenium.chromedriver import SeleniumChromiumTestCase
from django_tools.selenium.geckodriver import SeleniumFirefoxTestCase
}}}


See also existing unitests here:

* [[https://github.com/jedie/django-tools/blob/master/django_tools/django_tools_tests/test_unittest_selenium.py|/django_tools/django_tools_tests/test_unittest_selenium.py]]


**Note:**

To use Chromium test cases you need the **Chromium Browser WebDriver** e.g.: {{{apt install chromium-chromedriver}}}

To use Firefox test cases you need the **Firefox Browser WebDriver** aka **geckodriver**

e.g.:
{{{
~$ cd /tmp
/tmp$ wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz -O geckodriver.tar.gz
/tmp$ sudo sh -c 'tar -x geckodriver -zf geckodriver.tar.gz -O > /usr/bin/geckodriver'
/tmp$ sudo chmod +x /usr/bin/geckodriver
/tmp$ rm geckodriver.tar.gz
/tmp$ geckodriver --version
geckodriver 0.20.1
...
}}}
Current version number can be found here:

* https://github.com/mozilla/geckodriver/releases




=== Mockup utils

Create dummy PIL/django-filer images with Text, see:

* [[https://github.com/jedie/django-tools/blob/master/django_tools/unittest_utils/mockup.py|/django_tools/unittest_utils/mockup.py]]

usage/tests:

* [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_mockup.py|/django_tools_tests/test_mockup.py]]


=== Model instance unittest code generator

Generate unittest code skeletons from existing model instance. You can use this feature as django manage command or as admin action.

Usage as management command, e.g.:
{{{
$ ./manage.py generate_model_test_code auth.
...
#
# pk:1 from auth.User <class 'django.contrib.auth.models.User'>
#
user = User.objects.create(
    password='pbkdf2_sha256$36000$ybRfVQDOPQ9F$jwmgc5UsqRQSXxJs/NrZeTLguieUSSZfaSZbMmC+L5w=', # CharField, String (up to 128)
    last_login=datetime.datetime(2018, 4, 24, 8, 27, 49, 578107, tzinfo=<UTC>), # DateTimeField, Date (with time)
    is_superuser=True, # BooleanField, Boolean (Either True or False)
    username='test', # CharField, String (up to 150)
    first_name='', # CharField, String (up to 30)
    last_name='', # CharField, String (up to 30)
    email='', # CharField, Email address
    is_staff=True, # BooleanField, Boolean (Either True or False)
    is_active=True, # BooleanField, Boolean (Either True or False)
    date_joined=datetime.datetime(2018, 3, 6, 17, 15, 50, 93136, tzinfo=<UTC>), # DateTimeField, Date (with time)
)
...
}}}


=== create users

[[https://github.com/jedie/django-tools/blob/master/django_tools/unittest_utils/user.py|/unittest_utils/user.py]]:

* {{{django_tools.unittest_utils.user.create_user()}}} - create users, get_super_user
* {{{django_tools.unittest_utils.user.get_super_user()}}} - get the first existing superuser


=== Isolated Filesystem decorator / context manager

[[https://github.com/jedie/django-tools/blob/master/django_tools/unittest_utils/isolated_filesystem.py|django_tools.unittest_utils.isolated_filesystem.isolated_filesystem]] acts as either a decorator or a context manager.
Useful to for tests that will create files/directories in current work dir, it does this:

* create a new temp directory
* change the current working directory to the temp directory
* after exit:
* Delete an entire temp directory tree

usage e.g.:
{{{
from django_tools.unittest_utils.isolated_filesystem import isolated_filesystem

with isolated_filesystem(prefix="temp_dir_prefix"):
    open("foo.txt", "w").write("bar")
}}}

=== BaseUnittestCase

**django_tools.unittest_utils.unittest_base.BaseUnittestCase** contains some low-level assert methods:

* assertEqual_dedent()

Note: assert methods will be migrated to: {{{django_tools.unittest_utils.assertments}}} in the future!

//django_tools.unittest_utils.tempdir// contains **TempDir**, a Context Manager Class:
{{{
with TempDir(prefix="foo_") as tempfolder:
    # create a file:
    open(os.path.join(tempfolder, "bar"), "w").close()

# the created temp folder was deleted with shutil.rmtree()
}}}

usage/tests:

* [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_unittest_utils.py|/django_tools_tests/test_unittest_utils.py]]


=== DjangoCommandMixin

Helper to run shell commands. e.g.: "./manage.py cms check" in unittests.

usage/tests:

* [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_unittest_django_command.py|/django_tools_tests/test_unittest_django_command.py]]


=== DOM compare in unittests

The Problem:
You can???t easy check if e.g. some form input fields are in the response,
because the form rendering use a dict for storing all html attributes.
So, the ordering of form field attributes are not sorted and varied.

The Solution:
You need to parse the response content into a DOM tree and compare nodes.

We add the great work of Gregor M??llegger at his GSoC 2011 form-rendering branch.
You will have the following assert methods inherit from: django_tools.unittest_utils.unittest_base.BaseTestCase

* self.assertHTMLEqual() ??? for compare two HTML DOM trees
* self.assertDOM() ??? for check if nodes in response or not.
* self.assertContains() ??? Check if ond node occurs 'count??? times in response

More info and examples in [[https://github.com/jedie/django-tools/blob/master/django_tools/django_tools_tests/test_dom_asserts.py|./django_tools_tests/test_dom_asserts.py]]


=== @set_string_if_invalid() decorator

Helper to check if there are missing template tags by set temporary {{{'string_if_invalid'}}}, see: https://docs.djangoproject.com/en/1.8/ref/templates/api/#invalid-template-variables

Usage, e.g.:

{{{
from django.test import SimpleTestCase
from django_tools.unittest_utils.template import TEMPLATE_INVALID_PREFIX, set_string_if_invalid

@set_string_if_invalid()
class TestMyTemplate(SimpleTestCase):
    def test_valid_tag(self):
        response = self.client.get('/foo/bar/')
        self.assertNotIn(TEMPLATE_INVALID_PREFIX, response.content)
}}}
You can also decorate the test method ;)


=== unittest_utils/assertments.py


The file contains some common assert functions:

* {{{assert_startswith}}} - Check if test starts with prefix.
* {{{assert_endswith}}} - Check if text ends with suffix.
* {{{assert_locmem_mail_backend}}} - Check if current email backend is the In-memory backend.
* {{{assert_language_code() - Check if given language_code is in settings.LANGUAGES
* {{{assert_installed_apps()}}} - Check entries in settings.INSTALLED_APPS
* {{{assert_is_dir}}} - Check if given path is a directory
* {{{assert_is_file}}} - Check if given path is a file
* {{{assert_path_not_exists}}} - Check if given path doesn't exists

=== Speedup tests

Speedup test run start by disable migrations, e.g.:
{{{
from django_tools.unittest_utils.disable_migrations import DisableMigrations
MIGRATION_MODULES = DisableMigrations()
}}}

=== small tools
==== debug_csrf_failure()
Display the normal debug page and not the minimal csrf debug page.
More info in DocString here: [[https://github.com/jedie/django-tools/blob/master/django_tools/views/csrf.py|django_tools/views/csrf.py]]

==== import lib helper
additional helper to the existing {{{importlib}}}
more info in the sourcecode: [[https://github.com/jedie/django-tools/blob/master/django_tools/utils/importlib.py|./utils/importlib.py]]

==== http utils
Pimped HttpRequest to get some more information about a request.
More info in DocString here: [[https://github.com/jedie/django-tools/blob/master/django_tools/utils/http.py|django_tools/utils/http.py]]

==== @display_admin_error
Developer helper to display silent errors in ModelAdmin.list_display callables.
See: **display_admin_error** in [[https://github.com/jedie/django-tools/blob/master/django_tools/decorators.py|decorators.py]]

=== upgrade virtualenv
A simple commandline script that calls {{{pip install ???-upgrade XY}}} for every package thats installed in a virtualenv.
Simply copy/symlink it into the root directory of your virtualenv and start it.

**Note:** [[https://github.com/pypa/pip/issues/319|Seems that this solution can't observe editables right.]]

To use it, without installing django-tools:

{{{
~/$ cd goto/your_env
.../your_env/$ wget https://github.com/jedie/django-tools/raw/master/django_tools/upgrade_virtualenv.py
.../your_env/$ chmod +x upgrade_virtualenv.py
.../your_env/$ ./upgrade_virtualenv.py
}}}
This script will be obsolete, if [[https://github.com/pypa/pip/issues/59|pip has a own upgrade command]].


=== django_tools.utils.url.GetDict

Similar to origin django.http.QueryDict but:
 * urlencode() doesn't add "=" to empty values: "?empty" instead of "?empty="
 * always mutable
 * output will be sorted (easier for tests ;)

More info, see tests: [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_utils_url.py|django_tools_tests/test_utils_url.py]]


==== SignedCookieStorage

Store information in signed Cookies, use **django.core.signing**.
So the cookie data can't be manipulated from the client.
Sources/examples:
* [[https://github.com/jedie/django-tools/blob/master/django_tools/utils/client_storage.py|/django_tools/utils/client_storage.py]]
* [[https://github.com/jedie/django-tools/blob/master/django_tools_tests/test_signed_cookie.py|/django_tools_tests/test_signed_cookie.py]]


=== Print SQL Queries

Print the used SQL queries via context manager.

usage e.g.:
{{{
from django_tools.unittest_utils.print_sql import PrintQueries

# e.g. use in unittests:
class MyTests(TestCase):
    def test_foobar(self):
        with PrintQueries("Create object"):
            FooBar.objects.create("name"=foo)

# e.g. use in views:
def my_view(request):
    with PrintQueries("Create object"):
        FooBar.objects.create("name"=foo)
}}}

the output is like:
{{{
_______________________________________________________________________________
 *** Create object ***
1 - INSERT INTO "foobar" ("name")
    VALUES (foo)
-------------------------------------------------------------------------------
}}}

=== SetRequestDebugMiddleware

middleware to add debug bool attribute to request object.
More info: [[https://github.com/jedie/django-tools/blob/master/django_tools/debug/README.creole|./debug/README.creole]]

=== TracebackLogMiddleware

Put traceback in log by call [[https://docs.python.org/3/library/logging.html#logging.Logger.exception|logging.exception()]] on {{{process_exception()}}}
Activate with:
{{{
MIDDLEWARE_CLASSES = (
    ...
    'django_tools.middlewares.TracebackLogMiddleware.TracebackLogMiddleware',
    ...
)
}}}

=== FnMatchIps() - Unix shell-style wildcards in INTERNAL_IPS / ALLOWED_HOSTS
settings.py e.g.:
{{{
from django_tools.settings_utils import FnMatchIps

INTERNAL_IPS = FnMatchIps(["127.0.0.1", "::1", "192.168.*.*", "10.0.*.*"])
ALLOWED_HOSTS = FnMatchIps(["127.0.0.1", "::1", "192.168.*.*", "10.0.*.*"])
}}}


=== StdoutStderrBuffer()

redirect stdout + stderr to a string buffer. e.g.:
{{{
from django_tools.unittest_utils.stdout_redirect import StdoutStderrBuffer

with StdoutStderrBuffer() as buffer:
    print("foo")
output = buffer.get_output() # contains "foo\n"
}}}

=== Management commands


==== permission_info

List all permissions for one django user.
(Needs {{{'django_tools'}}} in INSTALLED_APPS)

e.g.:

{{{
$ ./manage.py permission_info
No username given!

All existing users are:
foo, bar, john, doe

$ ./manage.py permission_info foo
All permissions for user 'test_editor':
	is_active    : yes
	is_staff     : yes
	is_superuser : no
[*] admin.add_logentry
[*] admin.change_logentry
[*] admin.delete_logentry
[ ] auth.add_group
[ ] auth.add_permission
[ ] auth.add_user
...
}}}

==== logging_info

Shows a list of all loggers and marks which ones are configured in settings.LOGGING:

{{{
$ ./manage.py logging_info
}}}


==== nice_diffsettings

Similar to django 'diffsettings', but used pretty-printed representation:

{{{
$ ./manage.py nice_diffsettings
}}}


==== database_info

Just display some information about the used database and connections:

{{{
$ ./manage.py database_info
}}}


==== list_models

Just list all existing models in app_label.ModelName format. Useful to use this in 'dumpdata' etc:

{{{
$ ./manage.py list_models
}}}

=== ..all others???

There exist many miscellaneous stuff. Look in the source, luke!


== running django-tools unittests

Run all tests in all environment combinations via tox:

{{{
.../django-tools $ python3 setup.py tox
}}}

Run all tests in current environment via pytest:

{{{
.../django-tools $ python3 setup.py test
}}}



== Backwards-incompatible changes

(Older changes are [[https://github.com/jedie/django-tools/tree/f7aef5b778ba505848ba4b1a389d43cd3f559bb9#backwards-incompatible-changes|in git history]])

=== v0.39

File renamed: {{{django_tools/unittest_utils/{celery.py => celery_utils.py}}}}

=== v0.41

{{{@task_always_eager()}}} decorator was removed.

=== v0.42

* All celery related stuff was removed.
* The pseudo app for exra manage commands was removed. The commands are always available if "django_tools" is in INSTALLED_APPS
  * Please remove from your INSTALLED_APPS:
    * 'django_tools.manage_commands.django_tools_list_models',
    * 'django_tools.manage_commands.django_tools_nice_diffsettings',

=== v0.43

Selenium helpers moved:
{{{
-from django_tools.unittest_utils.selenium_utils import (
-    SeleniumChromiumTestCase, SeleniumFirefoxTestCase, chromium_available, find_executable, firefox_available
-)
+from django_tools.selenium.chromedriver import SeleniumChromiumTestCase, chromium_available
+from django_tools.selenium.geckodriver import SeleniumFirefoxTestCase, firefox_available
+from django_tools.selenium.utils import find_executable
}}}

Using the old place {{{django_tools.unittest_utils.selenium_utils}}} still works, but will be removed in the future!

=== v0.44

* remove old mockup image API (it was deprecated since v0.35)


== Django compatibility

|= django-tools    |= django version |= python         |
| >= v0.39         | 1.11, 2.0       | 3.5, 3.6, pypy3 |
| >= v0.38.1       | 1.8, 1.11       | 3.5, 3.6, pypy3 |
| >= v0.38.0       | 1.8, 1.11       | 3.5, 3.6        |
| >= v0.37.0       | 1.8, 1.11       | 3.4, 3.5        |
| >= v0.33.0       | 1.8, 1.11       | 2.7, 3.4, 3.5   |
| v0.30.1-v0.32.14 | 1.8, 1.9, 1.10  | 2.7, 3.4, 3.5   |
| v0.30            | 1.8, 1.9        | 2.7, 3.4        |
| v0.29            | 1.6 - 1.8       | 2.7, 3.4        |
| v0.26            | <=1.6           |                 |
| v0.25            | <=1.4           |                 |

(See also combinations in [[https://github.com/jedie/django-tools/blob/master/.travis.yml|.travis.yml]] and [[https://github.com/jedie/django-tools/blob/master/tox.ini|tox.ini]])


== history

* *dev* - [[https://github.com/jedie/django-tools/compare/v0.46.1...master|compare v0.46.1...master]]
* TBC
* v0.46.1 - 19.02.2020 - [[https://github.com/jedie/django-tools/compare/v0.46.0...v0.46.1|compare v0.46.0...v0.46.1]]
** less restricted dependency specification
** NEW: {{{"django_tools.middlewares.LogHeaders.LogRequestHeadersMiddleware"}}}
** SeleniumChromiumTestCase: set "accept_languages" and disable "headless" mode, see also: https://github.com/jedie/django-tools/issues/21
* v0.46.0 - 13.02.2020 - [[https://github.com/jedie/django-tools/compare/v0.45.3...v0.46.0|compare v0.45.3...v0.46.0]]
** {{{dynamic_site}}} was removed. Please use e.g.: [[https://github.com/jazzband/django-hosts|django-hosts]]
** modernize project setup and use {{{poetry}}}
** remove {{{lxml}}} decency by using [[https://github.com/mozilla/bleach|bleach]] for {{{html_utils.html2text}}}
** update code and code style
* v0.45.3 - 25.08.2019 - [[https://github.com/jedie/django-tools/compare/v0.45.2...v0.45.3|compare v0.45.2...v0.45.3]]
** Add {{{excepted_exit_code}}} to {{{django_tools.unittest_utils.django_command.DjangoCommandMixin}}} to it's possible to test errors in manage commands
* v0.45.2 - 26.06.2019 - [[https://github.com/jedie/django-tools/compare/v0.45.1...v0.45.2|compare v0.45.1...v0.45.2]]
** NEW: {{{django_tools.log_utils.throttle_admin_email_handler.ThrottledAdminEmailHandler}}}
* v0.45.1 - 03.04.2019 - [[https://github.com/jedie/django-tools/compare/v0.45.0...v0.45.1|compare v0.45.0...v0.45.1]]
** Bugfix ValueError in {{{django_tools.unittest_utils.email.print_mailbox}}}
* v0.45.0 - 01.04.2019 - [[https://github.com/jedie/django-tools/compare/v0.44.2...v0.45.0|compare v0.44.2...v0.45.0]]
** NEW: {{{OverwriteFileSystemStorage}}} with backup functionality
** NEW: {{{print_exc_plus()}}} - traceback with a listing of all the local variables
** NEW: {{{assert_pformat_equal}}} with {{{pprintpp}}} and {{{icdiff}}}
** NEW: {{{assert_filenames_and_content}}}
* v0.44.2 - 02.01.2019 - [[https://github.com/jedie/django-tools/compare/v0.44.1...v0.44.2|compare v0.44.1...v0.44.2]]
** Handle errors like: https://github.com/andymccurdy/redis-py/issues/995
* v0.44.1 - 02.01.2019 - [[https://github.com/jedie/django-tools/compare/v0.44.0...v0.44.1|compare v0.44.0...v0.44.1]]
** {{{LoggingBuffer}}}: Don't deactivate existing log handler, just append the buffer handler.
* v0.44.0 - 13.12.2018 - [[https://github.com/jedie/django-tools/compare/v0.43.2...v0.44.0|compare v0.43.2...v0.44.0]]
** NEW: {{{django_file = ImageDummy().create_django_file_info_image(text="")}}} e.g.: for attach to {{{models.ImageField()}}}
** Make {{{mockup.ImageDummy()}}} usable even if django-filer is not installed.
** {{{mockup.ImageDummy()}}} default image format changed from png to jpeg
** Cleanup: remove old, since v0.35 deprecated mockup image API
* v0.43.2 - 11.12.2018 - [[https://github.com/jedie/django-tools/compare/v0.43.1...v0.43.2|compare v0.43.1...v0.43.2]]
** Bugfix Selenium refactor: Use the class with the same functionality if old usage places are used.
* v0.43.1 - 11.12.2018 - [[https://github.com/jedie/django-tools/compare/v0.43.0...v0.43.1|compare v0.43.0...v0.43.1]]
** Bugfix: Selenium test cases: clear {{{ window.localStorage }}} after test run
* v0.43.0 - 11.12.2018 - [[https://github.com/jedie/django-tools/compare/v0.42.4...v0.43.0|compare v0.42.4...v0.43.0]]
** Refactor selenium helpers
** Split selenium test cases: with and without Django StaticLiveServerTestCase
** NEW: Selenium helper to access {{{ window.localStorage }}}
* v0.42.4 - 12.10.2018 - [[https://github.com/jedie/django-tools/compare/v0.42.3...v0.42.4|compare v0.42.3...v0.42.4]]
** Add {{{request}}} object to {{{TestUserMixin.login()}}} (needed for e.g.: django-axes auth backend)
* v0.42.3 - 10.10.2018 - [[https://github.com/jedie/django-tools/compare/v0.42.2...v0.42.3|compare v0.42.2...v0.42.3]]
** NEW: * {{{assertments.assert_is_dir}}}, {{{assertments.assert_is_file}}}, {{{assertments.assert_path_not_exists}}}
* v0.42.2 - 18.09.2018 - [[https://github.com/jedie/django-tools/compare/v0.42.1...v0.42.2|compare v0.42.1...v0.42.2]]
** NEW: {{{assert_installed_apps()}}} - Check entries in settings.INSTALLED_APPS
* v0.42.1 - 17.09.2018 - [[https://github.com/jedie/django-tools/compare/v0.42.0...v0.42.1|compare v0.42.0...v0.42.1]]
** NEW: {{{django_tools.unittest_utils.assertments.assert_language_code}}} - Check if given language_code is in settings.LANGUAGES
* v0.42.0 - 07.09.2018 - [[https://github.com/jedie/django-tools/compare/v0.41.0...v0.42.0|compare v0.41.0...v0.42.0]]
** remove all celery stuff
** NEW: {{{$ ./manage.py logging_info}}} Shows a list of all loggers and marks which ones are configured in settings.LOGGING
** manage commands {{{list_models}}} and {{{nice_diffsettings}}} are moved from seperate apps
* v0.41.0 - 28.08.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.6...v0.41.0|compare v0.40.6...v0.41.0]]
** NEW: {{{unittest_utils/assertments.py}}} with some common assert functions
** Remove {{{@task_always_eager()}}} decorator
* v0.40.6 - 28.08.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.5...v0.40.6|compare v0.40.5...v0.40.6]]
** Bugfix {{{@task_always_eager()}}} decorator
* v0.40.5 - 27.08.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.4...v0.40.5|compare v0.40.4...v0.40.5]]
** Bugfix {{{DjangoCommandMixin.call_manage_py()}}}: Use the given {{{manage.py}}} filename
* v0.40.4 - 21.08.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.3...v0.40.4|compare v0.40.3...v0.40.4]]
** NEW: {{{django_tools.debug.delay}}} to simulate longer processing time by set a delay via GET parameter (see above)
* v0.40.3 - 18.07.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.2...v0.40.3|compare v0.40.2...v0.40.3]]
** Enhance selenium test cases:
*** NEW: {{{assert_visible_by_id()}}}
*** NEW: {{{assert_clickable_by_id()}}}
*** NEW: {{{assert_clickable_by_xpath()}}}
*** add {{{desired_capabilities}}} to firefox and chrome test cases
*** enable logging in chrome test case
*** NEW: {{{assert_in_browser_log()}}} in chrome test case
* v0.40.2 - 04.07.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.1...v0.40.2|compare v0.40.1...v0.40.2]]
** Bugfix selenium Test Case if driver is None
** Bugfix django compatibility
* v0.40.1 - 28.06.2018 - [[https://github.com/jedie/django-tools/compare/v0.40.0...v0.40.1|compare v0.40.0...v0.40.1]]
** Bugfix selenium test case if executable can't be found.
* v0.40.0 - 15.06.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.6...v0.40.0|compare v0.39.6...v0.40.0]]
** NEW: selenium chrome and firefox test cases in {{{django_tools.unittest_utils.selenium_utils}}}
** Fix test project and add {{{run_test_project_dev_server.sh}}} for easy test
** Fixing tests
* v0.39.6 - 04.05.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.5...v0.39.6|compare v0.39.5...v0.39.6]]
** Enhance model instance unittest code generator
* v0.39.5 - 24.04.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.4...v0.39.5|compare v0.39.4...v0.39.5]]
** NEW: Model instance unittest code generator (see above)
* v0.39.4 - 06.04.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.3...v0.39.4|compare v0.39.3...v0.39.4]]
** NEW: {{{django_tools.unittest_utils.logging_utils.FilterAndLogWarnings}}} and {{{django_tools.unittest_utils.logging_utils.CutPathnameLogRecordFactory}}}
* v0.39.3 - 22.03.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.2...v0.39.3|compare v0.39.2...v0.39.3]]
** {{{django_tools.permissions.get_filtered_permissions}}} has new keyword argument: {{{exclude_actions}}}
* v0.39.2 - 22.03.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.1...v0.39.2|compare v0.39.1...v0.39.2]]
** NEW: {{{django_tools.parler_utils.parler_fixtures.ParlerDummyGenerator}}}
** NEW: {{{django_tools.fixture_tools.languages.iter_languages}}}
* v0.39.1 - 19.03.2018 - [[https://github.com/jedie/django-tools/compare/v0.39.0...v0.39.1|compare v0.39.0...v0.39.1]]
** NEW: {{{django_tools.unittest_utils.email.print_mailbox()}}}
** minor updates
* v0.39.0 - 02.03.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.9...v0.39.0|compare v0.38.9...v0.39.0]]
** NEW: Isolated Filesystem decorator / context manager
** Backwards-incompatible change: file renamed {{{django_tools/unittest_utils/{celery.py => celery_utils.py}}}}
** Skip run test with Django 1.8 and run tests with Django 1.11 and 2.0
* v0.38.9 - 05.02.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.8...v0.38.9|compare v0.38.8...v0.38.9]]
**  lowering log level on missing permissions from "error" to "debug"
* v0.38.8 - 05.02.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.7...v0.38.8|compare v0.38.7...v0.38.8]]
** send mail: use from celery import shared_task instead of djcelery_transactions
* v0.38.7 - 15.01.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.6...v0.38.7|compare v0.38.6...v0.38.7]]
** Add missing arguments (like "attachments", "cc" etc.) to {{{django_tools.mail.send_mail.SendMailCelery}}}
* v0.38.6 - 10.01.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.4...v0.38.5|compare v0.38.4...v0.38.5]]
** NEW: {{{./manage.py clear_cache}}}
** Display POST data in browser debug ({{{django_tools.unittest_utils.BrowserDebug.debug_response}}})
* v0.38.5 - 02.01.2018 - [[https://github.com/jedie/django-tools/compare/v0.38.4...v0.38.5|compare v0.38.4...v0.38.5]]
** NEW: Helper to assert django message framework output in unittests:
*** {{{BaseUnittestCase.get_messages()}}}: return a list of all messages
*** {{{BaseTestCase.assertMessages()}}}: compare messages
*** {{{BaseTestCase.assertResponse()}}}: has new keyword argument {{{messages}}}
** NEW: {{{BaseUnittestCase.assert_exception_startswith()}}}
* v0.38.4 - 28.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.38.3...v0.38.4|compare v0.38.3...v0.38.4]]
** Bugfix attach user group on existing user in: {{{django_tools.unittest_utils.user.get_or_create_user}}}
* v0.38.3 - 28.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.38.2...v0.38.3|compare v0.38.2...v0.38.3]]
** Bugfix: {{{unittest_utils.user.get_or_create_group}}} also removes obsolete permissions, too.
* v0.38.2 - 27.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.38.1...v0.38.2|compare v0.38.1...v0.38.2]]
** NEW: {{{./manage.py update_permissions}}}
* v0.38.1 - 21.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.38.0...v0.38.1|compare v0.38.0...v0.38.1]]
** refactor travis/tox/pytest/coverage stuff
** Tests can be run via {{{python3 setup.py tox}}} and/or {{{python3 setup.py test}}}
** Test also with pypy3 on Travis CI.
* v0.38.0 - 19.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.37.0...v0.38.0|compare v0.37.0...v0.38.0]]
** NEW: {{{django_tools.unittest_utils.user.get_or_create_group}}}
** NEW: {{{django_tools.unittest_utils.user.get_or_create_user}}}
** NEW: {{{django_tools.unittest_utils.user.get_or_create_user_and_group}}}
** NEW: {{{BaseUnittestCase.get_admin_change_url()}}} and {{{BaseUnittestCase.get_admin_add_url()}}}
** NEW: {{{BaseUnittestCase.assert_startswith()}}} and {{{BaseUnittestCase.assert_endswith()}}}
* v0.37.0 - 11.12.2017 - [[https://github.com/jedie/django-tools/compare/v0.36.0...v0.37.0|compare v0.36.0...v0.37.0]]
** Skip official support for python v2 (remove from text matrix)
** NEW: {{{./manage.py permission_info}}}: Display a list of all permissions for one django user
** NEW: {{{django_tools.permissions.get_filtered_permissions()}}} and {{{django_tools.permissions.pprint_filtered_permissions()}}}
** {{{django_tools.settings_utils.InternalIps}}} was renamed to {{{FnMatchIps}}} and can be also used for **ALLOWED_HOSTS**
** Bugfix/Enhance permission helpers
* v0.36.0 - 20.11.2017 - [[https://github.com/jedie/django-tools/compare/v0.35.0...v0.36.0|compare v0.35.0...v0.36.0]]
** NEW: {{{./manage.py database_info}}}
** Bugfix: **ModelPermissionMixin**
** Dynamic Sites is no longer maintained and tests are deactivated. It's currently not compatible with all django versions.
* v0.35.0 - 26.09.2017 - [[https://github.com/jedie/django-tools/compare/v0.34.0...v0.35.0|compare v0.34.0...v0.35.0]]
** CHANGE: The dummy image generation function in {{{django_tools.unittest_utils.mockup}}} has a new API.
* v0.34.0 - 18.09.2017 - [[https://github.com/jedie/django-tools/compare/v0.33.0...v0.34.0|compare v0.33.0...v0.34.0]]
** CHANGE: The test usernames changed and spaces was replace with underscores e.g.: "staff test user" -> "staff_test_user"
** Bugfix in mockup.create_pil_image: Created images has wrong sizes
* v0.33.0 - 11.07.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.14...v0.33.0|compare v0.32.14...v0.33.0]]
** Run tests only against Django v1.8 TLS and v1.11 TLS
** For Django 1.11: Add support for new-style middleware - contributed by benkonrath
** NEW: {{{django_tools.utils.request.create_fake_request()}}} for easier create a faked request object with {{{RequestFactory}}}
** NEW: {{{django_tools.utils.html_utils.html2text()}}} - Strip HTML tags with lxml Cleaner + Django 'strip_tags'
* v0.32.14 - 14.06.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.13...v0.32.14|compare v0.32.13...v0.32.14]]
** Bugfix for Python 2: {{{mock}}} backport package is needed and added to {{{setup.install_requires}}}
* v0.32.13 - 24.05.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.12...v0.32.13|compare v0.32.12...v0.32.13]]
** remove some warnings
* v0.32.12 - 04.05.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.11...v0.32.12|compare v0.32.11...v0.32.12]]
** NEW: {{{self.assertIn_dedent()}}} in {{{django_tools.unittest_utils.unittest_base.BaseUnittestCase}}}
* v0.32.11 - 02.05.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.10...v0.32.11|compare v0.32.10...v0.32.11]]
** Fix PyPi package mistake ({{{.tar.gz}}} archive contains {{{.tox}}} ;)
* v0.32.10 - 02.05.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.9...v0.32.10|compare v0.32.9...v0.32.10]]
** NEW: {{{django_tools.mail}}} to send text+html mails (see above)
* v0.32.9 - 21.03.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.8...v0.32.9|compare v0.32.8...v0.32.9]]
** Bugfix {{{DebugCacheLoader}}} if TemplateDoesNotExist was raised
* v0.32.8 - 16.03.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.7...v0.32.8|compare v0.32.7...v0.32.8]]
** NEW: {{{django_tools.template.loader.DebugCacheLoader}}} to add template name as html comments
** Change temp filename in BrowserDebug and use {{{django_tools_browserdebug_}}} prefix
** Bugfix in {{{django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware}}}
* v0.32.7 - 10.03.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.6...v0.32.7|compare v0.32.6...v0.32.7]]
** NEW: {{{django_tools.permissions}}} - helper for setup permissions
** NEW: {{{/unittest_utils/user.py}}} - helper for creating users (needfull in unittests)
* v0.32.6 - 22.02.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.5...v0.32.6|compare v0.32.5...v0.32.6]]
* {{{@task_always_eager()}}} decorator will set {{{CELERY_EAGER_PROPAGATES_EXCEPTIONS=True}}}, too.
* v0.32.5 - 10.02.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.4...v0.32.5|compare v0.32.4...v0.32.5]]
** NEW: Add {{{template_name}}} (optional) to {{{self.assertResponse()}}} (check with {{{assertTemplateUsed()}}})
* v0.32.4 - 01.02.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.3...v0.32.4|compare v0.32.3...v0.32.4]]
* Fix: Set "is_active" for created test users
* v0.32.3 - 25.01.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.2...v0.32.3|compare v0.32.2...v0.32.3]]
** Fix UnicodeDecodeError in BrowserDebug
** NEW: {{{@set_string_if_invalid()}}} decorator
** NEW: {{{@task_always_eager()}}} decorator
* v0.32.2 - 13.01.2017 - [[https://github.com/jedie/django-tools/compare/v0.32.1...v0.32.2|compare v0.32.1...v0.32.2]]
** NEW: django_tools.utils.url.GetDict
* v0.32.1 - 29.12.2016 - [[https://github.com/jedie/django-tools/compare/v0.32.0...v0.32.1|compare v0.32.0...v0.32.1]]
** NEW: TracebackLogMiddleware
* v0.32.0 - 19.12.2016 - [[https://github.com/jedie/django-tools/compare/v0.31.0...v0.32.0|compare v0.31.0...v0.32.0]]
** NEW: Management commands: 'nice_diffsettings', 'list_models'
** NEW: @display_admin_error to display silent errors in ModelAdmin.list_display callables.
** NEW: django_tools.template.render.render_template_file
** use [[https://pypi.python.org/pypi/pytest-django|pytest-django]]
** remove outdated stuff: See 'Backwards-incompatible changes' above.
* v0.31.0 - 03.11.2016 - [[https://github.com/jedie/django-tools/compare/v0.30.4...v0.31.0|compare v0.30.4...v0.31.0]]
** add Mockup utils to create dummy PIL/django-filer images with Text (see above)
** move tests into {{{/django_tools_tests/}}}
* v0.30.4 - 27.10.2016 - [[https://github.com/jedie/django-tools/compare/v0.30.2...v0.30.4|compare v0.30.2...v0.30.4]]
** add DjangoCommandMixin
* v0.30.2 - 05.10.2016 - [[https://github.com/jedie/django-tools/compare/v0.30.1...v0.30.2|compare v0.30.1...v0.30.2]]
** Bugfix Python 2 compatibility
* v0.30.1 - 26.08.2016 - [[https://github.com/jedie/django-tools/compare/v0.30.0...v0.30.1|compare v0.30.0...v0.30.1]]
** add: {{{django_tools.unittest_utils.disable_migrations.DisableMigrations}}} (see above)
** run tests also with django v1.10 and Python 3.5
** use tox
* v0.30.0 - 27.04.2016 - [[https://github.com/jedie/django-tools/compare/v0.29.5...v0.30.0|compare v0.29.5...v0.30.0]]
** Django 1.9 and Python 3 support contributed by [[https://github.com/jedie/django-tools/pull/9|naegelyd]]
* v0.29.4 and v0.29.5 - 10.08.2015 - [[https://github.com/jedie/django-tools/compare/v0.29.3...v0.29.5|compare v0.29.3...v0.29.5]]
** Some bugfixes for django 1.6 support
* v0.29.3 - 10.08.2015 - [[https://github.com/jedie/django-tools/compare/v0.29.2...v0.29.3|compare v0.29.2...v0.29.3]]
** Clear ThreadLocal request atttribute after response is processed (contributed by Lucas Wiman)
* v0.29.2 - 19.06.2015 - [[https://github.com/jedie/django-tools/compare/v0.29.1...v0.29.2|compare v0.29.1...v0.29.2]]
** Bugfix in unittest_utils.selenium_utils.selenium2fakes_response
** assertResponse used assertContains from django
** Add QueryLogMiddleware (TODO: add tests)
* v0.29.1 - 17.06.2015 - [[https://github.com/jedie/django-tools/compare/v0.29.0...v0.29.1|compare v0.29.0...v0.29.1]]
** Bugfixes for Py2 and Py3
** add StdoutStderrBuffer()
* v0.29.0 - 09.06.2015 - [[https://github.com/jedie/django-tools/compare/v0.26.0...v0.29.0|compare v0.26.0...v0.29.0]]
** WIP: Refactor unittests (DocTests must be updated for Py3 and more unittests must be written to cover all)
** catch more directory traversal attacks in BaseFilesystemBrowser (and merge code parts)
** Bugfix for "django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet." if using **UpdateInfoBaseModel**
** Bugfixes in **dynamic_site** for django 1.7
** add: [[https://github.com/jedie/django-tools/blob/master/django_tools/settings_utils.py|django_tools.settings_utils.InternalIps]]
* v0.28.0 - 12.02.2015 - [[https://github.com/jedie/django-tools/compare/v0.26.0...v0.28.0|compare v0.26.0...v0.28.0]]
** Work-a-round for import loops
** (new Version number, because of PyPi stress)
* v0.26.0 - 11.02.2015 - [[https://github.com/jedie/django-tools/compare/v0.25.1...v0.26.0|compare v0.25.1...v0.26.0]]
** Updates for Django 1.6 and Python 3
* v0.25.1 - 18.11.2013
** Bugfix: Fall back to "UTF-8" if server send no encoding info
* v0.25.0 - 28.08.2012
** Rename **cache.clear()** in SmoothCacheBackends to **cache.smooth_update()**, so that reset timestamp is independ from clear the cache.
* v0.24.10 - 24.08.2012
** Add **SmoothCacheBackends**: [[https://github.com/jedie/django-tools/blob/master/django_tools/cache/README.creole|./cache/README.creole]]
* v0.24.9 - 24.08.2012
** Bugfix in per-site cache middleware: set inital count values to None, if counting is disabled.
* v0.24.8 - 24.08.2012
** Enhanced **per-site cache middleware**: [[https://github.com/jedie/django-tools/blob/master/django_tools/cache/README.creole|./cache/README.creole]]
** Add **SetRequestDebugMiddleware**: [[https://github.com/jedie/django-tools/blob/master/django_tools/debug/README.creole|./debug/README.creole]]
* v0.24.7 - 21.08.2012
** Add the **per-site cache middleware** (see above)
** Add **import lib helper**: [[https://github.com/jedie/django-tools/blob/master/django_tools/utils/importlib.py|./utils/importlib.py]]
* v0.24.6 - 21.08.2012
** Add the **filemanager library** (see above)
* v0.24.5 - 06.08.2012
** Add **Print SQL Queries** context manager. (see above)
* v0.24.4 - 26.07.2012
** remove date from version string, cause of side-effects e.g.: user clone the repo and has the filter not installed
* v0.24.3 - 25.07.2012
** "Hardcode" the version string date attachment via [[https://github.com/jedie/python-code-snippets/tree/master/CodeSnippets/git|gitattribute filter script]] to fix [[https://github.com/jedie/django-tools/issues/1|a reported issues]] with [[https://github.com/pypa/pip/issues/145|pip requirements file bug]].
* v0.24.2 - 10.07.2012
** Split [[https://github.com/jedie/django-tools/blob/master/django_tools/models.py|UpdateInfoBaseModel()]]: So you can only set "createtime", "lastupdatetime" or "createby", "lastupdateby" or both types (This is backwards compatible)
* v0.24.1 - 12.06.2012
** Bugfix: UsergroupsModelField() and add unittests for it
** Add "normal users" in UsergroupsModelField()
** New: Add create_user() and create_testusers() to BaseTestCase
** Add a test project for the unittests. TODO: use this for all tests
* v0.24.0 - 04.06.2012
** [[https://github.com/jedie/django-tools/commit/a3cf1f7b2e9dbe4964306f4793c74f1782f8b2ea|Don't use auto_now_add and auto_now in UpdateInfoBaseModel]]
** Bugfix in [[https://github.com/jedie/django-tools/blob/master/django_tools/limit_to_usergroups.py|UsergroupsModelField]]
* v0.23.1
** [[https://github.com/jedie/django-tools/tree/master/django_tools/dynamic_site#dynamic-site-id|Dynamic Site]] would be only initialised if settings.USE_DYNAMIC_SITE_MIDDLEWARE = True
* v0.23.0
** Use cryptographic signing tools from django 1.4 in django_tools.utils.client_storage
* v0.22.0
** Add [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/static_path.py|static_path.py]] thats used settings.STATIC_ROOT.
** The old [[https://github.com/jedie/django-tools/blob/master/django_tools/fields/media_path.py|media_path.py]] which used settings.MEDIA_ROOT is deprecated and will be removed in the future.
** auto_add_check_unique_together() can use settings.DATABASES["default"]["ENGINE"], too.
* v0.21.1
** Bugfixes in [[https://github.com/jedie/django-tools/tree/master/django_tools/dynamic_site#dynamic-site-id|Dynamic Site]].
* v0.21.0beta
** New: site alias function
** refractory 'DynamicSiteMiddleware' to a own app (**Backwards-incompatible change:** change your settings if you use the old DynamicSiteMiddleware.)
* v0.20.1
** New: [[https://github.com/jedie/django-tools/blob/master/django_tools/views/csrf.py|debug_csrf_failure()]] to display the normal debug page and not the minimal csrf debug page.
* v0.20.0
** Add experimental [[https://github.com/jedie/django-tools/blob/master/django_tools/middlewares/DynamicSite.py|DynamicSiteMiddleware]], please test it and give feedback.
* v0.19.6
** Add some south introspection rules for LanguageCodeModelField and jQueryTagModelField
** fallback if message for anonymous user can't created, because django.contrib.messages middleware not used.
** Bugfix in django_tools.utils.messages.StackInfoStorage
* v0.19.5
** Add http://bugs.python.org/file22767/hp_fix.diff for https://github.com/gregmuellegger/django/issues/1
* v0.19.4
** Bugfix for PyPy in local_sync_cache get_cache_information(): sys.getsizeof() not implemented on PyPy
** Bugfix in template.filters.chmod_symbol()
** Nicer solution for template.filters.human_duration()
* v0.19.3
** Add support for https in utils/http.py
* v0.19.2
** Bugfix in utils/http.py timeout work-a-round
* v0.19.1
** utils/http.py changes:
*** Use a better solution, see:
*** Add timeout and add a work-a-round for Python < 2.6
* v0.19.0
** NEW: Add utils/http.py with helpers to get a webpage via http GET in unicode
** Change README from textile to creole ;)
* v0.18.2
** Bugfix: Add missing template in pypi package
* v0.18.0
** NEW: Add DOM compare from Gregor M??llegger GSoC work into unittest utils.
* v0.17.1
** Bugfix in ???limit_to_usergroups???: Make choices ???lazy???: Don???t access the database in //init//
* v0.17
** Add the script ???upgrade_virtualenv.py???
** Add ???limit_to_usergroups???
** Add ???local sync cache???
** Add models.UpdateInfoBaseModel
** Update decorators.render_to
** render_to pass keyword arguments to render_to_response() (e.g.: mimetype=???text/plain???)
** new argument ???skip_fail??? in get_filtered_apps(): If True: raise excaption if app is not importable
* v0.16.4
** Bugfix: {{{get_db_prep_save() got an unexpected keyword argument 'connection???}}} when save a SignSeparatedModelField()
* v0.16.3
** Update BrowserDebug: Use response.templates instead of response.template and make output nicer
* v0.16.2
** Merge stack info code and display better stack info on browser debug page
* v0.16.1
** Update django_tools.utils.messages.StackInfoStorage for django code changes.
* v0.16.0
** NEW: path model field (check if direcotry exist)
* v0.15.0
** NEW: Add a flexible URL field (own validator, model- and form-field)
* v0.14.1
** Bugfix: make path in MediaPathModelField relativ (remove slashes)
* v0.14
** NEW: django-tagging addon: Display existing tags under a tag field
* v0.13
** Bugfix UnicodeEncodeError in Browser debug
* v0.12
** NEW: django_tools.utils.messages.failsafe_message
* v0.11
** NEW: Store data in a secure cookie, see: utils/client_storage.py
* v0.10.1
** New: Display used templates in unittest BrowserDebug
** Bugfix: catch if last usermessages exist
* v0.10.0
** NEW: utils around django messages, see: /django_tools/utils/messages.py
* v0.9.1
** Bugfix: database column was not created: don???t overwrite get_internal_type()
* v0.9
** New: stuff in /django_tools/fields/
** see also backwards-incompatible changes, above!
* v0.8.2
** New: widgets.SelectMediaPath(): Select a sub directory in settings.MEDIA_ROOT
** New: fields.SignSeparatedField()
* v0.8.1
** Add ???no_args??? keyword argument to installed_apps_utils.get_filtered_apps()
* v0.8.0
** Add model LanguageCode field and form LanguageCode field in Accept-Language header format (RFC 2616)
* v0.7.0
** Add decorators.py
* v0.6.0
** Add forms_utils.LimitManyToManyFields, crosspost: http://www.djangosnippets.org/snippets/1691/
* v0.5.0
** Add template/filters.py from PyLucid v0.8.x
* v0.4.0
** Add experimental ???warn_invalid_template_vars???
* v0.3.1
** Bugfix: Exclude the instance if it was saved in the past.
* v0.3.0
** Add utils.installed_apps_utils
* v0.2.0
** Add models_utils, see: http://www.jensdiemer.de/_command/118/blog/detail/67/ (de)
* v0.1.0
** first version cut out from PyLucid CMS ??? http://www.pylucid.org


== links ==

| Homepage   | https://github.com/jedie/django-tools
| PyPi       | https://pypi.python.org/pypi/django-tools/


== donation ==

* [[https://www.paypal.me/JensDiemer|paypal.me/JensDiemer]]
* [[https://flattr.com/submit/auto?uid=jedie&url=https%3A%2F%2Fgithub.com%2Fjedie%2Fdjango-tools%2F|Flattr This!]]
* Send [[https://www.bitcoin.org/|Bitcoins]] to [[https://blockexplorer.com/address/1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F|1823RZ5Md1Q2X5aSXRC5LRPcYdveCiVX6F]]
