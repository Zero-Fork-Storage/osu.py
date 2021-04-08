#!/usr/bin/env bash

set -e
set -x

# shellcheck disable=SC2068
bash ./scripts/test.sh --cov-report=html ${@}