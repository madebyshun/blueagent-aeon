#!/usr/bin/env bash
set -euo pipefail
BRIEF_FILE="${1:-morning-brief.txt}"
MSG=$(cat "$BRIEF_FILE")
./notify "$MSG"
