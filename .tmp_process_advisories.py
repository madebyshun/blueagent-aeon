import json
import sys
import subprocess
import os

TRACKED = {'npm', 'pip', 'go', 'crates.io', 'github actions', 'rubygems', 'maven', 'nuget'}

SEEN_IDS = {
    'GHSA-vjc7-jrh9-9j86', 'CVE-2026-54769', 'GHSA-q9p7-wqxg-mrhc',
    'CVE-2026-55500', 'GHSA-qvfm-67h2-2qfx', 'CVE-2026-49445', 'GHSA-3fcv-jvfp-m4q9',
    'CVE-2026-53486', 'GHSA-mp2f-45pm-3cg9', 'CVE-2026-55786', 'GHSA-h9f9-h6gm-wc85',
    'GHSA-9rjw-3gwp-f59v', 'CVE-2026-54496', 'GHSA-ww9q-8r59-xv46',
    'CVE-2026-54771', 'GHSA-gjgq-w2m6-wr5q', 'CVE-2026-55615', 'GHSA-2pq5-3q89-j7cc'
}

KEV_THIS_WEEK = {
    'CVE-2026-48908', 'CVE-2026-55255', 'CVE-2026-56290', 'CVE-2026-48282'
}

def fetch_advisories(severity):
    result = subprocess.run(
        ['gh', 'api', f'/advisories?type=reviewed&severity={severity}&per_page=100',
         '-H', 'Accept: application/vnd.github+json'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return []
    try:
        return json.loads(result.stdout)
    except:
        return []

all_advisories = []
for sev in ['critical', 'high']:
    all_advisories.extend(fetch_advisories(sev))

deduped = {a['ghsa_id']: a for a in all_advisories}.values()

recent_48h = [a for a in deduped if a.get('published_at', '') >= '2026-07-06']

results = []
for a in recent_48h:
    ghsa = a.get('ghsa_id', '')
    cve = a.get('cve_id', '')

    if ghsa in SEEN_IDS or (cve and cve in SEEN_IDS):
        continue

    ecosystems = []
    packages = []
    patched = []
    for v in a.get('vulnerabilities', []):
        pkg = v.get('package', {})
        eco = (pkg.get('ecosystem') or '').lower()
        name = pkg.get('name', '')
        if eco:
            ecosystems.append(eco)
        if name:
            packages.append(f"{name} ({eco})")
        pv = v.get('patched_versions', '')
        if pv:
            patched.append(pv)

    in_tracked = any(e in TRACKED for e in ecosystems)
    in_kev = cve in KEV_THIS_WEEK

    if not in_tracked and not in_kev:
        continue

    cvss_score = None
    cvss_data = a.get('cvss', {})
    if cvss_data:
        cvss_score = cvss_data.get('score')

    results.append({
        'ghsa': ghsa,
        'cve': cve,
        'severity': a.get('severity', ''),
        'cvss': cvss_score,
        'summary': a.get('summary', ''),
        'ecosystems': ecosystems,
        'packages': packages,
        'patched': patched,
        'url': a.get('html_url', ''),
        'published': a.get('published_at', ''),
        'in_kev': in_kev
    })

print(json.dumps(results, indent=2))
