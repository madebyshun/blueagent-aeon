*Security Digest — 2026-06-17*
Verdict: 3 KEV confirmed exploited (infra), 5 to schedule, 3 no fix yet. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY* _(actively exploited per CISA)_
- [CVE-2026-48907](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Widget Factory Joomla Content Editor · KEV 2026-06-16 · EPSS 0.047 · CVSS n/a
  Unauth PHP file upload via editor profile creation. Due 2026-06-19.
  → apply vendor mitigation; discontinue use if unavailable.

- [CVE-2026-20262](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Cisco Catalyst SD-WAN Manager · KEV 2026-06-15 · EPSS 0.011 · CVSS n/a
  Authenticated path traversal → create/overwrite filesystem files. Due 2026-06-29.
  → patch to vendor-fixed release.

- [CVE-2026-35273](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Oracle PeopleSoft PeopleTools · KEV 2026-06-12 · EPSS 0.007 · CVSS n/a
  Missing auth → full system takeover. CISA due date 2026-06-15 (PAST).
  → patch immediately; due date passed.

*PATCH THIS WEEK*
- [CVE-2026-54309](https://github.com/advisories/GHSA-qrx8-25qr-5r7v) — n8n (npm) · CVSS 10.0 · no PoC
  MCP Browser HTTP transport exposes unauthenticated browser-control sessions.
  → upgrade n8n to ≥ 2.26.2 (or ≥ 1.123.55 on v1).

- [CVE-2026-54305](https://github.com/advisories/GHSA-2j5h-858j-5mpf) — n8n (npm) · CVSS 9.9 · no PoC
  Cross-tenant credential takeover via Dynamic Credentials EE endpoints.
  → upgrade n8n to ≥ 2.26.2 (or ≥ 1.123.55 on v1).

- [CVE-2026-54307](https://github.com/advisories/GHSA-pmqw-72cg-wx85) — n8n (npm) · CVSS 9.6 · no PoC
  Credential exfiltration via permission bypass on workflow credentials.
  → upgrade n8n to ≥ 2.26.2.

- [CVE-2026-33760](https://github.com/advisories/GHSA-9c59-2mvc-vfr8) — langflow (pip) · CVSS 8.8 · no PoC
  IDOR/BOLA on 7 Monitor API endpoints — missing ownership enforcement.
  → upgrade langflow to ≥ 1.9.0.

- [CVE-2026-52845](https://github.com/advisories/GHSA-f59h-q822-g45g) — caddy (go) · CVSS 8.1 · no PoC
  FastCGI header normalization bypass in forward_auth copy_headers.
  → upgrade caddy to ≥ 2.11.4.

*MONITOR*
- [CVE-2026-49980](https://github.com/advisories/GHSA-qw24-gh76-8rvv) — rclone (go) · CVSS 9.8 · no fix
  Unauth RCE via rcd --rc-serve inline remote instantiation (bypasses CVE-2026-41179 fix). ≥ 1.55.0.
  → avoid exposing rclone rc port; watch for patch.

- [CVE-2026-49468](https://github.com/advisories/GHSA-4xpc-pv4p-pm3w) — litellm (pip) · no fix
  Auth bypass via host header injection. < 1.84.0.
  → enforce strict host validation upstream; watch GHSA-4xpc-pv4p-pm3w.

- [GHSA-365w-hqf6-vxfg](https://github.com/advisories/GHSA-365w-hqf6-vxfg) — crawl4ai (pip) · CVSS 9.8 · no fix
  5+ pre-auth vulns in Docker server: RCE, auth bypass, SSRF, file write. ≤ 0.8.8.
  → do not expose crawl4ai Docker API publicly; watch for patched release.
