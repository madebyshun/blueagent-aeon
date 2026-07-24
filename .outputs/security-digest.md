*Security Digest — 2026-07-24*
Verdict: nothing urgent today. 4 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-59935 + 59936](https://github.com/advisories/GHSA-g867-7843-wf8q) — pypdf (pip) · CVSS 8.7 · EPSS 0.004 · no PoC
  Dual infinite-loop DoS in PDF inline image parsing. Two CVEs, one fix.
  → upgrade pypdf to ≥6.14.2.

- [CVE-2026-55575](https://github.com/advisories/GHSA-g357-x5c3-c72p) — liquidjs (npm) · CVSS 8.2 · EPSS 0.004 · public PoC
  `pop` filter bypasses `memoryLimit` — attacker allocates unbounded arrays regardless of budget.
  → upgrade liquidjs to ≥10.27.1.

- [CVE-2026-54673](https://github.com/advisories/GHSA-p2f4-r6v6-j797) — builder-util-runtime (npm) · CVSS 8.2 · EPSS 0.002 · no PoC
  Cross-origin redirect leaks PRIVATE-TOKEN and mixed-case Authorization headers to attacker hosts.
  → upgrade builder-util-runtime to ≥9.7.0 (electron-builder: update electron-builder).

- [CVE-2026-55685](https://github.com/advisories/GHSA-chx6-hx7r-mcp5) — react-router 7.x (npm) · CVSS unscored · no PoC
  Unauthenticated DoS via inefficient route matching in Framework Mode. All v7.0–v7.17.x affected.
  → upgrade react-router to ≥7.18.0.
