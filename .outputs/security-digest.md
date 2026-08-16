*Security Digest — 2026-08-16*
Verdict: nothing urgent today. 0 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*MONITOR*
- [GHSA-5fpj-28rv-84r7](https://github.com/advisories/GHSA-5fpj-28rv-84r7) — @budibase/server (npm) · CVSSv4 7.1 · EPSS 0.003 (est.) · fix available
  Automation steps (outgoing webhook, Zapier, n8n, Slack, Discord) make unvalidated HTTP requests, bypassing the IP blacklist. Cloud metadata endpoints (169.254.169.254) reachable by any automation user; default deployments have no SSRF protection.
  → upgrade @budibase/server to ≥3.41.3 and add BLACKLIST_IPS env var.
