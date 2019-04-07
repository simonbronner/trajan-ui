# trajan-ui

A django service providing the user interface for trajan project

## Pre-requisites

* [Python 3.7+](https://www.python.org)
* [Django](https://www.djangoproject.com) - 2.1.7
* [trajan-server](https://github.com/sxb8au/trajan)

## How to Run

Assuming you have docker, the following will download the dependencies (see: requirements.txt) and start the django server in debug mode:

```
drun.sh
```

It assumes that you already have trajan-server running on the the current host on port 8002.

## How To Package

The following will produce a docker image, with django configured in production mode:

```
docker build .
```

See: docker-build.sh for a convenience script to do the same.

## License

Copyright © 2019 Simon Bronner
