[![Build Status](https://travis-ci.org/rackerlabs/otter.svg?branch=master)](https://travis-ci.org/rackerlabs/otter)
[![codecov](https://codecov.io/gh/rackerlabs/otter/branch/master/graph/badge.svg)](https://codecov.io/gh/rackerlabs/otter)
# Rackspace Autoscale

*There Otter be an Otter scaling system.*

![Otter Cups](https://i.chzbgr.com/completestore/12/8/19/AjXtHogT4UqgJwDJsq7igA2.gif)

If you have docker installed then running `docker-compose up -d` should run otter
along with all its dependent services and cafe and trial integration tests
against it. Try checking `docker-compose logs cafe` to see cloudcafe test results
and `docker-compose logs trial` to see trial integration test results.

Talk with us! Join us in:

irc.freenode.net #rackerlabs/otter

Otter Dev Hall of Fame (alphabetical):

- cyli
- lvh
- manisht
- radix
- wirehead

Honorary Otters:

- glyph

Emeritus otters:

- dreid
- fsargent
- oubiwann
- rockstar

## `make` targets

### Development

- `make hooks` to set up pre-commit hooks for the project
  (PLEASE RUN THIS IF DEVELOPING ON THE PROJECT)

Build an environment:

- `make env-precheck` makes sure you have enough pre-existing
  infrastructure to be able to run `make env` to begin with.
- `make env` creates and switches into the Python virtualenv
  environment.  It'll also pip-install development requirements.

Run tests, check code quality:

- `make test` runs both unit and integration tests.
- `make unit` runs unit tests.
- `make integration` runs integration tests.
- `make coverage` performs coverage analysis.
- `make lint` performs a lint (PEP8, et. al.) check on the source
  code.
- `make listoutdated` returns the packages that are currently
  installed that have new versions available on PyPI. This is normally
  run as a part of `make lint`.
- `make flake8diff` looks at the diff introduced by your current
  branch and lints it. This is normally run as a part of `make lint`.
- `make flake8full` is like `flake8diff`, except on the entire
  repository.

Build the documentation:

- `make docs` builds all other documentation targets (listed below).
- `make sphinxdocs` builds all Sphinx documentation.
- `make docbook` builds all user-facing Docbook documentation.

### Deployment

- `make bundle` builds a "bundle" appropriate for deployment (Ubuntu
  only).  For Jenkins and Chef use only.
- `make run` starts up an instance of the Otter API.

### Cleaning up

- `make cleandocs` removes all documentation artifacts without
  removing other artifacts.
- `make clean` removes all build-time artifacts, leaving the
  repository in a distributable state.

### Build and migrate Cassandra schemata

Some tools for building Cassandra schemata as CQL files:

- `make schema-setup` generates the setup CQL files.
- `make schema-teardown` generates the teardown CQL files.
- `make schema` generates the CQL files corresponding to setting up
  and tearing down Otter's Cassandra schema.  Equivalent to running
  `make schema-setup schema-teardown` manually.

Some tools for applying Cassandra schemata (by default, these are
pointed at `localhost`, because they're typically only used within the
development VM):

- `make load-dev-schema` will attempt to load the development schema
  into Cassandra.
- `make migrate-dev-schema` will attempt to update the development
  schema on an existing Cassandra instance.
- `make teardown-dev-schema` will attempt to remove a development
  schema from an existing Cassandra instance.
- `make clear-dev-schema` first removes any existing development
  schema, then re-installs a fresh schema.
