*Security Digest — 2026-09-23*
Verdict: 3 actively exploited (KEV), 5 in stack to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-93616](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Check Point Multiple Products · KEV added 2026-09-22 · EPSS 0.024
  Path traversal → unauth upload + arbitrary script execution. Exploited per CISA.
  → apply Check Point hotfix immediately; restrict management interface access.

- [CVE-2026-94127](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — F5 BIG-IP APM · KEV added 2026-09-22 · EPSS 0.014
  Heap buffer overflow → unauth RCE when OAuth profile is configured. Exploited per CISA.
  → patch BIG-IP APM immediately; disable OAuth profile if patch unavailable.

- [CVE-2026-85102](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Check Point Multiple Products (VPN) · KEV added 2026-09-22 · EPSS 0.007
  Improper cert validation in VPN → unauth remote code execution. Exploited per CISA.
  → apply Check Point VPN hotfix immediately.

*PATCH THIS WEEK*
- [CVE-2026-77244](https://github.com/advisories/GHSA-wrhw-j3f9-8vc6) — mcp-atlassian (pip) · CVSS 10.0 · EPSS 0.005 · no patch yet
  HTTP transport accepts any opaque token — full auth bypass. 15+ CVEs filed against mcp-atlassian this week.
  → disable HTTP transport mode; restrict access until patch; monitor github.com/sooperset/mcp-atlassian.

- [CVE-2026-57149](https://github.com/advisories/GHSA-rr49-f9g6-c9r5) — plone.app.portlets (pip) · CVSS 9.9 · EPSS 0.006 · no patch yet
  TALES expression injection via portlets → arbitrary code execution. All versions affected.
  → restrict editor portlet access to trusted users now; monitor Plone security releases.

- [CVE-2026-77243](https://github.com/advisories/GHSA-3r68-hf9h-887v) — mcp-atlassian (pip) · CVSS 8.8 · EPSS 0.005 · no patch yet
  ENABLED_TOOLS toolset auth bypass — restricted tool set can be circumvented.
  → same remediation as CVE-2026-77244; part of mcp-atlassian cluster.

- [CVE-2026-62371](https://github.com/advisories/GHSA-5jpj-293f-rhvj) — KubeEdge (go) · CVSS 8.8 · EPSS 0.005 · no patch yet
  NodeUpgradeJob cmd injection via v1alpha2 API → RCE on edge nodes.
  → restrict cloud-side NodeUpgradeJob API; require network policy on edge node access.

- [CVE-2026-62182](https://github.com/advisories/GHSA-m3c6-2p7h-cfr3) — KubeEdge (go) · CVSS 8.8 · EPSS 0.005 · no patch yet
  ConfigUpdateJob updateFields shell injection → code execution on edge nodes.
  → restrict cloud-side ConfigUpdateJob API; monitor KubeEdge releases for patch.

*MONITOR*
- [CVE-2026-76819](https://github.com/advisories/GHSA-vxg7-f2jj-jmqm) — nuclei/v3 (go) · CVSS 8.6 · no fix yet
  Goja JS engine ACE via crafted Nuclei template. → run only trusted templates; watch for patched release.

- [CVE-2026-77262](https://github.com/advisories/GHSA-p6hp-93wp-fh6p) — mcp-atlassian (pip) · CVSS 8.6 · no fix yet
  confluence_upload_attachment path traversal → arbitrary server file read. → part of mcp-atlassian cluster above.

- [CVE-2026-77426](https://github.com/advisories/GHSA-72h8-wp98-7hch) — unleash-server (npm) · CVSS n/a · no fix yet
  Missing await on perm check + cross-project IDOR in admin API. → restrict Unleash admin API exposure.
