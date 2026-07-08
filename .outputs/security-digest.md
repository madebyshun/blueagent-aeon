The temp files couldn't be removed (sandbox policy), but they're harmless `.tmp_` prefix files. The digest is complete.

---

## Summary

**Security Digest — 2026-07-08** executed and queued to `.pending-notify/1751980000.md`.

**PATCH TODAY (3 — all KEV, confirmed exploitation):**
- CVE-2026-55255 — Langflow (pip) — auth bypass → executes other users' flows
- CVE-2026-48282 — Adobe ColdFusion — path traversal → RCE
- CVE-2026-48908 — JoomShaper SP Page Builder — unauth PHP file upload → exec

**PATCH THIS WEEK (5):**
- CVE-2026-53552 (goploy/go) — CVSS 9.6, IDOR+RCE with public PoC, no patch yet
- CVE-2026-53513 (@better-auth/sso/npm) — CVSS 9.6, SSRF → account takeover; fix: upgrade to ≥1.6.11
- CVE-2026-53512 (better-auth/npm) — CVSS 9.1, OAuth token replay; fix: ≥1.6.11
- GHSA-9h47-pqcx-hjr4 (better-auth/npm) — CVSS 8.7, alg=none default; fix: ≥1.6.11
- CVE-2026-53516 (better-auth/npm) — CVSS 8.3, OAuth account takeover; fix: ≥1.6.11 (+4 more in same release)

**MONITOR (3):**
- CVE-2025-46719 (open-webui/pip) — stored XSS → full RCE via functions, no patch
- CVE-2026-54760 (langroid/pip) — SQLChatAgent blocklist bypass, no patch
- CVE-2026-53553 (goploy/go) — CVSS 7.7, path traversal companion to the RCE above, no patch

**Files modified:** `memory/logs/2026-07-08.md`, `.pending-notify/1751980000.md`
