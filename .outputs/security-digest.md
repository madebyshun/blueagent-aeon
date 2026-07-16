*Security Digest — 2026-07-16*
Verdict: 2 actively exploited (KEV), 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-46817 — Oracle E-Business Suite · KEV added 2026-07-15 · EPSS 0.01 · CVSS n/a
  Unauthenticated HTTP attacker can fully compromise Oracle Payments — complete takeover. BOD 26-04 due 2026-07-18 (tomorrow).
  → apply vendor mitigation or discontinue use today.

- CVE-2023-4346 — KNX Association KNX Protocol · KEV added 2026-07-15 · EPSS 0.01 · CVSS n/a
  Lockout abuse lets unauthenticated attacker purge and brick BCU devices with no auth required.
  → enable Connection Authorization Option 2 or apply vendor mitigations.

*PATCH THIS WEEK*
- [GHSA-r3hx-x5rh-p9vv](https://github.com/advisories/GHSA-r3hx-x5rh-p9vv) — django-haystack (pip) · severity: high · CVSS n/a · EPSS n/a
  RCE via eval() in Elasticsearch result deserialization — untrusted index content executes on your server.
  → upgrade django-haystack to ≥3.4.0.

- [CVE-2026-54466](https://github.com/advisories/GHSA-xv26-6w52-cph6) — websocket-driver (npm) · severity: critical · CVSS n/a · EPSS n/a
  Message corruption via unbounded protocol length header — client can corrupt server payload state and cause incorrect parsing.
  → upgrade websocket-driver to ≥0.7.5.

- [GHSA-62gx-5q78-wrvx](https://github.com/advisories/GHSA-62gx-5q78-wrvx) — obsidian-local-rest-api (npm) · CVSS 8.8 · EPSS n/a
  Authenticated path traversal via URL-encoded %2F → arbitrary file read, write, and delete on the host.
  → upgrade obsidian-local-rest-api to ≥4.1.3.

*MONITOR*
- [CVE-2026-54449](https://github.com/advisories/GHSA-3pvh-63gf-j9mw) — langbot (pip) · CVSS 8.8 · no patch yet
  Authenticated RCE via malicious MCP server configuration. → track GHSA-3pvh-63gf-j9mw; no patch available.

- [CVE-2026-50289](https://github.com/advisories/GHSA-5xpp-75jx-m839) — systeminformation (npm) · severity: high · no patch yet
  OS command injection in networkInterfaces() via interfaces(5) source-directive on Linux. → avoid untrusted interface name input until patch ships.

- [CVE-2026-54504](https://github.com/advisories/GHSA-6f5r-5672-72j7) — @andrea9293/mcp-documentation-server (npm) · CVSS 8.8 · no patch yet
  Web UI/API binds all interfaces (0.0.0.0:3080) without auth — unauth doc read/write/delete from LAN. → firewall port 3080 or set START_WEB_UI=false.
