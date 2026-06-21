*Security Digest — 2026-06-21*
Verdict: nothing urgent today. 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-54527 / GHSA-f962-v9hr-pfg5](https://github.com/advisories/GHSA-f962-v9hr-pfg5) — jupyterlab-git (pip/npm) · CVSS 8.6 · EPSS N/A · public PoC
  Stored XSS via unsanitized Git filenames in diff viewer → RCE (terminal access). Both server and browser extension affected.
  → upgrade jupyterlab-git / @jupyterlab/git to ≥0.54.0.

- [GHSA-x975-rgx4-5fh4](https://github.com/advisories/GHSA-x975-rgx4-5fh4) — appium-mcp (npm) · CVSS 8.2 · EPSS N/A
  XSS in MCP-UI resource createLocatorGeneratorUI via unescaped locator data.
  → upgrade appium-mcp to ≥1.85.10.

- [GHSA-c795-2g9c-j48m](https://github.com/advisories/GHSA-c795-2g9c-j48m) — everos (pip) · CVSS 8.2 · EPSS N/A
  Path traversal in /api/v1/memory/add via unvalidated sender_id field.
  → upgrade everos to ≥1.0.1.

- [CVE-2026-54074 / GHSA-4936-9hrh-qqpw](https://github.com/advisories/GHSA-4936-9hrh-qqpw) — @tinacms/cli (npm) · CVSS 7.8 · EPSS N/A
  RCE via unsanitized __TINA_INTERNAL__ marker in user-controlled YAML labels during Forestry migration.
  → upgrade @tinacms/cli to ≥2.4.3.

- [GHSA-c3xh-98xp-6qhf](https://github.com/advisories/GHSA-c3xh-98xp-6qhf) — gouef/githubtoplanguages (GitHub Actions) · CVSS 7.1 · EPSS N/A · public PoC
  Command injection via issue title in CI workflow. Any issue opener can exec on runner and access workflow secrets.
  → pin action to ≥1.1.4.

*MONITOR*
- [GHSA-f4xh-w4cj-qxq8](https://github.com/advisories/GHSA-f4xh-w4cj-qxq8) — langsmith (pip) · CVSS 7.7 · EPSS N/A · fix: ≥0.8.18
  Arbitrary server-side file read via TracingMiddleware. → upgrade langsmith to ≥0.8.18.

- [GHSA-6v7p-g79w-8964](https://github.com/advisories/GHSA-6v7p-g79w-8964) — msgpack (pip) · CVSS 7.5 · EPSS N/A · fix: ≥1.2.1
  OOB read/crash on Unpacker reuse after caught error. → upgrade msgpack to ≥1.2.1.

- [GHSA-6gqw-jqv7-v88m +2](https://github.com/advisories/GHSA-6gqw-jqv7-v88m) — stigmem-node (pip) · 3× cross-tenant BOLA · fix: ≥0.9.0a12
  Decay sweep, quarantine review, and RTBF tombstones all cross tenant boundaries. → upgrade stigmem-node to ≥0.9.0a12.
