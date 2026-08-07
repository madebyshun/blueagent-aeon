*Security Digest — 2026-08-07*
Verdict: 5 KEV additions this week (3 shown), 4 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-34486](https://nvd.nist.gov/vuln/detail/CVE-2026-34486) — Apache Tomcat · KEV 2026-08-04 · EPSS 0.81 · CVSS 7.5
  EncryptInterceptor bypass, chainable with CVE-2025-24813 for session hijack. Due today.
  → apply Tomcat vendor patch per BOD 26-04 immediately.

- [CVE-2026-9198](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) — Langflow (pip) · KEV 2026-08-04 · EPSS 0.17 · CVSS 9.8
  Unauthenticated RCE on default Langflow deployments. Due today.
  → upgrade langflow now and redeploy; take offline if patching is delayed.

- [CVE-2026-18577](https://nvd.nist.gov/vuln/detail/CVE-2026-18577) — N-able N-central · KEV 2026-08-03 · EPSS 0.04 · CVSS n/a
  Auth bypass + account takeover; incomplete fix for CVE-2026-18556. Due 2026-08-06.
  → apply vendor mitigations. Also in KEV: CVE-2026-63077 (TeamCity RCE, CVSS 9.8, due 2026-08-08).

*PATCH THIS WEEK*
- [CVE-2026-65600](https://github.com/advisories/GHSA-cxjq-mrr5-89rv) — traefik (Go) · CVSS 9.1 · EPSS 0.004 · no PoC
  Auth bypass via ReplacePathRegex path traversal. Upgrading also fixes 3 more traefik CVEs (GHSA-fgjj-px3w-67xx CVSS 8.2, GHSA-3ccp-42pg-hgv6, GHSA-x677-9fxg-v5c5).
  → upgrade traefik to ≥3.7.10.

- [CVE-2026-71319](https://github.com/advisories/GHSA-279x-mwfv-vcqv) — @nuxt/devtools (npm) · CVSS 9.6 · EPSS 0.003 · no PoC
  Unauthenticated RCE via Vite HMR RPC on exposed dev port.
  → upgrade @nuxt/devtools to ≥3.3.1.

- [CVE-2026-69240](https://github.com/advisories/GHSA-v8fg-2rw7-q452) — sequelize (npm) · CVSS 9.8 · EPSS 0.003 · public PoC
  SQL injection Oracle dialect — TO_DATE escape bypass, data theft confirmed exploitable.
  → upgrade sequelize to ≥6.37.4.

- [CVE-2026-71320](https://github.com/advisories/GHSA-9473-5f9j-94wq) — nuxt (npm) · CVSS 8.1 · EPSS 0.004 · no PoC
  Server-side RCE via template injection in server island props (runtime compiler enabled).
  → upgrade nuxt to ≥4.5.1 (v4) or ≥3.21.10 (v3).

*MONITOR*
- [CVE-2026-16633](https://github.com/advisories/GHSA-hq66-cqwq-w95j) — pdfjs-dist (npm) · high · no CVSS · no fix listed
  Arbitrary JS execution on malicious PDF open. → patch to ≥6.2.108 if available; block untrusted PDF rendering.

- [CVE-2026-71476](https://github.com/advisories/GHSA-vp3h-ghgh-jr7g) — nx (npm) · EPSS 0.006 · no patch confirmed
  Zip-Slip in nx self-hosted remote cache on restore. → restrict cache to trusted sources; watch for patch.

- flowise/flowise-components (npm) ≤3.1.2 — 9 critical RCEs (CVE-2026-69251–CVE-2026-70478)
  Multiple sandbox escapes, code injection paths to full RCE. → isolate from public; verify 3.1.3+ availability.
