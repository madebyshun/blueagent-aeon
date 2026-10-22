*Security Digest — 2026-10-22*
Verdict: 3 confirmed exploited (new KEV entries), 5 to patch this week. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY* _(KEV — confirmed exploitation in the wild)_

- [CVE-2026-102764](https://nvd.nist.gov/vuln/detail/CVE-2026-102764) — BeyondTrust Remote Support · KEV added 2026-10-16 · EPSS 0.012 (67th %ile) · CVSS n/a
  Auth bypass via spoofing → unauthenticated file ops on appliance.
  → apply BeyondTrust Remote Support vendor patch immediately.

- [CVE-2026-106931](https://nvd.nist.gov/vuln/detail/CVE-2026-106931) — EG Secure Solutions SiteGuard Server Edition · KEV added 2026-10-20 · EPSS 0.012 (67th %ile)
  Unauthenticated OS command injection → root/SYSTEM RCE on host.
  → apply vendor mitigations or isolate from internet.

- [CVE-2025-61624](https://nvd.nist.gov/vuln/detail/CVE-2025-61624) — Fortinet FortiOS / FortiPAM / FortiProxy / FortiSwitchManager · KEV added 2026-10-16 · EPSS 0.011 (65th %ile)
  Authenticated admin path traversal → arbitrary file write/delete via CLI.
  → upgrade per Fortinet PSIRT advisory.

*PATCH THIS WEEK*

- [GHSA-673q-mjm6-r5xr](https://github.com/advisories/GHSA-673q-mjm6-r5xr) — next (npm) · CVSS 9.5 · no CVE yet · no EPSS
  Unauthenticated RCE via deserialization in App Router `use cache` functions returning typed arrays.
  → upgrade next to ≥ 16.4.1.

- CVE-2026-96652 / -96654 / -96655 / -96656 — Plex Media Server · KEV added 2026-10-20 · EPSS 0.002–0.008
  4-CVE chain: token-based SSRF + URI scheme injection + admin file write → potential RCE.
  → upgrade Plex Media Server; restrict to trusted networks.

- [GHSA-78g4-xqwv-q3g8](https://github.com/advisories/GHSA-78g4-xqwv-q3g8) — Pillow (pip) · high · no CVE
  Bundled libopenjp2 heap-buffer-overflow write via crafted JPEG 2000. OOB write → crash / control-flow primitive. Affects Pillow 11.1.0–12.3.0 wheels.
  → upgrade pillow to ≥ 13.0.0; pass `formats=` to Image.open() to restrict codecs.

- [GHSA-cg2g-xh64-v4q7](https://github.com/advisories/GHSA-cg2g-xh64-v4q7) — dompurify (npm) · critical · PoC published
  SAFE_FOR_TEMPLATES bypass via attached shadow roots → template expressions survive sanitization → XSS / template injection. Requires non-default config (SAFE_FOR_TEMPLATES + DOM-returning mode).
  → upgrade dompurify to latest; avoid SAFE_FOR_TEMPLATES + RETURN_DOM/IN_PLACE combo until patched.

- [CVE-2026-110936](https://nvd.nist.gov/vuln/detail/CVE-2026-110936) — Siemens Software Center · KEV added 2026-10-20 · EPSS 0.002 (14th %ile)
  Local DLL hijacking → code execution at app privilege (valid credentials required).
  → apply Siemens patch; restrict write access to app install directories.
