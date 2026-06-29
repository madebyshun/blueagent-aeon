## Summary

**Security Digest — 2026-06-29**

All three tiers empty. No notification sent.

**What I checked:**
- **CISA KEV (7-day window):** 4 entries, all added Jun 23–25 and covered in prior digests. No new KEV additions since Jun 25. CVE-2026-20230 (Cisco UCM SSRF) remains the highest EPSS in the window at 0.417 / 98.5th percentile, but is deduped (in Jun 27+28 logs).
- **GitHub Advisories (critical + high, last 48h):** Most recent critical published Jun 26 23:03 UTC (nezha, covered Jun 27). Most recent high published Jun 27 00:13 UTC (pnpm cluster, covered Jun 27/28). Nothing new.
- **EPSS:** Checked 7 CVEs. All low (<0.012) except the already-covered CVE-2026-20230.
- **New candidate screened out:** GHSA-jv46-xfwm-36j7 (CVE-2026-49454, CVSS 9.1) — SAML auth bypass in Erlang `relyra` package. Not in tracked stack (npm/pip/Go/crates.io/GitHub Actions), EPSS 0.001, no public PoC.

**Sources:** kev=ok, gh=ok, epss=ok → `SECURITY_DIGEST_OK`
