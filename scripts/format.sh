#!/bin/sh -e
set -x

isort osu tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables osu tests --exclude=__init__.py
black osu tests
isort osu tests