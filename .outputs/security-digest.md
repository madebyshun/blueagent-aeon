*Security Digest — 2026-06-23*
Verdict: nothing urgent today. 5 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-54352](https://github.com/advisories/GHSA-w7mq-r738-x278) — @budibase/server (npm) · CVSS 9.6 · EPSS n/a · public PoC
  Symlink upload reads any server file incl. env vars + credentials; default Docker image runs as root. Also covers 6 Budibase high-sev fixes in 3.39.x (SSRF, S3 pre-sign bypass, CSRF). → upgrade @budibase/* to ≥3.39.9.

- [CVE-2026-46488](https://github.com/advisories/GHSA-r3cw-c95m-wfh9) — motioneye (pip) · CVSS 9.1 · EPSS n/a
  Auth bypass via cookie manipulation and password hash exploitation. → upgrade motioneye to ≥0.44.0.

- [CVE-2026-48170](https://github.com/advisories/GHSA-9m6g-wc8r-q59c) — scim-patch (npm) · CVSS 9.1 · EPSS n/a · public PoC
  Prototype pollution via SCIM PATCH keys — enables privilege escalation and logic bypass process-wide. → upgrade scim-patch to ≥0.9.1.

- [Gogs cluster](https://github.com/advisories/GHSA-jq8v-rmf6-65jw) — gogs (Go) · CVSS 8.9 top · EPSS n/a
  4 CVEs: stored XSS in .ipynb preview (8.9), CSRF→org owner takeover (8.8), local repo import bypass (8.1), unauth attachment download (7.5). → upgrade Gogs to ≥0.14.3.

- [CVE-2026-49229](https://github.com/advisories/GHSA-cq9c-6w48-qmfg) — @actual-app/sync-server (npm) · CVSS 8.3 · EPSS n/a
  Disabled OpenID users retain valid session tokens indefinitely. → upgrade @actual-app/sync-server to ≥26.6.0.

*MONITOR*
- [GHSA-74p7-6h78-gw8p](https://github.com/advisories/GHSA-74p7-6h78-gw8p) — skillctl (crates.io) · no CVSS · no fix listed
  Arg injection in git, path traversal, FIFO DoS, hardlink exfiltration, commit-trailer forgery. → track; watch for patched release.
