Done. Here's the summary of what was executed:

## Summary

**Security Digest — 2026-08-12**

**Sources:** KEV=ok (curl), GH Advisory=ok (WebFetch), EPSS=ok (WebFetch)

**PATCH TODAY** (3 items — all CISA KEV additions from 2026-08-11, new this cycle):
- **CVE-2026-72898** — Metabase SQL Injection · EPSS 0.011 (1.1%) · Unauthenticated → full admin access, credential theft
- **CVE-2026-20349** — Cisco ASA/FTD Heap Inspection DoS · EPSS 0.010 (0.97%) · Unauthenticated remote device reload
- **CVE-2026-68820** — Microsoft Windows AFD/WinSock Use-After-Free · EPSS 0.004 (0.36%) · Local privilege escalation

**PATCH THIS WEEK** (1 item — tracked stack):
- **GHSA-87fv-vqqr-m4jr** / CVE-2026-73080 — SeaweedFS (Go) · CVSS 9.3 · EPSS 0.004 · Unauthenticated SSRF → IAM credential exposure on cloud deployments → upgrade to ≥4.24

**Deduped:** 2 older KEV entries (Progress LoadMaster CVE-2026-8037, JetBrains TeamCity CVE-2026-63077) and prior GHSA IDs from Aug 10–11 logs.

**Files created/modified:**
- `.pending-notify/security-digest-2026-08-12.md` — notification staged for post-run delivery
- `memory/logs/2026-08-12.md` — security-digest section appended
