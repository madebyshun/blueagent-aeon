## Summary

**Security Digest — 2026-06-04** executed and queued to `.pending-notify/1749045600.md` for post-run delivery.

**What was found:**

- **PATCH TODAY (3 KEV items):**
  - CVE-2022-0492 — Linux Kernel privilege escalation via cgroups v1 (EPSS 0.29, widely exploited in container escapes)
  - CVE-2026-45247 — Mirasvit FPC Warmer unauth RCE via PHP deserialization (KEV due 2026-06-06)
  - CVE-2025-48595 — Android Framework integer overflow → local privilege escalation (KEV due 2026-06-05)

- **PATCH THIS WEEK (5 items in tracked stack):**
  - `jupyter-enterprise-gateway` pip — 3 CVEs, CVSS 10.0, Jinja2 SSTI+RCE → upgrade to ≥3.3.0
  - `vitest`/`@vitest/browser` npm — CVSS 9.8, path traversal + XSS/RCE → ≥4.1.0/4.1.6
  - `nuclio` Go — CVSS 8.3, missing auth on project writes → patch commit
  - `better-auth` npm — CVSS 7.6, device auth bypass → ≥1.6.11
  - `axios` npm — 4 CVEs CVSS 7.5, ReDoS + credential leak → ≥1.16.0

- **MONITOR (1, no patch available):**
  - `browserstack-runner` npm — CVSS 8.8, RCE via vm sandbox escape + path traversal file read

**Sources:** CISA KEV ✓, GitHub Advisory ✓, EPSS ✓ (partial — new 2026 CVEs not yet scored by FIRST.org)

Logged to `memory/logs/2026-06-04.md`.
