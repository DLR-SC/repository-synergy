# Python Alexa
## First Release v1.5

This is the second release of my *alexa* library this release note will list some of the features it provides

* Simple request routing
* Get User Location
* Creat custom cards
* Work with Dialog Directives
* Simple Session management
* Simple response crafting
* Utterance Generation using in-code configuration
* Phrase loading - Allows easy integration of multi-language support using a simple JSON configuration file

This module is aimed at those who want to worry about the cool things you can do with Alexa and Lambda rather than having to worry about how you get the data in or out too much.

It is still recommended to use the Alexa Skills documentation to understand how to actually create a skill but this module will do the heavy lifting... or rather the tedious lifting for you.

I am planning to make this module more robust by making the code more fail-safe as well as adding some extra features like Utterance generation and Intent Scheme generation

Please let me know of bugs or feature requests in the Issues section

## Install
## Install via pip
`$ pip install git+ssh://github.com/nmyster/python-alexa.git`

### Upgrade via pip
`$ pip install git+ssh://github.com/nmyster/python-alexa.git - U`

## Usage

```python
"""Example skill using alexa module."""

from alexa import Alexa
import json
alexa = Alexa("Hello World")  # Setup a object for the Alexa class
response = alexa.response  # Use the Alexa response attribute to return responses


# Create your Lambda handler
def lambda_handler(event, context):
    """Lambda Handler."""
    return alexa.route(event)


@alexa.launch
def launch():
    """Launch Function."""
    return response.statement("Welcome to hello world!")


@alexa.intent("GetHello", mapping={"person": "name"})
def get_hello(session, person):
    """Get Hello Intent."""
    if "previous" in session.keys():
        response.card("Welcome to Hello World!")
        return response.question("<p>Welcome</p><p>Hello to you {}".format(person))
    else:
        response.session.set_attribute("previous", True)
        return response.question("<p>Welcome</p><p>Hello AGAIN to you {}".format(person))


@alexa.session_end
def close():
    """Close function."""
    return response.statement("Good bye")


if __name__ == '__main__':

    with open("./test_events.json") as d:
        tests = json.load(d)

    print(
        json.dumps(
            lambda_handler(
                tests['launch'],
                2
            ),
            indent=2
        )
    )
    print(
        json.dumps(
            lambda_handler(
                tests['intent_hello'],
                2
            ),
            indent=2
        )
    )
    print(
        json.dumps(
            lambda_handler(
                tests['end'],
                2
            ),
            indent=2
        )
    )

```

### Phrases
Using a simple JSON file, you can create a file full of your text responses that you return either in questions/statements or on cards. 

The idea of this file is to allow you to remove the phrases you send back from the code logic and make it easy for multiple language support. You can see in `examples/phrases.json` the sort of layout you might want to use.

Then, when it comes to loading a phrase, you can just call `alexa.phrases(<section>, <key>, <key word arguments to pass to the phrase>)`. This class will automatically check the locale of the request and if available, load the version of that phrase for that locale. If it doesn't exist, it will load a default value.

#### Example Phrases usage
**phrases.json**

```json
{
  "phrases": {
    "AMAZON.HelpIntent": {
      "help": {
        "default": [
          "I can help you by creating a repair reservation, tell you about Jung hein rick and keep you up to date on how your service with us is going. How can I assist?",
          "<p>there is a few ways I can help you. I can tell you about the status of your up coming support requests, arrange for a new request or tell you more about what we do and our service to you.</p> <p>What would you like to do?</p>"
        ]
      }
    },
    "AMAZON.StopIntent": {
      "afternoon": {
        "default": [
          "Good bye. Enjoy the rest of the day"
        ]
      },
      "evening": {
        "default": [
          "Good bye. Have a nice evening"
        ]
      },
      "morning": {
        "default": [
          "Good bye. Have a good day"
        ]
      },
      "night": {
        "default": [
          "Good bye. Have a good night"
        ]
      }
    },
    ...
```    

**skill.py**

```python
def lambda_handler(event, context):
    """Lambda Handler."""
    print(json.dumps(event))
    re = alexa.route(event, phrases='./phrases.json')  # Route the event using python-alexa
    print(json.dumps(re))
    return re
    
@alexa.intent("AMAZON.HelpIntent")
def help(s):
    return response.question(alexa.phrases.phrase(alexa.current_intent, "help"))
```


### Example Output
**Launch Request**

```json
{
  "version": "1.0", 
  "response": {
    "outputSpeech": {
      "ssml": "<speak>Welcome to hello world!</speak>", 
      "type": "SSML"
    }, 
    "shouldEndSession": true, 
    "reprompt": {
      "outputSpeech": {
        "text": null, 
        "type": "PlainText"
      }
    }
  }
}
```


**GetHello Intent**

```json
{
  "version": "1.0", 
  "response": {
    "outputSpeech": {
      "ssml": "<speak><p>Welcome</p><p>Hello AGAIN to you John Smith</speak>", 
      "type": "SSML"
    }, 
    "shouldEndSession": false, 
    "reprompt": {
      "outputSpeech": {
        "text": "How can I help?", 
        "type": "PlainText"
      }
    }
  }, 
  "sessionAttributes": {
    "previous": true
  }
}
```

**End Session**

```json
{
  "version": "1.0", 
  "response": {
    "outputSpeech": {
      "ssml": "<speak>Good bye</speak>", 
      "type": "SSML"
    }, 
    "shouldEndSession": true, 
    "reprompt": {
      "outputSpeech": {
        "text": null, 
        "type": "PlainText"
      }
    }
  }, 
  "sessionAttributes": {
    "previous": true
  }
}
```

# Acknowledgement 
This module was inspired by the a Flask focused Alexa project at
https://github.com/johnwheeler/flask-ask