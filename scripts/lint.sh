#!/usr/bin/env bash

set -e
set -x

mypy osu
flake8 osu tests
black osu tests --check
isort osu tests --check-only