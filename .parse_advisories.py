import json

SINCE = '2026-07-12'
ECOSYSTEMS = {'npm', 'pip', 'Go', 'crates.io', 'GitHub Actions', 'Rust', 'rubygems', 'Maven', 'PyPI', 'actions'}
SKIP_IDS = {
    'CVE-2026-55255', 'GHSA-qrpv-q767-xqq2',
    'CVE-2026-50551', 'GHSA-56mp-4f3v-fgj2',
    'CVE-2026-54158', 'GHSA-5xfx-xj4h-5p7r',
    'CVE-2026-54088', 'GHSA-m93h-4hw7-5qcm',
    'GHSA-g936-7jqj-mwv8',
    'GHSA-xrmc-c5cg-rv7x',
}

BASE = "/home/runner/.claude/projects/-home-runner-work-blueagent-aeon-blueagent-aeon/6c895db2-2713-4d66-9509-44366e6e997c/tool-results"
CRITICAL_FILE = BASE + "/b8af715yk.txt"
HIGH_FILE = BASE + "/boyjnwg1j.txt"

def parse(path):
    with open(path) as f:
        data = json.load(f)
    results = []
    for a in data:
        pub = (a.get('published_at') or '')[:10]
        if pub < SINCE:
            continue
        ghsa = a.get('ghsa_id') or ''
        cve = a.get('cve_id') or ''
        if ghsa in SKIP_IDS or cve in SKIP_IDS:
            continue
        vulns = a.get('vulnerabilities') or []
        ecosystems = [v.get('package', {}).get('ecosystem', '') for v in vulns if v.get('package')]
        if not any(e in ECOSYSTEMS for e in ecosystems):
            continue
        packages = []
        for v in vulns:
            pkg = v.get('package') or {}
            packages.append({
                'name': pkg.get('name', ''),
                'ecosystem': pkg.get('ecosystem', ''),
                'patched': v.get('patched_versions', ''),
                'vuln_range': v.get('vulnerable_version_range', '')
            })
        results.append({
            'ghsa_id': ghsa,
            'cve_id': cve,
            'summary': a.get('summary', ''),
            'severity': a.get('severity', ''),
            'cvss_score': (a.get('cvss') or {}).get('score'),
            'ecosystems': list(set(ecosystems)),
            'packages': packages,
            'html_url': a.get('html_url', ''),
            'published_at': pub
        })
    return results

critical = parse(CRITICAL_FILE)
high = parse(HIGH_FILE)
all_items = critical + high

seen = set()
unique = []
for item in all_items:
    key = item['ghsa_id'] or item['cve_id']
    if key and key not in seen:
        seen.add(key)
        unique.append(item)

print(json.dumps(unique, indent=2))
