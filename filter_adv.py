import json, sys
data = json.load(sys.stdin)
results = []
for a in data:
    pub = a.get('published_at', '')
    if '2026-07-28' not in pub and '2026-07-29' not in pub and '2026-07-30' not in pub:
        continue
    ecosystems = [v.get('package', {}).get('ecosystem', '').lower() for v in a.get('vulnerabilities', [])]
    tracked = {'npm', 'pip', 'go', 'crates.io', 'github actions'}
    if not any(e in tracked for e in ecosystems):
        continue
    results.append({
        'ghsa_id': a['ghsa_id'],
        'cve_id': a.get('cve_id'),
        'summary': a['summary'][:120],
        'cvss': a.get('cvss', {}).get('score'),
        'severity': a.get('severity'),
        'published_at': a['published_at'],
        'ecosystems': ecosystems,
        'html_url': a['html_url'],
        'patched': [v.get('first_patched_version') for v in a.get('vulnerabilities', []) if v.get('first_patched_version')],
        'pkg': [v.get('package', {}).get('name') for v in a.get('vulnerabilities', [])]
    })
print(json.dumps(results, indent=2))
