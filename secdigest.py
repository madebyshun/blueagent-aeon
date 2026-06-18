#!/usr/bin/env python3
"""Security digest data collector — run then read output files."""
import json, subprocess, sys, os

BASE = '/home/runner/work/blueagent-aeon/blueagent-aeon'

# 1. Parse KEV recent
with open(f'{BASE}/kev.json') as f:
    kev_data = json.load(f)
kev_recent = [v for v in kev_data['vulnerabilities'] if v.get('dateAdded','') >= '2026-06-11']
with open(f'{BASE}/kev_recent.json', 'w') as f:
    json.dump(kev_recent, f, indent=2)
print(f"KEV recent ({len(kev_recent)} entries):")
for v in kev_recent:
    print(f"  {v['dateAdded']} | {v.get('cveID','?')} | {v.get('vendorProject','')} {v.get('product','')} | {v.get('shortDescription','')[:90]}")

# 2. Fetch GitHub advisories via gh CLI
print("\nFetching GH advisories...")
for sev in ['critical', 'high']:
    result = subprocess.run(
        ['gh', 'api', f'/advisories?type=reviewed&severity={sev}&per_page=50',
         '-H', 'Accept: application/vnd.github+json'],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode == 0:
        data = json.loads(result.stdout)
        filtered = [v for v in data if (v.get('published_at') or '') >= '2026-06-16']
        with open(f'{BASE}/advisories_{sev}.json', 'w') as f:
            json.dump(filtered, f, indent=2)
        print(f"GH {sev}: {len(data)} total, {len(filtered)} last 48h")
        for v in filtered:
            pkgs = [(p.get('package') or {}).get('ecosystem','?') + ':' + (p.get('package') or {}).get('name','?')
                    for p in (v.get('vulnerabilities') or [])]
            cvss = (v.get('cvss') or {}).get('score','N/A')
            print(f"  {v.get('published_at','')} | {v.get('ghsa_id','')} | {v.get('cve_id','')} | CVSS:{cvss} | {', '.join(pkgs[:3])}")
            print(f"    {v.get('summary','')[:100]}")
    else:
        print(f"GH {sev} FAILED: {result.stderr[:100]}")
        with open(f'{BASE}/advisories_{sev}.json', 'w') as f:
            json.dump([], f)

print("\nDone.")
