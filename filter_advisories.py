import sys, json
raw = sys.stdin.read()
try:
    data = json.loads(raw)
except Exception as e:
    print(f'PARSE_ERROR: {e}')
    sys.exit(1)
cutoff = '2026-09-13'
tracked = {'npm', 'pip', 'go', 'rust', 'rubygems', 'maven', 'actions', 'composer'}
out = []
for a in data:
    pub = (a.get('published_at') or '')[:10]
    if pub < cutoff:
        continue
    pkgs = a.get('vulnerabilities') or []
    ecosystems = [(v.get('package') or {}).get('ecosystem','').lower() for v in pkgs if v.get('package')]
    if not any(e in tracked for e in ecosystems):
        continue
    out.append({
        'ghsa': a.get('ghsa_id'),
        'cve': a.get('cve_id'),
        'summary': a.get('summary'),
        'cvss': (a.get('cvss') or {}).get('score'),
        'eco': ecosystems,
        'pub': pub,
        'url': a.get('html_url'),
        'pkgs': [{'name':(v.get('package') or {}).get('name'), 'patched':(v.get('patched_versions') or ''),'vuln':(v.get('vulnerable_version_range') or '')} for v in pkgs]
    })
print(json.dumps(out, indent=2))
