#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .token_movers_msg.txt)
./notify "$MSG"
