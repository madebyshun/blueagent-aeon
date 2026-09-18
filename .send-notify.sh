#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat .pending-notify/token_movers_2026-09-18.md)
./notify "$MSG"
