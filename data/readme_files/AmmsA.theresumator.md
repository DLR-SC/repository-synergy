# theresumator  <sub><sup><sub> using [django-resumator](https://github.com/AmmsA/django-resumator/)</sup></sub></sup>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Need a web resume? theresumator is a Django project for creating resumes dedicated to people in computer science/engineering. It's built to be lightweight, simple, organized enough to be reusable by other people in other fields, and easily configured for your needs.

Currently, theresumator supports the following models: 
* Resume (a link to your PDF resume, if specified)
* Education (for your education info)
* Projects (Personal or work projects you worked on)
* Experience (Your work/research experience)
* Publications (research papers you've published or contributed to)

Need a live example of how it looks like? click [here](https://django-resumator.herokuapp.com/) to see a sample.  (note: may take awhile because it's under heroku's free plan)
[![](https://cloud.githubusercontent.com/assets/748271/11058151/802d9360-8745-11e5-87db-e91806c8a8c4.png)](https://django-resumator.herokuapp.com/)

## How to deploy
1. Click on the deploy to Heroku button above.
2. Name your application (e.g. `https://<NAME>.herokuapp.com`). You can change it to have use your own domain but that's a little tricky. Please look at the heroku documentation for more information on how to do it.
![](https://raw.githubusercontent.com/AmmsA/theresumator/master/github_images/app_name.png)
3. Write down a username and password for your app. This is going to be used for accessing the admin page (e.g. `https://<app_name>.herokuapp.com/admin`) to change and update your resume.
![](https://raw.githubusercontent.com/AmmsA/theresumator/master/github_images/passwords.png)
4. Click on the deploy button and wait for the application to be built and deployed.
5. After you've successfully deployed the app, from your heroku app page, go under the settings and click on the reveal config vars button and make sure you delete the `ADMIN_PASSWORD` and `ADMIN_USER` config variables as they are no longer needed.
![](https://raw.githubusercontent.com/AmmsA/theresumator/master/github_images/config_vars.png)


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

All parts of theresumator are free to use and abuse under the [open-source MIT license](https://github.com/AmmsA/theresumator/blob/master/LICENSE).

