Done. Here's the summary:

## Summary

**Security Digest — 2026-08-13** executed successfully.

**PATCH TODAY (1)**
- **CVE-2026-8037** — Progress Kemp LoadMaster, pre-auth command injection → root RCE. KEV added 2026-08-07, EPSS 0.993, CVSS 9.6. 792 exploit attempts confirmed in the wild; FCEB due date (Aug 10) already past. Fix: LoadMaster ≥7.2.63.2 (GA) or ≥7.2.54.18 (LTSF).

**PATCH THIS WEEK (1)**
- **GHSA-49m4-vp58-wgc9 / CVE-2026-55071** — stata-mcp (pip), command injection via newline in MCP tool param. CVSS 8.4, public PoC with Docker repro. Fix: `pip install stata-mcp>=1.19.0`.

**MONITOR (3)**
- GHSA-48p8-g2fx-3wwm — Argo Workflows (Go), allow-list bypass (incomplete fix for CVE-2026-31892), no patch yet.
- GHSA-cxgv-hp74-jj7r — ansible-jailexec (pip), symlink jail escape → arbitrary host file write as root, no patch yet.
- GHSA-rm43-82j9-r4mj — atomic-agents-stack (pip), dashboard path traversal → arbitrary file read, no patch yet.

**Sources**: KEV=ok (WebFetch), GH Advisory=ok (gh api), EPSS=ok (WebFetch). Notification staged to `.pending-notify/security-digest-2026-08-13.md`. Log appended to `memory/logs/2026-08-13.md`. All Aug 12 IDs (CVE-2026-72898, CVE-2026-20349, CVE-2026-68820, GHSA-87fv-vqqr-m4jr) correctly deduplicated.
