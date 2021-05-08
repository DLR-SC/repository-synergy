# PyMoves, a python library for the Moves App API

## Dependencies

The only dependency of this library is [Requests](http://docs.python-requests.org/en/latest/).

## Example Usage

	from moves import Moves
	m = Moves()

Get a request token URL:

	request_url = m.request_url()

Open the Moves app and enter the PIN, then you will be redirected the url specified in for the app. The next step is to use the code to get and access token:

	access_token = m.auth(code)

If you have an access token you can make requests like:

	m.get_profile(access_token)

This will fetch all user info. Other requests are also build in, but beware of the range requests as they have a limit of 7 days.
