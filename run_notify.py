import subprocess, os
msg = open('.security-digest-msg.txt').read().strip()
result = subprocess.run(['./notify', msg], capture_output=True, text=True)
print('stdout:', result.stdout)
print('stderr:', result.stderr)
print('rc:', result.returncode)
