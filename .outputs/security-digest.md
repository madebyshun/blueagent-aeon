## Summary

Security digest for 2026-08-04 completed. Key findings:

**PATCH TODAY (3):**
- **CVE-2026-18577** — N-able N-central auth bypass, KEV-confirmed exploitation (added 2026-08-03), EPSS 2.5%
- **GHSA-vmv7-4m6c-3cg5 / CVE-2026-69255** — Flowise CSV Agent pyodide RCE, CVSS 9.9, Metasploit root shell confirmed in published PoC → `flowise ≥3.1.3`
- **GHSA-3769-jgqc-cxm7 / CVE-2026-69254** — Flowise NodeVM sandbox escape, CVSS 9.4 v4, root shell PoC → `flowise ≥3.1.3`

**PATCH THIS WEEK (5):** 3 more Flowise critical/high RCEs (GHSA-x3hf-7cj6-3r4m, GHSA-x6vm-w76m-8j7g, GHSA-r745-8hwv-h473 all via `flowise ≥3.1.3`), unauthenticated session hijack (GHSA-6vh2-wg4h-4vwj), and python-cryptography DoS via exponential cert path-build (`cryptography ≥49.0.0`).

**MONITOR (3):** cryptography Bleichenbacher oracle (fix in 50.0.0), Flowise SSRF IPv4-mapped bypass, Flowise missing file auth — all fixed in flowise ≥3.1.3.

The story today is Flowise: a mass advisory dump of 6 CVEs across two advisory batches, all patched in 3.1.3 released today. Notification staged to `.pending-notify/security-digest-2026-08-04.md` (sandbox fallback); logged to `memory/logs/2026-08-04.md`.
