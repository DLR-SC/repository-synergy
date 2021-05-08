# ** NOTE **: Due to new authentication implemented by Frontier, EDCE no longer works. Please see the following if you wish to contribute: https://github.com/Andargor/edce-client/issues/30 **

# edce-client
Elite Dangerous Companion Emulator

## Purpose

This is an interface that emulates an iPhone accessing the [Elite Dangerous Companion](https://itunes.apple.com/gb/app/elite-dangerous/id897148481?mt=8) web API, which is normally used by a mobile application developed by Frontier Developments. This experimental code has not been created in association with [Frontier Developments](http://www.frontier.co.uk/) and is unsupported by them.

The EDCE client queries your Commander data on the Elite Dangerous Companion site as you would on your iPhone, and retrieves the data to file in JSON format. It also publishes market data to [EDDN](https://github.com/jamesremuscat/EDDN/wiki). No private information is published.

## Installation

* Requirements:
* - Python 3.3 or higher
* - Python requests library: `pip3 install requests`
* Run the client-setup.py program: python3 client-setup.py
* Enter your Frontier store credentials (NOTE: The password is stored unencrypted in the edce.ini file. You can leave the password blank, however this means you will need to run the client in interactive mode and you will be prompted to enter the password every time)

## Usage

* Launch the client: python3 edce_client.py
* The first time you run the program, the Elite Dangerous Companion website will request a verification code, which shall be sent to your account email. Enter the code at the prompt. You should only have to do this once
* The program will query your Commander's data, and dump the JSON result in the log directory (LZMA compressed, can be examined by 7-zip)
* The program will also post the market data from the current station where your Commander is docked to [EDDN](https://github.com/jamesremuscat/EDDN/wiki). If he/she is not docked, the data is not sent.

## General Notes

* Protect your edce.ini file as it contains your Frontier store credentials in unencrypted form
* Avoid querying the Elite Dangerous Companion site too often in order to avoid overloading it. As a rule, try not to query more than once every 2-3 minutes.
* The web API sometimes lags actual game state by several seconds. For example, you might dock, but only be able to post market data to EDDN after a few seconds until the web API catches up.
* You can modify the code as you wish, the [edce](https://github.com/Andargor/edce-client/tree/master/edce) subdirectory contains the core module to access the Elite Dangerous Companion web API
