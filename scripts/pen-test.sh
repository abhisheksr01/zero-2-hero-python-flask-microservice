#!/usr/bin/env bash

set -euo pipefail

echo "show current dir"
pwd

cd ../../../../zap/
echo "Running from containers home zap directory..."
mkdir wrk

echo "......................running zap......................"

zap-baseline.py -T 5 -w report.md -a -j -t "http://greetings.labs.armakuni.co.uk/health" | while read -r line; do if echo "${line}" | grep -q "FAIL-NEW: [0-9]+[\t ]+FAIL-INPROG: [0-9]+[\t ]+WARN-NEW: [0-9]+[\t ]+WARN-INPROG: [0-9]+[\t ]+INFO: [0-9]+[\t ]+IGNORE: [0-9]+[\t ]+PASS: [0-9]+" ; then pidof Xvfb | xargs -r kill ; fi ; echo "${line}" ; done
EXIT_CODE="${?}"
cat /zap/wrk/report.md
pidof Xvfb | xargs -r kill
exit "${EXIT_CODE}"