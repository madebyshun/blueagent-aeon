*Security Digest — 2026-07-06*
Verdict: 1 actively exploited, 5 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-48558](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — SimpleHelp · KEV added 2026-06-29 · EPSS 1.16% · CVSS N/A
  OIDC tokens accepted without signature check → unauthenticated technician session hijack. Actively exploited per CISA. Due date 2026-07-02 already passed.
  → apply vendor patch and rotate all technician credentials today.

*PATCH THIS WEEK*
- [CVE-2026-52830](https://github.com/advisories/GHSA-rxw2-pc8j-vxwm) — fast-mcp-telegram (pip) · CVSS 9.4 · EPSS 0.42%
  Bearer token path traversal bypasses session protection in MCP Telegram transport.
  → upgrade fast-mcp-telegram to ≥0.19.1.
- [CVE-2026-41052](https://github.com/advisories/GHSA-vx8h-4prv-g744) — rancher/rancher (Go) · CVSS 9.4 · EPSS 0.32%
  Project owner escalates to cluster host via PSA label modification.
  → upgrade rancher to ≥2.14.2.
- [CVE-2026-53943](https://github.com/advisories/GHSA-62q6-4hv4-vjrw) — ghost (npm) · CVSS 9.6 · EPSS 0.24%
  Cache-poisoning XSS via x-ghost-preview header in frontend renderer.
  → upgrade ghost to ≥6.37.0.
- [CVE-2026-49352](https://github.com/advisories/GHSA-jphh-m39h-6gwx) — 9router (npm) · CVSS 9.8 · EPSS N/A
  Hardcoded JWT secret (auth bypass) + OS command injection via unprotected endpoint (GHSA-g6g7-pvmx-m74p, CVSS 9.2); both fixed in same release.
  → upgrade 9router to ≥0.4.45.
- [CVE-2026-50027](https://github.com/advisories/GHSA-84hp-mqvj-3p8h) — mcp-memory-service (pip) · CVSS 9.8 · EPSS N/A
  Missing auth on document API endpoints — unauthenticated read/write of memory store.
  → upgrade mcp-memory-service to ≥10.67.1.

*MONITOR*
- [CVE-2026-44935](https://github.com/advisories/GHSA-xr65-5cpm-g36x) — rancher/fleet (Go) · critical · EPSS 0.57% · fix: 0.15.2
  Cross-namespace secret disclosure via unvalidated valuesFrom references.
  → upgrade fleet to ≥0.15.2; schedule this sprint.
- [CVE-2022-46292](https://github.com/advisories/GHSA-55f6-pf8r-c2f4) — openbabel (pip) · CVSS 7.8 · EPSS 0.82% · fix: 3.2.0
  Out-of-bounds write in MOPAC translation vectors (4yr-old CVE, advisory published today).
  → upgrade openbabel to ≥3.2.0 if in use.
