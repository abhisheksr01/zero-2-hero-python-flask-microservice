#!/usr/bin/env bash

set -euo pipefail

echo "show current dir"
pwd

cd ../../../../zap/

echo "......................running zap......................"
# The below command works well when we want a html report output.
# mkdir wrk && zap-baseline.py -t "${HEALTH_ENDPOINT}" -g gen.conf -r penetration-test-report.html || :
# The below command generates a reports.md which is easy to read on console
mkdir wrk && zap-baseline.py -T 5 -w report.md -a -j -t "${ROOT_ENDPOINT}/health" | while read -r line; do if echo "${line}" | grep -q "FAIL-NEW: [0-9]+[\t ]+FAIL-INPROG: [0-9]+[\t ]+WARN-NEW: [0-9]+[\t ]+WARN-INPROG: [0-9]+[\t ]+INFO: [0-9]+[\t ]+IGNORE: [0-9]+[\t ]+PASS: [0-9]+" ; then pidof Xvfb | xargs -r kill ; fi ; echo "${line}" ; done
EXIT_CODE="${?}"
cat /zap/wrk/report.md
pidof Xvfb | xargs -r kill
exit "${EXIT_CODE}"