#GAE Angular Material Starter
#####Easiest way to start Google App Engine Angular Material project on Earth & Mars!
As a base for this I've used starter projects [gae-init] and [MEANJS], so big thanks to them!

This full stack uses following technologies:
* Google App Engine
* Python Flask
* AngularJS
* Angular Material
* Gulp, Bower, npm

######You can see live demo here: https://gae-angular-material-starter.appspot.com/

##What's implemented?
* Everything about user authentication - signin, signup, forgot pass, reset pass ... and all the boring stuff is done for you :)
* Authentication with 11 different OAuth sites (Facebook, Twitter, etc.)
* User profile pages - users can view/edit their profiles
* Users list
* Admin Interface - admin can edit app config, edit/delete/block users, etc.
* "Send Feedback" page
* Ability to generate mock data, while developing
* Integration with no-captcha
* Tracking with Google Analytics
* Lots of useful angular directives and services

##What do I need?
First make sure you've got following things installed on your machine:
* [Google App Engine SDK for Python][]
* [Node.js][]
* [pip][]
* [virtualenv][]

##Install!
Using yeoman:
```
sudo npm install -g generator-gae-angular-material-starter
mkdir myNewApp && cd myNewApp
yo gae-angular-material-starter  # it will ask you few questions, e.g your app name, etc.
gulp run
```

Using github:
```
git clone https://github.com/madvas/gae-angular-material-starter
cd gae-angular-material-starter
npm install
gulp run
```
And that's it! You should now see the app running on port 8080.
You can now sign in via Google, or you can click "Generate Database" and then sign in as "admin" with password "123456"

##Deploy!
When you're done with your beautiful Material Design app it's time to deploy!
First, make sure you change your application name in `app.yaml`
```
gulp build
appcfg.py update main
```
And that's it! Your next big thing is out!

##What's left to do?
* Tests - soon to be done
* Docs/Tutorial - Although, docs doesn't exist yet, code is heavily commented, so you know what's going on :)

##Contribute!
Sure you can :)

License
--
MIT. Can't be more open, source ;)

[google app engine sdk for python]: https://developers.google.com/appengine/downloads
[node.js]: http://nodejs.org/
[pip]: http://www.pip-installer.org/
[virtualenv]: http://www.virtualenv.org/
[gae-init]: https://github.com/gae-init/gae-init
[meanjs]: https://github.com/meanjs/mean
