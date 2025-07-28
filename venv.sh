#!/bin/bash
set -e

l() {
    echo '$' "$@" 1>&2
    "$@"
}

# Script to create a virtual environment and install dependencies (using `uv`)
uv venv
source .venv/bin/activate

uv pip install --requirements=requirements/build.txt
uv pip install --requirements=requirements/development.txt || true
# Install itself in editable mode
uv pip install -e .
