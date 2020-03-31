#!/usr/bin/env bash
reset
cd "$(dirname "$0")"
echo "currently booting python stitch"
ulimit -n 10000
python3 slit.py