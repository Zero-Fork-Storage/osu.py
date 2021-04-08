#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --cov=osu --cov=tests --cov-report=term-missing --cov-report=xml tests ${@}
