# SlackBot
A [Slack](https://slack.com/) bot running in *daemon mode* with *Amazon SQS* integration.

Original version using *Flask* and *Outgoing WebHooks* integration by [llimllib/slask](https://github.com/llimllib/slask).

## Installation

1. Clone this repo
2. `pip install -r requirements.txt`
3. Add the Amazon SQS integration on [Slack](https://slack.com)
4. Add the Incoming WebHooks integration on [Slack](https://slack.com)
5. Update config.py with your information (tokens,keys,botname,etc)
6. Run `python bot.py start`
7. That's it! Try typing `!echo Hello World` into any chat room

### IAM Permission for Slack

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt2123981740180",
      "Effect": "Allow",
      "Action": [
        "sqs:*"
      ],
      "Resource": [
        "arn:aws:sqs:us-east-1:<account id>:<sqs queue name>"
      ]
    }
  ]
}
```

### Heroku

You can also host your Bot for free on [Heroku](http://heroku.com). It is ready to deploy.

```bash
heroku create
git push heroku master
heroku ps:scale worker=1
heroku ps
heroku logs
```

## Commands

Right now, `!help`, `!echo`, `!gif`, `!image`, `!youtube` and `!wiki` are the only available commands.

It's super easy to add your own commands! Just create a python file in the plugins directory with an `on_message` function that returns a string.

## Integrations

Besides commands you can also integrate other types of plugins that just listen for a specific message in the SQS queue.

See per example the [stackdriver-reader](https://github.com/fsalum/slackbot-python/blob/master/plugins/README.md) plugin that wait for Stackdriver to send policy alerts to a SNS topic which is subscribed by the SQS queue used by this daemon.
