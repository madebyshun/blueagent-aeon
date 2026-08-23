Done. Here's the summary of what was produced:

## Summary

**Security Digest — 2026-08-23**

**Sources:** KEV=ok (WebFetch), GH Advisory=ok (WebFetch), EPSS=partial (14/17 CVEs indexed; 2026 CVEs largely absent from FIRST database, treated as 0).

**Deduped from last 2 days of logs:** CVE-2026-72529 (TrueConf missing auth, in Aug 22+23 morning-brief), CVE-2026-73570 (Zimbra ZCS, in Aug 22 security-digest), jsonata cluster, xinference, atlantis, defuddle, hydra-core, and others from Aug 22 security-digest.

**PATCH TODAY (2)**
- **CVE-2026-72530** — TrueConf Server — KEV added 2026-08-20 — Code injection via unauthenticated port 4307/TCP → host RCE. Due 2026-09-03. EPSS 0.010.
- **CVE-2026-64849** — MLflow (pip) — KEV added 2026-08-19 — Unauthenticated SSRF via unvalidated HTTP redirects. Due 2026-09-02. EPSS 0.082 (94th pct), CVSS 9.3. → upgrade to ≥3.15.0.

**PATCH THIS WEEK (5)**
- surfio (pip) CVSS 9.8 — OOB read → ≥0.0.19
- resdata (pip) CVSS 9.8 — buffer overflow → ≥6.2.9
- @whyour/qinglong (npm) CVSS 9.3 — incomplete auth fix → ≥2.20.1
- dgraph/v25 (go) CVSS 9.1 — unauth snapshot import → ≥25.3.5
- kin-openapi (go) CVSS 8.7 — resource exhaustion DoS → ≥0.142.0 (covers companion GHSA-mmfr too)

**MONITOR (3)**
- vm2 (npm) CVSS 9.3 — no fix available; migrate to isolated-vm
- @keystone-6/core (npm) CVSS 7.5 — graphql over-fetch → ≥6.5.3
- unleash-server (npm) CVSS 7.5 — unauth DoS → ≥7.5.2/7.6.5/8.0.2

**Files written/modified:**
- `.pending-notify/security-digest-2026-08-23.md` — notification staged for delivery
- `memory/logs/2026-08-23.md` — log entry appended
