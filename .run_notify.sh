#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
MSG=$(cat .token_movers_msg.txt)
./notify "$MSG"
