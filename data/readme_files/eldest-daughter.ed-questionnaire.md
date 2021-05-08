ED Questionnaire
=====================

Current Status
------------
This project is no longer being actively maintained. I will merge non-conflicting PRs, but otherwise consider this project sunset.

Introduction
------------

ED Questionnaire is a Django questionnaire app which is easily customizable
and includes advanced dependency support using boolean expressions.

It allows an administrator to create and edit questionnaires in the Django
admin interface, with support for multiple languages.

History
-------

The questionnaire app was originally developed by [Seantis](https://github.com/seantis), itself derived from [rmt](https://github.com/rmt). We picked up the project because we had been using it and the Seantis version had entered a steady state of development. There are several feature changes we wanted and decided to head up the maintenance ourselves.

The old versions are tagged as follows:

 * tag 1.0 - state of last commit by the original developer (rmt)
 * tag 1.1 - contains merged changes by other forks improving the original
 * tag 2.0 - original updated trunk from Seantis version
 * tag 2.5 - contains the original Seantis version and all PRs merged in as of 12/09/15. It's considered to be the backwards compatible version of the repository.

The new version is the current trunk and is dubbed v3.0. It should be considered a new project and thus will contain backwards incompatible changes. When possible, we'll try and backport fixes to the v2.x branches, but it will not be a priority.

About this Manual
-----------------

ED Questionnaire is not a very well documented app so far to say the least. This manual should give you a general idea of the layout and concepts of it, but it is not as comprehensive as it should be.

What it does cover is the following:

 * **Integration** lays out the steps needed to create a new Django app together with the questionnaire. The same steps can be used to integrate the questionnaire into an existing site (though you would be entering unpaved ways).
 * **Concepts** talks about the data model and the design of the application.
 * **Migration** explains how a questionnaire defined with 1.0 can be used in 2.0.
 * **2.0 Postmortem** talks about some experiences made during the development of 2.0.

Integration
-----------

This part of the docs will take you through the steps needed to create a questionnaire app from scratch. It should also be quite handy for the task of integrating the questionnaire into an existing site.

First, create a folder for your new site:

    mkdir site
    cd site

Create a virtual environment so your python packages don't influence your system
    
    virtualenv --no-site-packages -p python2.7 .

Activate your virtual environment

    source bin/activate

Install Django and other dependencies

    pip install django unicodecsv

Create your Django site

    django-admin.py startproject mysite

Create a place for the questionnaire

    cd mysite
    mkdir apps
    cd apps

Clone the questionnaire source

    git clone git://github.com/eldest-daughter/ed-questionnaire.git

You should now have a ed-questionnaire folder in your apps folder

    cd ed-questionnaire

The next step is to install the questionnaire.

    python setup.py install

If you are working with ed-questionnaire from your own fork you may want to use `python setup.py develop` instead, which will save you from running `python setup.py install` every time the questionnaire changes.

Now let's configure your basic questionnaire.

First, you want to setup the languages used in your questionnaire. Open up your `mysite` folder in your favorite text editor.

Open `mysite/mysite/settings.py` and add following lines, representing your languages of choice:

    LANGUAGES = (
        ('en', 'English'),
        ('de', 'Deutsch')
    )

At the top of `settings.py` you should at this point add:

    import os.path

We will use that below for the setup of the folders.

In the same file add the questionnaire static directory to your STATICFILES_DIRS:

    STATICFILES_DIRS = (
    os.path.abspath('./apps/ed-questionnaire/questionnaire/static/'),
    )

Also add the locale and request cache middleware to MIDDLEWARE_CLASSES:

    'django.middleware.locale.LocaleMiddleware',
    'questionnaire.request_cache.RequestCacheMiddleware',

If you are using Django 1.7 you will need to comment out the following line, like so:
    # 'django.middleware.security.SecurityMiddleware',
otherwise you will get an error when trying to start the server.

Add the questionnaire template directory as well as your own to TEMPLATE_DIRS:

    os.path.abspath('./apps/ed-questionnaire/questionnaire/templates'),
    os.path.abspath('./templates'),

And finally, add `transmeta`, `questionnaire` to your INSTALLED_APPS:

    'django.contrib.sites',
    'transmeta',
    'questionnaire',
    'questionnaire.page',

To get the "sites" framework working you also need to add the following setting:

    SITE_ID = 1

Next up we want to edit the `urls.py` file of your project to link the questionnaire views to your site's url configuration.

For an empty site with enabled admin interface you add:

    from django.conf.urls import patterns, include, url

    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        
        # questionnaire urls
        url(r'q/', include('questionnaire.urls')),
        
        url(r'^take/(?P<questionnaire_id>[0-9]+)/$', 'questionnaire.views.generate_run'),
        url(r'^$', 'questionnaire.page.views.page', {'page_to_render' : 'index'}),
        url(r'^(?P<lang>..)/(?P<page_to_trans>.*)\.html$', 'questionnaire.page.views.langpage'),
        url(r'^(?P<page_to_render>.*)\.html$', 'questionnaire.page.views.page'),
        url(r'^setlang/$', 'questionnaire.views.set_language'),
    )

Having done that we can initialize our database. (For this to work you must have setup your DATABASES in `settings.py`.). First, in your CLI navigate back to the `mysite` folder:

    cd ../..

The check that you are in the proper folder, type `ls`: if you can see `manage.py` in your list of files, you are good. Otherwise, find your way to the folder that contains that file. Then type:

    python manage.py syncdb
    python manage.py migrate

The questionnaire expects a `base.html` template to be there, with certain stylesheets and blocks inside. Have a look at `./apps/ed-questionnaire/example/templates/base.html`.

For now you might want to just copy the `base.html` to your own template folder.

    mkdir templates
    cd templates
    cp ./apps/ed-questionnaire/example/templates/base.html .

Congratulations, you have setup the basics of the questionnaire! At this point this site doesn't really do anything, as there are no questionnaires defined.

To see an example questionnaire you can do the following (Note: this will only work if you have both English and German defined as Languages in `settings.py`):

    python manage.py loaddata ./apps/ed-questionnaire/example/fixtures/initial_data.yaml

You may then start your development server:

    python manage.py runserver

And navigate to [localhost:8000](http://localhost:8000/).

Concepts
--------

The ED Questionnaire has the following tables, described in detail below.

 * Subject
 * RunInfo
 * RunInfoHistory
 * Question
 * Choice
 * QuestionSet
 * Questionnaire
 * Answer

### Subject

A subject is someone filling out a questionnaire. 

Subjects are primarily useful in a study where the participants answer a questionnaire repeatedly. In this case a subject may be entered. Whoever is conducting the study (i.e. the person running the questionnaire app), may then periodically send emails inviting the subjects to fill out the questionnaire.

Sending Emails is covered in detail later.

Of course, not every questionnaire is part of a study. Sometimes you just want to find out what people regard as more awesome: pirates or ninjas*? 

*(it's pirates!)

Though a poll would be a better choice for this example, one can find the answer to that question with ED Questionnaire by using an anonymous subject. The next chapter *Questionnaire* will talk about that in more detail.

### RunInfo

A runinfo refers to the currently active run of a subject.

A subject who is presently taking a questionnaire is considered to be on a run. The runinfo refers to that run and carries information about it.

The most important information associated with a runinfo is the subject, a random value that is used to generate the unique url to the questionnaire, the result of already answered questions and the progress.

Once a run is over it is deleted with some information being carried over to the RunInfoHistory.

Runs can be tagged by any number of comma separated tags. If tags are used, questions can be made to only show up if the given tag is part of the RunInfo.

### RunInfoHistory

The runinfo history is used to refer to a set of answers.

### Question

A question is anything you want to ask a subject. There are a number of different types you can use:

 * **choice-yesno** - Yes or No
 * **choice-yesnocomment** - Yes or No with a chance to comment on the answer
 * **choice-yesnodontknow** - Yes or No or Whaaa?
 * **open** - A simple one line input box
 * **open-textfield** - A box for lengthy answers
 * **choice** - A list of choices to choose from
 * **choice-freeform** - A list of choices with a chance to enter something else
 * **choice-multiple** - A list of choices with multiple answers
 * **choice-multiple-freeform** - Multiple Answers with multiple user defined answers
 * **range** - A range of number from which one number can be chosen
 * **number** - A number
 * **timeperiod** - A timeperiod
 * **custom** - Custom question using a custom template
 * **comment** - Not a question, but only a comment displayed to the user
 * **sameas** - Same type as another question

*Some of these types, depend on checks or choices. The number question for instance can be controlled by setting the checks to something like `range=1-100 step=1`. The range question may also use the before-mentioned checks and also `unit=%`. Other questions like the choice-multiple-freeform need a `extracount=10` if ten extra options should be given to the user.

I would love to go into all the details here but time I have not so I my only choice is to kindly refer you to the qprocessor submodule which handles all the question types.*

Next up is the question number. The question number defines the order of questions alphanumerically as long as a number of questions are shown on the same page. The number is also used to refer to the question.

The text of the question is what the user will be asked. There can be one text for each language defined in the `settings.py` file.

The extra is an additional piece of information shown to the user. As of yet not all questions support this, but most do.

An important aspect of questions (and their parents, QuestionSets) is the checks field. The checks field does a lot of things (possibly too many), the most important of which is to define if a certain question or questionset should be shown to the current subject.

The most important checks on the question are the following:

 * **required** A required question must be answered by the user
 * **requiredif="number,answer"**  Means that the question is required if the question with *number* is equal to *answer*.
 * **shownif** Same as requiredif, but defining if the question is shown at all.
 * **maleonly** Only shown to male subjects
 * **femaleonly** Only shown to female subjects
 * **iftag="tag"** Question is only shown if the given tag is in the RunInfo

Checks allow for simple boolean expressions like this:
`iftag="foo or bar"` or `requiredif="1,yes and 2,no"`

### Choice

A choice is a possible value for a multiple choice question.

### QuestionSet

A number of questions together form a questionset. A questionset is ultimately single page of questions. Questions in the same questionset are shown on the same page.

QuestionSets also have checks, with the same options as Questions. There's only one difference, **required** and **requiredif** don't do anything.

A questionset which contains no visible questions (as defined by **shownif**) is skipped.

### Answer

Contains the answer to a question. The value of the answer is stored as JSON.

### Questionnaire 

A questionnaire is a group of questionsets together.


Migration of 1.x to 2.0
-----------------------

2.0 added new fields to the questionnaire, but it did so in a backwards compatible way. None of the new fields are mandatory and no changes should be necessary to your existing questionnaire. Since we do not have any relevant testing data however, you might find yourself on your own if it doesn't work. Please file an issue if you think we did something wrong, so we can fix it and help you.

As Django per default does not provide a way to migrate database schemas, we pretty much make use of the bulldozer way of migrating, by exporting the data from one database and import it into a newly created one.

From you existing 1.x site do:

    python manage.py dumpdata >> export.yaml

Copy your file to your new site and in your new site, create your empty database:

    python manage.py syncdb

You may then import your data from your old site, which should probably work :)

    python manage.py loaddata export.yaml

This of course covers only the data migration. How to migrate your custom tailored site to use questionnaire 2.0 is unfortunately something we cannot really document.

2.0 Postmortem
--------------

2.0 was the result of the work we put into Seantis questionnaire for our second project with it. We did this project without the help of the questionnaire's creator and were pretty much on our own during that time.

Here's what we think we learned:

### ED.questionnaire is a Framework

More than anything else ed.questionnaire should be thought of as a framework. Your site has to provide and do certain things for the questionnaire to work. If your site is a customized questionnaire for a company with other needs on the same site you will end up integrating code which will call questionnaire to setup runs and you will probably work through the answer records to provide some sort of summary.

If it was a library you could just work with a nice API, which does not exist.

### Don't Go Crazy with Your Checks

We used a fair amount of checks in both questionset and questions to control a complex questionnaire. We offloaded the complexity of the questionnaire into an Excel file defined by the customer and generated checks to copy that complexity into our application.

Though this approach certainly works fine it does not give you a good performance. The problem is, if you have hundreds of questions controlled by runinfo tags, that you end up with most CPU cycles spent on calculating the progress bar on each request. It is precisely for that reason that we implemented the QUESTIONNAIRE_PROGRESS setting (you can learn more about that by looking at the example settings.py).

We managed to keep our rendering time low by doing the progress bar using AJAX after a page was rendered. It is only a workaround though. Calculating the progress of a run in a huge questionnaire remains a heavy operation, so for really huge questionnaires one might consider removing the progress bar altogether. There is still some optimization to be made, but it essentially will remain the slowest part of the questionnaire, because at the end of the day interpreting loads of checks is not something you can do in a fast way, unless your name is PyPy and your programmers are insanely talented.

### There are not Enough Tests

There are a few that do some simple testing, but more are needed. More tests would also mean that more refactoring could be done which would be nice, because there certainly is a need for some refactoring.

### The Admin Interface is not Good Enough

Django admin is a nice feature to have, but we either don't leverage it well enough, or it is not the right tool for the questionnaire. In any case, if you are expecting your customer to work with the questionnaire's structure you might have to write your own admin interface. The current one is not good enough.


