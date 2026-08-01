#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat /tmp/token-movers-msg.txt)
./notify "$MSG"
