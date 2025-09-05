#!/usr/bin/env sh
set -e
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip