#!/usr/bin/env bash
set -euo pipefail
mkdir -p .pending-notify
MSG=$(cat .notify_msg.txt)
./notify "$MSG"
