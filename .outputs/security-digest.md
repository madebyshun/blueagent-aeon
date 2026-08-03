*Security Digest — 2026-08-03*
Verdict: nothing urgent today. 1 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [GHSA-vpx6-8pjr-4g3v](https://github.com/advisories/GHSA-vpx6-8pjr-4g3v) — @angular/platform-server (npm) · CVSS 8.6 · EPSS n/a · no public PoC
  SSR missing escaping in fallback elements (<iframe>/<noscript>/<noframes>) → unauthenticated XSS. Network, low complexity, passive user interaction.
  → upgrade @angular/platform-server to ≥22.0.7 (v22) / ≥21.2.19 (v21) / ≥20.3.27 (v20).

_KEV note: 3 confirmed-exploited entries this week (Cisco FMC, Fortinet FortiOS, Arista VeloCloud) — all reported Aug 1–2, not repeating._
