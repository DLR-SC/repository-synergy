**WARNING: The contents of this repository are old and we aren't supporting it any more. The examples probably don't work with the latest versions of BigchainDB. We're keeping this repository around (in read-only mode) because it explored many interesting ideas.**

# Kyber

> Tutorials, Examples and Experiments with BigchainDB. Welcome to the BigchainDB application laboratory!

![banner-kyber 2x](https://cloud.githubusercontent.com/assets/90316/25490941/bb123a3e-2b6e-11e7-9208-53127d336115.png)

## What?! ¯\\\_(ツ)_/¯

Kyber is a full suite of [BigchainDB](https://www.bigchaindb.com) repo's including:

- BigchainDB [server](https://github.com/bigchaindb/kyber#server-side-setup)
- BigchainDB client Tutorials (
[python](https://github.com/bigchaindb/kyber#python-client-tutorials), 
[JavaScript](https://github.com/bigchaindb/kyber#javascript-client-tutorials))
- [Example applications](https://github.com/bigchaindb/kyber#example-applications-with-reactjs-frontend)
- [Experimental stuff](https://github.com/bigchaindb/kyber#experimental-stuff)

All versions of the above:
- Are in sync with the master branch of each BigchainDB repo
- Might have experimental features (watch out that you don't burn yourself ;-) )

### BigchainDB

Getting started with BigchainDB? Have a look at our docs:

- the [HTTP API](https://docs.bigchaindb.com/projects/server/en/latest/drivers-clients/http-client-server-api.html)
- a [Python driver](https://docs.bigchaindb.com/projects/py-driver/en/latest/index.html)
- a (minimal) [JavaScript driver](https://github.com/bigchaindb/kyber/tree/master/drivers/javascript) for creating transactions

## Server-side setup

First things first. You'll need a BigchainDB server to get going with the API.
If you want run the server locally follow these steps:

Clone this repo (using submodules)

```bash
git clone git@github.com:bigchaindb/kyber.git --recursive 
```

and

```bash
cd kyber
```

### Quickstart with Docker (Windows, OSX, lazy Linux)

#### Prequisites

You must have `docker`, `docker-compose` (and `make`) installed.
These versions or higher should work:

- `docker`: `v1.13.0`
- `docker-compose`: `v1.7.1`

#### Locally launch BigchainDB server and other (sometimes experimental) services 

To spin up the services, simple run the make command, which will orchestrate `docker-compose`

```bash
make
```

This might take a few minutes, perfect moment for a :coffee:!

Once docker-composed has built and launched all services, have a look:

```bash
docker-compose ps
```

```
       Name                Command          State                              Ports                             
----------------------------------------------------------------------------------------------------------------
kyber_bdb-server_1   bigchaindb start       Up      0.0.0.0:49984->9984/tcp                                      
kyber_rdb_1          rethinkdb --bind all   Up      0.0.0.0:32772->28015/tcp, 29015/tcp, 0.0.0.0:58585->8080/tcp 
...
```

Which means that the internal docker port for the API is `9984` 
and the external one is `49984`.

The external ports might change, so for the following use the ports as indicated by `docker-compose ps`.

You can simply check if it's running by going to `http://localhost<external-docker-port-bdb-server>`.

Also you can access the RethinkDB dashboard on `http://localhost:<external-docker-port-rdb>`, which is `58585` in our case

If you already built the images and want to `restart`:

```bash
make restart
```

Stop the containers with

```bash
make stop
```

#### Launch docker-compose services manually

No make? Launch the services manually:

Launch RethinkDB:

```bash
docker-compose up -d rdb
```

Wait about 10 seconds and then launch the server:

```bash
docker-compose up -d bdb-server
```

## Python Client Tutorials

### Prequisites

Ok, so this goes well under LINUX, as most python devs know. OSX might be fine too, see the 
[BigchainDB driver docs](](https://docs.bigchaindb.com/projects/py-driver/en/latest/index.html))

If you want to run the Python tutorial with the experimental driver, 
you'll need to install the local python driver and server of bigchaindb
 (in a `python3` virtual environment would be smart e.g. `virtualenv venv -p python3 && source venv/bin/activate`):

```bash
cd drivers/python/
pip install -e .
cd ../../
```

### Run Tutorials

Here is a list of Python tutorials for a BigchainDB client:
- [simple_transactions.py](https://github.com/bigchaindb/kyber/blob/master/tutorials/01_simple_transactions/simple_transactions.py):
 Prepare, sign and post basic `CREATE`, `TRANSFER` transactions
- [assets_unspents.py](https://github.com/bigchaindb/kyber/blob/master/tutorials/02_assets_unspents/assets_unspents.py):
 Create, transfer and list assets, unspents, etc.
- [divisible_transactions.py](https://github.com/bigchaindb/kyber/blob/master/tutorials/03_divisible_transactions/divisible_transactions.py):
 Split and combine transactions with divisible assets
- [cryptoconditions_transactions.py](https://github.com/bigchaindb/kyber/blob/master/tutorials/04_cryptoconditions_transactions/cryptoconditions_transactions.py):
 Create custom UTXO scripts using [py-crypto-conditions](https://github.com/bigchaindb/cryptoconditions)
 
Descend into the tutorials directory

```bash
cd tutorials/
```

The tutorials require a `BDB_SERVER_URL`. 
If you are running the server locally with docker we needed to remember the external port `<external-docker-port>` of the API in docker (run `docker-compose ps` in the repo root).
In our case the `BDB_SERVER_URL` was `http://localhost:49984`.

For example:

```bash
PYTHONPATH=. BDB_SERVER_URL=<bigchaindb-server-url> python 01_simple_transactions/simple_transactions.py
```

## JavaScript Client Tutorials

### Prequisites

If you want to run the JavaScript tutorial, you'll need `node` and `npm`:
These versions or higher should work:

- `node`: `v6.2.2`
- `npm`: `v3.9.5`

### Run Tutorials

Here is a list of JavaScript tutorials:

- [simple_transactions.js](https://github.com/bigchaindb/kyber/blob/master/tutorials/01_simple_transactions/simple_transactions.js):
 Prepare, sign and post basic `CREATE`, `TRANSFER` transactions
- [assets_unspents.js](https://github.com/bigchaindb/kyber/blob/master/tutorials/02_assets_unspents/assets_unspents.js):
 Create, transfer and list assets, unspents, etc.
- [divisible_transactions.js](https://github.com/bigchaindb/kyber/blob/master/tutorials/03_divisible_transactions/divisible_transactions.js):
 Split and combine transactions with divisible assets
- [TODO] Create custom UTXO scripts using [js-crypto-conditions](https://github.com/interledgerjs/five-bells-condition)
 
The JavaScript driver will be served from the local repo (until stable enough to appear on `npm.registry`)

This means we have to link `js-bigchaindb-quickstart` from the local `drivers/javascript`repo before install.
Here is how you do that:

```bash
cd drivers/javascript
npm install
npm link
cd ../../tutorials
npm link js-bigchaindb-quickstart
```

We can now build the JavaScript bundles using `npm`.
Make sure you are in the `tutorials` directory first.

The tutorials require a `BDB_SERVER_URL`. If you are running the server locally with docker we needed to remember the external port `<external-docker-port>` of the API in docker (run `docker-compose ps` in the repo root).
In our case the `BDB_SERVER_URL` was `http://localhost:49984`.

```bash
BDB_SERVER_URL=<bigchaindb_server_url> npm install
```

A few more sips of :coffee: later...

If all goes well, you'll see `webpack` spitting out the bundles. That's a good sign!

Once we have the bundles under `tutorials/build`, we're all set to inject them into a `html` file.
There are some simple webpages in each tutorial that can be served under the `tutorials` directory.

Due to `same-origin` policy, you'll need to start a local webserver (in another terminal) to serve the folder `tutorials`.

Here are some go-to's to server local `html` files:

- `python`: `python -m SimpleHTTPServer`
- `python3`: `python3 -m http.server`
- `node`: the `local-web-server` module see [https://www.npmjs.com/package/local-web-server](https://www.npmjs.com/package/local-web-server)

For example, using the python server uses `port:8000`. 
You can access a (blank) page that will run the JavaScript in the background:

- [http://localhost:8000/01_simple_transactions/simple_transactions.html](http://localhost:8000/01_simple_transactions/simple_transactions.html)
- [http://localhost:8000/02_assets_unspents/assets_unspents.html](http://localhost:8000/02_assets_unspents/assets_unspents.html)
- [http://localhost:8000/03_divisible_transactions/divisible_transactions.html](http://localhost:8000/03_divisible_transactions/divisible_transactions.html)

The tutorials only use JavaScript without frontend visuals. (sorry for that, could go into the ideabox)
However statements are printed in the dev console (`F12` in the browser, and `F5` to reload)

#### _[optional]_ 
Launch webpack in `watch` mode and wait for the bundles to be emitted:

```bash
BDB_SERVER_URL=<bigchaindb_server_url> webpack -w 
```

As long as the webpack watcher is running, every code change will be trigger a new build of the affected bundle(s).

## Example Applications (with ReactJS frontend)

If you used the `make` approach, then examples should be running under the Docker container `examples-client-frontend`:

```bash
          Name                     Command                     State                      Ports           
---------------------------------------------------------------------------------------------------------
kyber_examples-client-     node server.demo.js        Up                         0.0.0.0:33000->3000/tcp  
frontend_1                                                                                                
```

Typically the port is `33000`, so you can simple see the examples on [http://localhost:33000/](http://localhost:33000/).

