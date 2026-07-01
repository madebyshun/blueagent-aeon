*Security Digest — 2026-07-01*
Verdict: nothing urgent today. 0 to patch, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*MONITOR*
- [GHSA-wmgg-3p4h-48x7](https://github.com/advisories/GHSA-wmgg-3p4h-48x7) +8 related — fission (Go) · CVSS 9.9 cluster · EPSS 0.003 · no patch
  PodSpec/EnvironmentRef injection → node escape, cluster takeover, cross-namespace reads. All fission ≤ 1.23.0 (9 advisories published Jun 30).
  → track cluster; no patch yet — disable multi-tenant Fission or restrict untrusted pod/env inputs.

- [GHSA-g4w6-vmgf-xqvx](https://github.com/advisories/GHSA-g4w6-vmgf-xqvx) — @cedar-policy/authorization-for-expressjs (npm) · CVSS 8.8 · EPSS 0.0 · no patch
  Auth bypass via query string manipulation; Cedar policy checks can be circumvented on Express.js routes. ≤ 0.2.0.
  → track GHSA-g4w6-vmgf-xqvx; no patch yet — use the Cedar SDK directly rather than this wrapper.

- [GHSA-f5mr-q85p-6hh6](https://github.com/advisories/GHSA-f5mr-q85p-6hh6) — sigstore/fulcio (Go) · CVSS 8.7 · EPSS 0.0 · no patch
  OIDC discovery redirect → SSRF + JWKS substitution + Kubernetes service account token leakage. ≤ 1.8.5.
  → track GHSA-f5mr-q85p-6hh6; no patch yet — restrict Fulcio exposure to trusted internal networks.
