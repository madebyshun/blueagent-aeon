#!/usr/bin/env python3
import subprocess
import json
import sys
from datetime import datetime

CUTOFF = "2026-07-06"
ALLOWED_ECOSYSTEMS = {"npm", "pip", "go", "crates.io", "github actions", "rubygems", "maven", "nuget"}
SEEN = {
    "GHSA-vjc7-jrh9-9j86", "CVE-2026-54769", "GHSA-q9p7-wqxg-mrhc", "CVE-2026-55500",
    "GHSA-qvfm-67h2-2qfx", "CVE-2026-49445", "GHSA-3fcv-jvfp-m4q9", "CVE-2026-53486",
    "GHSA-mp2f-45pm-3cg9", "CVE-2026-55786", "GHSA-h9f9-h6gm-wc85", "GHSA-9rjw-3gwp-f59v",
    "CVE-2026-54496", "GHSA-ww9q-8r59-xv46", "CVE-2026-54771", "GHSA-gjgq-w2m6-wr5q",
    "CVE-2026-55615", "GHSA-2pq5-3q89-j7cc"
}

def fetch_advisories(severity):
    result = subprocess.run(
        ["gh", "api", f"/advisories?type=reviewed&severity={severity}&per_page=100",
         "-H", "Accept: application/vnd.github+json"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        sys.stderr.write(f"Error fetching {severity}: {result.stderr}\n")
        return []
    return json.loads(result.stdout)

def is_recent(published_at):
    if not published_at:
        return False
    date_str = published_at[:10]
    return date_str >= CUTOFF

def has_allowed_ecosystem(advisory):
    vulns = advisory.get("vulnerabilities") or []
    for v in vulns:
        pkg = v.get("package") or {}
        eco = (pkg.get("ecosystem") or "").lower()
        if eco in ALLOWED_ECOSYSTEMS:
            return True
    return False

def is_seen(advisory):
    ghsa = advisory.get("ghsa_id") or ""
    cve = advisory.get("cve_id") or ""
    return ghsa in SEEN or cve in SEEN

def extract(advisory):
    vulns = advisory.get("vulnerabilities") or []
    ecosystems = list({(v.get("package") or {}).get("ecosystem", "").lower() for v in vulns if (v.get("package") or {}).get("ecosystem")})
    package_names = list({(v.get("package") or {}).get("name", "") for v in vulns if (v.get("package") or {}).get("name")})
    patched_versions = []
    for v in vulns:
        pv = v.get("patched_versions")
        if pv:
            patched_versions.append(pv)
    cvss = advisory.get("cvss") or {}
    return {
        "ghsa_id": advisory.get("ghsa_id"),
        "cve_id": advisory.get("cve_id"),
        "severity": advisory.get("severity"),
        "cvss_score": cvss.get("score"),
        "summary": advisory.get("summary"),
        "ecosystems": ecosystems,
        "package_names": package_names,
        "patched_versions": patched_versions,
        "html_url": advisory.get("html_url"),
        "published_at": advisory.get("published_at"),
        "epss_score": None
    }

critical = fetch_advisories("critical")
high = fetch_advisories("high")

all_advisories = critical + high

seen_ghsa = set()
filtered = []
for adv in all_advisories:
    ghsa = adv.get("ghsa_id", "")
    if ghsa in seen_ghsa:
        continue
    seen_ghsa.add(ghsa)
    if not is_recent(adv.get("published_at")):
        continue
    if not has_allowed_ecosystem(adv):
        continue
    if is_seen(adv):
        continue
    filtered.append(extract(adv))

cve_ids = [a["cve_id"] for a in filtered if a.get("cve_id")]

epss_raw = None
if cve_ids:
    cve_param = ",".join(cve_ids)
    try:
        result = subprocess.run(
            ["curl", "-sf", "--max-time", "20",
             f"https://api.first.org/data/v1/epss?cve={cve_param}"],
            capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            epss_raw = json.loads(result.stdout)
        else:
            epss_raw = None
    except Exception:
        epss_raw = None

if epss_raw is None and cve_ids:
    import urllib.request
    cve_param = ",".join(cve_ids)
    try:
        url = f"https://api.first.org/data/v1/epss?cve={cve_param}"
        with urllib.request.urlopen(url, timeout=20) as resp:
            epss_raw = json.loads(resp.read().decode())
    except Exception as e:
        sys.stderr.write(f"WebFetch fallback also failed: {e}\n")
        epss_raw = None

if epss_raw and isinstance(epss_raw, dict):
    epss_map = {}
    for item in epss_raw.get("data", []):
        epss_map[item.get("cve", "").upper()] = item.get("epss")
    for adv in filtered:
        cve = adv.get("cve_id")
        if cve and cve.upper() in epss_map:
            adv["epss_score"] = float(epss_map[cve.upper()])

output = {
    "advisories": filtered,
    "epss_raw": epss_raw
}
print(json.dumps(output, indent=2))
