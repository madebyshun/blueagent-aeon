#!/usr/bin/env bash
MSG=$(cat /tmp/token_movers_msg.txt)
./notify "$MSG"
