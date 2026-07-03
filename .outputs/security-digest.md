*Security Digest — 2026-07-03*
Verdict: 2 actively exploited (CISA KEV) + 1 critical npm PoC · 5 to patch this week · 3 to monitor _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-45659](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Microsoft SharePoint Server · KEV 2026-07-01 · EPSS 0.032 · CVSS N/A
  Deserialization RCE via authenticated network request. Due date: 2026-07-04.
  → Apply Microsoft SharePoint patch immediately.

- [CVE-2026-48558](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — SimpleHelp · KEV 2026-06-29 · EPSS 0.012 · CVSS N/A
  OIDC auth bypass — unauthenticated attackers forge tokens for full sessions. Due: 2026-07-02 (overdue).
  → Upgrade SimpleHelp per vendor advisory.

- [CVE-2026-49352](https://github.com/advisories/GHSA-jphh-m39h-6gwx) — npm/9router · CVSS 9.8 · EPSS 0 · public PoC in advisory
  Hardcoded fallback JWT secret ("9router-default-secret-change-me") — forge auth tokens if JWT_SECRET unset.
  → upgrade 9router to ≥0.4.45 and set JWT_SECRET env var.

*PATCH THIS WEEK*
- [CVE-2026-50027](https://github.com/advisories/GHSA-84hp-mqvj-3p8h) — pip/mcp-memory-service · CVSS 9.8 · EPSS 0
  Unauthenticated read/write/delete on all document API endpoints.
  → upgrade mcp-memory-service to ≥10.67.1.

- [CVE-2026-52830](https://github.com/advisories/GHSA-rxw2-pc8j-vxwm) — pip/fast-mcp-telegram · CVSS 9.4 · EPSS 0.004
  Bearer token path traversal bypasses Telegram session file protection.
  → upgrade fast-mcp-telegram to ≥0.19.1.

- [CVE-2026-49255](https://github.com/advisories/GHSA-v5ff-xmfp-p245) — npm/electerm · CVSS 8.8 · EPSS 0
  Command injection in rmrf/mv/cp file system ops.
  → upgrade electerm to ≥3.11.11.

- [GHSA-g6g7-pvmx-m74p](https://github.com/advisories/GHSA-g6g7-pvmx-m74p) — npm/9router · critical · CVSS N/A · EPSS 0
  Missing auth + OS command injection (companion to CVE-2026-49352).
  → upgrade 9router to ≥0.4.45.

- [CVE-2026-49360](https://github.com/advisories/GHSA-rh62-j648-g5qc) — pip/recce · high · CVSS N/A · EPSS 0
  Unauthenticated SQL exec via query API → DuckDB file read/write.
  → upgrade recce to ≥1.50.0 or restrict to trusted networks.

*MONITOR*
- [CVE-2026-49353](https://github.com/advisories/GHSA-6g2f-w7g3-77vf) — npm/9router · CVSS 7.5 · EPSS 0 · no patch
  Incomplete fix — Host header spoofing bypasses local-only access gate.
  → watch for patch; enforce strict Host validation at reverse proxy.

- [GHSA-vv65-f55v-xm6g](https://github.com/advisories/GHSA-vv65-f55v-xm6g) — npm/@grackle-ai · high · CVSS N/A · no patch
  Git worktree arg injection → RCE via unsanitized input on provisioned hosts.
  → avoid exposing worktree API to untrusted input; watch for fix.

- [GHSA-f9ff-5x35-7gfw](https://github.com/advisories/GHSA-f9ff-5x35-7gfw) — npm/@grackle-ai/mcp · high · CVSS N/A · no patch
  Fail-open auth — scoped agents bypass task/session boundaries in MCP tool layer.
  → restrict to trusted environments; watch for patch.
