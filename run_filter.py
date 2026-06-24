import json, re, sys

CUTOFF = "2026-06-22T00:00:00Z"
VALID_ECOSYSTEMS = {"npm", "pip", "Go", "crates.io", "actions"}
EXCLUDED_IDS = {
    "GHSA-w7mq-r738-x278", "CVE-2026-54352",
    "GHSA-r3cw-c95m-wfh9", "CVE-2026-46488",
    "GHSA-9m6g-wc8r-q59c", "CVE-2026-48170",
    "GHSA-jq8v-rmf6-65jw", "GHSA-52800", "GHSA-52801", "GHSA-52799",
    "GHSA-cq9c-6w48-qmfg", "CVE-2026-49229",
    "GHSA-74p7-6h78-gw8p"
}

POC_PATTERNS = re.compile(r'proof of concept|poc|exploit|demonstration', re.IGNORECASE)

files = [
    "/home/runner/.claude/projects/-home-runner-work-blueagent-aeon-blueagent-aeon/3b755d2e-e900-4d9f-9838-1e84d8e65340/tool-results/b331eo5nt.txt",
    "/home/runner/.claude/projects/-home-runner-work-blueagent-aeon-blueagent-aeon/3b755d2e-e900-4d9f-9838-1e84d8e65340/tool-results/b895j9jnp.txt",
]

results = []

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"JSON error in {filepath}: {e}", file=sys.stderr)
        data = []

    if not isinstance(data, list):
        data = [data]

    print(f"File {filepath}: {len(data)} advisories total", file=sys.stderr)

    for adv in data:
        ghsa_id = adv.get("ghsa_id", "")
        cve_id = adv.get("cve_id")
        published_at = adv.get("published_at", "")

        if published_at < CUTOFF:
            continue

        ids_to_check = {ghsa_id}
        if cve_id:
            ids_to_check.add(cve_id)
        if ids_to_check & EXCLUDED_IDS:
            continue

        vulns = adv.get("vulnerabilities", [])
        matching_packages = []
        has_valid_ecosystem = False
        for vuln in vulns:
            pkg = vuln.get("package", {})
            ecosystem = pkg.get("ecosystem", "")
            if ecosystem in VALID_ECOSYSTEMS:
                has_valid_ecosystem = True
                matching_packages.append({
                    "ecosystem": ecosystem,
                    "name": pkg.get("name", ""),
                    "patched_versions": vuln.get("patched_versions"),
                    "vulnerable_version_range": vuln.get("vulnerable_version_range"),
                })

        if not has_valid_ecosystem:
            continue

        summary = adv.get("summary", "") or ""
        description = adv.get("description", "") or ""

        cvss_score = None
        cvss = adv.get("cvss")
        if cvss and isinstance(cvss, dict):
            cvss_score = cvss.get("score")

        has_poc = bool(POC_PATTERNS.search(description)) or bool(POC_PATTERNS.search(summary))

        results.append({
            "ghsa_id": ghsa_id,
            "cve_id": cve_id,
            "summary": summary[:200],
            "severity": adv.get("severity"),
            "cvss_score": cvss_score,
            "published_at": published_at,
            "html_url": adv.get("html_url"),
            "packages": matching_packages,
            "has_poc": has_poc,
        })

print(f"Total matching: {len(results)}", file=sys.stderr)
print(json.dumps(results, indent=2))
