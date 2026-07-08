#!/usr/bin/env bash
MSG=$(cat .tmp_digest_msg.md)
./notify "$MSG"
