*Security Digest — 2026-09-10*
Verdict: 1 actively exploited, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-60004](https://github.com/advisories/GHSA-rcr6-4jqh-j84m) — gitea (Go) · EPSS 86.8% · CVSS 9.8
  RCE via diffpatch git hook installation. EPSS 86.8% — near-certain active exploitation.
  → upgrade gitea to ≥1.27.1 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-75604](https://github.com/advisories/GHSA-p293-qw3h-jr36) — next (npm) · EPSS 2.5% · CVSS 9.0
  Unauthenticated RCE on Windows-hosted Next.js servers via path traversal. Affects v13.4–15.x and v16.x.
  → schedule upgrade: next → ≥15.5.24 (v15) or ≥16.3.3 (v16).

- [CVE-2026-59161](https://github.com/advisories/GHSA-q5j5-6p94-4gwc) — excelize/v2 (Go) · EPSS 0.66% · CVSS 8.7
  Streaming GetRows row-bound bypass causes attacker-controlled heap allocation.
  → schedule upgrade: excelize/v2 → ≥2.11.0.

- [CVE-2026-73294](https://github.com/advisories/GHSA-xp7j-h7jc-4w8p) — semaphoreui/semaphore (Go) · EPSS 0.57% · CVSS 9.9
  OS command injection via untrusted git_url argument. Authenticated low-priv exploitable.
  → schedule upgrade: semaphore → ≥0.0.0-20260704181911-7e8a9434bd81.

- [CVE-2026-78676](https://github.com/advisories/GHSA-284h-m62q-gf8w) — GitPython (pip) · EPSS 0.43% · CVSS 9.8
  Dormant multi-line git-config values corrupted into live injected directives — RCE.
  → schedule upgrade: GitPython → ≥3.1.59.

- [CVE-2026-86076](https://github.com/advisories/GHSA-hw8v-xxg5-vvvx) — n8n (npm) · EPSS 0.33% · CVSS 8.7
  Expression sandbox escape via class-field sanitizer rebinding — arbitrary code execution.
  → schedule upgrade: n8n → ≥1.123.76 / ≥2.37.7 / ≥2.38.2.
