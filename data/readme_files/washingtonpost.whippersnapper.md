# Whippersnapper

Whippersnapper is an automated screenshot tool to keep a visual history
of content on the web.

The concept for Whippersnapper first came up as a last-ditch backup system
for the Washington Post's live election results maps. Election nights
are notoriously volatile for news organizations, so we planned to store
static image versions of our results maps throughout the night in case
the need for a fallback arose.

<p align="center">
    <img src="https://raw.githubusercontent.com/washingtonpost/whippersnapper/master/us-house.gif" alt="U.S. House map"/>
</p>

<p align="center">
    <em>An animation of the U.S. House maps captured on election night 2014.</em>
</p>

## Use cases

As a backup tool, Whippersnapper can capture any CSS selector on the
target website and publish timestamped image files to Amazon S3. It
automatically updates a "latest" image file so you can always access the
most recent screenshot of the target.

Whippersnapper doesn't have to be used as a static backup system,
though. It can be pointed at any page on the web to monitor and record
changes -- consider using it to visualize how content on the web changes
over time.

## Installation

Whippersnapper requires [PhantomJS](http://phantomjs.org/) and
[depict](https://github.com/kevinschaul/depict) to be installed. On OS
X, these can be installed via [homebrew](http://brew.sh/) and
[node's](http://www.nodejs.org/) package manager
[npm](https://www.npmjs.org/):

    # Install phantomjs
    brew update
    brew install phantomjs

    # Install depict
    npm install -g depict

Then, install whippersnapper from
[PyPI](https://pypi.python.org/pypi/whippersnapper).
We recommend using
[pip](http://pip.readthedocs.org/en/latest/index.html) with
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/):

    # Install python dependencies
    mkvirtualenv whippersnapper
    pip install whippersnapper

This will install the command `whippersnapper`.

## Usage

Create whippersnapper's config file. This file may be a good
starting point:

- [config.yaml.template](config_templates/config.yaml.template)

Then, run `whippersnapper` with this config file as its first argument:

    whippersnapper CONFIG_PATH

### Config file options

The [config_templates](config_templates) directory includes a few
examples of different ways you might use Whippersnapper, such as [only
storing the images locally](config_templates/local.yaml.template) or
[setting target-specific options](config_templates/targets.yaml.template).

- **targets** - List of target suboptions

  Required. A list of images to include. Each item in this list can
  include these suboptions:

    - **slug** - String

      Required. Used to name the image files.

    - **url**

      Required. The URL of the page you are screenshotting.

    - **target_selector** - String

      Optional. Defaults to `body`. The selector of the element you wish
      to screenshot.

    The following options can override the global options on a
    per-target basis:
    - **page_load_delay**
    - **wait_for_js_signal**
    - **local_image_directory**
    - **aws_subpath**
    - **override_css_file**
    - **failure_timeout**

- **local_image_directory**

  Required. Local directory to store images in.

- **skip_upload**

  Optional. Default: `false`. Whether to skip the upload process.

- **aws_bucket**

  Required (unless `skip_upload` is true). Amazon S3 bucket to store the
  images in. Full path on AWS will be `<aws_bucket>/<aws_subpath>`.

- **aws_subpath**

  Required (unless `skip_upload` is true). The rest of the Amazon S3
  path to store the images in. Full path on AWS will be
  `<aws_bucket>/<aws_subpath>`.

- **aws_access_key**

  Required (unless `skip_upload` is true). Access key credential for Amazon S3.

- **aws_secret_key**

  Required (unless `skip_upload` is true). Secret key credential for Amazon S3.

- **log_file** - String

  Optional. Default: `$(pwd)/screenshotter.log` Path to a file to store
  logging information in.

- **delete_local_images** - Boolean

  Optional. Default: `false`. Whether to delete the local images after
  uploading them to Amazon S3.

- **time_between_screenshots** - Number

  Optional. Default: `60`. Seconds to wait between taking screenshots

- **hide_selector**

  Optional. The CSS selector(s) of elements on the page which you wish to
  hide before capturing the screnshot (works by setting `display: none;`).

- **override_css_file**

  Optional. Path to a CSS file that overrides any existing styles on the
  page. Useful when screenshotting a page that you cannot or do not want
  to modify.

- **page_load_delay** - Number

  Optional. Default: `2`. Seconds to wait after the page is loaded, to
  ensure that any JavaScript has finished running.

- **browser_width** - Number

  Optional. Default: `1440`. The width of the browser window, can be used
  to capture a particular step in a responsive layout.

- **wait_for_js_signal** - Boolean

  Optional. Default: `false`. Instruct depict to wait for the target
  page's JavaScript to call the function `window.callPhantom()`. This
  may be used to wait for an amount of JavaScript to execute instead of
  the option `page_load_delay`, which waits an amount of time.

- **failure_timeout** - Number

  Optional. Default: `30`. The maximum number of seconds the browser
  remains open. If PhantomJS can't open the page or something hangs up,
  this will kill the process. For no time limit, set `failure_timeout`
  to `0`.

## Create gifs

Some uses of Whippersnapper lend themselves well to creating gifs of
images. To do that, install [ImageMagick](http://www.imagemagick.org/)
and run a command like the following:

    convert -delay 10 *.png weather.gif

