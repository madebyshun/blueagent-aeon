*Security Digest — 2026-06-16*
Verdict: 2 actively exploited (CISA KEV), 1 public exploit (CVSS 9.8), 5 to schedule. _Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-11645](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Google Chromium V8 · KEV added 2026-06-09 · due 2026-06-23
  OOB memory r/w enabling sandbox escape via crafted HTML. Affects Chrome, Edge, Opera. Exploited per CISA.
  → update all browsers to latest stable build today.

- [CVE-2026-10520](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Ivanti Sentry · KEV added 2026-06-11 · OVERDUE (due 2026-06-14)
  OS command injection → unauthenticated remote root execution on unmanaged appliances. Exploited per CISA.
  → apply Ivanti Sentry patch immediately; isolate appliance from internet if patch unavailable.

- [CVE-2026-53633](https://github.com/advisories/GHSA-g8mr-85jm-7xhm) — @vitest/browser (npm) · CVSS 9.8 · EPSS 0.09% · public PoC
  Exposed CDP bridge in Vitest Browser Mode allows remote config overwrite → RCE. Triggered when api.host=0.0.0.0.
  → upgrade @vitest/browser to ≥3.2.5 / ≥4.1.8 / ≥5.0.0-beta.4 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-48519](https://github.com/advisories/GHSA-v5ff-9q35-q26f) — langflow (pip) · CVSS 9.6 · EPSS 0.09% · public PoC
  Unauthenticated RCE via shareable playground — attacker injects arbitrary Python via public flow payload.
  → upgrade langflow to ≥1.9.2.

- [CVE-2026-54257](https://github.com/advisories/GHSA-q6m5-f73j-m9mc) — electron (npm) · CVSS 9.3 · EPSS 0.02%
  Incorrect Buffer byte-length calculations → heap buffer overflow, crashes or attacker code execution.
  → upgrade electron to ≥42.3.3.

- [CVE-2026-48039](https://github.com/advisories/GHSA-9gw6-46qc-99vr) — meta-ads-mcp (pip) · CVSS 9.1 · EPSS 0.13%
  Unauthenticated MCP tool execution; Meta API access token leaked verbatim in error response body.
  → upgrade meta-ads-mcp to ≥1.0.109.

- [CVE-2026-48746](https://github.com/advisories/GHSA-94f4-hr76-p5j6) — vllm (pip) · CVSS 9.1 · EPSS 0.08%
  OpenAI API auth bypass via Host-header smuggling on ASGI. Instances behind nginx are not affected.
  → upgrade vllm to ≥0.22.0 or place behind nginx.

- [CVE-2026-48150](https://github.com/advisories/GHSA-6xp4-cf37-ppjh) — @budibase/server (npm) · CVSS 9.0 · EPSS 0.06%
  Workspace-scoped builder mass-assigns global admin via /api/public/v1/roles/assign. Enterprise tenants only.
  → upgrade budibase to ≥3.39.0.
