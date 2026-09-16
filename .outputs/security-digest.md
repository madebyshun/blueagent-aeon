*Security Digest — 2026-09-16*
Verdict: 3 actively exploited (KEV), 5 in tracked stack to patch this week, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-19490](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Citrix NetScaler ADC/Gateway · KEV 2026-09-09 · EPSS 0.056 · CVSS N/A
  Auth bypass via alternate path on AAA/gateway-configured instances. Exploited in the wild.
  → apply vendor patches per BOD 26-04; disable gateway role if unpatched.

- [CVE-2025-25249](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Fortinet FortiOS/FortiSwitchManager/FortiSASE · KEV 2026-09-09 · EPSS 0.024 · CVSS N/A
  Heap-based buffer overflow enables arbitrary code execution. Exploited in the wild.
  → upgrade affected Fortinet products per vendor advisory immediately.

- [CVE-2026-86060](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — MikroTik RouterOS · KEV 2026-09-10 · EPSS 0.011 · CVSS N/A
  Argument delimiter bypass enables policy mask modification and privilege escalation.
  → upgrade RouterOS to vendor-latest; restrict admin interface exposure.

*PATCH THIS WEEK*
- [GHSA-cv3r-c5h8-f4g5](https://github.com/advisories/GHSA-cv3r-c5h8-f4g5) — @zereight/mcp-gitlab (npm <2.1.30) · CVSS 9.8 · EPSS 0.007
  File read via upload_markdown leaks PAT tokens → full account takeover. 3 bundled CVEs (SSRF, DNS rebinding, safety bypass) all fixed in 2.1.30.
  → upgrade @zereight/mcp-gitlab to ≥2.1.30.

- [GHSA-5h8j-6crg-7rmw](https://github.com/advisories/GHSA-5h8j-6crg-7rmw) — lmdeploy (pip ≥0.9.1,<0.10.2) · CVSS 9.8 · EPSS 0
  RCE via Pickle deserialization in zmq_rpc.call_and_response().
  → upgrade lmdeploy to ≥0.10.2.

- [GHSA-vrh8-c9cm-wh8v](https://github.com/advisories/GHSA-vrh8-c9cm-wh8v) — zitadel (Go <4.15.3) · CVSS 8.1 · EPSS 0.004
  OAuth2 Token Exchange grants unauthorized privilege escalation.
  → upgrade github.com/zitadel/zitadel to ≥4.15.3.

- [GHSA-pg97-jvmf-qfvc](https://github.com/advisories/GHSA-pg97-jvmf-qfvc) — djust (pip <1.0.7) · CVSS 8.1 · EPSS 0
  CSRF on SSE transport + multi-tenant data leak + mass-assignment (3 CVEs, all fixed in 1.0.7).
  → upgrade djust to ≥1.0.7.

- [GHSA-5hq8-qhww-jm7q](https://github.com/advisories/GHSA-5hq8-qhww-jm7q) — libp2p-quic (crates.io <0.13.1) · CVSS N/A · EPSS 0.002
  Remote panic via cert expiry race during QUIC handshake.
  → upgrade libp2p-quic to ≥0.13.1.

*MONITOR*
- [GHSA-r2pf-9cw4-5j65](https://github.com/advisories/GHSA-r2pf-9cw4-5j65) — node-opcua (npm <2.170.0) · CVSS 7.0 · EPSS 0
  TCP socket leak under keepalive reconnect → resource exhaustion. No exploitation signal.
  → upgrade node-opcua to ≥2.170.0 at next maintenance window.
