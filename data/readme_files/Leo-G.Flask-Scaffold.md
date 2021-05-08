Flask-Scaffold 2.0 let's you Prototype Database Driven Web Apps (Angular 6, Bootstrap 4) and REST API's  (Flask python framework), 



![](https://i.imgur.com/GeZ9vAB.png)
![](https://i.imgur.com/XHpxJrM.png)
![](https://i.imgur.com/RpsXaoe.png)

Features include

 - Python 3 Support
 - RESTFUL JSON API
 - Continous Integration with Travis-CI
 - Inbuilt User Management and Admin Dashboard
 - [Google Analytics](#google-analytics)
 - Datatables support

###[Demo](http://flaskscaffold.cloudapp.net) Sign Up and Login


###Installation

Please ensure that development libraries for [PostgreSQL](http://techarena51.com/blog/flask-sqlalchemy-postgresql-tutorial/) are installed
along with NPM.

####Step 1:Clone the project to your application folder.

    git clone git@github.com:Leo-g/Flask-Scaffold.git YourAppFolderName && cd YourAppFolderName

####Step 2: Install the requirements and add your Database configuration details.

    pip install -r requirements.txt
    cd app/templates/static
    npm install

    vim config.py
    #Fill in your database username, password, name, host etc


#### Step 3 : Declare your Resource and it's fields in a YAML file as follows

For a list of supported fields please see https://github.com/Leo-g/Flask-Scaffold/wiki/Fields

    vim scaffold/blog.yaml
    posts:
     - title:string
     - body:text
     - author:string
     - creation_date:datetime
     - published:boolean
    comments:
     - author:string
     - body:text
     - author_url:url
     - created_on:date
     - approved:boolean
    authors:
     - name:string
     - profile:text
     - url:url

#### Step 4 : Run the Scaffolding  and database migrations script

    python scaffold.py scaffold/blog.yaml
    python db.py db init
    python db.py db migrate
    python db.py db upgrade

####  Step 5 : Run the Server

    python run.py

**You should be able to see the Login Page at http://localhost:5000, Sign Up and Login



####For unit testing with python Unit tests

    For a Single module

    python app/<module_name>/test_<module_name>.py

    For all modules

    bash tests.bash

###API

API calls can be made to the following URL

Note: This example is for a Post module

| HTTP Method  | URL  | Results |
| :------------ |:---------------:| -----:|
| GET      | http://localhost:5000/api/v1/posts.json | Returns a list of all Posts |
| POST     | http://localhost:5000/api/v1/posts.json      |   Creates a New Post |
| GET | http://localhost:5000/api/v1/posts/1.json      | Returns details for the a single Post |
| PATCH | http://localhost:5000/api/v1/posts/1.json      | Update a Post |
| DELETE | http://localhost:8001/api/v1/posts/1.json      | Delete a Post |

The JSON format follows the spec at jsonapi.org and a sample is available in the sample.json   file

###Tutorials
https://techarena51.com/blog/buidling-a-database-driven-restful-json-api-in-python-3-with-flask-flask-restful-and-sqlalchemy/?utm_source=gh-flask-scaffold-readme

https://techarena51.com/blog/tag/flask-tutorials/?utm_source=gh-flask-scaffold-readme

###Directory Structure
        Project-Folder
            |-- config.py
            |--run.py
            |--requirements.txt
            |--conf.js
            |__ /venv
            |-- db.py
            |__ /scaffold
            |-- scaffold.py
            |-- tests.bash    #Tests for all modules
            |__ app/
                |-- __init__.py
                +-- module-1
                    |-- __init__.py
                    |-- models.py
                    |-- test_module-1.py  # Unit Tests for module 1
                    |-- views.py
                        
                +-- module-2
                    |-- __init__.py
                    |-- models.py
                    |-- test_module-2.py  # Unit Tests for module 2
                    |-- views.py
                |__ templates
                   +-- static
                          + -- js
                                 |-- app.js
                                 |-- login.js
                          |-- css
                          |-- images
                   +-- module-1
                                   |-- _form.html
                                   |-- index.html
                                   |-- add.html
                                   |-- update.html
                                   |-- controller.js
                                   |--conf.js
                                   |--spec.js
                   +-- module-2
                                   |-- _form.html
                                   |-- index.html
                                   |-- add.html
                                   |-- update.html
                                   |-- controller.js
                                   |-- conf.js
                                   |-- spec.js


## Google Analytics

Add your tracking ID and Domain name in app.js in the app.config  section

      app.config(function (AnalyticsProvider) {
                  // Set a single account
                  AnalyticsProvider.setAccount('UA-XXXXX-xx');
                  AnalyticsProvider.setDomainName('XXX');

       });


For complete Documentation see the [wiki](https://github.com/Leo-G/Flask-Scaffold/wiki/Add-Google-Analytics-to-Angularjs-UI-Routes)

Note: This app in based on https://github.com/start-angular/SB-Admin-BS4-Angular-6