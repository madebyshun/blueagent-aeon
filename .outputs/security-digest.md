*Security Digest — 2026-08-24*
Verdict: 2 patch today (1 KEV/CISA + 1 CVSS 9.8+PoC), 0 to schedule, 1 to monitor. Sources: KEV, GH Advisory (extended weekly scan), EPSS

PATCH TODAY
- CVE-2025-62593 — ray (pip) · KEV added 2026-08-17 · EPSS 0.169 (96.8th pct) · CVSS 9.4
  RCE via DNS rebinding through Firefox/Safari; exploits unauthenticated /api/jobs endpoint. CISA due 2026-08-20 — past due. Public PoC (Singularity DNS rebind + User-Agent bypass).
  → upgrade ray to ≥2.52.0 and enable auth per Ray security docs.

- GHSA-cfcw-xp6x-25gj / CVE-2026-47698 — vm2 (npm) · CVSS 9.8 · EPSS 0.006 · public PoC
  Sandbox breakout via WebAssembly prototype manipulation bypasses prior fix; host-level RCE. Companion GHSA-m5w8-4gq2-6f8x (Aug 23) unpatched.
  → upgrade vm2 to ≥3.11.6 today; plan migration away from vm2 long-term.

MONITOR
- GHSA-m283-3h24-438v / CVE-2026-47686 — vm2 (npm) · CVSS critical · no fix · EPSS 0.004
  Missing Error.cause sanitization enables sandbox escape to RCE. Third vm2 critical advisory this cycle; no patch for this variant.
  → accelerate migration away from vm2; track for fix.

GH 48h advisory window empty for npm/pip/Go/Actions. vm2 items surfaced via extended weekly scan.
