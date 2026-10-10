#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"
python3 summarize.py
echo "calculator_handoff=confirm every expression above in Calculator before accepting the report"
osascript -e 'tell application "Calculator" to activate'
