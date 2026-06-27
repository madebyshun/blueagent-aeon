#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .notify_msg_token_movers.txt)
./notify "$MSG"
