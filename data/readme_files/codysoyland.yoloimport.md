# yoloimport
*Never see another ImportError*

Are you tired of seeing ImportErrors? **yoloimport** makes ImportErrors a relic of the past, by installing your dependencies for you whenever you import a missing package. Now you can focus on writing code instead of installing dependencies!

## Installation

To install, just run `pip install yoloimport` and kiss pip goodbye, because yoloimport will deal with pip for you!

## Example

Let's try to use the [itty framework](https://github.com/toastdriven/itty) for the first time!


    >>> from itty import get, run_itty
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named itty


Who wants to see that nonsense!? Let's try it after importing **yoloimport**!

    >>> import yoloimport
    >>> from itty import get, run_itty
    Collecting itty
      Using cached itty-0.8.2-py2.py3-none-any.whl
    Installing collected packages: itty

    Successfully installed itty-0.8.2
    Collecting -winreg
      Could not find any downloads that satisfy the requirement -winreg
      No distributions at all found for -winreg
    >>> @get('/')
    ... def index(request):
    ...     return 'Hello World!'
    ...
    >>> run_itty()
    itty starting up (using wsgiref)...
    Listening on http://localhost:8080...
    Use Ctrl-C to quit.

Who knows what that "-winreg" error was all about? I sure don't, but who cares? We got itty working without any pesky ImportErrors getting in our way!

*Happy April 1st!*
