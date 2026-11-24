import json, sys

TRACKED = {'npm', 'pip', 'Go', 'crates.io', 'GitHub Actions', 'PyPI', 'RubyGems', 'Maven', 'NuGet'}

with open(sys.argv[1]) as f:
    data = json.load(f)

results = []
for a in data:
    pkgs = a.get('vulnerabilities', [])
    ecosystems = [p.get('package', {}).get('ecosystem', '') for p in pkgs]
    pkg_names = [p.get('package', {}).get('name', '') for p in pkgs]
    patched = [p.get('patched_versions', '') for p in pkgs]
    cvss = a.get('cvss', {})
    matched = any(e in TRACKED for e in ecosystems)
    results.append({
        'ghsa_id': a.get('ghsa_id'),
        'cve_id': a.get('cve_id'),
        'summary': a.get('summary', '')[:150],
        'severity': a.get('severity'),
        'cvss_score': cvss.get('score') if cvss else None,
        'ecosystems': ecosystems,
        'packages': pkg_names,
        'patched_versions': patched,
        'html_url': a.get('html_url'),
        'published_at': a.get('published_at'),
        'in_tracked_stack': matched
    })

print(json.dumps(results, indent=2))
