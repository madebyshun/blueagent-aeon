*Security Digest — 2026-11-25*
Verdict: 3 actively exploited, 2 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-133469](https://github.com/advisories/GHSA-2r3w-c2vx-fv5g) — xo-server (npm) · KEV added 2026-11-25 · EPSS 0.011 · CVSS 9.8
  Empty-object login token bypasses auth on Xen Orchestra; unauthenticated admin access. In KEV and npm stack.
  → upgrade xo-server past 5.7.4 and patch Xen Orchestra host immediately.

- [CVE-2026-131914](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Idunno.AntiCsrf (.NET) · KEV added 2026-11-24 · EPSS 0.043
  Unsafe deserialization → unauthenticated RCE. Product may be EOL; CISA flagged active exploitation.
  → remove or replace Idunno.AntiCsrf; no patch available.

- [CVE-2024-10441](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Synology DSM · KEV added 2026-11-18 · EPSS 0.028
  Improper output escaping in system plugin daemon → remote RCE. Known ransomware exploitation on record.
  → apply Synology DSM security update now.

*PATCH THIS WEEK*
- [GHSA-mc8w-wjhw-45x5](https://github.com/advisories/GHSA-mc8w-wjhw-45x5) — ep_etherpad-lite (npm) · CVSS 9.8 · EPSS 0.041 · no public PoC
  Pre-auth arbitrary file read on etherpad-lite >= 1.8.14, < 3.3.3.
  → upgrade etherpad-lite to ≥ 3.3.3.

- [GHSA-x8q7-6c7m-52gw](https://github.com/advisories/GHSA-x8q7-6c7m-52gw) — nltk (pip) · CVSS 9.8 · EPSS 0.007 · no public PoC
  Incomplete sandbox fix — additional JVM/JAR bypass via unvalidated launcher tokens in java() args.
  → upgrade nltk to ≥ 3.10.4.

*MONITOR*
- [GHSA-p34x-fmph-9fjx](https://github.com/advisories/GHSA-p34x-fmph-9fjx) — flyto-core (pip) · CVSS 10 · EPSS 0.008 · no fix yet
  Arbitrary file write via unguarded data.*/file.* modules; incomplete fix of CVE-2026-67429.
  → track flyto-core; audit exposure; no patch yet.

- [GHSA-crj3-q72p-ggqm](https://github.com/advisories/GHSA-crj3-q72p-ggqm) — @waline/client (npm) · CVSS 9.3 · EPSS 0.004 · no fix yet
  Stored XSS via unsanitized comment edit previews.
  → track @waline/client; restrict comment editing; no patch yet.

- [GHSA-833v-v58w-294h](https://github.com/advisories/GHSA-833v-v58w-294h) — @doist/todoist-mcp (npm) · CVSS 9.3 · EPSS 0.002 · no fix yet
  DNS rebinding lets external sites write/delete Todoist data via local MCP server.
  → avoid exposing todoist-mcp beyond localhost; watch for fix.
