Rate Exchange JSON/JSONP APIs
=============================

This is the rate exchange JSON/JSONP APIs project which is deployed at http://rate-exchange.appspot.com/.

Currently only currency and temperature rate exchange are supported.

Usage
----

### Currency API

By invoking the currency API, just send a request to `/currency` as follow:

    /currency?from=USD&to=EUR&q=1&callback=jsonpCallback

And note that the parameter `q` and `callback` is optional.
One more thing is that the rate fetched from google is cached by 10mins in this application.

Here are some samples:

| Request |Response|
|---------|--------|
| `/currency?from=USD&to=EUR` | <code>{<br />&nbsp;&nbsp;&nbsp;&nbsp;"to": "EUR",<br />&nbsp;&nbsp;&nbsp;&nbsp;"rate": 0.77966630299999995,<br />&nbsp;&nbsp;&nbsp;&nbsp;"from": "USD"<br />}</code> |
| `/currency?from=USD&to=EUR&q=2` | <code>{<br />&nbsp;&nbsp;&nbsp;&nbsp;"to": "EUR",<br />&nbsp;&nbsp;&nbsp;&nbsp;"rate": 0.77966630299999995,<br />&nbsp;&nbsp;&nbsp;&nbsp;"from": "USD",<br />&nbsp;&nbsp;&nbsp;&nbsp;"v": 1.5593326059999999<br/>}</code> |
| `/currency?from=USD&to=EUR&callback=jsonpCallback` | <code>jsonpCallback({<br />&nbsp;&nbsp;&nbsp;&nbsp;"to": "EUR",<br />&nbsp;&nbsp;&nbsp;&nbsp;"rate": 0.77966630299999995,<br />&nbsp;&nbsp;&nbsp;&nbsp;"from": "USD"<br />})</code> |
| `/currency?from=USD&to=EUR&q=2&callback=jsonpCallback` | <code>jsonpCallback({<br />&nbsp;&nbsp;&nbsp;&nbsp;"to": "EUR",<br />&nbsp;&nbsp;&nbsp;&nbsp;"rate": 0.77966630299999995,<br />&nbsp;&nbsp;&nbsp;&nbsp;"from": "USD",<br />&nbsp;&nbsp;&nbsp;&nbsp;"v": 1.5593326059999999<br />})</code> |
| `/currency?from=USD` | <code>{<br />&nbsp;&nbsp;&nbsp;&nbsp;"err": "invalid request"<br />}</code> |
| `/currency?from=USD&to=LAK` | <code>{<br />&nbsp;&nbsp;&nbsp;&nbsp;"err": "not supported rate conversion."<br />}</code> |
| `/currency?from=MXV&to=USD` | <code>{<br />&nbsp;&nbsp;&nbsp;&nbsp;"err": "Parse error in query. - tokens = 1 MXV =? U.S. dollar"<br />}</code> |

### Temperature API

By invoking the temperature API, send a request to `/temperature` as follows:

    /temperature?mode=C2F&q=37

The mode can be `C2F`(Celsius to Fahrenheit) or `F2C`(Fahrenheit to Celsius). A jsonp `callback` parameter is optional. The response is as:

    {"v": 98.6, "mode": "C2F", "qty": 37.0}


Help needed!
------------

We've reached the [GAE URL Fetch Quota](https://developers.google.com/appengine/docs/quotas#UrlFetch) for the currency API.
And I need your help to enable billing to get larger quota. Do please help to click [this link](http://ko-fi.com?i=8d071856392d304) and donate me $1.00USD.

License
-------
ExchangeRates is released under the MIT license:
+ www.opensource.org/licenses/MIT