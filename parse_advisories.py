import json, sys
data = json.load(sys.stdin)
results = []
for a in data:
    pkgs = []
    for v in (a.get('vulnerabilities') or []):
        p = v.get('package') or {}
        pkgs.append({'ecosystem': p.get('ecosystem',''), 'name': p.get('name',''), 'patched': v.get('patched_versions',''), 'vuln_range': v.get('vulnerable_version_range','')})
    cvss_obj = a.get('cvss') or {}
    results.append({'ghsa_id': a.get('ghsa_id'), 'cve_id': a.get('cve_id'), 'summary': a.get('summary'), 'severity': a.get('severity'), 'cvss_score': cvss_obj.get('score'), 'packages': pkgs, 'html_url': a.get('html_url'), 'published_at': a.get('published_at')})
print(json.dumps(results, indent=2))
