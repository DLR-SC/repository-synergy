# Djangobot

Djangobot is a bridge between Slack and a [Channels](https://channels.readthedocs.org)-enabled Django app.

Specifically, it is a protocol server that produces and consumes messages for channels-based apps.

It is built atop [autobahn](http://autobahn.ws/python/) and [twisted](http://twistedmatrix.com/trac/).

## Installation & Usage

To install, simply use pip.

```shell
$ pip install djangobot
```

Djangobot should be installed in the virtual environment of your application as it needs to be able to import one of the specified channel layers defined in your `settings.py`.

Then, assuming your django project is named `myapp`, the ASGI file is named `asgi.py` and you've created a channel layer in it named `channel_layer`, run this command:

```shell
$ DJANGOBOT_TOKEN=[your slack token] djangobot myapp.asgi:channel_layer
```

In production, you'll want to keep this process alive with [supervisor](http://supervisord.org/), [circus](https://circus.readthedocs.org/en/latest/) or a similar tool.

## What's it doing?

When beginning `djangobot`, it will:

1. Connect to the Slack API and request users and channels for your team.
2. Initiate a [Real-Time Messaging Connection](https://api.slack.com/rtm).
3. Forward any RTM events onto the `slack.{type}` channel. For example, message events
  (whose `type` is `message`) are sent along the `slack.message` channel.
4. Send any messages on the `slack.send` channel back to slack.

## Receiving events in your application

In your `routing.py`, you'll need to specify consumer functions to handle events on the slack
channels like so:

```python
channel_routing = {
    'websocket.receive': 'path.to.my.consumer',
    'websocket.connect': 'path.to.another.consumer',
    'websocket.disconnect': 'path.to.yet.another.consumer',

    # Slack channels
    'slack.message': 'function.to.handle.slack.messages',
    'slack.hello': 'handle.when.djangobot.connects',
    # and so forth
```

## Sending messages to slack

To send messages to slack, simply send a dictionary at least a `text` key. You may optionally include the `channel` on which to post the message. This can be the human-readable version or a channel id. Note that `djangobot` necessarily posts messages as the user tied to your Slack API token.

For example:

```python
import channels

channels.Channel('slack.send').send({'text': 'Why hello there!', 'channel': 'general'})
```

Of course, part of the beauty of channels is that this can be done from anywhere.

# Why is this useful?

This simply bridges your slack team to your production application in real-time. On it's own, it does nothing else. Implementing actual features is up to you. Off the top of my head, some ideas:

1. Make Slack a logging destination.
2. 2FA to approve certain tasks.
3. Chat through Slack to users.

# Contributing

1. Fork this repository.
2. Create a branch with your feature or bug fix.
3. Work on it, push commits.
4. Submit a Pull Request.

# Todo

1. Testing: I would appreciate help testing twisted clients.
2. Setting up the reply channel: Right now both djangobot and applications must hard-code the `slack.send` outgoing channel name which isn't ideal.
2. Logging: Djangobot could `logger.debug` a lot more.

