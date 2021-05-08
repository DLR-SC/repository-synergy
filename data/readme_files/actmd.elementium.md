Elementium
==========
![](https://travis-ci.org/actmd/elementium.svg?branch=master)

[http://github.com/actmd/elementium](http://github.com/actmd/elementium)

jQuery-style syntactic sugar for highly reliable automated browser testing in Python

* Chainable methods with obvious names
* Easy to read
* Concise to write
* Built-in fault tolerance

For an introduction to why you'd want to use Elementium, take a look at [the following post](http://prschmid.blogspot.com/2014/07/elementium-browser-testing-done-right.html).

Before & After
--------------

### With only the [Selenium Python Bindings](http://selenium-python.readthedocs.org/en/latest/index.html)

```python
# From http://selenium-python.readthedocs.org/en/latest/getting-started.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
driver.close()
```

### With Elementium

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elementium.drivers.se import SeElements

se = SeElements(webdriver.Firefox())
se.navigate("http://www.python.org").insist(lambda e: "Python" in e.title)
se.find("q").write("selenium" + Keys.RETURN)

```

Installation
------------

### The easy way

```sh
pip install elementium
```

### The developer way

```sh
git clone git@github.com:actmd/elementium.git
cd elementium
python setup.py install
```

Compatability
-------------

Elementium has been tested for Python 2.6, 3.4, 3.5, 3.7, and pypy using [Travis CI](https://travis-ci.org/actmd/elementium)

Usage
-----

Elementium includes by default a wrapper for the [Selenium Python Bindings](http://selenium-python.readthedocs.org/en/latest/api.html). As such, all of the usage examples make use of the Selenium driver.

### Wrap the browser with an Elementium object

```python
from selenium import webdriver
from elementium.drivers.se import SeElements

se = SeElements(webdriver.Firefox())
```

### Navigating to a web page

```python
se.navigate("http://www.google.com")
```

### Finding DOM elements

Elementium simplifies most of Selenium's many `find` methods...

* `find_element_by_id`
* `find_element_by_name`
* `find_element_by_tag_name`
* `find_element_by_class_name`
* `find_element_by_css_selector`
* `find_element_by_link_text`
* `find_element_by_partial_link_text`

...into two `find()` and `find_link()` methods:

```python
# Find by ID
se.find("#foo")

# Find by name
se.find("[name='foo']")

# Find by tag name
se.find("input")

# Find by class name
se.find(".cssClass")

# Find by link text
se.find_link("Click me")

# Find by partial link text
se.find_link("Click", exact=False)
```

`find()` and `find_link()` will also return multiple elements, if present, so you can forget about all the additional `find_elements_...` methods, too:

```html
<div>...</div> <div>...</div> <div>...</div>
```

```python
len(se.find("div")) # == 3
```

Under the hood, `find()` returns a new `SeElements` object containing a list of all of the items that matched. (These individual items are also of type `SeElements`.)

### Getting specific items

The `get` method lets you pull out a specific item in a chainable manner.

```html
<button>Foo</button> <button>Bar</button> <button>Baz</button>
```

```python
# Get the second button
se.find("button").get(1)
```

#### Accessing the raw object

If you would rather get the raw object (e.g. `SeleniumWebElement`) that is returned by the underlying driver, use `items`:

```python
# Find elements on a page for a given class
buttons = se.find("button")
for button in buttons.items:
    print type(button)
```

The `item` alias will return the *first* raw item:

```python
se.find("button").item
```

### Getting values

```html
<input value="blerg" />
```

```python
se.find("input").value() # returns 'blerg'
```

### Clicking things

```html
<button>Click me</button>
```

```python
se.find("button").click()
```

```html
<input type="checkbox" value="check1">
<input type="checkbox" value="check2">
<input type="checkbox" value="check3">
```

```python
# Click all three checkboxes
se.find("input[type='checkbox']").click()
```

### Typing

```html
<input type="text" />
```

```python
se.find("input").write("If not now, when?")
```

### Selecting

```html
<select>
    <option value="cb">Corned Beef</option>
    <option value="ps">Pastrami</option>
</select>
```

```python
# Select by visible text
se.find("select").select(text="Corned Beef")

# Select by value
se.find("select").select(value="cb")

# Select by index
se.find("select").select(i=0)
```

If manipulating a multiple select, you may use the `deselect()` method in a similar manner:

```html
<select multiple>
    <option value="h">Hummus</option>
    <option value="t">Tahina</option>
    <option value="c">Chips</option>
    <option value="a">Amba</option>
</select>
```

```python
# Deselect by visible text
se.find("select").deselect(text="Chips")

# Deelect by value
se.find("select").deselect(value="c")

# Deselect by index
se.find("select").deselect(i=2)

# Deselect all
se.find("select").deselect()
```


### Waiting

So far, we haven't taken any huge leaps from off-the-shelf Selenium, though we're certainly typing less!

One of the big issues with Selenium is waiting for pages to load completely and all of the retry logic that may have to be used to have tests that work well. A common solution is to [wrap your code with "retry" functions](https://saucelabs.com/resources/selenium/lose-races-and-win-at-selenium).

For example, a naive way of retrying might have been:

```python
browser = webdriver.Firefox()
els = None
while not els:
    els = browser.find_element_by_tag_name('button')
    time.sleep(0.5)
```

With Elementium, just tell `find()` to wait:

```python
# Retry until we find a button on the page (up to 20 seconds by default)
se.find('button', wait=True)
```

Have a more complex success condition? Use `until()`:

```python
# Retry until we find 3 buttons on the page (up to 20 seconds by default)
se.find('button').until(lambda e: len(e) == 3)

# Retry for 60 seconds
se.find('button').until(lambda e: len(e) == 3, ttl=60)
```

Both of the above methods will raise a ``elementium.elements.TimeoutError`` if the element is not found in the specified period of time.

Basically all methods that are part of the `SeElements` object will be automatically retried for you. Under the hood, each selector (e.g. '.foo' or '#foo') is stored as a callback function (similar to something like ``lambda: selenium.find_element_by_id('foo')``). This way, when any of the calls to any of the methods of an element has an expected error (``StaleElementException``, etc.) it will recall this function. If you perform chaining, this will actually propagate that refresh (called ``update()``) up the entire chain to ensure that all parts of the call are valid. Cool!

(Look at the code for more detail.)


### Making assertions

```python
se.find('input').insist(lambda e: e.value() == 'Pilkington')
```

This works exactly like `until()` above, only it raises an ``AssertionError`` instead.

### Other useful methods

See the full Elementium documentation for more details on the following methods.

* `filter()`
* `scroll()`
* `scroll_top()`
* `scroll_bottom()`

The following are simply more reliable versions of their Selenium counterparts. Some have been renamed for ease of use.

* `is_displayed()`
* `is_enabled()`
* `is_selected()`
* `text()`
* `tag_name()`
* `attribute()`
* `clear()`
* `parent()`
* `xpath()`
* `source()`
* `refresh()`
* `current_url()`
* `execute_script()`
* `get_window_size()`
* `set_window_size()`
* `switch_to_active_element()`

Examples
--------

There are a couple examples in the aptly named examples directory. Take a look there for fully functioning source code.

Running the Tests
-----------------

### Simple

First, make sure to install the testing requirements

```sh
pip install -r requirements-tests.txt
```

Then run the tests via nose

```sh
nosetests
```

### Running the tests across multiple python versions in parallel

If you don't trust our Travis CI badge above, you can run all of the tests across multiple python versions by using [pyenv](https://github.com/yyuu/pyenv) and [detox](https://pypi.python.org/pypi/detox). A good writeup for what you need to do to set this up can be found [here](http://blog.pinaxproject.com/2015/12/08/how-test-against-multiple-python-versions-parallel/). If you are using OS X and installed pyenv with brew, make sure to follow [these instructions](https://github.com/yyuu/pyenv#homebrew-on-mac-os-x) as well.

```sh
# Assuming OS X with Homebrew installed
brew update
brew install pyenv
```

```sh
# Install tox and detox
pip install tox
pip install detox
```

You'll want to make sure that you have all of the different python versions are installed so that they can be tested:

```sh
# Install the pyenv versions
pyenv install 2.7.13
pyenv install 3.4.7
pyenv install 3.5.4
pyenv install 3.6.0
pyenv install 3.7.3

# Set all these to be global versions
pyenv global system 2.7.13 3.4.7 3.5.4 3.6.0 3.7.3

# Make sure that they are all there (they should all have a * next to them)
pyenv versions
```

Note, if you are running in to issues installing python due to a `zlib` issue, then take a look at [the solution in this thread](https://github.com/pyenv/pyenv/issues/1219) which can be summarized by saying that you should install your pyenv versions as follows

```
CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" before your pyenv install ...
```

Once you get everything installed, you can run the tests across the different versions as follows.

```sh
detox
```

Note this assumes that you have detox installed globally.

Assuming all goes well, you should see a result akin to

```sh
py27-1.7: commands succeeded
py27-1.8: commands succeeded
py27-1.9: commands succeeded
py27-master: commands succeeded
py34-1.7: commands succeeded
py34-1.8: commands succeeded
py34-1.9: commands succeeded
py34-master: commands succeeded
py35-1.8: commands succeeded
py35-1.9: commands succeeded
py35-master: commands succeeded
congratulations :)
```

If you run in to an issue with running detox, make sure that you have the latest version of pip as there are [some issues](https://github.com/yyuu/pyenv/issues/531) with pyenv and older versions of pip.

The Future
----------

There are several features planned for the future to improve Elementium and they will be rolled out as they pass through our internal scrutiny. If you have great ideas, you can be part of Elementium's future as well!

Contributing
------------

If you would like to contribute to this project, you will need to use [git flow](https://github.com/nvie/gitflow). This way, any and all changes happen on the development branch and not on the master branch. As such, after you have git-flow-ified your elementium git repo, create a pull request for your branch, and we'll take it from there.

Acknowledgements
----------------

Elementium has been a collaborative effort of [ACT.md](http://act.md).
