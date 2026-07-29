Security digest for 2026-07-29 is complete. Here's the summary:

## Summary

**Sources:** KEV (WebFetch ✓), GitHub Advisory API (gh api ✓), EPSS (WebFetch ✓)

**PATCH TODAY (3)** — all KEV-confirmed exploitation in the wild:
- **CVE-2026-16232** — Check Point SmartConsole · EPSS 0.70 (strongest signal) · unauthenticated admin token theft
- **CVE-2025-68686** — Fortinet FortiOS · EPSS 0.013 · symlink persistence bypass post-patch
- **CVE-2026-16812** — Arista VeloCloud Orchestrator · EPSS 0.009 · OS command injection

**PATCH THIS WEEK (5):**
- @hypequery/clickhouse (npm) · CVSS 9.8 · SQL injection → fix ≥2.0.2
- goshs (go) · CVSS 9.1 · WebDAV + SFTP double auth bypass → fix ≥v2.1.4
- style-dictionary (npm) · CVSS 8.8 · prototype pollution → fix ≥5.4.4
- datamodel-code-generator (pip) · CVSS 8.8 · 9-advisory batch (code injection/SSRF/file-read) → fix ≥0.64.0
- swagger-typescript-api (npm) · CVSS 8.3 · 4-vector code injection → fix ≥13.12.2

**MONITOR (1):** QTINeon (pip+npm) · CVSS 8.6 · unauthenticated relay amplification · no fix yet

Notification queued to `.pending-notify/` for post-run delivery. Log entry appended to `memory/logs/2026-07-29.md`.
