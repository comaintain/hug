#!/usr/bin/env bash
set -euo pipefail
rm -rf build/ dist/ hug_upgraded.egg-info/
./setup.py sdist bdist_wheel
