import subprocess, json, sys

tracked = {'npm', 'pip', 'Go', 'Rust', 'actions'}
since = '2026-08-17'
results = []

for sev in ['critical', 'high']:
    r = subprocess.run(
        ['gh', 'api', f'/advisories?type=reviewed&severity={sev}&per_page=50'],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"ERROR fetching {sev}: {r.stderr}", file=sys.stderr)
        continue
    data = json.loads(r.stdout)
    for a in data:
        if a.get('published_at', '') < since:
            continue
        ghsa = a.get('ghsa_id', '')
        cve = a.get('cve_id', '')
        # skip already-reported IDs
        skip_ids = {
            'CVE-2025-62593','GHSA-q279-jhrf-cc6v','GHSA-2qvg-qr73-mqxp','CVE-2026-55158',
            'GHSA-m44r-7c5h-m6mj','CVE-2026-53728','GHSA-ggr8-5vv4-36mx','CVE-2026-40345',
            'GHSA-m5w8-4gq2-6f8x','GHSA-m283-3h24-438v','CVE-2026-47686','GHSA-cfcw-xp6x-25gj',
            'CVE-2026-47698','GHSA-7gwp-5pfp-969j','CVE-2026-64849','GHSA-8r8v-xf7q-rcpr',
            'CVE-2026-71479','GHSA-6x2c-phff-wx57','CVE-2026-64859','GHSA-73wf-9vmv-5pv9',
            'CVE-2026-62982','GHSA-8g4w-4ffg-8vgx','CVE-2026-56677'
        }
        if ghsa in skip_ids or cve in skip_ids:
            continue
        ecosystems = [v.get('package', {}).get('ecosystem', '') for v in a.get('vulnerabilities', [])]
        in_tracked = any(e in tracked for e in ecosystems)
        # Include if in tracked ecosystem OR if it's a KEV entry
        kev_ids = {'CVE-2026-33824','CVE-2026-59310','CVE-2026-55040','CVE-2026-65400'}
        if not in_tracked and cve not in kev_ids:
            continue
        results.append({
            'ghsa_id': ghsa,
            'cve_id': cve,
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

# dedupe by ghsa_id
seen = set()
deduped = []
for r in results:
    key = r['ghsa_id'] or r['cve_id']
    if key not in seen:
        seen.add(key)
        deduped.append(r)

print(json.dumps(deduped, indent=2))
