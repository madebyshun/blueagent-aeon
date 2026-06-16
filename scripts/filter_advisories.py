import sys, json
data = json.load(sys.stdin)
recent = [a for a in data if a.get('published_at','') >= '2026-06-14']
print(json.dumps(recent))
