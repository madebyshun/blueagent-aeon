*Security Digest — 2026-10-17*
Verdict: 2 KEV additions + 1 with public PoC. 4 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-102764](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — BeyondTrust Remote Support · KEV added 2026-10-16 · EPSS 0.006 · due 2026-10-19
  Auth bypass by spoofing → arbitrary file ops on appliance. Actively exploited per CISA.
  → apply vendor mitigation or discontinue use by Oct 19.

- [CVE-2025-61624](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Fortinet FortiOS/FortiPAM/FortiProxy/FortiSwitchManager · KEV added 2026-10-16 · EPSS 0.006 · due 2026-10-19
  Path traversal (authenticated admin) → write/delete arbitrary files via CLI. Exploited per CISA.
  → apply vendor mitigation by Oct 19.

- [CVE-2026-105192](https://github.com/advisories/GHSA-w5f2-9q9c-ff4h) — lmcache (pip) · CVSS 9.8 · EPSS 0.005 · public PoC
  RCE via unsafe ZeroMQ deserialization in multiprocess transport. PoC Python code published in advisory.
  → upgrade lmcache to ≥0.5.6 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-84994](https://github.com/advisories/GHSA-x586-xvc8-g7q6) — @builder.io/qwik / @qwik.dev/core (npm) · CVSS 8.7 · EPSS 0.005 · no public PoC
  Unauthenticated request thenable crashes Qwik server.
  → upgrade qwik to ≥1.20.0 / @qwik.dev/core to ≥2.0.0-beta37.

- [CVE-2026-100349](https://github.com/advisories/GHSA-74vm-87hj-r66f) — kin-openapi (Go) · CVSS 8.2 · EPSS 0.004 · no public PoC
  Nil-pointer panic in ValidateResponse on response header with content schema.
  → upgrade kin-openapi to ≥0.146.0.

- [CVE-2026-96620](https://github.com/advisories/GHSA-h4mw-j7qp-8mwm) — claude-agent-sdk (pip) · CVSS 9.2 · EPSS 0 · no public PoC
  Arg injection via resume option → arbitrary command exec, bypasses SDK permission controls. Requires untrusted session-ID input.
  → upgrade claude-agent-sdk to ≥0.2.121.

- [CVE-2026-96627](https://github.com/advisories/GHSA-pw5q-rjx4-7f7p) — Arcane backend (Go) · CVSS 8.8 · EPSS 0 · no public PoC
  users:update permission escalates to full admin via password reset.
  → upgrade arcane/backend to ≥2.6.0.
