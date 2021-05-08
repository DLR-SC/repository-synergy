# pass-rotate

pass-rotate is a library and CLI for rotating passwords on various web services.
This software makes it easier to rotate your passwords, one at a time or in
bulk, when security events or routine upkeep of your online accounts makes it
necessary. This is the first step towards a better future - one where users
never interact with passwords at all and they're managed entirely by software.

Adding new services is a tedious process. If you'd like to support pass-rotate,
you can contribute my [Patreon page](https://patreon.com/sircmpwn) and request
support for specific providers.

## CLI usage

Copy pass-rotate.ini to `~/.config/pass-rotate.ini` and edit it to your liking.
You'll have to find a shell command (or write a script) that gets passwords from
and adds passwords to your password manager. Examples for
[pass](http://passwordstore.org) are provided in the example config.

Rotate passwords like so:

```
$ pass-rotate news.ycombinator.com github.com
Rotating news.ycombinator.com... OK
Rotating github.com...
  Enter your two factor (TOTP) code: 
  OK
```

Full usage:

```
Usage:
  pass-rotate <accounts>...
  pass-rotate --list-accounts
  pass-rotate --list-providers
  pass-rotate --list-options <provider>

Options:
  --list-accounts   Print all configured accounts
  --list-providers  Print all supported service providers and exit
  --list-options    Prints options for the specified provider and exit
  --config=<file>   Specify an alternate config file (default: ~/.config/pass-rotate.ini)
```

For a list of currently supported services, see [the
wiki](https://github.com/SirCmpwn/pass-rotate/wiki/Currently-supported-services).
Please help us add more services - it's easy!

## Installation

```
pip install -e .
```

## Library usage

The CLI is a frontend for the passrotate Python library, which is intended to be
easily integrated with various password managers to provide password rotation
functionality.

```python
>>> from passrotate import PassRotate
>>> pass_rotate = PassRotate()
>>> github = pass_rotate.get_provider("github.com", { "username": "example" })
>>> github.prepare(old_password) # Verifies credentials, prompts for two-factor, etc
>>> github.execute(old_password, new_password) # Actually changes the password
```

You can also get a provider's class with `PassRotate.get_provider_class(name)`,
which includes the following properties:

- `name`: User-friendly provider name
- `domains`: List of domains this password applies to
- `options`: Expected format of the options dict you pass into the constructor.
  This is a dict with option names, whose values are
  `passrotate.provider.ProviderOption` instances.

You may get a list() of supported provider classes with
`PassRotate.get_providers()`, and you can also just directly import specific
providers from `passrotate.providers`.

### Prompting for two-factor

Some providers may need to prompt the user to do things like provide a
two-factor authorization code. You may set a function to fulfill this prompt by
using `PassRotate.set_prompt(func)`, where `func` is a function that takes a
`prompt` string and a `prompt_type`. The latter is an instance of the
`passrotate.provider.PromptType` enum. This function should return a string -
the answer to the prompt.

### ProviderOption

This class is used by Provider.options to specify the format of the options dict
for this provider.
