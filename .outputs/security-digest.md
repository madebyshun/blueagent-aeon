*Security Digest — 2026-09-24*
Verdict: 1 KEV due tomorrow + 1 critical PoC, 4 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-93952](https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183) — Arista VeloCloud Orchestrator · KEV added 2026-09-22 · EPSS 0.009 · BOD 26-04 due 2026-09-25
  Improper input validation enables remote privilege escalation + RCE. Actively exploited per CISA. BOD remediation due tomorrow.
  → apply Arista vendor mitigations or discontinue internet exposure today.

- [CVE-2026-59167](https://github.com/advisories/GHSA-6rf4-v2fh-m6p4) — suneditor (npm) · CVSS 10.0 · EPSS 0.004 · public PoC
  Sanitizer bypass via namespaced HTML elements enables stored XSS, session hijack, credential theft. PoC published.
  → upgrade suneditor to ≥2.47.11 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-91130](https://github.com/advisories/GHSA-wx4m-69m9-gx3m) — homeassistant (pip) · CVSS 9.3 · EPSS 0.004 · public PoC
  Statistics Graph card renders entity names as raw HTML; integration providers can silently deliver XSS.
  → upgrade homeassistant to ≥2026.7.0.

- [CVE-2026-63132](https://github.com/advisories/GHSA-34fc-gh42-pj53) — openbao (Go) · CVSS 9.1 · EPSS 0.005
  Timing attack on recovery mode token validation allows full instance compromise.
  → upgrade github.com/openbao/openbao to ≥v2.6.0.

- [CVE-2026-61685](https://github.com/advisories/GHSA-wmw4-mw6x-6vfm) — @fecommunity/reactpress (npm) · High · EPSS 0.005
  SQL injection via dynamic column names in TypeORM query builders.
  → schedule upgrade to patched version.

- [CVE-2026-58269](https://github.com/advisories/GHSA-92cr-jxw4-5wjg) — @sync-in/server (npm) · High · EPSS 0.002
  Complete 2FA bypass via POST /api/auth/token.
  → schedule upgrade to patched version.

*MONITOR*
- [CVE-2026-85734](https://github.com/advisories/GHSA-frch-4w6v-q5xx) — lightrag-hku (pip) · Critical · EPSS 0.004 · no patch
  No rate limiting on /login allows brute-force credential attacks.
  → add reverse-proxy rate limiting; watch for patch.

- [CVE-2026-77394](https://github.com/advisories/GHSA-gvf2-2rh5-mpgf) — @openc3/vue-common (npm) · High · EPSS 0.004
  Stored cross-user XSS via Telemetry screen BUTTON widget.
  → restrict telemetry UI access; track GHSA-gvf2-2rh5-mpgf for patch.

- [CVE-2026-56681](https://github.com/advisories/GHSA-5mj8-gf6m-fhw8) — 9router (npm) · High · EPSS 0.005
  Auth bypass via spoofable X-9r-Real-Ip header in LLM API routes.
  → avoid exposing LLM API publicly; watch for patched release.
