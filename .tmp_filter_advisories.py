#!/usr/bin/env python3
import json, subprocess, sys

cutoff = '2026-08-20T00:00:00Z'
tracked = {'npm', 'pip', 'Go', 'crates.io', 'GitHub Actions'}
skip_ids = {
    'CVE-2026-72529','CVE-2026-72530','CVE-2026-64849',
    'GHSA-rrwh-6jrq-wp5v','GHSA-ghvf-qf6h-g8x5','GHSA-f5f4-3hh4-f54m',
    'GHSA-v667-gc2r-2xm7','GHSA-533j-2v4q-mw5h','GHSA-23m2-mghx-vqmf',
    'GHSA-c7hr-448w-65px','GHSA-2xhg-73j7-rrgx','GHSA-rr55-jp92-8wp2',
    'GHSA-j4r7-8ph4-43g3','GHSA-cc2g-gq8c-r332','GHSA-9gmc-jqmh-3rvm'
}
kev_cves = {'CVE-2026-73570','CVE-2026-33824','CVE-2026-59310','CVE-2026-55040','CVE-2026-65400','CVE-2025-62593'}

def filter_advisories(data):
    results = []
    for a in data:
        if a.get('published_at','') < cutoff:
            continue
        if a.get('ghsa_id') in skip_ids or a.get('cve_id') in skip_ids:
            continue
        ecosystems = set()
        for v in (a.get('vulnerabilities') or []):
            pkg = v.get('package') or {}
            if pkg.get('ecosystem'):
                ecosystems.add(pkg['ecosystem'])
        if not (ecosystems & tracked) and a.get('cve_id') not in kev_cves:
            continue
        item = {
            'ghsa_id': a.get('ghsa_id'),
            'cve_id': a.get('cve_id'),
            'summary': a.get('summary'),
            'severity': a.get('severity'),
            'cvss_score': (a.get('cvss') or {}).get('score'),
            'published_at': a.get('published_at'),
            'html_url': a.get('html_url'),
            'packages': [
                {
                    'ecosystem': (v.get('package') or {}).get('ecosystem'),
                    'name': (v.get('package') or {}).get('name'),
                    'patched_versions': v.get('patched_versions'),
                    'vulnerable_version_range': v.get('vulnerable_version_range')
                }
                for v in (a.get('vulnerabilities') or [])
            ]
        }
        results.append(item)
    return results

# Read critical advisories from stdin if file provided, else fetch
severity = sys.argv[1] if len(sys.argv) > 1 else 'critical'
with open(f'/home/runner/work/blueagent-aeon/blueagent-aeon/.tmp_{severity}.json') as f:
    data = json.load(f)

results = filter_advisories(data)
print(json.dumps(results, indent=2))
