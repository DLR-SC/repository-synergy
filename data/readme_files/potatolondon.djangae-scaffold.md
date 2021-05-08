{% if False %}
# The Djangae Project Template

This is a barebones Django project template configured for use on App Engine using [Djangae](https://github.com/potatolondon/djangae)


## How to use this to create your project

To get started:

- Install any supported Django version (`$ pip install Django==1.11`)
- Run this command replacing `projectname` with your desired project name:

```
$ django-admin.py startproject  --template https://github.com/potatolondon/djangae-scaffold/zipball/master  --extension py,yaml,md  projectname
```
      
- Run `cd projectname && ./install_deps` to install dependencies into a 'sitepackages' folder which is added to the path. 
- Run `python manage.py check --deploy --settings=projectname.settings_live` to run all security checks. Replace `projectname` with your new app name.
- Run `python manage.py runserver`

Each time you run the `install_deps` script helper your sitepackages will be wiped out and reinstalled with pip. The SDK will only be downloaded the first time (as it's a large download).

## Deployment

Create a Google App Engine project. Edit `app.yaml` and change `application: djangae-scaffold` to `application: your-app-id`. Then, if you're in the `djangae-scaffold` directory, run:

    $ appcfg.py update ./

If you have two-factor authentication enabled in your Google account, run:

    $ appcfg.py --oauth2 update ./

## Custom Domains

There is currently a [bug in App Engine](https://code.google.com/p/googleappengine/issues/detail?id=7427) which means that HSTS headers are stripped from responses served from a custom domain.  If you're using HTTPS on a custom domain then you should make a request to Google to get your domain whitelisted for HSTS.

## Troubleshooting

If you are on OS X and using Homebrew-ed Python, you might get the following error when running `./install_deps`:

    error: must supply either home or prefix/exec-prefix -- not both

[This is a known issue](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md#note-on-pip-install---user) and a possible workaround is to make an "empty prefix" by default by adding a `~/.pydistutils.cfg` file with the following contents:

```bash
[install]
prefix=
```

## License 

Copyright 2014–2017 Potato London Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

{% endif %}

# {{ project_name }} project
