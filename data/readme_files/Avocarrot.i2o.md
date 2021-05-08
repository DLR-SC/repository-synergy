<img src="https://cloud.githubusercontent.com/assets/1907604/7903383/7e204d10-07e3-11e5-88cb-95e84c002c19.png" width=180/>

## Purpose
This project allows you to trigger sound effects from a web hook. You can play sounds or listen to a message using text to speech. 

We built this during an office hackday at [Avocarrot](http://www.avocarrot.com). We use it with Slack's web hooks and a Rasberry Pi to get notified about calendar events, build statuses or just troll each other:)

## Contents

- [Getting started](#getting-started)
- [Play sounds](#play-sounds)
- [Text to speech](#text-to-speech)
- [Contributing](#contributing)

## Getting started

1. Fork the project
2. Install dependencies using ```pip install -r pip-reqs.txt```
3. Start the web server using ```python manage.py runserver```
4. Start Celery worker with ```celery -A i2o worker -l info``` (you should also run RabbitMQ or change the broker settings in the settings.py)
5. Have fun!

## Play sounds

**Endpoint** 

```
http://localhost:8000/events/send
```


**Request body - Play sound from file**

```json
{
	"cmd" : "play -f users/batman.wav"
}
```

**Request body - Play sound from url**

```json
{
	"cmd" : "play -u https://www.youtube.com/watch?v=3R5gHF0vzew"
}
```

## Text to speech

**Endpoint** 

```
http://localhost:8000/events/send
```

**Request body**

```json
{
	"cmd" : "speak -m 'Hello World'"
}
```

## Contributing

We'd love more people to contribute to this project so feel free to submit your pull requests.

1. Fork the repo
2. Apply your changes
3. Write tests
4. Submit your pull request
