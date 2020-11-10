#!/bin/bash
export $(grep -v '^#' .flaskenv | xargs)
coverage run --omit */site-packages/*,tests/*,*/lib/*,*/model/*  --rcfile=$(pwd)/tests/test.coveragerc -m unittest discover -s tests/
coverage report -m
coverage html --rcfile=$(pwd)/tests/test.coveragerc
