*Security Digest — 2026-06-28*
Verdict: nothing urgent today. 0 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

KEV note: CVE-2026-12569 (PTC Windchill) + CVE-2026-20230 (Cisco UCM) remediation deadline is today — both already in Jun 26 digest; apply patches if not done.

*MONITOR*
- [CVE-2026-48749](https://github.com/advisories/GHSA-2q3f-q5pq-g8wv) — Incus (go) · CVSS 9.9 · EPSS not yet scored · no confirmed patch
  Malicious container image with rootfs/ symlink achieves arbitrary file read+write on host at image-import time. Sibling cluster (CVE-2026-48750–48769) fixed ≥7.2.0 (Jun 27 digest); API null for this CVE but same release likely covers it.
  → if not already on ≥7.2.0, upgrade now; reject untrusted image sources.

- [CVE-2026-48713](https://github.com/advisories/GHSA-2933-q333-qg83) — i18next-fs-backend (npm) · CVSS 9.1 · EPSS 0.004 · no fix yet
  Prototype pollution via crafted missing-key string; server-side Node.js filesystem translation backend. Attacker-controlled locale keys can pollute Object.prototype.
  → track GHSA-2933-q333-qg83; no patch yet; audit locale key input sources.

- [CVE-2026-48714](https://github.com/advisories/GHSA-f49m-vf83-692w) — i18next-http-middleware (npm) · CVSS 9.1 · EPSS 0.004 · no fix yet
  MissingKeyHandler accepts keys with prototype-polluting segments (__proto__, constructor). Same class as CVE-2026-48713; Express/Koa middleware.
  → track GHSA-f49m-vf83-692w; no patch yet; validate i18next keys server-side.
