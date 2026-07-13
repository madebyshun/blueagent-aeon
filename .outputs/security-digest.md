*Security Digest — 2026-07-13*
Verdict: 1 KEV-confirmed, 2 CVSS 9.9 with public PoC → patch today. 3 more to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-55255](https://github.com/advisories/GHSA-qrpv-q767-xqq2) — langflow (pip) · KEV 2026-07-07 · EPSS 0.006 · CVSS 8.4
  Auth bypass in /api/v1/responses lets any authed user execute any flow via UUID. CISA-confirmed in-the-wild exploitation.
  → upgrade langflow to ≥1.9.1 and redeploy.

- [CVE-2026-50551](https://github.com/advisories/GHSA-56mp-4f3v-fgj2) — siyuan/kernel (Go) · CVSS 9.9 · EPSS 0.004 · public PoC
  Stored XSS→RCE via unsanitized asset cell content in Electron renderer. PoC payload published in advisory.
  → upgrade siyuan to ≥build 2026-06-28 and redeploy.

- [CVE-2026-54158](https://github.com/advisories/GHSA-5xfx-xj4h-5p7r) — siyuan/kernel (Go) · CVSS 9.9 · EPSS 0.003 · public PoC
  Stored XSS→RCE in genAVValueHTML(); workspace sync attack vector. Same build fixes both SiYuan entries.
  → upgrade siyuan to ≥build 2026-06-28 and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-54088](https://github.com/advisories/GHSA-m93h-4hw7-5qcm) — filebrowser/v2 (Go) · CVSS 9.3 · EPSS 0.005 · public PoC
  Pre-auth RCE via shell metacharacters in login credentials exploiting auth hook substitution.
  → schedule upgrade: filebrowser → ≥2.63.6.

- [GHSA-g936-7jqj-mwv8](https://github.com/advisories/GHSA-g936-7jqj-mwv8) — tsdproxy (Go) · CVSS 9.0 · no CVE/EPSS
  Internal proxy auth token forwarded to all backends; backend can replay to mgmt port with arbitrary identity.
  → schedule upgrade: tsdproxy → ≥1.4.4 (build 2026-06-03).

- [GHSA-xrmc-c5cg-rv7x](https://github.com/advisories/GHSA-xrmc-c5cg-rv7x) — safeinstall-cli (npm) · CVSS 8.8 · no CVE/EPSS
  Agent guard shell parsing miss lets raw package execution bypass safety checks.
  → schedule upgrade: safeinstall-cli → ≥0.10.2.
