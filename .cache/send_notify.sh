#!/usr/bin/env bash
MSG=$(cat .cache/notify_msg.txt)
./notify "$MSG"
