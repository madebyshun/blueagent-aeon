*Security Digest — 2026-09-06*
Verdict: 3 actively exploited (Sep 2 KEV re-surfaced). 0 new KEV additions today. 1 new crates.io advisory. 5 to schedule.
_Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY* (KEV Sep 2 — confirmed exploitation, outside 2-day dedup window)
- [CVE-2026-48710](https://github.com/advisories/GHSA-86qp-5c8j-p5mr) — Starlette (pip) · KEV 2026-09-02 · EPSS 0.36 · CVSS 6.5
  Host header omission → path-based auth bypass. Exploited per CISA.
  → upgrade starlette to ≥1.0.1 and redeploy.

- CVE-2026-9586 — Sangoma Switchvox · KEV 2026-09-02 · EPSS 0.12
  SQL injection → unauth arbitrary query execution + RCE vs PostgreSQL backend.
  → apply vendor patch; isolate admin interface.

- CVE-2026-82329 — JFrog Artifactory · KEV 2026-09-02 · EPSS 0.08
  Default-config auth bypass → unauthenticated admin privilege escalation.
  → apply JFrog Artifactory security update today.

*PATCH THIS WEEK*
- [CVE-2026-59822](https://github.com/advisories/GHSA-7488-6r32-c95q) — LiteLLM (pip) · KEV 2026-09-02 · EPSS 0.009 · CVSS 8.8
  Fabricated Bearer token establishes authenticated MCP session → all connected tools exposed.
  → upgrade litellm to ≥1.84.0.

- [GHSA-848m-r628-vrxw](https://github.com/advisories/GHSA-848m-r628-vrxw) — SurrealDB (crates.io) · CVSS 8.1 · EPSS 0.004 · no public PoC [NEW]
  Authenticated cross-tenant namespace traversal → reach another tenant's custom API endpoints.
  → schedule upgrade: surrealdb → ≥3.2.0.

- CVE-2026-49869 — Kestra OSS · KEV 2026-09-02 · EPSS 0.019
  Unauth OS command injection via workflow creation → unauthenticated RCE.
  → apply vendor patch; restrict workflow creation endpoint.

- CVE-2026-83549 — SonicWall SMA1000 · KEV 2026-09-02 · EPSS 0.016
  Admin-auth OS command injection → RCE. Exploited per CISA.
  → apply SonicWall SMA1000 firmware update.

- CVE-2026-83548 — SonicWall SMA1000 · KEV 2026-09-02 · EPSS 0.007
  Unauth SSRF → internal sensitive function access and unauthorized operations.
  → apply SonicWall SMA1000 firmware update.
