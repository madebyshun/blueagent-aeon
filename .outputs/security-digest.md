The temp files can stay — they're harmless dotfiles. The skill is complete. Here's the summary:

## Summary

**Security Digest — 2026-09-05** executed successfully.

**Verdict:** Nothing urgent today (no new KEV entries, no EPSS ≥ 0.5). 5 to schedule, 3 to monitor.

**PATCH THIS WEEK (5):**
1. **codewhale-tui** (npm/crates.io) — 9-advisory cluster; CVSS 9.3 lead (git_show arg injection → arbitrary file write). No fix.
2. **openchoreo cluster-gateway** (Go) — CVSS 9.0 new critical; unauthenticated internal proxy reads all K8s Secrets + mutates workloads. No fix.
3. **semaphore UI** (Go) — CVSS 8.8; manager→owner privilege escalation via slug collision. No fix.
4. **SiYuan** (Go) — 15 new HIGH advisories (Sep 3–4), CVSS 8.7 peak; XSS, cookie key disclosure, WebSocket broadcast bypass, SSTI→SQL. Adds to the 3 CRITICAL advisories logged Sep 4. No fix.
5. **@toon-format/toon** (npm) — CVSS 8.3; prototype pollution via `__proto__`. No fix.

**MONITOR (3):**
- **toml** (npm) — CVSS 8.2/7.5; prototype pollution + recursion. No fix.
- **@typespec/spector** (npm) — CVSS 7.5; unauthenticated shutdown endpoint. No fix.
- **ffuf** (Go) — CVSS 7.5; decompression bomb OOM. No fix.

**Sources:** CISA KEV (ok), GitHub Advisory API (ok), FIRST EPSS (ok, 12 CVEs enriched). Notification queued to `.pending-notify/` for post-run delivery. Log appended to `memory/logs/2026-09-05.md`.
