import json, sys

data = json.loads(open('/home/runner/.claude/projects/-home-runner-work-blueagent-aeon-blueagent-aeon/f1ea2dbc-49ee-4fd7-b81b-3233ea6347bb/tool-results/bhwg87fzv.txt').read())

tracked = {'npm', 'pip', 'Go', 'crates.io', 'GitHub Actions', 'PyPI', 'RubyGems', 'Maven'}
skip_cves = {'CVE-2026-40217', 'CVE-2026-133968', 'CVE-2026-129448', 'CVE-2026-59726', 'CVE-2026-64855', 'CVE-2026-90817', 'CVE-2026-115731', 'CVE-2026-123890'}

results = []
for a in data:
    cve_id = a.get('cve_id', '')
    if cve_id in skip_cves:
        continue
    ecosystems = []
    for v in a.get('vulnerabilities', []):
        pkg = v.get('package', {})
        eco = pkg.get('ecosystem', '')
        if eco:
            ecosystems.append(eco)
    in_stack = any(e in tracked for e in ecosystems)
    if not in_stack:
        continue
    item = {
        'ghsa_id': a.get('ghsa_id'),
        'cve_id': cve_id,
        'summary': a.get('summary', ''),
        'severity': a.get('severity'),
        'cvss_score': (a.get('cvss') or {}).get('score'),
        'html_url': a.get('html_url'),
        'published_at': a.get('published_at'),
        'vulnerabilities': [
            {
                'ecosystem': v.get('package', {}).get('ecosystem'),
                'name': v.get('package', {}).get('name'),
                'patched': v.get('patched_versions'),
                'vulnerable': v.get('vulnerable_version_range'),
            }
            for v in a.get('vulnerabilities', [])
        ]
    }
    results.append(item)

print(json.dumps(results, indent=2))
print(f'\nTotal in-stack: {len(results)}', file=sys.stderr)
