import sys, json
data = json.load(sys.stdin)
if isinstance(data, list):
    items = data
else:
    items = []
recent = [a for a in items if a.get('published_at','') >= '2026-06-12']
print(f"Total: {len(items)}, Recent (>=Jun12): {len(recent)}")
for a in recent:
    cve = a.get('cve_id') or 'no-cve'
    score = (a.get('cvss') or {}).get('score', 'N/A')
    pkgs = [(v['package']['ecosystem'], v['package']['name'], v.get('patched_versions',''), v.get('vulnerable_version_range','')) for v in a.get('vulnerabilities',[]) if v.get('package')]
    print(f"\n{a['ghsa_id']} | {cve} | CVSS:{score} | {a['published_at'][:10]}")
    print(f"  {a['summary'][:100]}")
    for eco, name, patched, vulnr in pkgs:
        print(f"  PKG: [{eco}] {name} | patched:{patched} | vuln:{vulnr}")
