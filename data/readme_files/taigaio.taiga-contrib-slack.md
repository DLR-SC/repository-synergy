Taiga contrib slack
===================

[![Kaleidos Project](http://kaleidos.net/static/img/badge.png)](https://github.com/kaleidos "Kaleidos Project")
[![Managed with Taiga.io](https://img.shields.io/badge/managed%20with-TAIGA.io-709f14.svg)](https://tree.taiga.io/project/taiga/ "Managed with Taiga.io")

The Taiga plugin for slack integration.

![taiga-contrib-slack example](doc/img/taiga-slack-notifications.png)

Installation
------------
### Production env

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-slack` with:

```bash
  pip install taiga-contrib-slack
```

Modify in `taiga-back` your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["taiga_contrib_slack"]
```

Then run the migrations to generate the new need table:

```bash
  python manage.py migrate taiga_contrib_slack
```

#### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-slack` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/taigaio/taiga-contrib-slack/tags/$(pip show taiga-contrib-slack | awk '/^Version: /{print $2}')/front/dist" "slack"
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/slack/slack.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/slack/slack.json"
    ]
...
```

### Dev env

#### Taiga Back

Clone the repo and

```bash
  cd taiga-contrib-slack/back
  workon taiga
  pip install -e .
```

Modify in `taiga-back` your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["taiga_contrib_slack"]
```

Then run the migrations to generate the new need table:

```bash
  python manage.py migrate taiga_contrib_slack
```

#### Taiga Front

After clone the repo link `dist` in `taiga-front` plugins directory:

```bash
  cd taiga-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../taiga-Contrib-slack/front/dist slack
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/slack/slack.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/slack/slack.json"
    ]
...
```

In the plugin source dir `taiga-contrib-slack/front` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.


How to use
----------

Follow the instructions on our support page [Taiga.io Support > Contrib Plugins > Slack integration](https://tree.taiga.io/support/contrib-plugins/slack-integration/ "Taiga.io Support > Contrib Plugins > Slack integration")
