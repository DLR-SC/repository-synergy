A blank Flask app template using MongoDB.

Requirements:
* Python
* MongoDB
* Flask Framework http://flask.pocoo.org
* PyMongo (pip install pymongo==2.8)
* MongoEngine http://mongoengine.org
* Flask Bcrypt extension for encrypting your login passwords (pip install flask-bcrypt)
* Flash CSRF extension for protecting you app against cross-site forgery (pip install flask-csrf)
* Apache + mod_wsgi (optional)

Initial data:
* To use this app you first need to enter some data [manually] into MongoDB for Post model using the "tumblelog" database (see models.py).
* You will also need to create a user if you want to use the login/logout views. Create the user manually and use python's bcrypt module to create a password.
