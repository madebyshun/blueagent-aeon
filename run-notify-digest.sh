#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .security-digest-output.md)
./notify "$MSG"
