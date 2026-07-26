*Security Digest — 2026-07-26*
Verdict: nothing urgent today. 5 to schedule, 3 to monitor. _Sources: KEV (no new adds since Jul 22), GH Advisory, EPSS_

*PATCH THIS WEEK*
- [GHSA-w4hw-qcx7-56pr](https://github.com/advisories/GHSA-w4hw-qcx7-56pr) + [GHSA-gm3r-q2wp-hw87](https://github.com/advisories/GHSA-gm3r-q2wp-hw87) — shescape (npm) · CVSS 9.2 / 8.7 · EPSS n/a
  Shell injection via unescaped parens on Windows CMD + quadratic-time DoS in flag-protection. Two bugs, one fix.
  → upgrade shescape to ≥2.1.14 (v2) or ≥3.0.1 (v3).

- [GHSA-vh45-f885-3848](https://github.com/advisories/GHSA-vh45-f885-3848) — sm-crypto (npm) · CVSS 9.1 · EPSS n/a
  SM2 private key generated from Math.random + wall clock in Node.js — CSPRNG branch skipped. Keys recoverable. PoC included.
  → upgrade sm-crypto to ≥0.5.0.

- [GHSA-hp6v-6jw7-gv2f](https://github.com/advisories/GHSA-hp6v-6jw7-gv2f) — @budibase/server (npm) · CVSS 9.0 · EPSS n/a
  OIDC SSO account takeover: email claim linked without checking email_verified. Attacker claims victim email via unverified IdP account → inherits admin session.
  → upgrade budibase to ≥3.39.30.

- [GHSA-mqhr-6j6h-74p5](https://github.com/advisories/GHSA-mqhr-6j6h-74p5) — @budibase/server (npm) · critical · EPSS n/a
  Unauthenticated REST credential theft: stored Bearer tokens forwarded to attacker-controlled host via PUBLIC query + path param. One request, no login. PoC confirmed.
  → upgrade budibase to ≥3.40.1.

- [GHSA-6vch-q96h-7gc3](https://github.com/advisories/GHSA-6vch-q96h-7gc3) + [GHSA-xg4h-6gfc-h4m8](https://github.com/advisories/GHSA-xg4h-6gfc-h4m8) — etcd (go) · CVSS 8.7 / 7.1 · EPSS n/a
  TLS listener goroutine DoS (no handshake deadline) + Watch API RBAC bypass (any READ grant reads full keyspace). Both fixed same release.
  → upgrade etcd to ≥3.7.1 / 3.6.14 / 3.5.33.

*MONITOR*
- [GHSA-hmj8-5xmh-5573](https://github.com/advisories/GHSA-hmj8-5xmh-5573) — py-libp2p (pip) · CVSS 7.5 · no fix yet
  yamux connection DoS: 12-byte frame claiming 4 GB body stalls read loop. Default new_host() affected. Any post-handshake peer can trigger it.
  → track issue; no patch yet; consider restricting peer connections.

- [GHSA-jvxp-qmx7-gjpx](https://github.com/advisories/GHSA-jvxp-qmx7-gjpx) / CVE-2026-16756 — aws-smithy-http-server (crates.io) · CVSS 8.7 · EPSS 0.004
  Slowloris DoS: no connection/header-read timeout in default serve() path. Unauthenticated.
  → upgrade aws-smithy-http-server to ≥0.66.5.

- [GHSA-j6g5-3hh3-pgw8](https://github.com/advisories/GHSA-j6g5-3hh3-pgw8) / CVE-2026-16796 — bedrock-agentcore (pip) · CVSS 8.4 · EPSS 0.003
  Argument injection in install_packages(): crafted package specifier → arbitrary command exec inside Code Interpreter sandbox.
  → upgrade bedrock-agentcore to ≥1.18.1.
