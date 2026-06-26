#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .sec_digest_msg.txt)
./notify "$MSG"
