import json, sys

data = json.load(sys.stdin)
tracked = {'go', 'npm', 'pip', 'crates.io', 'actions', 'github actions'}
deduped = {
  'CVE-2026-54067', 'CVE-2026-54072', 'CVE-2026-54089', 'CVE-2026-54174',
  'CVE-2026-54069', 'CVE-2026-54066', 'CVE-2026-54063', 'CVE-2026-49866',
  'CVE-2026-48939', 'CVE-2026-56291',
  'GHSA-mvjr-vv3c-w4qv', 'GHSA-h29v-hj44-q8cv', 'GHSA-xqp3-jq6g-x3qm',
  'GHSA-fpg8-7664-jc5q', 'GHSA-hvr9-72v2-fff3', 'GHSA-p4m3-mgmm-c664',
  'GHSA-h69g-9hx6-f3v4', 'GHSA-cwc9-cp4j-mcvv'
}
recent = []
for a in data:
    pub = a.get('published_at', '')
    if pub < '2026-07-11':
        continue
    ghsa = a.get('ghsa_id', '')
    cve = a.get('cve_id') or ''
    if ghsa in deduped or (cve and cve in deduped):
        continue
    vuln_pkgs = a.get('vulnerabilities', [])
    ecos = [v.get('package', {}).get('ecosystem', '').lower() for v in vuln_pkgs]
    if not any(e in tracked for e in ecos):
        continue
    cvss = a.get('cvss_severities', {}).get('cvss_v3', {}).get('score', 0) or 0
    recent.append({
        'ghsa': ghsa, 'cve': cve, 'summary': a.get('summary', ''),
        'severity': a.get('severity', ''), 'published': pub,
        'cvss': cvss,
        'url': a.get('html_url', ''),
        'vulns': [
            {
                'eco': v.get('package', {}).get('ecosystem', ''),
                'name': v.get('package', {}).get('name', ''),
                'patched': v.get('first_patched_version', '')
            }
            for v in vuln_pkgs
        ]
    })

recent.sort(key=lambda x: x['cvss'], reverse=True)
for r in recent:
    print(r['ghsa'] + ' | ' + r['cve'] + ' | ' + r['severity'] + ' | CVSS ' + str(r['cvss']) + ' | ' + r['published'][:10])
    print('  ' + r['summary'])
    for v in r['vulns']:
        print('  [' + v['eco'] + '] ' + v['name'] + ' -> ' + v['patched'])
    print()
print('Total: ' + str(len(recent)))
