#!/bin/bash

DIR=$(dirname "${BASH_SOURCE[0]}")
DIR=$(realpath "${DIR}")

echo $DIR
cd $DIR
source $DIR/venv/bin/activate
envdir env gunicorn feedservice.wsgi -c feedservice/gunicorn.conf.py

pkill -P $$

