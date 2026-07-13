import subprocess, json, sys

tracked = {'go', 'npm', 'pip', 'crates.io', 'actions', 'github actions'}
deduped = set([
  'CVE-2026-54067', 'CVE-2026-54072', 'CVE-2026-54089', 'CVE-2026-54174',
  'CVE-2026-54069', 'CVE-2026-54066', 'CVE-2026-54063', 'CVE-2026-49866',
  'CVE-2026-48939', 'CVE-2026-56291',
  'GHSA-mvjr-vv3c-w4qv', 'GHSA-h29v-hj44-q8cv', 'GHSA-xqp3-jq6g-x3qm',
  'GHSA-fpg8-7664-jc5q', 'GHSA-hvr9-72v2-fff3', 'GHSA-p4m3-mgmm-c664',
  'GHSA-h69g-9hx6-f3v4', 'GHSA-cwc9-cp4j-mcvv'
])

all_items = []
for sev in ['critical', 'high']:
    result = subprocess.run(
        ['gh', 'api', '/advisories?type=reviewed&severity=' + sev + '&per_page=100'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print('gh api error for ' + sev + ': ' + result.stderr[:200])
        continue
    try:
        data = json.loads(result.stdout)
    except Exception as e:
        print('JSON parse error: ' + str(e))
        continue

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
        cvss = (a.get('cvss_severities') or {}).get('cvss_v3', {}).get('score', 0) or 0
        all_items.append({
            'ghsa': ghsa, 'cve': cve,
            'summary': a.get('summary', ''),
            'severity': a.get('severity', '') + '_from_' + sev,
            'published': pub,
            'cvss': cvss,
            'url': a.get('html_url', ''),
            'description': a.get('description', '')[:500],
            'vulns': [
                {
                    'eco': v.get('package', {}).get('ecosystem', ''),
                    'name': v.get('package', {}).get('name', ''),
                    'patched': v.get('first_patched_version', ''),
                    'range': v.get('vulnerable_version_range', '')
                }
                for v in vuln_pkgs
            ]
        })

seen = set()
unique = []
for item in all_items:
    k = item['ghsa'] or item['cve']
    if k not in seen:
        seen.add(k)
        unique.append(item)

unique.sort(key=lambda x: x['cvss'], reverse=True)
print(json.dumps(unique, indent=2))
print('# Total new: ' + str(len(unique)), file=sys.stderr)
