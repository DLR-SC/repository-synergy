
# reddit_utils

A collection of reddit utility scripts organized as a self-hosted web app. Currently the following features are available:

* Search through your saved posts (submissions/comments)
* Search through posts that you've made (submissions/comments)
* Ability to fetch your subreddits

<img src="https://i.imgur.com/ErmXBLv.png" width="909">

<center>

| <img src="https://i.imgur.com/I2yUn5j.gif" width="260"/> | <img src="https://i.imgur.com/PmxrN3G.png" width="260"/> | <img src="https://i.imgur.com/YZ0ggwN.png" width="260"/> |
|:--------------------------------------------------------:|:--------------------------------------------------------:|:--------------------------------------------------------:|
| GIF of Search Interface | Looking at Saved Posts | Trying the List Subreddits feature |

</center>

## Install Process

1. Clone the repository to your local machine
1. Make sure Python 3.5+ is installed
1. Build a `.whl` (wheel) file
1. Set up a virtual environment
1. Install the `.whl` file
1. Run the flask app 
1. Open [http://localhost:5000](http://localhost:5000) in browser

[Full instructions can be found here](http://flask.pocoo.org/docs/1.0/tutorial/deploy/#build-and-install)

Note: This web app is meant to be self-hosted on something like a [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)

## Development Process

This web app is built on [Flask](http://flask.pocoo.org/) + [Bootstrap 4](http://getbootstrap.com/) + [PRAW](https://github.com/praw-dev/praw)

Here are the general instructions:

1. Create a virtual environment
1. Make changes to code
1. Run the flask app

Specific instructions for Windows PowerShell:

```
>>> git clone https://github.com/roman-ku/reddit_utils.git
>>> cd reddit_utils
>>> virtualenv env
>>> ./env/Scripts/activate
>>> pip install -r requirements.txt
>>> $env:FLASK_ENV = "development"
>>> $env:FLASK_APP = "reddit_utils"
>>> flask run
```

Here are some helpful links that provide more detail:

* https://virtualenv.pypa.io/en/stable/userguide/
* http://flask.pocoo.org/docs/1.0/tutorial/factory/#run-the-application
* http://flask.pocoo.org/docs/1.0/tutorial/install/#install-the-project

## Contributions

Contributions to this project are welcome. If you contribute to the project, your name will appear on the about page.

Helped wanted with the following:

* Change login procedure to use [web app](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#web-application) procedure instead of the [script procedure](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application)
* Add HTTPS support
* Loading indicator
* Persist saved posts for faster searching
* Ability to have multiple search terms (underlying code is there but needs GUI)
* Ability to restrict search by subreddit (underlying code is there but needs GUI)
* <del>Ability to search your own submissions -> Added 2/14/2019</del>
* Ability to search past the 1000 item limit
* Ability to unhide all your posts
* Ability to export your saved posts in various formats
* For really long comments (only show the first few paragraphs or so, collapse the rest)
* Highlight search terms in results (something like [this](https://markjs.io/))

I will slowly add features as I need them and I encourage people to do the same

## To Add Your Own Feature

1. Add it to the nav bar (file: `templates/nav.htm.j2`)
1. Create a usage/help modal (file: `templates\modals.htm.j2`)
1. Create a template file for the feature (create file in: `templates\features`)
1. Write the backend Python code (put code in: `features`)
1. Add your entry point function to the init file (file: `__init__.py`)

Please use the `Search Saved Posts` and `List Subreddits` features as examples

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Disclaimer

The developer (Roman Kuleshov) of this application (reddit_utils) has no affiliation with Reddit Inc.
