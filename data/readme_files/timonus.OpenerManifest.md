# Opener Manifest

[Opener](https://www.opener.link) is an app for iOS that allows people to open web links in native apps instead. It does so by transforming web links within an engine powered by a rule set. This repo is the public version of that rule set.

## Overview

There are four main entities (apps, actions, formats, and browsers) under three top level keys (`apps`, `actions`, and `browsers`) that define a many-to-many relationship between web URLs and the apps they can be opened in.

![](graphic.jpg)

Actions contain formats as child dictionaries, and formats are matched with apps through identifiers. Browsers contain keys from each of the action, app, and format constructs and are intended to be capable of handling any http or https URL as an input.

## Apps

The `apps` top level key in the manifest contains an ordered list of dictionaries, each representing an app supported by Opener. Each app contains the following fields

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>identifier</code></td><td>string</td><td>A human-readable identifier for this app, used elsewhere in the manifest.</td></tr>
<tr><td><code>displayName</code></td><td>string</td><td>The user-facing name for this app within Opener.</td></tr>
<tr><td><code>storeIdentifier</code></td><td>number as string</td><td>The identifier of the app on the App Store. (Optional in v2, required in v1)</td></tr>
<tr><td><code>iconURL</code></td><td>URL string</td><td>A URL to an icon for this app, mutually exclusive with <code>storeIdentifier</code>. This is intended for first party app support.</td></tr>
<tr><td><code>scheme</code></td><td>URL string</td><td>A URL containing only the scheme that will open this app.</td></tr>
<tr><td><code>new</code></td><td>bool</td><td>Indicates whether or not this app will be include in the "New Apps" group in Opener.</td></tr>
<tr><td><code>platform</code></td><td>string</td><td>Specifies if this app should only show up on iPhone/iPod Touch (value=<code>phone</code>) or on iPad (value=<code>pad</code>), shows on both if unspecified. (Opener 1.0.1 and above)</td></tr>
<tr><td><code>country</code></td><td>string</td><td>If the app isn't globally available, including a country code in which it is available in this field will allow the app's icon to show regardless of the user's store. (Opener 1.1.1 and above)</td></tr>
</table>

For example, if Opener were to include itself as an app

```json5
{
    "identifier": "opener",
    "storeIdentifier": "989565871",
    "displayName": "Opener",
    "scheme": "opener://",
    "new": true
}
```


## Actions

The `actions` top level key in the manifest contains a list of dictionaries, each corresponding to a web URL-to-native URL rule. There's a many-to-many relationship between the values in `actions` and `apps`.

### Common values

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>title</code></td><td>string</td><td>The user-facing title for this action.</td></tr>
<tr><td><code>regex</code></td><td>string</td><td>A regular expression string that the input URL is matched against. If this regex is matched by Opener for a given input, this action will appear in the list of available opening options.</td></tr>
<tr><td><code>includeHeaders</code></td><td>bool</td><td>Indicates if headers should be included in the string that <code>regex</code> is matched with. If <code>true</code>, the headers are included in the input as a JSON encoded string separated from the input URL by a newline. (Opener 1.0.2 and above)</td></tr>
<tr><td><code>formats</code></td><td>array of dictionaries</td><td>Specifies the apps that an action can be opened in (see <a href="#formats">below</a>).</td></tr>
</table>

### <a tag="#formats">Formats</a>

Because an action could taken in multiple apps, there's an array within each action dictionary named `formats`. Each entry in this array matches the input URL with an app-specific output for the given action. Each of these contains the following keys.

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>appIdentifier</code></td><td>string</td><td>The identifier of the app that this action applies to. Should match the <code>identifier</code> of an app.</td></tr>
<tr><td><code>format</code></td><td>string</td><td>The regex template applied to the input. Mutually exclusive with <code>script</code>.</td></tr>
</table>

### Advanced URL generation in formats

Some app native URLs can't be generated using simple regex templating, they require lookups or encoding of some sort. To do this, action formats can provide JavaScript methods that are executed to convert input URLs to app native action URLs.

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>script</code></td><td>JavaScript string</td><td>Mutually exclusive with <code>format</code>, can coexist with <code>script2</code>.</td></tr>
<tr><td><code>script2</code></td><td>JavaScript string</td><td>Mutually exclusive with <code>format</code>, can coexist with <code>script</code>.</td></tr>
</table>

This script must contain a JavaScript function named `process` that takes two inputs, a URL and an anonymous function to be called upon completion. Once complete, the completion handler should be called passing the result or `null` on failure.

For example

```javascript
function process(url, completionHandler) {
    // do something with URL...
    url = rot13(url);
    
    completionHandler(url);
}
```

The contents of the `script` field are executed in a `UIWebView`, which gives it a full set of functionality but is a bit slow and costly. The `script2` field is instead run inside of an engine that uses JavaScriptCore, which is much more performant but doesn't have some small functionality that the `UIWebView` has. For convenience, the environment that the `script2` field is executed in has the following functions.

- `httpRequest` makes a blocking call to download the contents of a URL.
- `jsonRequest` makes a blocking call to download the contents of a URL and parses the results into JSON.
- `btoa` base 64 encodes its input.
- `htmlDecode` decodes HTML entities in the input string.
- `base64DigitsToBase10String` takes an array of base 64 digits as integers and converts them into a base 10 string. (Used for decoding [some types of identifiers](http://carrot.is/coding/instagram-ids)).

If `script2` is provided it's used, otherwise we fall back to `script` if specified. Clients prior to version 1.1.8 are only capable of using the `script` field.

Some common scenarios and best practices for using the script fields are outlined [here](./best-practices.md). Opener enforces a timeout of 15 seconds if `completionHandler` isn't called.

### Testing

To keep Opener maintainable, tests for actions can and should be provided.

At the `action` level:

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>testInputs</code></td><td>array of strings</td><td>An array of test inputs that will be run against <code>regex</code> then each action.</td></tr>
</table>

At the `format` level:

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>testResults</code></td><td>array of strings or nulls</td><td>An array of expected results for this format for each of the test inputs. <code>null</code> should be used to specify that a test input <i>should not</i> match</td></tr>
</table>

For example

```json5
{
    ...
    "regex": "http(?:s)?://(?:www\\.)?foo\.bar/(\\d+).*$",
    "testInputs": [
        "https://foo.bar/1234"
        "http://www.foo.bar/wat"
    ],
    "formats": [
        {
            ...
            "format": "foo-app://entry/$1",
            "testResults": [
                "foo-app://entry/1234",
                null
            ]
        },
        {
            ...
            "script": "function process(url, completion) { completion('bar-app://' + encodeURIComponent(url)); }",
            "testResults": [
                "bar-app://https%3A%2F%2Ffoo.bar%2F1234",
                null
            ]
        }
    ]
}
```

Testing formats that have `includeHeaders` is not currently possible.

## Browsers

Support for opening any http or https URL in browsers was added in Opener 1.1. Browsers live under the `browsers` top level key, each one contains a subset of the keys from the other `app`, `action`, and `format` dictionaries.

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td><code>identifier</code></td><td>string</td><td>A human-readable identifier for this app, used elsewhere in the manifest.</td></tr>
<tr><td><code>displayName</code></td><td>string</td><td>The user-facing name for this app within Opener.</td></tr>
<tr><td><code>storeIdentifier</code></td><td>number as string</td><td>The identifier of the app on the App Store. (Optional in v2, required in v1)</td></tr>
<tr><td><code>iconURL</code></td><td>URL string</td><td>A URL to an icon for this app, mutually exclusive with <code>storeIdentifier</code>. This is intended for first party app support.</td></tr>
<tr><td><code>scheme</code></td><td>URL string</td><td>A URL containing only the scheme that will open this app.</td></tr>
<tr><td><code>new</code></td><td>bool</td><td>Indicates whether or not this app will be include in the "New Apps" group in Opener.</td></tr>
<tr><td><code>platform</code></td><td>string</td><td>Specifies if this app should only show up on iPhone/iPod Touch (value=<code>phone</code>) or on iPad (value=<code>pad</code>), shows on both if unspecified. (Opener 1.0.1 and above)</td></tr>
<tr><td><code>country</code></td><td>string</td><td>If the app isn't globally available, including a country code in which it is available in this field will allow the app's icon to show regardless of the user's store. (Opener 1.1.1 and above)</td></tr>
<tr><td><code>regex</code></td><td>string</td><td>A regular expression string that the input URL is matched against, used for pattern replacements.</td></tr>
<tr><td><code>format</code></td><td>string</td><td>The regex template applied to the input. Mutually exclusive with <code>script</code>.</td></tr>
<tr><td><code>script</code></td><td>JavaScript string</td><td>Mutually exclusive with <code>format</code>.</td></tr>
<tr><td><code>testInputs</code></td><td>array of strings</td><td>An array of test inputs that will be run against <code>regex</code> then each action.</td></tr>
<tr><td><code>testResults</code></td><td>array of strings or nulls</td><td>An array of expected results for this format for each of the test inputs. <code>null</code> should be used to specify that a test input <i>should not</i> match</td></tr>
</table>

For example, here's Google Chrome's dictionary:

```json5
{
    "displayName": "Chrome",
    "identifier": "chrome",
    "scheme": "googlechrome://",
    "storeIdentifier": "535886823",
    "regex": "http(s)?(.*)$",
    "format": "googlechrome$1$2",
    "testInputs": [
        "http://www.opener.link/",
        "https://twitter.com/openerapp"
    ],
    "testResults": [
        "googlechrome://www.opener.link/",
        "googlechromes://twitter.com/openerapp"
    ]
}
```

## Redirect Rules

There's a fourth top-level key in the manifest named `redirectRules` that's not directly tied to opening in particular apps. If Opener's unable to resolve a URL into a set of actions it performs a HTTP `HEAD` request to follow its input URL to its final destination, then retries resolving on that URL. For example, a bit.ly link to a Tweet wouldn't naturally resolve because Opener has no way of knowing the bit.ly link points to a Tweet, so we perform a `HEAD` request to get the final URL, which does resolve.

Some popular services have URL redirection that doesn't work when followed through an HTTP `HEAD` request, but instead require loading HTML to get a redirect to occur. Links of this variety break Opener's system for resolving URLs, and loading up an invisible web page just to see if something redirects doesn't seem acceptable. Some of these services include

- Google (and some Google AMP links)
- Facebook (and Facebook Messenger)
- Reddit
- Tumblr
- Pinterest

`redirectRules` solves this by serving as a static set of rules for mapping input URLs to what they'd redirect to if they were loaded up as HTML from services like this. The format for these rules is pretty simple.

<table>
<tr><th>Key</th><th>Type</th><th>Description</th></tr>
<tr><td>Dictionary key</td><td>string</td><td>The keys for the entries in <code>redirectRules</code> are regular expressions to match. If a match is found, the rule within it used.</td>
<tr><td><code>param</code></td><td>string</td><td>A URL query parameter name. If the rule is matched, the value for <code>param</code> is used as the resulting URL to redirect to. Mutually exclusive with <code>format</code>.</td>
<tr><td><code>format</code></td><td>string</td><td>A regex template to be used on the input if the rule is matched. Mutually exclusive with <code>param</code></td>
</table>

So, for example if links like `https://mycoolsite.com/redirect?redirecturl=foobar.com` redirect to `foobar.com`, you'd use a rule like this.

```
"https://mycoolsite\\.com/redirect.*$" {
	"param": "redirecturl"
}
```

`redirectRules` also supports lightweight tests in the form of a dictionary under the `tests` key. The keys of `tests` are sample inputs, and the values are the expected outputs.

```
"https://mycoolsite\\.com/redirect.*$" {
	"param": "redirecturl",
	"test": {
		"https://mycoolsite.com/redirect?redirecturl=foobar.com": "foobar.com"
	}
}
```

`redirectRules` are only supported by Opener version 1.5.8 and above.

## Minify Script

There's a python script included named [minify.py](./minify.py), this script takes a copy of the manifest as an input and outputs a file with suffix `-minified.json` as output. This script strips out all unnecessary keys for Opener's operation when running in the client (testing, documentation, etc.) and minifies the JSON to be compact.

Sample usage:

```shell
python minify.py openerManifest-v3.json
```

## Versions

The manifest file has a `-v3` on the end, this indicates the major version of the manifest. If there are ever changes to the app that make the manifest not backwards compatible with a former version, the suffix of the manifest file is bumped.

<table>
<tr><th>Manifest Version</th><th>App Version</th><th>Changes</th></tr>
<tr><td>v2</td><td>1.0.10</td><td>Made app dictionary <code>storeIdentifier</code> field optional. This was required in v1. Change was made in order to support first party apps, which lack an iTunes identifier.</td></tr>
<tr><td>v3</td><td>1.1.8</td><td>Add support for <code>script2</code> field, which is processed using JavaScriptCore instead of a <code>UIWebView</code>.</td></tr>
</table>

## Contributing

Pull requests are welcome! Because Opener is a closed source app with an experience that I'd like to keep great, I'm going to be pedantic about these requests. I will likely manipulate the order of the apps and actions that are added, and handle the `new` flag for them.
