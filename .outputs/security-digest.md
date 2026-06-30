*Security Digest — 2026-06-30*
Verdict: 1 actively exploited, 0 likely soon, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-48558](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — SimpleHelp · KEV added 2026-06-29 · EPSS 0.012 · CVSS unscored
  OIDC auth bypass: forged identity tokens accepted without signature verification → unauthenticated admin session takeover, may also bypass MFA. Confirmed exploitation in wild.
  → apply SimpleHelp vendor update per CISA BOD 26-04 guidance today.

*MONITOR*
- [GHSA-q2m9-6jp9-c6mc](https://github.com/advisories/GHSA-q2m9-6jp9-c6mc) — dgraph/v25 (Go) · CVSS 7.5 · EPSS unscored · affects ≤ 25.3.3 · no patch
  DQL injection via checkUserPassword GraphQL query — password interpolated via fmt.Sprintf without escaping; double-quote breaks string literal, allows arbitrary DQL injection.
  → track GHSA-q2m9-6jp9-c6mc; avoid exposing Dgraph GraphQL auth endpoints publicly until patch lands.
