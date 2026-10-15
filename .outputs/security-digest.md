*Security Digest — 2026-10-15*
Verdict: 3 actively exploited, 0 likely soon, 0 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-105134](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) — Ahsay AhsayCBS · KEV added 2026-10-14 · EPSS 0.032 · CVSS n/a
  Command injection in replication endpoint; chains with CVE-2026-105133 (auth bypass) → unauth RCE. Exploited per CISA.
  → patch AhsayCBS; block /rps/api/json/UpdateReceivers.do at perimeter. Due 2026-10-17.

- [CVE-2026-21589](https://nvd.nist.gov/vuln/detail/CVE-2026-21589) — Atlassian DC (Bitbucket/Confluence/Jira/Bamboo/Crowd) · KEV added 2026-10-15 · EPSS 0.028 · CVSS n/a
  Unauth read of web app root files across all DC editions. Exploited per CISA.
  → apply Atlassian patches immediately; audit access logs for file disclosure. Due 2026-10-18.

- [CVE-2026-76519](https://nvd.nist.gov/vuln/detail/CVE-2026-76519) — Cisco Secure Email Gateway · KEV added 2026-10-14 · EPSS 0.017 · CVSS n/a
  Unauth path traversal → arbitrary OS file write. Exploited per CISA.
  → upgrade Cisco SEG firmware per vendor advisory. Due 2026-10-17.

_(+2 KEV over cap: CVE-2026-0322 Palo Alto PAN-OS auth code injection → root RCE · EPSS 0.011; CVE-2026-105133 Ahsay auth bypass · EPSS 0.007 — same Oct 17 deadline)_
