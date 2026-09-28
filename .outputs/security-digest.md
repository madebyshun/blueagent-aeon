*Security Digest — 2026-09-28*
Verdict: 3 confirmed in-the-wild (KEV), 5 KEV overflow past BOD deadline, 1 npm to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-88772 — Citrix NetScaler ADC/Gateway · KEV added 2026-09-27 · due 2026-09-30 · EPSS n/a
  Memory buffer overflow → RCE or DoS. Unauthenticated. Actively exploited per CISA.
  → apply Citrix security update per CTX advisory before 2026-09-30.

- CVE-2026-88771 — Citrix NetScaler ADC/Gateway · KEV added 2026-09-27 · due 2026-09-30 · EPSS n/a
  Improper input validation → unauthenticated arbitrary command execution.
  → apply Citrix patch; both CVEs resolved in same maintenance window.

- CVE-2026-71362 — Adobe Commerce / Magento · KEV added 2026-09-24 · EPSS 0.896 · BOD deadline 2026-09-27 PAST DUE
  Incorrect authz → elevated access, no user interaction. Highest exploitation signal this week.
  → upgrade Adobe Commerce to latest patched build immediately.

*PATCH THIS WEEK*
- CVE-2026-5430 — WSO2 (API CP/Manager/Gateway) · KEV · due 2026-09-27 (PAST DUE)
  Path traversal → unrestricted file upload → RCE. → apply WSO2 Security Advisory.

- CVE-2026-94127 — F5 BIG-IP APM · KEV · due 2026-09-25 (PAST DUE)
  Heap overflow w/ OAuth config → unauthenticated RCE. → apply F5 fix; disable OAuth vserver as workaround.

- CVE-2026-93616 — Check Point Security Mgmt · KEV · due 2026-09-25 (PAST DUE)
  Path traversal → unauthenticated script upload + exec. → apply Check Point hotfix.

- CVE-2026-85102 — Check Point Security Gateway (VPN) · KEV · due 2026-09-25 (PAST DUE)
  Improper cert validation → unauthenticated RCE on gateway. → apply fix; restrict VPN exposure.

- CVE-2026-93952 — Arista VeloCloud Orchestrator (on-prem) · KEV · due 2026-09-25 (PAST DUE)
  Improper input validation → privileged internal access. → apply Arista VCO patch.

*MONITOR*
- GHSA-456v-xq2p-r4cj — code-ollama (npm) · CVSS 7.8 · no fix yet
  Command injection in grep_search via unescaped shell substitution. Affects AI agent toolchains.
  → pin or sanitize inputs; watch for patched release.
