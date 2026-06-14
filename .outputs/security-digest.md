The `rm` command needs approval in this environment — the temp files will persist but aren't consequential. The skill is complete.

---

## Summary

**Security Digest — 2026-06-14 complete.**

**Sources:** KEV (curl, ok) · GitHub Advisory API (WebFetch, ok) · FIRST EPSS (WebFetch, ok)

**Dedup:** All 11 IDs from Jun 13 log were filtered out. CVE-2026-50751 (Check Point) was in the KEV feed dated Jun 8 but absent from the Jun 13 digest — included today.

**Tier counts: today=1 · week=2 · monitor=3**

**PATCH TODAY**
- **CVE-2026-50751** — Check Point Security Gateway · KEV Jun 8 · EPSS 0.137 (94.5th pct) · CVSS 9.3 · Auth bypass via deprecated IKEv1 VPN, exploited by Qilin ransomware (CISA confirmed) → apply sk185033 hotfix or disable IKEv1

**PATCH THIS WEEK**
- **GHSA-36hh-v3qg-5jq4** — `pyo3` (crates.io) · CVSS 8.7 · Out-of-bounds read in list/tuple iterators, network-accessible, no auth → upgrade to ≥0.29.0
- **GHSA-w5fm-68j4-fpc4 / CVE-2026-54092** — `filebrowser/v2` (Go) · CVSS 8.7 · Unauthenticated DoS via public login API → upgrade to ≥2.63.6

**MONITOR**
- 3× File Browser (Go) access control cluster (CVE-2026-54091, -54097, -54096) — CVSS 7.1–7.5 · v2 patched, v1 has no fix

**Outputs:**
- Notification queued to `.pending-notify/security-digest-20260614.md` (sandbox network blocked direct delivery)
- Log appended to `memory/logs/2026-06-14.md`
