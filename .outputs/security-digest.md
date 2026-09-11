*Security Digest — 2026-09-11*
Verdict: 3 actively exploited (KEV), 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-85046](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) — Google Chromium V8 · KEV added 2026-09-04 · EPSS 1.26%
  Type confusion enables RCE via malicious HTML in Chromium-based browsers. Exploited per CISA.
  → update Chrome/Chromium and Electron apps today.

- [CVE-2026-67277](https://nvd.nist.gov/vuln/detail/CVE-2026-67277) — MikroTik RouterOS · KEV added 2026-09-10 · EPSS 0.75%
  Missing auth in btest service exposes kernel memory, enables DoS. Exploited per CISA.
  → patch RouterOS per vendor advisory today.

- [CVE-2026-86060](https://nvd.nist.gov/vuln/detail/CVE-2026-86060) — MikroTik RouterOS · KEV added 2026-09-10 · EPSS 0.69%
  Argument-delimiter injection in policy mask enables privilege escalation. Exploited per CISA.
  → patch RouterOS per vendor advisory today.

*PATCH THIS WEEK*
- [CVE-2026-88018](https://github.com/advisories/GHSA-xwwr-4h3p-r22c) — rclone serve s3 (Go) · CVSS 9.8 · EPSS 0.49% · PoC public
  --auth-proxy without --auth-key accepts any SigV4 signature — full S3 backend access unauthenticated.
  → upgrade rclone to ≥1.75.1 and redeploy.

- [GHSA-26w7-cxv4-gfx2](https://github.com/advisories/GHSA-26w7-cxv4-gfx2) — astro (npm) · CVSS 9.8 · no public PoC
  Malicious AVIF triggers RCE via libheif in Sharp image service. No auth required.
  → upgrade astro to ≥7.2.8.

- [CVE-2026-88044](https://github.com/advisories/GHSA-p569-5gjg-9cmj) — rclone RC (Go) · CVSS 9.1 · EPSS 0.49% · PoC public
  Per-server auth-proxy bypass: S3 clients reach wrong backends; FTP gets unauthenticated R/W.
  → upgrade rclone to ≥1.75.1.

- [CVE-2026-59160](https://github.com/advisories/GHSA-2r5q-h53f-9rp3) — @yeger/turbo-graph (npm) · CVSS 8.8
  Unauthenticated /api/run endpoint executes arbitrary tasks for any network caller.
  → upgrade or block network exposure.

- [CVE-2026-88007](https://github.com/advisories/GHSA-qqjf-53cj-pwvv) — Traefik (Go) · EPSS 0.37% · PoC public
  HTTP/3 reuses NTLM-authenticated backend connection across clients — identity hijack without credentials.
  → upgrade Traefik to ≥v2.11.57 (v2) or ≥v3.7.13 (v3).

*MONITOR*
- [CVE-2026-88062](https://github.com/advisories/GHSA-hf57-cqmx-p4gr) — omniroute (npm) · EPSS 0.40% · no fix
  ACP custom-agent endpoint allows unauthenticated RCE. → watch for patched release.

- [GHSA-2xp9-vwfh-vxw4](https://github.com/advisories/GHSA-2xp9-vwfh-vxw4) — next (npm) · critical · no fix
  AVIF image optimization RCE (distinct from yesterday's CVE-2026-75604). → disable AVIF until patched.

- [CVE-2026-84445](https://github.com/advisories/GHSA-2v4p-qf9q-27wj) — grpc (Go) · high · no fix
  xDS server crash via missing :authority/Host — remote DoS. → watch for patched release.
