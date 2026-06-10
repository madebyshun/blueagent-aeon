*Security Digest — 2026-06-10*
Verdict: 3 actively exploited, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-7473](https://nvd.nist.gov/vuln/detail/CVE-2026-7473) — Arista EOS · KEV 2026-06-09 · EPSS 0.22 · CVSS n/a
  Tunnel decap incomplete comparison; actively exploited in the wild.
  → apply Arista EOS vendor patch today.

- [CVE-2026-11645](https://nvd.nist.gov/vuln/detail/CVE-2026-11645) — Google Chromium V8 · KEV 2026-06-09 · EPSS 0.05 · CVSS n/a
  Out-of-bounds RCE via crafted HTML; all Chromium-based browsers affected.
  → update Chrome/Edge/Brave to latest release today.

- [CVE-2026-20245](https://nvd.nist.gov/vuln/detail/CVE-2026-20245) — Cisco Catalyst SD-WAN Manager · KEV 2026-06-09 · EPSS 0.003 · CVSS n/a
  Authenticated local command injection escalates to root.
  → apply Cisco SD-WAN Manager patch today.

*PATCH THIS WEEK*
- [GHSA-wm5r-5qp3-5vxf](https://github.com/advisories/GHSA-wm5r-5qp3-5vxf) — dbgate-api (npm) · CVSS 9.4 · EPSS n/a · no public PoC
  Authenticated RCE via loadReader functionName code injection.
  → upgrade dbgate-api to ≥7.1.9.

- [GHSA-mqq6-462x-jxmm](https://github.com/advisories/GHSA-mqq6-462x-jxmm) — go-base (Go) · CVSS 9.1 · EPSS n/a
  Hardcoded JWT secret allows token forgery by any user.
  → upgrade github.com/dhax/go-base to ≥0.0.0-20260517152733.

- [GHSA-7qjx-gp9h-65qj](https://github.com/advisories/GHSA-7qjx-gp9h-65qj) — dex (Go) · CVSS 8.7 · EPSS n/a · no public PoC
  Token-exchange endpoint skips AllowedConnectors enforcement; auth bypass.
  → upgrade github.com/dexidp/dex to ≥0.0.0-20260303131938.

- [GHSA-9vc9-4jv3-rf86](https://github.com/advisories/GHSA-9vc9-4jv3-rf86) — @hulumi/policies (npm) · CVSS 8.5 · EPSS n/a
  HULUMI-H5 policy bypassed via decoy sibling resource targeting different bucket.
  → upgrade @hulumi/policies to ≥1.4.0.

- [GHSA-rhgj-6g2c-frmm](https://github.com/advisories/GHSA-rhgj-6g2c-frmm) — @hulumi/policies (npm) · CVSS 8.4 · EPSS n/a
  Policy bypass via forged Pulumi-URN logical name.
  → upgrade @hulumi/policies to ≥1.4.0.
