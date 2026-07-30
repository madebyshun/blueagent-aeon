#!/usr/bin/env bash
MSG=$(cat .security-digest-msg.txt)
./notify "$MSG"
