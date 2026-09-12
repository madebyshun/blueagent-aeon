import json, sys

filepath = sys.argv[1] if len(sys.argv) > 1 else '/home/runner/.claude/projects/-home-runner-work-blueagent-aeon-blueagent-aeon/b6300ec5-bd2f-453d-9349-cc8793700f56/tool-results/bfsykufnu.txt'

with open(filepath) as f:
    data = json.load(f)

TRACKED = {'npm', 'pip', 'Go', 'crates.io', 'GitHub Actions', 'RubyGems', 'Maven', 'NuGet'}

recent = [a for a in data if a.get('published_at','') >= '2026-09-10']
print(f'Total: {len(data)}, since 2026-09-10: {len(recent)}')

for a in recent:
    pkgs = a.get('vulnerabilities', [])
    ecosystems = list(set(p.get('package',{}).get('ecosystem','') for p in pkgs if p.get('package')))
    tracked_match = bool(set(ecosystems) & TRACKED)
    pkg_names = [p.get('package',{}).get('name','') for p in pkgs if p.get('package')]
    patched = [p.get('patched_versions','') for p in pkgs]
    cvss = a.get('cvss', {})
    cve = a.get('cve_id','')
    print(f"{'[TRACKED]' if tracked_match else '[SKIP]'} {a['ghsa_id']} | {cve} | CVSS {cvss.get('score','?')} | {a.get('published_at','')[:10]} | ecosystems:{ecosystems}")
    print(f"  pkgs: {pkg_names[:5]}")
    print(f"  patched: {patched[:3]}")
    print(f"  summary: {a.get('summary','')[:120]}")
    print()
