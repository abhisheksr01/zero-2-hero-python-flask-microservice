#!/usr/bin/env bash

set -euo pipefail

echo "show current dir"
pwd

cd ../../../../zap/
echo "Running from containers home zap directory..."
mkdir wrk

echo "......................running zap......................"
../tini -s -- zap-baseline.py -t "http://greetings.labs.armakuni.co.uk/health" -g gen.conf -r penetration-test-report.html || :