*Security Digest — 2026-10-02*
Verdict: 3 actively exploited (KEV, infra), 5 in tracked stack to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-104286](https://nvd.nist.gov/vuln/detail/CVE-2026-104286) — Fortinet FortiMail · KEV added 2026-10-01 · EPSS 0.018 · CVSS n/a · due 2026-10-04
  Path traversal + null byte → unauthenticated arbitrary file write on underlying system. Actively exploited per CISA.
  → apply FortiMail patch per FG-IR-26-175 today.

- [CVE-2026-102489](https://nvd.nist.gov/vuln/detail/CVE-2026-102489) — Zammad · KEV added 2026-10-02 · EPSS 0.006 · CVSS n/a · due 2026-10-05
  Session fixation → RCE as zammad user. Chains with CVE-2026-102490 (local priv-esc to root). Exploited per CISA.
  → upgrade Zammad to latest patched release today.

- [CVE-2026-102490](https://nvd.nist.gov/vuln/detail/CVE-2026-102490) — Zammad · KEV added 2026-10-02 · EPSS 0.003 · CVSS n/a · due 2026-10-05
  Improper privilege management → local escalation to root. Chains with CVE-2026-102489 above.
  → upgrade Zammad to latest patched release today.

*PATCH THIS WEEK*
- [CVE-2026-102992](https://github.com/advisories/GHSA-67c8-pqhq-4rmx) — piscina (npm) · critical · EPSS 0.004 · CVSS n/a
  Prototype-pollution gadget in ThreadPool.options enables RCE via execArgv / loadBalancer / env.
  → upgrade piscina to ≥5.3.2.

- [CVE-2026-92958](https://github.com/advisories/GHSA-6rh5-qq4q-97xh) — vm2 (npm) · CVSS 8.5 · EPSS 0.004
  fs/promises denylist bypass despite -fs flag; allows host filesystem writes from sandboxed code. (10-01 batch tail, same fix.)
  → upgrade vm2 to ≥3.11.7.

- [CVE-2026-92950](https://github.com/advisories/GHSA-jxxv-8r27-vm4p) — vm2 (npm) · CVSS 8.6 · EPSS 0.002
  CLI provides no sandbox isolation; host-realm require() reachable from sandboxed scripts. (10-01 batch tail, same fix.)
  → upgrade vm2 to ≥3.11.7.

- [GHSA-9cqf-hhrq-7v45](https://github.com/advisories/GHSA-9cqf-hhrq-7v45) — siyuan/kernel (Go) · CVSS 8.6 · EPSS —
  Database row content returned to anonymous readers; no publish-access check on getAttributeViewSearchTarget. Reopens class closed one day earlier.
  → upgrade to ≥v3.1.26 (0.0.0-20260812083335).

- [CVE-2026-102831](https://github.com/advisories/GHSA-6966-vjj6-99xv) — jupyterlab (pip) · CVSS 8.1 · EPSS 0.002
  Stored XSS via notebook cells pasted from system clipboard.
  → upgrade jupyterlab to ≥4.6.4.
