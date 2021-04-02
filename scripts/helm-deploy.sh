#!/usr/bin/env bash

set -euo pipefail

: "${EKS_NAMESPACE}"
: "${RELEASE_NAME}"

echo "print content of test.txt"
#VERSION=$(cat version/docker-version.txt)
VERSION=latest
echo "Deploying app version : ${VERSION}"
helm upgrade \
--install \
--wait \
--namespace "${EKS_NAMESPACE}" \
--set buildno="${VERSION}" \
"${RELEASE_NAME}" ./kubernetes/helm-chart