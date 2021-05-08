# Daily Photo

This application picks up a photo from a specified directory, sends it to a specified Telegram chat
and then deletes that photo. Simple as that.

I use it to make a "Daily Photo" channel.

## Usage

Dependencies are managed using [pipenv](https://pipenv.readthedocs.io/en/latest/).

You should [set up your Telegram bot](https://core.telegram.org/bots#6-botfather) and invite it to
your desired channel or group. Then you should pick up the chat id from
https://api.telegram.org/YOUR_TOKEN/getUpdates

Define the following environment variables:
* DAILY_PHOTO_DIRECTORY - The directory containing the photos
* DAILY_PHOTO_BOT_TOKEN - The token of your bot
* DAILY_PHOTO_CHAT_ID - The chat ID of the group, channel or chat
* *Optional* DAILY_PHOTO_SENTRY_DSN - A DSN for [Sentry](https://sentry.io/welcome/)

After the you can just run the app with `pipenv run daily_photo`. The app should send a single photo
and then quit. You can use cron, systemd-timers or any other scheduler to run it periodically.
