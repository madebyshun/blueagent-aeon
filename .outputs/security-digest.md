*Security Digest — 2026-10-07*
Verdict: 3 confirmed exploited (KEV), 5 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-104286 — Fortinet FortiMail · KEV 2026-10-01 · EPSS 0.022 · CVSS —
  Unauth path traversal → arbitrary file write via crafted HTTP/HTTPS. Active exploitation confirmed.
  → upgrade FortiMail per vendor advisory; BOD 26-04 deadline passed.

- CVE-2026-76504 — Cisco Catalyst SD-WAN Manager · KEV 2026-09-30 · EPSS 0.018 · CVSS —
  Hex-encoded URI bypass grants unauth remote admin access. Active exploitation confirmed.
  → upgrade SD-WAN Manager per Cisco advisory; BOD 26-04 deadline passed.

- CVE-2026-102489 — Zammad · KEV 2026-10-02 · EPSS 0.014 · CVSS —
  Session fixation → RCE as zammad user; chains with CVE-2026-102490 (priv esc → root).
  → upgrade Zammad per vendor advisory; BOD 26-04 deadline passed.

*PATCH THIS WEEK*
- GHSA-pq68-rvw4-xp4r — vm2 (npm) · CVSS 10.0 · EPSS 0.007 · no patch
  Sandbox escape, all vm2 ≤3.12.0. Project unmaintained.
  → replace vm2 with isolated-vm or native Node worker_threads now.

- GHSA-r543-q48m-4c9j — WeasyPrint (pip) · CVSS 8.8 · EPSS 0.007 · no patch
  EPS images route through Ghostscript → RCE. All versions ≤69.0 affected.
  → block EPS input to WeasyPrint; disable Ghostscript path until patch lands.

- GHSA-g2v8-7jhw-pp8p — @backstage/plugin-scaffolder-backend (npm) · CVSS 9.6 · EPSS 0.005
  Sensitive info exposure in Scaffolder. Lead advisory of a 10-advisory Backstage batch.
  → upgrade plugin-scaffolder-backend ≥4.1.0 and plugin-techdocs-node ≥1.15.4.

- GHSA-qmw3-745m-w99g — @backstage/plugin-techdocs-node (npm) · CVSS 8.8 · EPSS —
  Improper MkDocs config validation; 5 related TechDocs CVEs in same release.
  → upgrade plugin-techdocs-node ≥1.15.4 (fixes all TechDocs batch CVEs).

- GHSA-826h-28h9-65hg — @backstage/plugin-auth-backend-module-oidc-provider (npm) · CVSS 8.1 · EPSS 0.003
  Improper OIDC auth; affects OIDC-based SSO flows.
  → upgrade plugin-auth-backend-module-oidc-provider ≥0.4.20.

*MONITOR*
- GHSA-c3wx-c55w-pxjq — hydra-core (pip) · CVSS 7.8 · EPSS 0.002
  Unsafe callable resolution in logging config; code exec path.
  → schedule upgrade: hydra-core → ≥1.3.6.

- GHSA-jg6q-3qfh-r9f8 — @insumermodel/mppx-condition-gate (npm) · CVSS 7.5 · EPSS 0.003
  Wallet access without ownership proof; no patch.
  → track; avoid mppx-condition-gate/mppx-token-gate until patched.

- GHSA-cq7v-rfgc-5c7v — @backstage/backend-defaults (npm) · CVSS 7.6 · EPSS 0.002
  Credential delegation drops access restrictions.
  → schedule upgrade: @backstage/backend-defaults → ≥0.17.8.
