*Security Digest — 2026-08-01*
Verdict: 1 PoC-confirmed critical, 5 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-67429](https://github.com/advisories/GHSA-2956-977x-2w3r) — flyto-core (pip) · CVSS 10.0 · EPSS 0.005 · PoC published
  Arbitrary file write, no auth — output_dir='/' bypasses sandbox; all file-writing modules affected incl. MCP interface.
  → upgrade flyto-core to ≥2.26.7 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-55100](https://github.com/advisories/GHSA-g956-2f74-rmv7) — hashi-vault-js (npm) · CVSS 8.7 · EPSS 0.004 · no PoC
  Unencoded identifiers → path traversal to sys/ admin paths or query injection with app's Vault token.
  → upgrade hashi-vault-js to ≥0.5.2.
- [CVE-2026-53502](https://github.com/advisories/GHSA-cj54-hpcc-gj6h) — thumbor (pip) · CVSS 8.7 · EPSS 0.004 · no PoC
  Path traversal via post-validation URL-decode bypass in file_loader.
  → upgrade thumbor to ≥7.8.0 (clears 6 CVEs in this batch).
- [CVE-2026-54729](https://github.com/advisories/GHSA-5846-7qm3-r52j) — dssrf (npm) · CVSS 8.7 · EPSS 0.003 · no PoC
  SSRF via 1.1.1.1 DNS NXDOMAIN for localhost; localhost filter bypassed.
  → upgrade dssrf to ≥1.0.5.
- [CVE-2026-67426](https://github.com/advisories/GHSA-jx74-cqjv-2c67) — flyto-core (pip) · CVSS 9.3 · EPSS 0.003 · PoC published
  Unauthed SSRF + runner-secret exfiltration via unvalidated callback_url; leaks FLYTO_RUNNER_SECRET.
  → upgrade flyto-core to ≥2.26.7.
- [CVE-2026-53500](https://github.com/advisories/GHSA-6x26-6r6f-m537) — thumbor (pip) · CVSS 8.2 · EPSS 0.003 · no PoC
  ALLOWED_SOURCES strings treated as unescaped regex; hostname-bypass via crafted domain.
  → upgrade thumbor to ≥7.8.0.
