## Tumblr Themr

TumblrThemr is a standalone tool to develop tumblr themes offline on your desktop (osx/win/linux)! It lets you get rid of the painful process of copy pasting your theme onto tumblr's interface to preview it and lets you use your favorite editor for development.

Themes are rendered against the default tumblr data. You can also test against your own tumble blog, for that you will need to import your tumble blog's data , from Tumblr Themr itself, using your Tumblr developer API Key.

The project initially started as an exercise in writing a complete parser from scratch; building desktop gui app; desktop web app and eventually evolving into a complete app and is written in Python.

### Download

[http://tumblrthemr.com/TumblrThemr.zip](http://tumblrthemr.com/TumblrThemr.zip) (OSX)

For Windows & Linux - unfortunately a standalone build is not available at this point.  But you can still use this tool.

 * Install the [pre-requisits](https://github.com/kalyan02/tumblrthemr#pre-requisits)
 * checkout out this repository
 * execute the main.py python script ( python main.py )

### Getting started

To run the app, follow these steps:

 * Run TumblrThemr.app  
![Web Interface](https://raw.github.com/kalyan02/tumblrtemplatr/master/etc/screenshot_2.png)

 * Select the directory containing your themes  

```
Example directory structure  
/projects                 <-- *you need to pick this*
  +--theme_in_development
  |  +-index.html         <-- index.html must be your theme
  |  +-style.css
  |
  +--theme2
```

 * Optionally select the port (default:13323)
 * Click on 'Start Server' to start the offline tumblr server
 * A browser window with the default webpage will open  
![Web Interface](https://raw.github.com/kalyan02/tumblrtemplatr/master/etc/screenshot_1.png)

### Preview your theme
 * From the homepage (default [http://localhost:13323](http://localhost:13323)) , you can select an available theme
 * If your theme doesn't appear, then you will have to stop the server and pick again
 * Open your theme from the "Select Project" section

### Testing your theme
Its simple - just refresh your browser after an edit and you can preview the changes - just as you would develop your html/css templates!

### Custom tumblr data

 * To test against your own tumblr blog/data, you will first need an API Key
 * If you do not have an API key, you will need to request for it here by registering a dummy application - [http://www.tumblr.com/oauth/apps](http://www.tumblr.com/oauth/apps)
 * In the "Import Data Source" section add your API Key and the tumblr blog's username
 * Select Import 
 
 
### Switching data source
 TumblrThemr allows you to test your themes against multiple data sources. If you want to switch data source, select the prefered source from "Select Data Source" section.

## Pre-requisits 
The .app file is a standalone bundle and does not have any dependencies

To build the app from source you will require the following 
 * python2.7
 * bottle
 * jinja2
 * wx [framework]
 * distutils

## Todo
 * Implement full tumblr spec
 * Add support for windows / py2exe

## Contribution
If you would like to contribute, please send a pull request and add your name to this section along with your commit.
Am currently looking for help mainly in these areas:
 * Complete the tumblr spec - its only partially implemented to cover major aspects
 * A port to windows exe using py2exe
 * Improvements the parser/etc

* [kalyan02](http://twitter.com/kalyan02)

### Implementing the tumblr tags / spec

The tags are implemented by simply mapping them to the data fields that correspond to the JSON API output from tumblr.
Entire spec is simply one data structure called `contextDataMapper` - [https://github.com/kalyan02/tumblrthemr/blob/master/src/engine.py#L502](https://github.com/kalyan02/tumblrthemr/blob/master/src/engine.py#L502)

Each key in the contextDataMapper corresponds to the actual tag, the value corresponds to a lambda function which will perform the retrieval from json

Eg1:

`'title' : _path('blog.title')`  
`_path ` returns a method which retrieves `json['data']['blog']['title']` from the json.

Eg2:

`'dayofmonth': _date('e')`  
`_date` returns a method that performs `dparser.parse( node['data']['date'] ).strftime('%e')` on the corresponding node!

Eg3:

`'posts' : ('posts',{...`  
Here 'posts' tumblr tag maps to the 'posts' section of the json data. The context mapper supports nesting, so you can add additional such conditions to map the entire json to tags.

Eg4:
```
'audio' : ( lambda node: node['data']['type'] == 'audio', {
  							'formattedplaycount' : 'plays',
								'audioplayerwhite' : 'player',
								'caption' : 'caption'
							}),
```  
One can also perform conditional mapping. In the above example, a sub map for audio data is created only if the node type is audio.
If so, then formattedplaycount, caption, audioplayerwhite variables are simply mapped to their corresponding json fields, without any processing.

## License
This free software is released under [MIT License](http://opensource.org/licenses/MIT)
```
Copyright (c) 2013 Kalyan Chakravarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
