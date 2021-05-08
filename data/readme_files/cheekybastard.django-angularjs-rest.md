
Please Note: Project is not working as yet.

Under Construction


django-angularjs-rest
=====================

Django + AngularJS + Django-Rest-Framework + Twitter Bootstrap(angular-ui) project starter/demo.

<h1>Angular-UI Bootstrap</h1>
https://github.com/angular-ui/bootstrap
    "aiming at providing a set of AngularJS directives based on Twitter's bootstrap markup and CSS. The goal is to provide native AngularJS directives without any dependency on jQquery or Bootstrap's JavaScript. It is often better to rewrite an existing JavaScript code and create a new, pure AngularJS directive. Most of the time the resulting directive is smaller as compared to the orginal JavaScript code size and better integrated into the AngularJS ecosystem."

Why replace bootstrap jquery?
    For me, AngularJS applications are noticeably quicker then other JS frameworks ( aka. Snappy app reactions are sexy).
    http://jsperf.com/angular-vs-knockout-vs-ember/2

$$$$$$$$$$ angularJS $$$$$$$$$$$$$$$

http://docs.angularjs.org/api/ngResource.$resource

A factory which creates a resource object that lets you interact with RESTful server-side data sources.
The returned resource object has action methods which provide high-level behaviors without the need to interact with the low level $http service.

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

<h1>Behaviour-driven development with Salad: aka Lettuce & Splinter</h1>

    https://github.com/wieden-kennedy/salad
    https://github.com/gabrielfalcao/lettuce
    http://github.com/cobrateam/splinter/
    
    http://cilliano.com/blog/2011/02/07/django-bdd-with-lettuce-and-splinter/
    http://lettuce.it/
    http://splinter.cobrateam.info/docs/

Test of Django Project Example:
    https://github.com/gabrielfalcao/lettuce/tree/master/tests/integration/django/alfaces/

<h3>Run Test</h3>
Example:
    user@machine:~projects/djangoproject $ python manage.py harvest

<h3>Specifying feature files</h3>
Example:
    user@machine:~projects/djangoproject $ python manage.py harvest path/to/my-test.feature

<h1>devserver runserver commands:</h1>
https://github.com/dcramer/django-devserver

    --werkzeug 	Tells Django to use the Werkzeug interactive debugger, instead of it's own.
    --forked 	Use a forking (multi-process) web server instead of threaded.
    --dozer 	Enable the dozer memory debugging middleware (at /_dozer)
    --wsgi-app 	Load the specified WSGI app as the server endpoint.

<h1>iPython shell_plus & Notebook</h1>
shell_plus = Django shell with autoloading of the apps database models

<h3>ipython notebook:</h3>
interactive Python shell with web browser as user interface, code & results can be saved to notebooks.
Apps database models are autoloading.
http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
    ./manage.py shell_plus --notebook

    requirements:
        ipython
        django_extensions  #imports django app models into ipython notebook
        tornado
        pip install pyzmq --install-option="--zmq=bundled"

<h1>Copyright and license</h1>

    The MIT License

    Copyright (c) 2012 CheekyBastard

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
