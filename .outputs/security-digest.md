## Summary

**security-digest — 2026-10-14**

All three tiers empty. No notification sent (`SECURITY_DIGEST_OK`).

**What ran:**
- **CISA KEV**: 7 entries added this week — all already covered in the 2026-10-12 and 2026-10-13 logs (Ivanti ICS, Windows Shell, BIND, Apache Struts, Strapi, ONLYOFFICE, ProFTPD). No new KEV additions today.
- **GitHub Advisories (last 48h)**: Microsoft Patch Tuesday dominated — 23 new advisories published Oct 13. All are `nuget` (ASP.NET Core / .NET runtimes), outside the tracked stack (npm/pip/Go/crates.io/GitHub Actions). Most notable: CVE-2026-105016 (Microsoft QUIC RCE, CVSS 9.8) — but EPSS = 1.0%, no exploitation signal, and nuget is not tracked.
- **EPSS**: Fetched for 3 new critical CVEs; all scored 0.8–1.0% (negligible exploitation probability).

**Sources**: kev=ok, gh=ok, epss=ok  
**Logged** to `memory/logs/2026-10-14.md`  
**./notify**: skipped per spec (all tiers empty, sources healthy)
