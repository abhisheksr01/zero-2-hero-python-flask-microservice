#!/usr/bin/env bash

set -euo pipefail

echo "show current dir"
pwd

cd ../../../../zap/
echo "Running from containers home zap directory..."
mkdir wrk && zap-baseline.py -t "${ROOT_ENDPOINT}/health" -g gen.conf -r penetration-test-report.html || :