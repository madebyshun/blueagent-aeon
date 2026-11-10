*Security Digest — 2026-11-10*
Verdict: 3 actively exploited (KEV, patch by 2026-11-13), 2 npm supply-chain patches + 3 more to schedule, 3 to monitor.
_Sources: CISA KEV (+13 this week), GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-123158 — OpenSSH (Linux) · KEV 2026-11-09 · EPSS 0.165 · CVSS n/a
  Auth bypass via mishandled return values. → upgrade OpenSSH immediately; due 2026-11-12.

- CVE-2026-116779 — FreeSwitch (SignalWire) · KEV 2026-11-09 · EPSS 0.022 · CVSS n/a
  Code injection exposes creds + enables call control and RCE. → patch FreeSwitch; due 2026-11-12.

- CVE-2026-116606 — Barracuda ESG · KEV 2026-11-10 · EPSS 0.016 · CVSS n/a
  Unauth backup restore rewrites appliance config (auth bypass). → apply Barracuda fix; due 2026-11-13.

*PATCH THIS WEEK*
- GHSA-pcrw-h46h-c93h (CVE-2026-125120) — mongoose (npm) · CVSS critical · EPSS 0.006
  sanitizeFilter silently skipped on countDocuments — query selector injection. → upgrade mongoose to ≥9.9.2 / ≥8.24.3 / ≥7.8.12 / ≥6.13.11.

- GHSA-gg4r-jv3p-qx3c (CVE-2026-125119) — mongoose (npm) · CVSS high · EPSS 0.005 · public PoC
  Connection-level sanitizeFilter never applies — password {$ne:null} bypasses auth. Same fix versions. → upgrade mongoose (same targets as above).

- CVE-2026-111560 — Barracuda (multiple) · KEV 2026-11-10 · EPSS 0.011 · CVSS n/a
  Admin can inject root OS commands via crafted timezone value. → apply vendor patch; due 2026-11-13.

- CVE-2026-102895 — GPUStack · KEV 2026-11-09 · EPSS 0.006 · CVSS n/a
  Unauthenticated users gain admin access + code exec via inference endpoint. → patch GPUStack; due 2026-11-12.

- CVE-2026-119977 — WordPress Core · KEV 2026-11-03 · EPSS 0.012 · CVSS n/a
  TOCTOU race during core upgrade lets unauth attackers execute code. → update WordPress core now (due date 2026-11-06 already passed).

*MONITOR*
- CVE-2026-124194 — Microsoft Office/Outlook · KEV 2026-11-10 · EPSS n/a · CVSS n/a
  Spoofing via missing user-interaction checks for risky actions. → watch for patch; due 2026-11-24.

- CVE-2026-125350 — Google Chromium · KEV 2026-11-10 · EPSS n/a · CVSS n/a
  Use-after-free in XML component, sandbox RCE. → update Chromium/Chrome; due 2026-11-24.

- CVE-2026-123218 — IBM Aspera Faspex · KEV 2026-11-09 · EPSS 0.007 · CVSS n/a
  Authenticated users escalate privileges via crafted messages. → apply IBM patch; due 2026-11-12.
