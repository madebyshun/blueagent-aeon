The security digest is complete. Cleanup was blocked by sandbox permissions, but those are non-critical temp files. Here's the summary:

## Summary

**Security Digest 2026-07-17 — executed successfully.**

**Sources:** KEV ok (curl), GH Advisory ok (gh api), EPSS ok (WebFetch)

**PATCH TODAY (3 — all new KEV Jul 16):**
- CVE-2026-39808 — Fortinet FortiSandbox unauthenticated OS cmdinj · EPSS **0.84** (highest signal this cycle)
- CVE-2026-25089 — Fortinet FortiSandbox/Cloud/PaaS unauthenticated OS cmdinj · EPSS 0.36
- CVE-2026-58644 — Microsoft SharePoint deserialization RCE · EPSS 0.015

**PATCH THIS WEEK (2 — tracked Go ecosystem):**
- CVE-2026-53713 — Envoy Gateway auth bypass → secret disclosure · CVSS 9.1 · fix ≥1.7.4/1.8.1
- CVE-2026-52833 — Nuclio build-time RCE via Groovy injection · CVSS 8.0 · fix ≥1.16.5

**MONITOR (3):**
- mcp (pip) — 3 CVEs (WebSocket Origin bypass, HTTP session auth bypass, task IDOR) · CVSS 7.1–7.6 · fix ≥1.28.1 — notable for AI agent ecosystem
- Pomerium (Go) — pre-auth DoS via zstd · CVSS 7.5 · fix ≥0.32.8
- Envoy Gateway (Go) — xDS info disclosure · CVSS 7.4 · same fix as above

**Delivery:** Queued to `.pending-notify/1752796800.md` for post-run channel delivery. Log written to `memory/logs/2026-07-17.md`.
