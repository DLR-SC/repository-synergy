Google search link fix
=============================

Google search link fix is a Firefox, Chrome and Opera extension that prevents Google and Yandex search pages from modifying search result links when you click them. This is useful when copying links but it also helps privacy by preventing the search engines from recording your clicks. [Detailed description](https://palant.de/2011/11/28/google-yandex-search-link-fix)

Installing build prerequisites
------------------------------

In order to build Google search link fix you will need to install [Node.js](https://nodejs.org/) first (Node 10 or higher is required). You will also need [Gulp](http://gulpjs.com/), run the following command to install it (administrator privileges required):

    npm install --global gulp-cli

Additional dependencies are installed using the following command in the extension directory:

    npm install

How to build
------------

If all the dependencies are installed, creating a Firefox build is simply a matter of running Gulp:

    gulp xpi

This will produce a file named like `searchlinkfix-n.n.n.xpi`. Creating a build for Chrome and Opera is similar:

    gulp crx

This will create an unsigned Chrome package named like `searchlinkfix-n.n.n.zip`.

How to test
-----------

In order to test your changes you can load the repository to your browser as an unpacked extension directly. Then you will only have to reload in order for the changes to apply.

Integration tests
-----------------

You can run the integration tests with the following command:

    gulp test

This uses [Puppeteer](https://pptr.dev/) to instrument Google Chrome and test Google search link fix on various websites. All JavaScript files from the `test` directory will be executed via the [Mocha test framework](https://mochajs.org/). If you want to run a specific test, use `--test` command line switch:

    gulp test --test=google_search
