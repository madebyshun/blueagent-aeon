*Security Digest — 2026-09-29*
Verdict: 3 actively exploited (KEV — all PAST DUE), 1 new KEV due 10-02, 3 npm to monitor. _Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-87902](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — WordPress Core · KEV 2026-09-25 · EPSS 0.197 · CVSS N/A
  Unauthenticated RCE via PHP file inclusion in page-template resolution. CISA deadline 2026-09-28 PAST DUE.
  → update WordPress core immediately and audit template plugins.

- [CVE-2026-65660](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Microsoft SharePoint · KEV 2026-09-25 · EPSS 0.021 · CVSS N/A
  Code injection; authorized attacker executes arbitrary code over network. CISA deadline 2026-09-28 PAST DUE.
  → apply Microsoft SharePoint patch via Windows Update or MSRC today.

- [CVE-2026-67279](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — MikroTik RouterOS · KEV 2026-09-25 · EPSS 0.010 · CVSS N/A
  Unauthenticated remote exec request via improper session workflow. CISA deadline 2026-09-28 PAST DUE.
  → upgrade RouterOS immediately; restrict Winbox/SSH to trusted IPs.

*PATCH THIS WEEK*
- [CVE-2026-86950](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Apple iOS/macOS/iPadOS · KEV added TODAY · EPSS 0.008 · CVSS N/A
  Out-of-bounds write in CoreGraphics → arbitrary code execution. CISA due 2026-10-02 (3 days). Actively exploited.
  → install Apple security update ASAP via Software Update.

*MONITOR*
- [GHSA-9qh4-3jw8-366w](https://github.com/advisories/GHSA-9qh4-3jw8-366w) — electron (npm) · CVSS 8.3 · EPSS pending · no fix yet
  <webview> bypasses embedder restriction and enables Node.js in Web Workers. Affects < 41.10.6 / 42.x < 42.9.2 / 43.x < 43.4.1. 4 related Electron CVEs in same batch.
  → watch electron releases; prefer 41.10.6+ or 42.9.2+ if on those branches.

- [GHSA-rfgv-xxqx-mfg5](https://github.com/advisories/GHSA-rfgv-xxqx-mfg5) — undici (npm) · CVSS 7.5 · EPSS 0.004 · no fix yet
  WebSocket DoS via unrequested subprotocol negotiation. Affects all current undici versions.
  → track undici releases; monitor for patch.

- [GHSA-6h2x-m376-mqjq](https://github.com/advisories/GHSA-6h2x-m376-mqjq) — joi (npm) · CVSS 7.5 · EPSS pending · no fix yet
  Quadratic ReDoS in Joi.string().isoDate() validation.
  → avoid validating untrusted ISO date strings with joi until patched.
