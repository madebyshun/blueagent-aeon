*Security Digest — 2026-09-12*
Verdict: 3 actively exploited, 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-85706](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) — GitLab CE/EE · KEV 2026-09-11 · EPSS 1.15% · CVSS n/a
  Unauth path traversal in repo commits API → arbitrary file read. Actively exploited per CISA.
  → upgrade GitLab to latest vendor-patched release immediately.

- [CVE-2026-42016](https://nvd.nist.gov/vuln/detail/CVE-2026-42016) + [CVE-2026-42018](https://nvd.nist.gov/vuln/detail/CVE-2026-42018) — JFrog Artifactory · KEV 2026-09-11 · EPSS ~0.9% · CVSS n/a
  Token scope bypass (priv-esc) + anonymous token leaked to unauth callers. Dual exploitation confirmed.
  → apply vendor patch; audit for unauthorized access.

- [CVE-2026-84869](https://nvd.nist.gov/vuln/detail/CVE-2026-84869) — ConnectWise ScreenConnect · KEV 2026-09-11 · EPSS 0.69% · CVSS n/a
  Missing auth allows unauth file transfer/exec via active remote sessions.
  → upgrade ScreenConnect; audit session logs for anomalous transfers.

*PATCH THIS WEEK*
- [GHSA-rqfv-2mw9-78g2](https://github.com/advisories/GHSA-rqfv-2mw9-78g2) / CVE-2026-59971 — mysql-mcp-server (pip) · CVSS 10.0 · 25 exposed instances scanned
  No origin/host validation on SSE transport → unauth SQL execution via DNS rebinding.
  → upgrade mysql-mcp-server to ≥0.4.2; bind SSE port to 127.0.0.1.

- [GHSA-h8m9-jgf8-vwvp](https://github.com/advisories/GHSA-h8m9-jgf8-vwvp) / CVE-2026-59151 — prowler-cloud (pip) · CVSS 9.6 · EPSS 0.32% · no patch
  SAML domain claiming → cross-tenant account takeover.
  → disable SAML auth until fix; watch prowler-cloud releases.

- [GHSA-325j-mg25-8q58](https://github.com/advisories/GHSA-325j-mg25-8q58) / CVE-2026-61534 — yayson (npm) · CVSS 9.1 · PoC in advisory
  Prototype pollution via type=__proto__ in JSON:API deserialization → process-wide object corruption.
  → upgrade yayson to ≥4.3.0.

- [GHSA-rqx4-3f6q-3x2v](https://github.com/advisories/GHSA-rqx4-3f6q-3x2v) / CVE-2026-59148 — @mockoon/commons-server (npm) · CVSS 8.8 · EPSS 0.26% · no patch
  Unauth admin API + wildcard CORS → mock-state hijack and credential theft.
  → bind Mockoon CLI admin port to 127.0.0.1; watch for patch.

- [GHSA-wpmr-8h3q-fwj7](https://github.com/advisories/GHSA-wpmr-8h3q-fwj7) / CVE-2026-87016 — open-webui (pip) · CVSS 8.1 · EPSS 0.33% · no patch
  OAuth wildcard subject claim → sign-in as any user on SQLite backends.
  → use PostgreSQL backend or disable OAuth; monitor releases.

*MONITOR*
- [GHSA-jmc6-2wr8-h3wj](https://github.com/advisories/GHSA-jmc6-2wr8-h3wj) / CVE-2026-87995 — open-webui (pip) · CVSS 8.7 · no fix
  XSS via terminal iframe allow-same-origin → full account takeover. → disable terminal feature; watch for fix.

- [GHSA-65h7-9wrw-629c](https://github.com/advisories/GHSA-65h7-9wrw-629c) / CVE-2026-59973 — mcp-from-openapi (npm) · CVSS 8.5 · no fix
  External $ref SSRF bypass via alternate resolution path. → avoid untrusted OpenAPI inputs.

- [GHSA-6xcw-7xm6-48c6](https://github.com/advisories/GHSA-6xcw-7xm6-48c6) / CVE-2026-86083 — n8n (npm) · no fix
  Expression sandbox escape via shared builtin tampering → arbitrary code execution.
  → restrict expression use to trusted workflows; watch for patch.
