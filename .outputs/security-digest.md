*Security Digest — 2026-06-13*
Verdict: 3 actively exploited, 5 to schedule, 3 to monitor. _Sources: CISA KEV · GH Advisory · EPSS_

*PATCH TODAY*
- CVE-2026-42271 — BerriAI LiteLLM (pip) · KEV 2026-06-08 · EPSS 0.61 · due 2026-06-22
  Command injection: low-priv API keys execute arbitrary host commands. Confirmed exploited per CISA.
  → upgrade litellm today; verify no staging exposure.

- CVE-2026-10520 — Ivanti Sentry · KEV 2026-06-11 · due TOMORROW 2026-06-14
  Unauthenticated OS command injection → root RCE on unmanaged appliances.
  → apply Ivanti Sentry patch before Jun 14 BOD deadline.

- CVE-2026-35273 — Oracle PeopleSoft PeopleTools · KEV 2026-06-12 · due 2026-06-15
  Missing auth → unauthenticated full system takeover.
  → apply Oracle patch by 2026-06-15 or disconnect from internet.

_Also in KEV this week: Chromium V8 RCE (CVE-2026-11645 · due Jun 23), Arista EOS (CVE-2026-7473), Cisco SD-WAN (CVE-2026-20245). Update browsers and network gear._

*PATCH THIS WEEK*
- [GHSA-9gw6-46qc-99vr](https://github.com/advisories/GHSA-9gw6-46qc-99vr) — meta-ads-mcp (pip) · CVSS 9.1 · no fix yet
  Unauthenticated HTTP call leaks operator's Meta access token.
  → restrict MCP server to authenticated callers; watch for patch.

- [GHSA-6xp4-cf37-ppjh](https://github.com/advisories/GHSA-6xp4-cf37-ppjh) — @budibase/server (npm) · CVSS 9.0 · no fix yet
  Workspace builder → global admin privilege escalation via roles API.
  → restrict builder access; upgrade when patch lands.

- [GHSA-gv7w-rqvm-qjhr](https://github.com/advisories/GHSA-gv7w-rqvm-qjhr) — esbuild (npm) · CVSS 8.1 · no fix yet
  Deno module skips binary integrity check → RCE via poisoned NPM_CONFIG_REGISTRY.
  → pin esbuild binary checksums; audit CI registry config.

- [GHSA-3gp5-q4jw-3v94](https://github.com/advisories/GHSA-3gp5-q4jw-3v94) — @budibase/server (npm) · CVSS 8.1 · no fix yet
  App users rewrite datasource URL to exfiltrate stored REST credentials.
  → restrict datasource config access; upgrade when patched.

- [GHSA-r236-5pc3-3qcp](https://github.com/advisories/GHSA-r236-5pc3-3qcp) — aws-advanced-go-wrapper (go) · CVSS 8.0
  Privilege escalation in Aurora PostgreSQL via wrapper SDK.
  → schedule upgrade; review IAM roles used by wrapper.

*MONITOR*
- [GHSA-8c9q-7855-wfxq](https://github.com/advisories/GHSA-8c9q-7855-wfxq) — filebrowser/v2 (go) · high · no fix
  Shell metacharacter injection bypasses command allowlist → arbitrary execution.
  → disable shell execution; track for patch.

- [GHSA-24fp-5v3p-rvpw](https://github.com/advisories/GHSA-24fp-5v3p-rvpw) — chisel (go) · high · no fix
  ACL bypass via SSH ExtraData injection post-handshake.
  → restrict chisel to trusted networks; track for patch.

- [GHSA-fp5j-4fj2-4jvq](https://github.com/advisories/GHSA-fp5j-4fj2-4jvq) — radius-project/radius (go) · CVSS 7.7 · no fix
  Annotation injection can delete container resources in multi-tenant installs.
  → avoid untrusted annotation input; watch GHSA-fp5j.
