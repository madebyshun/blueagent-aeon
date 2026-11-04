*Security Digest — 2026-11-04*
Verdict: 3 actively exploited, 2 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-76418](https://nvd.nist.gov/vuln/detail/CVE-2026-76418) — Cisco Secure Firewall ASA/FTD · KEV 2026-10-29 · EPSS 0.008 · CVSS N/A
  Unauth remote NULL ptr deref causes device reload (DoS). CISA confirmed exploitation.
  → patch Cisco ASA/FTD firmware and redeploy.

- [CVE-2026-41709](https://nvd.nist.gov/vuln/detail/CVE-2026-41709) — Broadcom VMware ESX · KEV 2026-10-28 · EPSS 0.007 · CVSS N/A
  Admin ops bypass audit logging; enables covert persistence on ESX hosts. CISA confirmed exploitation.
  → apply Broadcom ESX update and audit recent admin activity.

- [CVE-2024-27834](https://nvd.nist.gov/vuln/detail/CVE-2024-27834) — Apple iOS/macOS/Safari/tvOS/watchOS · KEV 2026-11-04 · EPSS 0.006 · CVSS N/A
  Pointer authentication bypass with arbitrary read/write. Added to KEV today.
  → update all Apple devices; prioritize internet-facing installs.

*PATCH THIS WEEK*
- [CVE-2026-44266](https://github.com/advisories/GHSA-7w38-ggh5-v542) — @enspirit/elo (npm) · CVSS 9.8 · EPSS 0.010 · public PoC verified
  Ruby backend RCE via unescaped #{} string interpolation in emitted code; PoC verified on Ruby 3.x.
  → upgrade @enspirit/elo to >=1.0.1.

- [CVE-2026-62331](https://github.com/advisories/GHSA-48v2-6jcm-fc99) — praktor (Go) · CVSS 8.2 · EPSS 0.008 · no public PoC
  Path traversal in Telegram file upload handler allows writes outside agent workspace.
  → upgrade github.com/mtzanidakis/praktor to >=0.9.1.
