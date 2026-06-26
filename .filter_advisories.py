import json, sys

data = json.load(sys.stdin)
tracked = {'npm', 'pip', 'go', 'crates.io', 'github actions'}
for adv in data:
    ecosystems = [v['package']['ecosystem'].lower() for v in adv.get('vulnerabilities', [])]
    pkgs = [v['package']['name'] for v in adv.get('vulnerabilities', [])]
    patched = [v.get('first_patched_version') for v in adv.get('vulnerabilities', [])]
    if any(e in tracked for e in ecosystems) or not ecosystems:
        cvss = adv.get('cvss', {}).get('score', 0)
        epss_pct = adv.get('epss', {}).get('percentage', 0)
        print(f"GHSA: {adv['ghsa_id']} | CVE: {adv['cve_id']} | CVSS: {cvss} | EPSS: {epss_pct}")
        print(f"  Summary: {adv['summary']}")
        print(f"  Ecosystems: {ecosystems} | Pkgs: {pkgs}")
        print(f"  Patched: {patched}")
        print(f"  Published: {adv['published_at']}")
        print(f"  URL: {adv['html_url']}")
        print()
