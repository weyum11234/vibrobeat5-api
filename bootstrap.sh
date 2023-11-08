#!/bin/bash

export FLASK_APP=./vibrobeat5-api/webscraper.py

pipenv run flask --debug run -h 0.0.0.0