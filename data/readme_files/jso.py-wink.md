py-wink ;-)
=======

Python library for interfacing with Wink devices, including:
- "Eggminder" eggtray
- "Nimbus" cloud_clock
- "Pivot Power Genius" powerstrip
- "Porkfolio" piggy_bank
- "Spotter" sensor_pod

This library implements the API at: http://docs.wink.apiary.io/

### Status

I am still in the early testing and exploration stages, currently focusing on
the Nimbus cloud_clock. As soon as I can get my hands on the other devices :) I
will be adding support for those as well.

I am generally satisfied with the library architecture and will be focusing on
adding features and working with the team at Quirky to iron out any issues I
find with the API.

All bug reports and feature requests are much appreciated.

### Getting started

1. Get Oauth tokens to access the API.  The Wink API is currently in beta and
   not yet publicly available. However, you may request a set of tokens by
   emailing questions@quirky.com and asking for early access to the Wink API. 

2. Run the "login.py" script and provide your tokens and Wink account
   credentials. This will overwrite the sample config.cfg file and allow you to
   interact with the API.

3. Run the "test.py" script in interactive mode (`python -i test.py`) so you
   can interact with the Wink servers. All the test script does is fetch a list
   of your Wink devices, and print out the type and id for each.

### Let's see what this can do

After you have authenticated, check out the scripts in the "examples"
directory.

#### cloud_clock.py

1. demos each dial, showing the extent of the needle positions and
corresponding values

2. rotates the dials to the left

3. reverts to the original configuration

### Requirements

- httplib2
- That's all, folks!

### Thanks

Thanks to Steven Shaw and everyone at Quirky for providing an API! Steven has
been really responsive in several forums over the last few weeks as they have
been rolling out the API. See this forum for more details:
http://www.quirky.com/forums/topic/21462
