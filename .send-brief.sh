#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat /home/runner/work/blueagent-aeon/blueagent-aeon/.morning-brief-2026-08-13.txt)
/home/runner/work/blueagent-aeon/blueagent-aeon/notify "$MSG"
