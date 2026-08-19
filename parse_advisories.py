import sys, json

data = json.load(sys.stdin)
tracked = {'npm', 'pip', 'Go', 'Rust', 'actions'}
since = '2026-08-17'
results = []
for a in data:
    if a.get('published_at', '') < since:
        continue
    ecosystems = [v.get('package', {}).get('ecosystem', '') for v in a.get('vulnerabilities', [])]
    in_tracked = any(e in tracked for e in ecosystems)
    results.append({
        'ghsa_id': a.get('ghsa_id'),
        'cve_id': a.get('cve_id'),
        'summary': a.get('summary', '')[:150],
        'severity': a.get('severity'),
        'cvss': a.get('cvss', {}).get('score') if a.get('cvss') else None,
        'published_at': a.get('published_at'),
        'html_url': a.get('html_url'),
        'ecosystems': ecosystems,
        'in_tracked': in_tracked,
        'packages': [
            {
                'ecosystem': v.get('package', {}).get('ecosystem'),
                'name': v.get('package', {}).get('name'),
                'patched': v.get('patched_versions'),
                'vuln': v.get('vulnerable_version_range')
            }
            for v in a.get('vulnerabilities', [])
        ]
    })
print(json.dumps(results, indent=2))
