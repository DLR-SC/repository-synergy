# nlgserv

nlgserv is a simple server that accepts JSON representations of sentences and generates English sentences from those.

It uses SimpleNLG (under the [MPL 2.0 licence](https://www.mozilla.org/MPL/)) available [on github.com](https://github.com/simplenlg/simplenlg) for natural language generation.

In order to use SimpleNLG (which is implemented in Java), [Jython 2.7.0](http://www.jython.org) is also bundled, under the terms of the [PSF v.2](http://www.jython.org/license.html).

Additionally, it uses Bottle v0.12.9 (under the [MIT licence](https://github.com/defnull/bottle/blob/0.12.9/LICENSE) available [on github.com](https://github.com/defnull/bottle/tree/0.12.9) for handling HTTP requests.

> This was something I cobbled together to act as part of my PhD project.
> Consequently, I don't really have time to maintain it or fix bugs, as
> it suits the purposes I need it for.
>
> Feel free to take the code and try and fix it, but I'm afraid I can't
> really help you. If you are able to use the Java library directly,
> I'd really recommend you do that instead.
>
> Thanks,
> Darren


#### Steps in starting the nlg server on localhost: 

1.  Install nlgserv package in local python environment using the command :
    ```python
    pip install nlgserv
    ```
    Or you can even download the repo, extract it and use `python setup.py install`

2.  Type the following commands in the shell to start the nlg server : <br>
    ```python
    import nlgserv
    s = nlgserv.start_server("localhost",8000) # You can change the host and port here, use it same throughout

    ```
    
    To get the following output: <br>
    ```
    Starting nlgserv on localhost:8000 <br>
    <subprocess.Popen object at 0x7fdc6e008290>
    ```
    
    Now the nlg server has started on localhost:8000
    
    In order to run simpleNLG on this server, a POST request should be sent to the server. The request should be in a proper     Json format :
    
    For example
    ```JSON
      {  
         "sentence":
        {  
            "subject":"John",
            "verb":"like",
            "object":
            {  
               "type":"coordinated_phrase",
               "coordinates":
               [  
                  "apples",
                  "oranges"
               ]
            },
            "modifiers":
            [  
               "very much"
            ],
            "indirect_object":"",
            "features":
            {  
               "tense":"present"
            }
         }
      }
    ```
    Note that the keys are the different components of the sentence we want to construct. 
    
    The above Json request will get you the following response :
    ```
    John likes apples and oranges very much.
    ```

    To test the response, you can use the RESTED extention in Firefox. (You can even use Postman) <br> 
    Send a post request to http://localhost:8000/generateSentence <br>
    The headers will contain the following : <br>
    Name : content-type <br>
    Value : application/json <br>
    
    <kbd>![normal](https://raw.githubusercontent.com/mnestis/nlgserv/b1444950e30880d93c0445a8d2396b01dca276e2/screenshots/one.png)</kbd>
    <br>
    <br>
    Adding the Json data in the body and getting a response:
    <kbd>![normal](https://raw.githubusercontent.com/mnestis/nlgserv/b1444950e30880d93c0445a8d2396b01dca276e2/screenshots/two.png)</kbd>


Build status
------------

[![Build Status](https://travis-ci.org/mnestis/nlgserv.svg?branch=master)](https://travis-ci.org/mnestis/nlgserv)
[![Latest Version](https://img.shields.io/pypi/v/nlgserv.svg)](https://pypi.python.org/pypi/nlgserv/)
