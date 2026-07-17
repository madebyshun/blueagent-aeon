import subprocess, time

msg = open('security-digest-msg.txt').read()
ts = int(time.time())

with open(f'.pending-notify/{ts}.md', 'w') as f:
    f.write(msg)
print(f'Written to .pending-notify/{ts}.md')

result = subprocess.run(['./notify', msg], capture_output=True, text=True)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr)
print('RC:', result.returncode)
