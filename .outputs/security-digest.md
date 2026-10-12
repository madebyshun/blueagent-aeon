*Security Digest — 2026-10-12*
Verdict: 3 actively exploited (KEV, BOD 26-04 overdue), 5 to schedule, 1 to monitor. _Sources: CISA KEV +5, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2015-3306](https://nvd.nist.gov/vuln/detail/CVE-2015-3306) — ProFTPD · KEV 2026-10-08 · EPSS 0.995 · CVSS 9.8
  Unauth file read/write via SITE CPFR/CPTO. BOD 26-04 due 2026-10-11 — OVERDUE.
  → patch ProFTPD; disable mod_copy if unused; restrict FTP to trusted hosts.

- [CVE-2015-5477](https://nvd.nist.gov/vuln/detail/CVE-2015-5477) — ISC BIND · KEV 2026-10-08 · EPSS 0.994 · CVSS 7.5
  Remote DoS via crafted TKEY queries. BOD 26-04 due 2026-10-11 — OVERDUE.
  → upgrade BIND or apply vendor mitigation immediately.

- [CVE-2016-3081](https://nvd.nist.gov/vuln/detail/CVE-2016-3081) — Apache Struts · KEV 2026-10-08 · EPSS 0.961 · CVSS 9.8
  RCE via Dynamic Method Invocation (method: prefix). BOD 26-04 due 2026-10-11 — OVERDUE.
  → disable DMI; upgrade to patched Struts 2.x release.

*PATCH THIS WEEK*
- [CVE-2023-22894](https://nvd.nist.gov/vuln/detail/CVE-2023-22894) — Strapi (npm) · KEV 2026-10-08 · EPSS 0.036 · CVSS 7.7
  Cleartext admin panel storage → chains with CVE-2023-22621 for RCE. KEV overdue; may be EoL.
  → upgrade Strapi to supported version; restrict admin panel access.

- [GHSA-w7x8-q2gp-5cgg](https://github.com/advisories/GHSA-w7x8-q2gp-5cgg) — flowise (npm) · CVSS 9.0 · EPSS 0.010
  Prompt injection → RCE via CSV/Airtable Python validator bypass. Published 2026-10-07.
  → upgrade flowise + flowise-components to ≥3.1.3.

- [GHSA-pq68-rvw4-xp4r](https://github.com/advisories/GHSA-pq68-rvw4-xp4r) — vm2 (npm) · CVSS 10.0 · EPSS 0.007
  Sandbox escape. Published 2026-10-07.
  → upgrade vm2 to ≥3.12.1.

- [GHSA-6rvj-qwjf-3m4q](https://github.com/advisories/GHSA-6rvj-qwjf-3m4q) — Vikunja (Go) · CVSS 8.7 · EPSS 0.006
  /api/v2 pre-auth endpoints unthrottled — enables credential brute force. Published 2026-10-09.
  → upgrade code.vikunja.io/api to ≥2.6.0.

- [GHSA-9gvv-qjj3-2p6g](https://github.com/advisories/GHSA-9gvv-qjj3-2p6g) — flowise (npm) · CVSS 9.4 · EPSS 0.006
  NodeVM sandbox escape via puppeteer allowlist → authenticated RCE + arbitrary file read. Published 2026-10-07.
  → upgrade flowise + flowise-components to ≥3.1.3.

*MONITOR*
- [GHSA-32r8-5843-4qw2](https://github.com/advisories/GHSA-32r8-5843-4qw2) — Vikunja (Go) · CVSS 7.5 · EPSS 0.004 · no fix yet
  Link-share principal-type confusion → cross-account team removal + bot access. Published 2026-10-09.
  → track GHSA-32r8-5843-4qw2; avoid public link-share team management until patched.
