Done.

## Summary

**What I did:**
- Read `memory/MEMORY.md` and last 2 days of logs to extract 9 CVE/GHSA IDs to exclude (all reported Aug 12–13)
- Fetched CISA KEV via WebFetch — confirmed 4 KEV entries this week, all previously reported; no new additions since Aug 13
- Fetched GitHub critical + high advisories via `gh api` (last 48h); filtered to tracked stack (npm, pip, Go, crates.io, GitHub Actions)
- Enriched new candidates with EPSS via WebFetch; fetched advisory detail pages for top candidates

**Tier results:**
- **PATCH TODAY (0):** No new KEV, no EPSS ≥ 0.5, no (CVSS ≥ 9.8 + PoC)
- **PATCH THIS WEEK (1):** CVE-2026-73654 — `@trigger.dev/core` (npm) CVSS 8.5, fix at 4.5.6, public PoC (single-request Object.prototype corruption, cross-tenant DoS)
- **MONITOR (3):** CVE-2026-12243 `nltk` (pip, fix ≥3.10.0, PoC exists, EPSS 0.006) · CVE-2026-54917 `seaweedfs` (Go, no fix) · CVE-2026-46369 `nimiq-blockchain` (crates.io, no fix)

**Files created/modified:**
- `.pending-notify/security-digest-2026-08-14.md` — staged notification for postprocessing
- `memory/logs/2026-08-14.md` — appended `### security-digest` log entry
