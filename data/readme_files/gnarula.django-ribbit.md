django-ribbit
=============

Ribbit - A Twitter Clone made using Django

A live demo of the app can be found at http://vast-earth-7154.herokuapp.com/

***

To set the application locally, first clone the repo

```  
git clone https://github.com/gnarula/django-ribbit.git
```

Make a virtual environment

```
virtualenv --no-site-packages ribbit_env
```
  
With the the virtual environment activated, install the dependencies

```
pip install Django South
```
  
Next, `cd` into the repository and run the `syncdb` command to create the tables and superuser account

```
python manage.py syncdb
```

Then, apply the migrations

```
python manage.py migrate ribbit_app
```
  
Finally, start the development server to preview the application

```
python manage.py runserver
```
