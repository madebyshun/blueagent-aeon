*Security Digest — 2026-08-20*
Verdict: 1 actively exploited, 1 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-64849](https://nvd.nist.gov/vuln/detail/CVE-2026-64849) — mlflow (pip) · KEV added 2026-08-19 · EPSS 0.011 · CVSS TBD
  SSRF via unauthenticated webhook endpoint reaches internal services and cloud metadata (IMDS). Actively exploited per CISA. Due 2026-09-02.
  → upgrade mlflow to ≥3.15.0 and redeploy.

*PATCH THIS WEEK*
- [GHSA-c7hr-448w-65px](https://github.com/advisories/GHSA-c7hr-448w-65px) — meshcentral (npm) · CVSS 8.3 · EPSS N/A · public PoC
  Stored XSS via unsanitized agent osdesc field; executes on admin panel load, no user interaction required.
  → schedule upgrade: meshcentral → ≥1.1.60.

*MONITOR*
- [GHSA-2xhg-73j7-rrgx](https://github.com/advisories/GHSA-2xhg-73j7-rrgx) / CVE-2026-53957 — @contentful/mcp-server (npm) · CVSS 7.7 · EPSS ~0 · PoC confirmed
  Prompt-injection SSRF: LLM-controlled host/proxy args in export_space/import_space exfiltrate Contentful PAT to attacker endpoint.
  → upgrade @contentful/mcp-server ≥1.7.19 and @contentful/mcp-tools ≥0.4.5 if in use.
- [GHSA-rr55-jp92-8wp2](https://github.com/advisories/GHSA-rr55-jp92-8wp2) + siblings — faf-mcp cluster (npm: claude-faf-mcp, faf-mcp, grok-faf-mcp) · CVSS 7.5 · no fix
  Arbitrary local file R/W via unconfined path arg in fs_* MCP tools. All three packages affected.
  → remove from MCP server if installed; no patch yet.
- [GHSA-9gmc-jqmh-3rvm](https://github.com/advisories/GHSA-9gmc-jqmh-3rvm) / CVE-2026-53951 — copier (pip) · EPSS 0.002 · no fix
  Trust-prefix bypass via path traversal runs tasks unprompted without user confirmation.
  → track GHSA-9gmc-jqmh-3rvm; watch for patched release, avoid untrusted template sources.
