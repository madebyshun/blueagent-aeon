#!/usr/bin/env python3
import subprocess, sys

with open(sys.argv[1]) as f:
    msg = f.read().strip()

result = subprocess.run(['./notify', msg], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print(result.stderr, file=sys.stderr)
sys.exit(result.returncode)
