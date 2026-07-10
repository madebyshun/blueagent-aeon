*Security Digest — 2026-07-10*
Verdict: 2 actively exploited/critical-with-PoC, 4 to patch this week, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-55255](https://github.com/advisories/GHSA-qrpv-q767-xqq2) — langflow (pip) · KEV added 2026-07-07 · EPSS 0.005 · CVSS —
  IDOR in /api/v1/responses: auth'd attacker executes any user's flow by supplying victim flow ID. Public PoC. KEV due: today.
  → upgrade langflow to ≥ 1.9.1 now.

- [CVE-2026-52831](https://github.com/advisories/GHSA-v5px-423j-pf7p) — nuclio (Go) · CVSS 10.0 · EPSS — · public PoC
  Cron trigger headers/body unsanitized → shell injection → persistent root RCE in CronJob pods. Backdoors survive function deletion.
  → upgrade nuclio to ≥ 1.16.4 today.

*PATCH THIS WEEK*
- [CVE-2026-53649](https://github.com/advisories/GHSA-xqhv-chqm-fhcc) — joro (Go) · CVSS 9.6 · EPSS —
  Default localhost API + CORS wildcard: any page the operator visits can upload a malicious plugin and trigger RCE on restart.
  → upgrade joro past commit 5c0ca35db828.

- [CVE-2026-50197](https://github.com/advisories/GHSA-659f-rgp5-w4wf) — skipper (Go) · CVSS 8.7 · EPSS — · public PoC
  opaAuthorizeRequestWithBody bypassed on chunked/HTTP2 requests: OPA evaluates empty body, full payload passes upstream.
  → upgrade skipper to ≥ 0.26.10.

- [CVE-2026-49471](https://github.com/advisories/GHSA-37h2-6p4f-mp3q) — serena-agent (pip) · CVSS 8.3 · EPSS 0.002
  Unauthenticated Flask dashboard on fixed port exposed to DNS rebinding → memory poisoning → RCE.
  → upgrade serena-agent to ≥ 1.5.2.

- [CVE-2026-49825](https://github.com/advisories/GHSA-4jhm-jv67-739f) — lxml-html-clean (pip) · CVSS 8.2 · EPSS —
  Cleaner misses javascript: URLs in namespaced attributes; XSS via sanitized output.
  → upgrade lxml-html-clean to ≥ 0.4.5.

*MONITOR*
- [GHSA-2wc2-fm75-p42x](https://github.com/advisories/GHSA-2wc2-fm75-p42x) — soupsieve (pip) · CVSS 7.5 · no fix yet (≤ 2.8.3)
  Memory exhaustion + ReDoS via oversized selector lists. Affects all beautifulsoup4 users.
  → track soupsieve; no patch yet.

- [GHSA-52vm-mxx8-f227](https://github.com/advisories/GHSA-52vm-mxx8-f227) — phantom-audio (pip) · no CVSS · no fix yet (≤ 1.3.0)
  Unconfined MCP tool paths → arbitrary file write + decode-bomb DoS.
  → track phantom-audio; no patch yet.
