*Security Digest — 2026-09-25*
Verdict: 3 actively exploited, 2 to schedule, 3 to monitor. _Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-71362](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Adobe Commerce/Magento · KEV 2026-09-24 · EPSS 0.896 · CVSS N/A
  Incorrect authz → elevated resource access, no interaction needed. Due 2026-09-27 (tomorrow).
  → apply Adobe security patches immediately; discontinue if unavailable.

- [CVE-2026-61732](https://github.com/advisories/GHSA-g5f9-3xfg-p9mf) — decepticon-core/decepticon-sdk (pip) · CVSS 10.0 · EPSS 0.012 · public PoC
  ChatML token injection via crawled pages forges operator turns → RCE in agent sandbox. All 16 specialist agents affected.
  → upgrade decepticon/decepticon-core/decepticon-sdk to ≥ 1.1.17 today.

- [CVE-2025-39682](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Linux Kernel TLS · KEV 2026-09-18 · EPSS 0.029 · CVSS N/A
  Zero-length TLS records bypass handler, corrupting subsequent record processing.
  → apply kernel updates; prioritize internet-facing hosts (past due 2026-09-21).

*PATCH THIS WEEK*
- [CVE-2026-59723](https://github.com/advisories/GHSA-3cj3-hqcr-g934) — cline (npm) · CVSS 8.8 · EPSS 0.002 · public PoC
  Cross-origin WebSocket hijack via cline dashboard → RCE, credential theft when victim visits attacker page.
  → upgrade cline to ≥ 3.0.30.

- [CVE-2026-57171](https://github.com/advisories/GHSA-r4vp-3vw6-r2x5) — compliance-trestle (pip) · CVSS 8.4 · EPSS 0.002 · no PoC
  Path traversal in author generate commands allows arbitrary file write.
  → upgrade compliance-trestle to ≥ 3.12.4 (3.x) or ≥ 4.1.0 (4.x).

*MONITOR*
- [CVE-2026-57231](https://github.com/advisories/GHSA-4hq8-gpf5-8p68) — podman (Go) · CVSS 7.5 · EPSS 0.004 · no fix yet
  Malformed image leaks host env vars into container at run time.
  → avoid untrusted images; track GHSA-4hq8-gpf5-8p68.

- [CVE-2026-61782](https://github.com/advisories/GHSA-jmg2-rcxh-w8q3) — @rsdoctor/rspack-plugin (npm) · CVSS 7.5 · EPSS 0.004 · no fix yet
  Unauthenticated HTTP API exposes full project source code and build metadata.
  → restrict build-tool ports; track GHSA-jmg2-rcxh-w8q3.

- [CVE-2026-61604](https://github.com/advisories/GHSA-w3rp-4cm2-4wgc) — ixo-blockchain (Go) · critical · EPSS 0.003 · no fix yet
  DID-resolved payer drain + ICA authorization bypass in x/bonds and x/entity modules.
  → track GHSA-w3rp-4cm2-4wgc; no patch available for v7 or below.
