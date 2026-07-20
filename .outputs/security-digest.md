*Security Digest — 2026-07-20*
Verdict: 3 KEV overdue (infrastructure), 3 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-39808](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Fortinet FortiSandbox · KEV 2026-07-16 · EPSS 0.842 · CVSS —
  Unauth OS command injection via crafted HTTP. Highest active exploitation probability of the week.
  → Apply FortiSandbox vendor mitigations per BOD 26-04 today; discontinue if unavailable.

- [CVE-2026-25089](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Fortinet FortiSandbox · KEV 2026-07-16 · EPSS 0.361 · CVSS —
  Unauth arbitrary command execution. Same product and attack surface as CVE-2026-39808.
  → Apply FortiSandbox vendor mitigations per BOD 26-04 today; discontinue if unavailable.

- [CVE-2008-4128](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Cisco IOS · KEV 2026-07-13 · EPSS 0.239 · CVSS —
  CSRF via HTTP interface enables remote command execution. All three KEV due dates overdue.
  → Apply Cisco IOS patch; disable HTTP server or restrict admin access per BOD 26-04.

*PATCH THIS WEEK*
- [CVE-2026-53713 / GHSA-wcrf-9vrr-854f](https://github.com/advisories/GHSA-wcrf-9vrr-854f) — envoy-gateway (Go) · CVSS 9.1 · EPSS n/a
  Auth bypass via improper Lua validation in EnvoyExtensionPolicy — allows secret disclosure.
  → upgrade envoy-gateway to ≥1.7.4 (1.7.x) or ≥1.8.1 (1.8.x) and redeploy.

- [CVE-2026-52833 / GHSA-3v79-m2cg-89ww](https://github.com/advisories/GHSA-3v79-m2cg-89ww) — nuclio (Go) · CVSS 8.0 · EPSS n/a
  Unsanitized runtimeAttributes.repositories injected into Groovy build.gradle → build-time RCE.
  → upgrade nuclio to ≥1.16.5 and redeploy.

- [GHSA-vj7q-gjh5-988w](https://github.com/advisories/GHSA-vj7q-gjh5-988w) + [GHSA-jpw9-pfvf-9f58](https://github.com/advisories/GHSA-jpw9-pfvf-9f58) + [GHSA-hvrp-rf83-w775](https://github.com/advisories/GHSA-hvrp-rf83-w775) — mcp Python SDK (pip) · CVSS 7.1–7.6 · EPSS n/a
  Three high CVEs in mcp <1.28.1: WebSocket host validation bypass, HTTP session auth bypass, cross-client task handler access.
  → upgrade mcp to ≥1.28.1.

*MONITOR*
- [CVE-2026-54504 / GHSA-6f5r-5672-72j7](https://github.com/advisories/GHSA-6f5r-5672-72j7) — @andrea9293/mcp-documentation-server (npm) · CVSS 8.8 · no fix yet
  Web UI API binds to 0.0.0.0 without authentication by default. No patched release confirmed.
  → restrict to localhost or remove; track GHSA-6f5r-5672-72j7 for patch.
